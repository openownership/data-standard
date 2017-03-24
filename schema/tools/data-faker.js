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



// add common definitions for faker formats
// patch in company and natural person names
jsonschema.definitions.PersonName = schemapatches.definitions.PersonName;
jsonschema.definitions.PersonStatement.properties.name = {"$ref": "#/definitions/PersonName"};
jsonschema.definitions.CompanyName = schemapatches.definitions.CompanyName;
jsonschema.definitions.EntityStatement.properties.name = {"$ref": "#/definitions/CompanyName"};

// patch in identifiers - missing software agents
jsonschema.definitions.PersonIdentifier = schemapatches.definitions.PersonIdentifier;
jsonschema.definitions.CompanyIdentifier =   schemapatches.definitions.CompanyIdentifier;
jsonschema.definitions.EntityStatement.properties.identifiers = {"type": "array",
"items": {"$ref": "#/definitions/CompanyIdentifier"}};
jsonschema.definitions.PersonStatement.properties.identifiers = {"type": "array",
"items": {"$ref": "#definitions/PersonIdentifier"}};

//patch in fuzzy dates
jsonschema.definitions.FuzzyDate = schemapatches.definitions.FuzzyDate;
jsonschema.definitions.PersonStatement.properties.birthDate = {"$ref": "#/definitions/FuzzyDate"};
jsonschema.definitions.PersonStatement.properties.deathDate = {"$ref": "#/definitions/FuzzyDate"};
jsonschema.definitions.EntityStatement.properties.createdDate = {"$ref": "#/definitions/FuzzyDate"};
jsonschema.definitions.EntityStatement.properties.endDate = {"$ref": "#/definitions/FuzzyDate"};
jsonschema.definitions.Interest.properties.startDate = {"$ref": "#/definitions/FuzzyDate"};
jsonschema.definitions.Interest.properties.endDate = {"$ref": "#/definitions/FuzzyDate"};


var beneficialOwnershipStatement = jsonschema.definitions.BeneficialOwnershipStatement;
var statementGroups = jsonschema.properties.statementGroups;

if (!program.crossref) {
    // adjust schema for nested publication
    beneficialOwnershipStatement.required = ["entity"];
    beneficialOwnershipStatement.anyOf = [
        {"required": ["interestedParty"]},
        {"required": ["qualifications"]}
    ];
    // replace StatementReference from oneOf in nested properties
    beneficialOwnershipStatement.properties.entity = {"$ref": "#/definitions/EntityStatement"};
    beneficialOwnershipStatement.properties.interestedParty = {
          "oneOf": [
            {
              "$ref": "#/definitions/EntityStatement"
            },
            {
              "$ref": "#/definitions/PersonStatement"
            }
          ]
        };
    beneficialOwnershipStatement.properties.qualifications.items = { "$ref": "#/definitions/QualificationStatement"};
    beneficialOwnershipStatement.properties.provenance = {"$ref": "#/definitions/ProvenanceStatement" };
    jsonschema.definitions.PersonStatement.properties.provenance = {"$ref": "#/definitions/ProvenanceStatement" };
    jsonschema.definitions.EntityStatement.properties.provenance = {"$ref": "#/definitions/ProvenanceStatement" };
    jsonschema.definitions.QualificationStatement.properties.provenance = {"$ref": "#/definitions/ProvenanceStatement" };


    // remove arrays of top-level statements for cross-ref publication
    delete statementGroups.properties.entityStatements;
    delete statementGroups.properties.personStatements;
    delete statementGroups.properties.qualificationStatements;
    delete statementGroups.properties.provenanceStatements;
    // adjust provenance types and names
    jsonschema.definitions.ProvenanceStatement.required = ["attributedTo", "id"];
    // patch in attributedTo, with oneOf constraint
    jsonschema.definitions.ProvenanceStatement.properties.attributedTo = schemapatches.definitions.attributedTo;

}
else {
    // patch in statement references
    jsonschema.definitions.StatementReference = schemapatches.definitions.StatementReference;
    jsonschema.definitions.EntityStatementReference = schemapatches.definitions.EntityStatementReference;
    jsonschema.definitions.PersonStatementReference = schemapatches.definitions.PersonStatementReference;
    jsonschema.definitions.QualificationStatementReference = schemapatches.definitions.QualificationStatementReference;
    jsonschema.definitions.ProvenanceStatementReference = schemapatches.definitions.ProvenanceStatementReference;
    
    beneficialOwnershipStatement.properties.entity = {"$ref": "#/definitions/EntityStatementReference"};
    beneficialOwnershipStatement.properties.interestedParty = {
          "oneOf": [
            {
              "$ref": "#/definitions/EntityStatementReference"
            },
            {
              "$ref": "#/definitions/PersonStatementReference"
            }
          ]
        };
    beneficialOwnershipStatement.properties.qualifications.items = { "$ref": "#/definitions/QualificationStatementReference"};
    beneficialOwnershipStatement.properties.provenance = {"$ref": "#/definitions/ProvenanceStatementReference"};
};

var modifySchema = function(schema) {
    var change_definition = function(def, prop) {

        delete def.title
        delete def.description
    
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
            def.items.faker = 'address.countryCode'
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
            modifySchema(def)
        }
        if (def.format === 'date') {
            def.format = 'date-time'
        }
        if (def.format && def.format === 'uri') {
            def.format = 'URI'
        }

        // generate blank data
        if (program.blank) {
          if (def.type === 'array') {
            def.minItems = 1
            def.maxItems = 1
          }
          if (def.type === 'string') {
            delete def.format
            def.enum = [""]
          }
          if (def.type === 'number') {
            def.enum = [0]
          }
          if (def.type === 'boolean') {
            def.enum = [false]
          }
        }
    }
    var prop;
    var definition;

    for (prop in schema.properties) {
      var def = schema.properties[prop]
      change_definition(def, prop)
    }

    if (schema.definitions) {
        for (definition in schema.definitions) {
            if (schema.definitions[definition].hasOwnProperty('properties')) {
              modifySchema(schema.definitions[definition])
            } else {
              change_definition(schema.definitions[definition])
            }
        }
    }

    return schema
}

jsonschema = modifySchema(jsonschema);

if (program.debugschema) {
    console.log(JSON.stringify(jsonschema, null, 2));
}
else {
    sample = jsf(jsonschema);
    console.log(JSON.stringify(sample, null, 2));
}


