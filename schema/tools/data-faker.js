#!/usr/bin/env node

var program = require('commander');
var jsf = require('json-schema-faker');
var faker = require('faker');
var schema;

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

jsf.option({
    alwaysFakeOptionals: true
});

var minBeneficialOwnershipStatements = 1;
var beneficialOwnershipStatement = jsonschema.definitions.BeneficialOwnershipStatement;
var statementGroups = jsonschema.properties.statementGroups;
var flat_arrays = ["qualificationStatements", "entityStatements",
                   "personStatements", "provenanceStatements"];

var applyCommonPatches = function(original, patched) {
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

    //patch in fuzzy dates
    original.definitions.FuzzyDate = patched.definitions.FuzzyDate;
    original.definitions.PersonStatement.properties.birthDate = {"$ref": "#/definitions/FuzzyDate"};
    original.definitions.PersonStatement.properties.deathDate = {"$ref": "#/definitions/FuzzyDate"};
    original.definitions.EntityStatement.properties.foundingDate = {"$ref": "#/definitions/FuzzyDate"};
    original.definitions.EntityStatement.properties.dissolutionDate = {"$ref": "#/definitions/FuzzyDate"};
    original.definitions.Interest.properties.startDate = {"$ref": "#/definitions/FuzzyDate"};
    original.definitions.Interest.properties.endDate = {"$ref": "#/definitions/FuzzyDate"};
};

var applyHierarchicalPatches = function(original, patched) {
    // adjust schema for nested publication
    original.definitions.BeneficialOwnershipStatement.required = ["entity"];
    original.definitions.BeneficialOwnershipStatement.anyOf = [
        {"required": ["interestedParty"]},
        {"required": ["qualifications"]}
    ];
    // replace StatementReference from oneOf in nested properties
    original.definitions.BeneficialOwnershipStatement.properties.entity = {"$ref": "#/definitions/EntityStatement"};
    original.definitions.BeneficialOwnershipStatement.properties.interestedParty = {
          "oneOf": [
            {
              "$ref": "#/definitions/EntityStatement"
            },
            {
              "$ref": "#/definitions/PersonStatement"
            }
          ]
        };
    

    // remove arrays of top-level statements for cross-ref publication
    // adjust provenance types and names
    
    // patch in attributedTo, with oneOf constraint
    
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
    original.definitions.ProvenanceStatementReference = patched.definitions.ProvenanceStatementReference;
    
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

var modifySchema = function (schema) {
    var change_definition = function(def, prop) {

        if (def.hasOwnProperty('title')) {
            delete def.title;
        }

        if (def.hasOwnProperty('description')) {
            delete def.description;
        }
    
        if (prop === 'id') {
            def['minLength'] = 20;
            def['type'] = 'string';
            def['faker'] = 'random.uuid';
        }
        if (prop === 'jurisdiction' ||
            prop === 'country')  {
            def.faker = 'address.countryCode';
        }

        if (prop === 'nationalities') {
            def.items.faker = 'address.countryCode';
        }

        if (prop === 'address') {
            def.faker = 'address.streetAddress';
        }

        if (prop === 'postCode') {
            def.faker = 'address.zipCode';
        }
        if (prop === 'fullName') {
            def.faker = 'name.findName';
        }
        if (def.type === 'object') {
            modifySchema(def);
        }
        if (def.format === 'date') {
            def.format = 'date-time';
        }
        if (def.format && def.format === 'uri') {
            def.format = 'URI';
        }

        // generate blank data
        if (program.blank) {
               
          if (def.type === 'array') {
            def.minItems = 1;
            def.maxItems = 1;
          }
          if (def.type === 'string') {
            delete def.faker;
            delete def.format;
            def.enum = [""];
          }
          if (def.type === 'number') {
            def.enum = [0];
          }
          if (def.type === 'boolean') {
            def.enum = [false];
          }


        }
    }
    var prop;
    var definition;

    for (prop in schema.properties) {
      var def = schema.properties[prop];
      change_definition(def, prop);
    }

    if (schema.definitions) {
        for (definition in schema.definitions) {
            if (schema.definitions[definition].hasOwnProperty('properties')) {
              modifySchema(schema.definitions[definition]);
          } else {
              change_definition(schema.definitions[definition]);
            }
        }
    }

    return schema
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

var makeSample = function() {
    applyCommonPatches(jsonschema, schemapatches);

    if (!program.crossref) {
            applyHierarchicalPatches(jsonschema, schemapatches);
            jsonschema = modifySchema(jsonschema);
            if (program.debugschema) {
                console.log(JSON.stringify(jsonschema, null, 2));
            }
            else {
                sample = jsf(jsonschema);
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
};

if (require.main === module) {
    makeSample();
}

