To install dependencies for these tools, cd into this directory an run

```
npm install .
```


Data Faker
----------

To generate fake data into a file run:

```
node data-faker.js > myfakedatafile.json
```

By default, data is genarated with entity, person, qualification and provenance statements nested in beneficial ownership statements.

To generate cross-referenced fake data, with benefical ownership, entity, person, qualification and provenance statements held in arrays in a statement group, run:

```
node data-faker.js -c > crossrefdatafile.json
```    

To generate a datafile with all the fields blank:

```
node data-faker.js -b > myblankdatafile.json
```

The fake data generator alters the schema, and uses data types from JSON Schema Faker, to create realistic-looking data. To generate a file with this altered schema, run:

```
node data-faker.js -d > alteredschema.json
```  
