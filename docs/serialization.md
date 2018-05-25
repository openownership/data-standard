Serialization
=============

The beta specification does not contain detailed information on serialization. We have currently modelled the schema with the option for:

* (1) Entity, person and provenance statements to be nested inside a beneficial ownership statement;
* (2) Each kind of statement to be provided at the same level of heiarchy, with a cross-reference between them;

This second option is sketched out with a view of serialisations that may make use of the [JSON Lines](http://jsonlines.org/) format for sharing or streaming large quantities of statements, rather than enclosing all statements ot be exchanged in a single object. 

However, the specification, defined by a JSON Schema, is designed to support:

* Nested JSON documents; 
* Individual statements expressed using JSON lines;
* XML representation
* Flattened representations in CSV or Excel;
* JSON-LD; 

See the [initial conceptual model document for more](https://docs.google.com/document/d/1-nvxqKLVkWHOpu1bbr3s7E_ZCO416MrjjIMzivYjPgQ/edit#heading=h.4b74mxz3j34d).
