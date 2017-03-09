#!/usr/bin/env node

var program = require('commander');
var jsf = require('json-schema-faker');
var faker = require('faker');
var schema

program
    .option('-b --blank', 'Blank data')
    .parse(process.argv);



var jsonschema = 
    JSON.parse(
        require('fs').readFileSync(
            require('path').resolve(
                __dirname, 
                '../beneficial-ownership-statements.json'),
            'utf8'));



jsf.format('URI', function(gen, jsonschema) {
    return gen.randexp('^http://[A-Za-z0-9]+\\.com$');
});

jsf.option({
    alwaysFakeOptionals: true
});


var modifySchema = function(schema) {
    var change_definition = function(def, prop) {

        delete def.title
        delete def.description
    
        if (prop === 'id') {
            def['minLength'] = 20;
            def['type'] = 'string';
            def['faker'] = 'random.uuid';
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
