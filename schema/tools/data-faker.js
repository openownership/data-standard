#!/usr/bin/env node

var program = require('commander');
var jsf = require('json-schema-faker');
var faker = require('faker');
var sample;

program
    .option('-b --blank', 'Blank data')
    .option('-c --crossref', 'Cross-referenced data')
    .option('-d --debugschema', 'Output modified schema')
    .parse(process.argv);

var jsonschema = 
    JSON.parse(
        require('fs').readFileSync(
            require('path').resolve(
                __dirname, 
                '../beneficial-ownership-statements.json'),
            'utf8'));

var schemapatches = 
    JSON.parse(require('fs').readFileSync(
        require('path').resolve(
            __dirname,
        'schemapatches.json'),
    'utf8'));



jsf.format('URI', function(gen, jsonschema) {
    return gen.randexp('^http://[A-Za-z0-9]+\\.com$');
});

jsf.extend('faker', function(faker) {
  faker.custom = {
    fullAddress: function() {
      return faker.address.streetAddress() + ", " + faker.address.city();
    }
  };
  return faker;
});

jsf.option({
    alwaysFakeOptionals: true
});

var minBeneficialOwnershipStatements = 1;
var beneficialOwnershipStatement = jsonschema.definitions.BeneficialOwnershipStatement;

var flat_arrays = [ "qualificationStatements", "entityStatements",
                   "personStatements"];
var fuzzy_dates = [ "birthDate", "deathDate", "foundingDate", 
                    "dissolutionDate", "startDate", "endDate"];


var applyCommonPatches = function(original, patched) {
    var modified = JSON.parse(JSON.stringify(original), function(key, value) {
        if (key === "definitions") {
            value.FuzzyDate = patched.definitions.FuzzyDate;
            return value;
        }
        if (fuzzy_dates.includes(key) && !program.blank) {
            return {"$ref": "#/definitions/FuzzyDate"};
        }
        return value;
    });
    return modified;
};





/*var applyCommonPatches = function(original, patched) {
    // add common definitions for faker formats
    // patch in company and natural person names
    original.definitions.PersonName = patched.definitions.PersonName;
    original.definitions.PersonStatement.properties.name = {"$ref": "#/definitions/PersonName"};
    original.definitions.CompanyName = patched.definitions.CompanyName;
    original.definitions.EntityStatement.properties.name = {"$ref": "#/definitions/CompanyName"};

    // patch in identifiers - missing software agents
    original.definitions.PersonIdentifier = patched.definitions.PersonIdentifier;
    original.definitions.CompanyIdentifier = patched.definitions.CompanyIdentifier;
    original.definitions.EntityStatement.properties.identifiers = {"type": "array",
    "items": {"type": "object", "$ref": "#/definitions/CompanyIdentifier"}};
    original.definitions.PersonStatement.properties.identifiers = {"type": "array",
    "items": {"type": "object", "$ref": "#/definitions/PersonIdentifier"}};
    //original.definitions.PersonStatement.properties.identifiers = {"type": "array","items": {"type": "object", "$ref": "#definitions/PersonIdentifier"}};
};*/

var applyHierarchicalPatches = function(original, patched) {
    // adjust schema for nested publication
    var modified;
    modified = original;
    modified.definitions.BeneficialOwnershipStatement.required = ["entity", "interestedParty", "id",
            "statementDate", "interests"];
    // replace StatementReference from oneOf in nested properties
    modified.definitions.BeneficialOwnershipStatement.properties.entity = {"$ref": "#/definitions/EntityStatement"};
    //original.definitions.BeneficialOwnershipStatement.properties.interestedParty = patched.hierarchicalDefinitions.interestedParty;
    return modified;
    
};

var applyCrossReferencedPatches = function(original, patched) {
    original.properties.statementGroups.required = flat_arrays; 
    original.definitions.BeneficialOwnershipStatement.required = ["entity"];
    original.definitions.BeneficialOwnershipStatement.anyOf = [
        {"required": ["interestedParty"]},
        {"required": ["qualifications"]}
    ];
    // patch in statement references
    original.definitions.StatementReference = patched.definitions.StatementReference;
    original.definitions.EntityStatementReference = patched.definitions.EntityStatementReference;
    original.definitions.PersonStatementReference = patched.definitions.PersonStatementReference;
    original.definitions.QualificationStatementReference = patched.definitions.QualificationStatementReference;
    
    original.definitions.BeneficialOwnershipStatement.properties.entity = {"$ref": "#/definitions/EntityStatementReference"};
    original.definitions.BeneficialOwnershipStatement.properties.interestedParty = {
          "oneOf": [
            {
              "$ref": "#/definitions/EntityStatementReference"
            },
            {
              "$ref": "#/definitions/PersonStatementReference"
            }
          ]
        };
    original.definitions.BeneficialOwnershipStatement.properties.qualifications.items = { "$ref": "#/definitions/QualificationStatementReference"};
    original.definitions.BeneficialOwnershipStatement.properties.provenance = {"$ref": "#/definitions/ProvenanceStatementReference"};

};

var makeBlank =  function(schema) {
    /**
    * Reviver function to parse the schema and set to blank defautls
    */
    var modified = JSON.parse(JSON.stringify(schema), function(key, value){
        if (key === 'title' || key === 'description') {
            return undefined;
        }
        if (key === "type" && value === "array") {
            this.minItems = 1;
            this.maxItems = 1;
        }
        if (key === "type" && value === "string") {
            delete this.faker;
            delete this.format;
            delete this.pattern;
            delete this.minLength;
            delete this.maxLength;
            this.enum = [""];
        }

        if (key === "type" && value === "number") {
            this.enum = [0];
        }
        if (key ==="type" && value === "boolean") {
            this.enum = [false];
        }
        return value;

    });
    // put back description properties
    modified.definitions.Annotation.properties.description = {"type": "string", "enum": [""]};
    modified.definitions.NullParty.properties.description = {"type": "string", "enum": [""]};
    modified.definitions.Source.properties.description = {"type": "string", "enum": [""]};


    return modified;
};

var modifyForFaker = function(schema) {
    var modified = JSON.parse(JSON.stringify(schema), function(key, value) {
        
        // mitigates this empty array pruning bug - https://github.com/json-schema-faker/json-schema-faker/issues/232
        if (key === 'type' && value === 'array') {
            this.minItems = 1;
        }
    
        if (key === 'title' || key === 'description') {
            return undefined;
        }
        if (value === 'date' || value === 'datetime') {
            return 'date-time';
        }
        if (key === 'id' || key === 'ReplacesStatement' || key === 'replacesStatementGroup') {
            value.minLength = 20;
            value.type = 'string';
            value.faker = 'random.uuid';
        }
        if (key === 'jurisdiction' ||
            key === 'country') {
            value.faker = 'address.countryCode';
        }
        if (key === 'nationalities') {
            value.items.faker = 'address.countryCode';
        }
        if (key === 'format' && value === 'uri') {
            return 'URI';
        }
        if (key === 'address') {
            value.faker = 'custom.fullAddress';
        }
        if (key === 'postCode') {
            value.faker = 'address.zipCode'
        }
        if (key == 'EntityStatement') {
            value.properties.name.faker = 'company.companyName';
        }
        if (key === 'AlternateName') {
            value.properties.familyName.faker = 'name.lastName';
            value.properties.givenName.faker = 'name.firstName';
        }
        if (key === 'url') {
            value.faker = 'internet.url';
        } 
        return value;
        
    });
    // put back the description properties removed in reviver function
    modified.definitions.Annotation.properties.description = schema.definitions.Annotation.properties.description;
    modified.definitions.NullParty.properties.description = schema.definitions.NullParty.properties.description;
    modified.definitions.Source.properties.description = schema.definitions.Source.properties.description;

    return modified;
};

var postProcessCrossrefencedSample = function (modifiedSchema) {
    var sample = jsf(modifiedSchema);
    //add some extra items to prune after sample data is generated
    for (prop in modifiedSchema.properties.statementGroups.properties) {
        if(flat_arrays.includes(prop)) {
            modifiedSchema.properties.statementGroups.properties[prop].minItems = minBeneficialOwnershipStatements * 5;
        }
    }
    //store statement IDs generated in beneficial ownership statement
    var identifiers = {"entityStatements": [],
           "personStatements": [],
           "qualificationStatements": [],
           "provenanceStatements": []};
    sample
        .statementGroups
        .beneficialOwnershipStatements
        .forEach(function(sg) {
            identifiers.entityStatements.push(sg.entity.id);
            if(sg.hasOwnProperty('interestedParty')){
                if(sg.interestedParty.type === "entityStatement") {
                    identifiers.entityStatements.push(sg.interestedParty.id);
                }
                if(sg.interestedParty.type === "personStatement") {
                    identifiers.personStatements.push(sg.interestedParty.id);
                }
            }
            if(sg.hasOwnProperty('provenance')) {
                identifiers.provenanceStatements.push(sg.provenance.id);
            }
            if(sg.hasOwnProperty('qualifications')) {
                sg.qualifications.forEach(function(qual) {
                    identifiers.qualificationStatements.push(qual.id);
                });
            }
        });

        //delete empty statement groups if they exist
        Object.keys(identifiers).forEach(function(id_array) {
            if(identifiers[id_array].length === 0) {
                delete identifiers[id_array];
                delete sample.statementGroups[id_array];
            }
        });

        Object.keys(identifiers).forEach(function (id_array) {
            //trim beneficial ownership statement references and cross-referenced data to same size
            if (identifiers[id_array] && sample.statementGroups[id_array]) {
                if (identifiers[id_array].length > sample.statementGroups[id_array].length) {
                    identifiers[id_array] = identifiers[id_array].slice(0, sample.statementGroups[id_array].length);
                }
                else {
                    sample.statementGroups[id_array] = sample.statementGroups[id_array].slice(0, identifiers[id_array].length);
                }

                //swap out random guids for guids present in beneficial ownership statement
                sample.statementGroups[id_array].forEach(function(sg, index) {
                    Object.keys(sg).forEach(function(prop) {
                        if(prop === "id") {
                            sample.statementGroups[id_array][index]["id"] = identifiers[id_array][index];
                        }
                    });
                });
            }
        });
    console.log(JSON.stringify(sample, null, 2));
};

var postProcessShare = function(share) {
    if (Math.random() > 0.5) {
        delete share.exact;
        if (share.minimum > share.maximum) {
            var newMax = share.minimum;
            share.minimum = share.maximum;
            share.maximum = newMax;
        }
    } else {
        share.minimum = share.exact;
        share.maximum = share.exact;
        delete share.exclusiveMinimum;
        delete share.exclusiveMaximum;
    }
    return share;
}

var postProcessHierarchicalSample = function(sample, schema) {
    var no_identifiers =  ["legalEntity", "arrangement",
                           "anonymousEntity", "unknownEntity",
                           "anonymousPerson", "unknownPerson"];
    var unknown_types = ["anonymousEntity", "unknownEntity",
                      "anonymousPerson", "unknownPerson"];
    var unknown_properties = ["addresses", "name", "alternateNames",
                              "nationalities"]
    var modified = sample.statementGroups.forEach(function (sg) {
        Object.keys(sg).forEach( function (arr) {
                    if (flat_arrays.includes(arr)) {
                       delete sg[arr];
                    }
                    if (arr === 'beneficialOwnershipStatements') {
                        sg[arr].forEach(function (bos) {
                            bos.interestedParty = fakeInterestedParty(schema);
                        });
                    }
                });
    });
    modified = JSON.parse(JSON.stringify(sample), function(key, value) {
        if(key === "identifiers" && no_identifiers.includes(this.type)) {
            return undefined;
        }
        if (unknown_properties.includes(key)  && unknown_types.includes(this.type)) {
            return undefined;
        }
        if (key === "share") {
            if (this.type === "shareholding") {
                return postProcessShare(value);
            } else {
                return undefined;
            }
        }
        if (key === 'fullName') {
            return this.givenName + " " + this.familyName;
        }
        if (key === 'alternateNames') {
            this.name = value[0].fullName;
        }
        return value;
    });
    return modified;
}

var pickOne = function(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
};

var fakeInterestedParty = function(schema){
    var nestedInterestPartyStatements = [schema.definitions.PersonStatement,
                                         schema.definitions.EntityStatement, 
                                         schema.definitions.NullParty];
    return fakeSchemaChunk(schema, pickOne(nestedInterestPartyStatements));
};

var postProcessBlankSample = function (sample, schema) {
    // workaround to create samples for nested objects that otherwise aren't guaranteed to generate
    var modified = sample;
    var nestedInterestPartyStatements = [schema.definitions.PersonStatement,
                                         schema.definitions.EntityStatement, 
                                         schema.definitions.NullParty]
    modified.statementGroups[0].beneficialOwnershipStatements[0].interestedParty = 
    fakeSchemaChunk(schema, pickOne(nestedInterestPartyStatements));
    if (!("source" in sample.statementGroups[0].beneficialOwnershipStatements[0])) {
        var newSource = fakeSchemaChunk(schema, schema.definitions.Source);
        modified.statementGroups[0].beneficialOwnershipStatements[0].source = newSource;
    }
    if (!("replacesStatement" in sample.statementGroups[0].beneficialOwnershipStatements[0])) {
        var newRP = fakeSchemaChunk(schema, schema.definitions.ReplacesStatement);
        modified.statementGroups[0].beneficialOwnershipStatements[0].replacesStatement = newRP;
    }

    // remove flat arrays used in flat publishing structure
    Object.keys(modified.statementGroups[0]).forEach( function (k) {
        if(flat_arrays.includes(k)) {
            delete modified.statementGroups[0][k];
        }
    });
    return modified;
};

var fakeSchemaChunk = function (schema, schemaChunk, chunkKey="k", withKey = false) {
    // fake a bit of a schema
    var modifiedSchema = {"properties": {}};
    modifiedSchema.properties[chunkKey] = schemaChunk; 
    modifiedSchema.definitions = schema.definitions;
    if (withKey) {
        return jsf(modifiedSchema);
    }
    return jsf(modifiedSchema)[chunkKey];
};

var makeSample = function(schema, patches) {
    //console.log(patches);
    var modifiedSchema = schema;
    var sample;
    if (program.blank) {
        if (!program.crossref) {
            modifiedSchema = applyHierarchicalPatches(modifiedSchema, patches);
        }
        modifiedSchema = makeBlank(modifiedSchema);
        modifiedSchema.definitions.BeneficialOwnershipStatement.required = Object.keys(modifiedSchema.definitions.BeneficialOwnershipStatement.properties);
        if (program.debugschema) {
            console.log(JSON.stringify(modifiedSchema, null, 2));
            return;
        }
        sample = jsf(modifiedSchema);
        sample = postProcessBlankSample(sample, modifiedSchema);
        console.log(JSON.stringify(sample, null, 2));
        return;
    } else {
        modifiedSchema = applyCommonPatches(jsonschema, patches);
        if (! program.crossref) {
            modifiedSchema = applyHierarchicalPatches(modifiedSchema, patches);
            modifiedSchema = modifyForFaker(modifiedSchema);
            if (program.debugschema) {
                console.log(JSON.stringify(modifiedSchema, null, 2));
                return;
            }
            sample = jsf(modifiedSchema);
            sample = postProcessHierarchicalSample(sample, modifiedSchema);
            console.log(JSON.stringify(sample, null, 2));
            return;
        } else {
            throw new Error('Cross-referenced example data not implemented yet');
        }

    }
}

    


/*    if (!program.crossref) {
            applyHierarchicalPatches(jsonschema, schemapatches);
            //jsonschema = modifySchema(jsonschema);
            jsonschema = modifyForFaker(jsonschema);
            if (program.blank) {
                jsonschema = makeBlank(jsonschema);
            }
            if (program.debugschema) {
                console.log(JSON.stringify(jsonschema, null, 2));
            }
            else {
                sample = jsf(jsonschema);
                sample = postProcessHierarchicalSample(sample);
                console.log(JSON.stringify(sample, null, 2));
            }
        }
    else {
        applyCrossReferencedPatches(jsonschema, schemapatches);
        jsonschema = modifySchema(jsonschema);
        if (program.debugschema) {
            console.log(JSON.stringify(jsonschema, null, 2));
        }
            else {
                postProcessCrossrefencedSample(jsonschema);
            }

        }
};*/

if (require.main === module) {
    makeSample(jsonschema, schemapatches);
}

