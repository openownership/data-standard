.. _schema-reference:

Schema reference
================

.. include:: warningbox.rst

This is an A - Z guide to the objects of the Data Standard's schema and its `codelists`_ . Details of each object's properties are provided in a table. For a structured view of how objects fit together in the JSON schema, use the :doc:`Schema browser <schema-browser>`.

The top-level objects are :any:`Statements <schema-statement>`. Each statement contains record details for one of three beneficial ownership elements:

- :any:`Entity <schema-entity-record>`
- :any:`Person <schema-person-record>`
- :any:`Relationship <schema-relationship-record>`

BODS data MAY be published as a valid `JSON document <https://tools.ietf.org/html/rfc8259>`_. See :any:`Serialisation <guidance-serialisation>` for other options.


.. _schema-address:

Address
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Address/description

.. jsonschema:: ../_build_schema/components.json
   :collapse: country
   :pointer: /$defs/Address
   :externallinks: {"type":{"url":"#address-type","text":"Address Type"}}
   :allowexternalrefs:
   :allowurnrefs:


.. note::

     Various address formats are used across data management systems, and data is often inconsistent. That is why the BODS schema uses a simple address format for data exchange. Systems importing BODS data will need to parse BODS addresses before carrying out any structured comparison.

     Designers of new data collection systems should choose an appropriate structured format, with reference to established standards, that can accommodate addresses from across the world. See `issue 18 <https://github.com/openownership/data-standard/issues/18>`_ for more details.

.. _schema-annotation:

Annotation
----------

The ``annotations`` property of statements is an array of Annotation objects. 

Annotations can be used to:

* hold information that does not have an appropriate field in the schema
* provide additional context to information in the schema (e.g. if data has been transformed) 

Annotations can apply to a whole statement, part of a statement or a specific field. ``annotation.statementPointerTarget`` indicates where the annotation applies. 

.. jsonschema:: ../_build_schema/statement.json
   :pointer: /$defs/Annotation
   :externallinks: {"motivation":{"url":"#annotation-motivation","text":"Annotation Motivation"}}
   :allowexternalrefs:
   :allowurnrefs:


.. _schema-country:

Country
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Country/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Country
   :allowexternalrefs:
   :allowurnrefs:


.. _schema-identifier:

Identifier
----------

The Identifier object connects a statement to the natural person, entity or item that it refers to. See :any:`Real world identifiers <guidance-identifiers>` for guidance on using this object.

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Identifier/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Identifier
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-interest:

Interest
--------

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest/description

.. jsonschema:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest
   :collapse: share
   :externallinks: {"share":{"url":"#share","text":"Share"}, "type":{"url":"#interest-type","text":"Interest Type"}}
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-jurisdiction:


Jurisdiction
------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Jurisdiction/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Jurisdiction
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-name:

Name
----

.. json-value:: ../_build_schema/person-record.json
   :pointer: /$defs/Name/description

.. jsonschema:: ../_build_schema/person-record.json
   :pointer: /$defs/Name
   :externallinks: {"type":{"url":"#name-type","text":"Name Type"}}
   :allowexternalrefs:
   :allowurnrefs:


.. _schema-pep-status:

PEPstatusDetails
------------------

.. json-value:: ../_build_schema/person-record.json
   :pointer: /$defs/PepStatusDetails/description

.. jsonschema:: ../_build_schema/person-record.json
   :pointer: /$defs/PepStatusDetails
   :collapse: jurisdiction,source
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-public-listing:

PublicListing
--------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /$defs/PublicListing/description

.. jsonschema:: ../_build_schema/entity-record.json
   :pointer: /$defs/PublicListing
   :collapse: securitiesListings
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-publicationdetails:

Publication Details
-------------------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/publicationDetails/description

.. jsonschema:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/publicationDetails
   :collapse: publisher
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-publisher:

Publisher
---------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/publicationDetails/properties/publisher/description

.. jsonschema:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/publicationDetails/properties/publisher
   :allowexternalrefs:
   :allowurnrefs:


.. _schema-entity-record:

Record Details (entity)
------------------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /description

.. jsonschema:: ../_build_schema/entity-record.json
   :collapse: identifiers,addresses,jurisdiction,publicListing,unspecifiedEntityDetails
   :externallinks: {"entityType/type":{"url":"#entity-type","text":"Entity Type"},"entityType/subtype":{"url":"#entity-subtype","text":"Entity Subtype"}}
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-person-record:

Record Details (person)
------------------------

.. json-value:: ../_build_schema/person-record.json
   :pointer: /description

.. jsonschema:: ../_build_schema/person-record.json
   :collapse: names,identifiers,placeOfBirth,addresses,nationalities,politicalExposure/details,taxResidencies,unspecifiedPersonDetails
   :externallinks: {"personType":{"url": "#person-type","text":"Person Type"}}
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-relationship-record:

Record Details (relationship)
-------------------------------

See :ref:`representing-bo` for detailed requirements.

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /description

.. jsonschema:: ../_build_schema/relationship-record.json
   :collapse: interests
   :allowexternalrefs:
   :allowurnrefs:


.. _schema-record-id:

Record Id
---------

See :ref:`record-identifiers` for information about Record Ids 

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/recordId/description

.. _schema-securities-listing:

SecuritiesListing
------------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /$defs/SecuritiesListing/description

See :any:`Real world identifiers <guidance-identifiers>` for guidance on representing securities listings.

.. jsonschema:: ../_build_schema/entity-record.json
   :pointer: /$defs/SecuritiesListing
   :externallinks: {"security/idScheme":{"url":"#securities-identifier-schemes","text":"Securities Identifier Schemes"}}
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-share:

Share
-----

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest/properties/share/description

.. jsonschema:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest/properties/share
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-source:

Source
------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Source/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Source
   :externallinks: {"type":{"url":"#source-type","text":"Source Type"}}
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-statement:

Statement
---------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/description

.. jsonschema:: ../_build_schema/statement.json
   :pointer: /$defs/Statement
   :collapse: source,annotations,publicationDetails
   :externallinks: {"recordStatus":{"url":"#record-status","text":"Record Status"},"recordId":{"url":"#record-id","text":"Record Id"},"statementId":{"url":"#statement-id","text":"Statement Id"},"publicationDetails":{"url":"#publication-details","text":"Publication Details"},"recordDetails":{"url":"#record-details-entity","text":"Record details"}}
   :allowexternalrefs:
   :allowurnrefs:

.. _schema-statement-id:

Statement Id
------------

See :ref:`generating-statements` for advice on generating unique Statement Ids

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/statementId/description

.. _schema-unspecified-record:

UnspecifiedRecord
-----------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/UnspecifiedRecord/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/UnspecifiedRecord
   :externallinks: {"reason":{"url":"#unspecified-reason","text":"Unspecified Reason"}}
   :allowexternalrefs:
   :allowurnrefs:


.. _schema-codelists:

Codelists
---------

Address Type
++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/addressType.csv


Annotation Motivation
+++++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/annotationMotivation.csv


Direct Or Indirect
++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/directOrIndirect.csv


Entity Type
+++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/entityType.csv



Entity Subtype
+++++++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/entitySubtype.csv



Interest Type
+++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/interestType.csv


Name Type
+++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/nameType.csv


Person Type
+++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/personType.csv


Record Status
+++++++++++++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/recordStatus.csv



Record Type
+++++++++++++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/recordType.csv


Securities Identifier Schemes
+++++++++++++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/securitiesIdentifierSchemes.csv


Source Type
+++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/sourceType.csv


Unspecified Reason
++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/unspecifiedReason.csv


