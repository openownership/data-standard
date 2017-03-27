faker = require('faker');
traverse = require('traverse');

module.exports = {
  readjson: function (filename) {
    return JSON.parse(require('fs')
        .readFileSync(require('path')
            .resolve(
                filename), 'utf8'));
  },

  writejson: function (obj, filename) {
        require('fs')
        .writeFile(require('path')
            .resolve(filename),
            JSON.stringify(obj, null, 2));
  },

copyWithNewIds: function(obj) {
    /**
    * Returns a copy of the object with all id attributes regenerated using faker random.uuid.
    */
    var entity = JSON.parse(JSON.stringify(obj));
    var idd = traverse(entity).map(function (x) {
        if (this.key === "id") this.update(faker.random.uuid());
    });
    return idd;
},

makeBlank: function(schema) {
    /**
    * Traverse the object and set to blank: NOT FINISHED
    */
    var blankschema = JSON.parse(JSON.stringify(schema));
    var idd = traverse(blankschema).map(function (x) {
        if (this.key === "enum") {
            this.update([""]);
        }
    });
    return idd;

},

interestedPartyAsEntity: function(bos) {
    /**
    * Takes a beneficial ownership statement and returns 
    */
}
    

};

//module.exports.blank = module.exports.readjson("../../examples/blank-example.json");


