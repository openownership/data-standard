.. _functional-requirements:

Functional requirements
=======================

The Beneficial Ownership Data Standard can accommodate data from a range of sources. Collection and publication systems need to ensure that this data is of high quality and that it can be shared efficiently. They therefore need to meet the following functional requirements:

* Source systems should keep a full audit log with the source of data and changes made to data;

* Publication systems should assign a unique identifier to each statement produced;

* Publication systems should be able to assert when one statement replaces another;

* Publication systems should be able to produce statements in JSON format;

* Publication systems should be able to validate statements against the JSON schema;

* Statements should be immutable.
