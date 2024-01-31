.. _schema-reference:

Schema reference
================

.. include:: warningbox.rst

The following is an A - Z guide to the objects of the Data Standard's schema, plus its `codelists`_ . Details of each object's properties are provided in a table generated from the JSON schema. (For a structured view of how objects fit together in the JSON schema, use the :doc:`Schema browser <schema-browser>`.)

The top-level objects are :doc:`statements <concepts>`:

- :any:`Ownership-or-control statements <schema-ownership-or-control-statement>`
- :any:`Entity statements <schema-entity-statement>`
- :any:`Person statements <schema-person-statement>`

Statements are built up from a set of nested objects and properties, each of which has a field name, a title and a description that defines how the object or field should be used.

BODS data MAY be published as a valid `JSON document <https://tools.ietf.org/html/rfc8259>`_. See :any:`Serialization <guidance-serialization>` for more options.


.. _schema-address:

Address
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Address/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Address
   :externallinks: {"type":{"url":"#address-type","text":"Address Type"}}
   :allowexternalrefs:


.. note::

    A diversity of address formats are used across data management systems, and data is often inconsistently entered across data fields in these source systems (and legacy datasets). Therefore the BODS schema uses a very simple address format for data exchange. Consuming systems will need to parse BODS addresses before carrying out any structured comparison.

    Designers of new data collection systems are encouraged to choose an appropriate structured format, with reference to established standards, and awareness of the need to accomodate addresses from across the world. See `issue 18 <https://github.com/openownership/data-standard/issues/18>`_ for more details.

.. _schema-agent:

Agent
-----

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Agent/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Agent
   :collapse:
   :allowexternalrefs:

.. _schema-annotation:

Annotation
----------

The ``annotations`` property of statements currently allows an array of these simple annotation objects to be included. An annotation can be used to hold information (structured or otherwise) for which a place does not exist elsewhere in the schema. See :ref:`Sources and annotations <provenance>` for further guidance.

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Annotation
   :externallinks: {"motivation":{"url":"#annotation-motivation","text":"Annotation Motivation"}}
   :allowexternalrefs:

.. _schema-country:

Country
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Country/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Country
   :allowexternalrefs:


.. _schema-entity-statement:

Entity Statement
----------------

.. json-value:: ../_build_schema/entity-statement.json
   :pointer: /description

.. jsonschema:: ../_build_schema/entity-statement.json
   :collapse: identifiers,addresses,source,jurisdiction,annotations,publicationDetails,publicListing
   :externallinks: {"statementDate":{"url":"#statement-date","text":"Statement Date"},"entityType":{"url":"#entity-type","text":"Entity Type"},"entitySubtype/generalCategory":{"url":"#entity-subtype-category","text":"Entity Subtype Category"}, "unspecifiedEntityDetails/reason":{"url":"#unspecified-reason","text":"Unspecified Reason"},"replacesStatements":{"url":"#replaces-statements","text":"Replaces Statements"},"publicationDetails":{"url":"#publication-details","text":"Publication Details"},"publicListing":{"url":"#public-listing","text":"Public Listing"}}
   :allowexternalrefs:

.. _schema-id:

ID
--

A string of minimum length 32 and maximum length 64.

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/ID/description

.. _schema-identifier:

Identifier
----------

The Identifier object is used to connect a statement to the real-world person or entity that it refers to, using one or more existing known identifiers. See :any:`Real world identifiers <guidance-identifiers>` for technical guidance on when and how to use this object.

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Identifier/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Identifier
   :allowexternalrefs:

.. _schema-interest:

Interest
--------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Interest/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Interest
   :collapse: share
   :externallinks: {"share":{"url":"#share","text":"Share"}, "type":{"url":"#interest-type","text":"Interest Type"}}
   :allowexternalrefs:

.. _schema-interested-party:

Interested Party
----------------

.. json-value:: ../_build_schema/ownership-or-control-statement.json
   :pointer: /$defs/InterestedParty/description

.. jsonschema:: ../_build_schema/ownership-or-control-statement.json
   :pointer: /properties/interestedParty
   :collapse:
   :externallinks: {"unspecified/reason":{"url":"#unspecified-reason","text":"Unspecified Reason"}}
   :allowexternalrefs:

.. _schema-jurisdiction:

Jurisdiction
------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Jurisdiction/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Jurisdiction
   :allowexternalrefs:

.. _schema-name:

Name
----

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Name/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Name
   :externallinks: {"type":{"url":"#name-type","text":"Name Type"}}
   :allowexternalrefs:

.. _schema-ownership-or-control-statement:

Ownership Or Control Statement
------------------------------

If a person is a beneficial owner of an entity - whether directly or indirectly - and the person or entity is required to declare this beneficial ownership, there MUST be an Ownership-or-control Statement connecting the two which represents the beneficial ownership relationship. See :ref:`representing-bo` for detailed requirements.

.. json-value:: ../_build_schema/ownership-or-control-statement.json
   :pointer: /description


.. jsonschema:: ../_build_schema/ownership-or-control-statement.json
    :externallinks: {"statementDate":{"url":"#statement-date","text":"Statement Date"},"interestedParty":{"url":"#interested-party","text":"Interested Party"},"replacesStatements":{"url":"#replaces-statements","text":"Replaces Statements"},"publicationDetails":{"url":"#publication-details","text":"Publication Details"}}
    :collapse: interests,source,annotations,interestedParty,publicationDetails
    :allowexternalrefs:


.. _schema-pep-status:

PEP Status Details
------------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/PepStatusDetails/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/PepStatusDetails
   :collapse: jurisdiction,source
   :externallinks: {"source/type":{"url":"#source-type","text":"Source Type"}}
   :allowexternalrefs:

.. _schema-person-statement:

Person Statement
----------------

.. json-value:: ../_build_schema/person-statement.json
   :pointer: /description

.. jsonschema:: ../_build_schema/person-statement.json
   :collapse: names,identifiers,source,placeOfResidence,placeOfBirth,addresses,nationalities,annotations,politicalExposure/details,publicationDetails,taxResidencies
   :externallinks: {"statementDate":{"url":"#statement-date","text":"Statement Date"},"personType":{"url": "#person-type","text":"Person Type"}, "unspecifiedPersonDetails/reason":{"url":"#unspecified-reason","text":"Unspecified Reason"},"replacesStatements":{"url":"#replaces-statements","text":"Replaces Statements"},"publicationDetails":{"url":"#publication-details","text":"Publication Details"},"politicalExposure/details":{"url":"#pep-status-details","text":"PEP Status Details"}}
   :allowexternalrefs:


.. _schema-public-listing:

Public Listing
--------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/PublicListing/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/PublicListing
   :collapse: securitiesListings
   :externallinks: {"securitiesListings":{"url":"#securities-listing","text":"Securities Listing"}}
   :allowexternalrefs:

.. _schema-publicationdetails:

Publication Details
-------------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/PublicationDetails/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/PublicationDetails
   :collapse: publisher
   :allowexternalrefs:

.. _schema-publisher:

Publisher
---------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Publisher/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Publisher
   :allowexternalrefs:



.. _schema-replaces-statements:

Replaces Statements
-------------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/ReplacesStatements/description

See :any:`Updating statements <guidance-updating-data>` for technical guidance on working with updates to data.


.. _schema-securities-listing:

Securities Listing
------------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/SecuritiesListing/description

See :any:`Real world identifiers <guidance-identifiers-other>` for technical guidance on representing securities listings.


.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/SecuritiesListing
   :externallinks: {"security/idScheme":{"url":"#securities-identifier-schemes","text":"Securities Identifier Schemes"}}
   :allowexternalrefs:

.. _schema-share:

Share
-----

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Interest/properties/share/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Interest/properties/share
   :allowexternalrefs:


.. _schema-source:

Source
------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Source/description

.. jsonschema:: ../_build_schema/components.json
   :pointer: /$defs/Source
   :collapse: assertedBy
   :externallinks: {"type":{"url":"#source-type","text":"Source Type"}}
   :allowexternalrefs:


See :any:`Sources and annotations <provenance>` for a discussion of provenance modelling.

.. _schema-statement-date:

Statement Date
--------------

Dates MUST conform with the extended format of `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_. All of the following, for example, are valid:

* A full datetime string (YYYY-MM-DDTHH:MM:SSZ)
* A year, month and day (YYYY-MM-DD)

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



Entity Subtype Category
+++++++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/entitySubtypeCategory.csv



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


Statement Type
++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/statementType.csv


Unspecified Reason
++++++++++++++++++

.. csv-table-no-translate::
   :header-rows: 1
   :class: codelist-table
   :file: ../_build_schema/codelists/unspecifiedReason.csv


