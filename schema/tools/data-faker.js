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
    // remove arrays of top-level statements for cross-ref publication
    delete statementGroups.properties.entityStatements;
    delete statementGroups.properties.personStatements;
    delete statementGroups.properties.qualificationStatements;
    delete statementGroups.properties.provenanceStatements;
}
else {
    // adjust schema for cross-referenced publication
    jsonschema.definitions
        .BeneficialOwnershipStatement
        .properties.entity = {"$ref": "#/definitions/StatementReference"};
}

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
            prop === 'country' ||
            prop === 'nationalities') {
            def.faker = 'address.countryCode';
        }
        if (prop === 'address') {
            def.faker = 'address.streetAddress';
        }
        // conflating natural person and company names
        if (prop === 'name') {
            def.faker = 'company.companyName';
        }
        if (prop === 'postCode') {
            def.faker = 'address.zipCode';
        }
        if (prop === 'fullName') {
            def.faker = 'name.findName';
        }
        if (prop === 'startDate' || prop === 'endDate') {
            def.format = 'date-time';
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
sample = jsf(jsonschema);
console.log(JSON.stringify(sample, null, 2))
if (program.debugschema) {
    console.log(JSON.stringify(jsonschema, null, 2));
}
else {
    sample = jsf(jsonschema);
    console.log(JSON.stringify(sample, null, 2));
}


