.. _schema-reference:

Schema reference
================

.. include:: warningbox.rst

The following is an A - Z guide to the objects of the Data Standard's schema, plus its `codelists`_ . Details of each object's properties are provided in a table generated from the JSON schema. (For a structured view of how objects fit together in the JSON schema, use the :doc:`Schema browser <schema-browser>`.)

The top-level objects are :doc:`statements <concepts>`:

- :any:`Ownership-or-control statements <schema-relationship-record>`
- :any:`Entity statements <schema-entity-record>`
- :any:`Person statements <schema-person-record>`

Statements are built up from a set of nested objects and properties, each of which has a field name, a title and a description that defines how the object or field should be used.

BODS data MAY be published as a valid `JSON document <https://tools.ietf.org/html/rfc8259>`_. See :any:`Serialization <guidance-serialization>` for more options.


.. _schema-address:

Address
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Address/description


.. note::

    A diversity of address formats are used across data management systems, and data is often inconsistently entered across data fields in these source systems (and legacy datasets). Therefore the BODS schema uses a very simple address format for data exchange. Consuming systems will need to parse BODS addresses before carrying out any structured comparison.

    Designers of new data collection systems are encouraged to choose an appropriate structured format, with reference to established standards, and awareness of the need to accomodate addresses from across the world. See `issue 18 <https://github.com/openownership/data-standard/issues/18>`_ for more details.


Annotation
----------

The ``annotations`` property of statements currently allows an array of these simple annotation objects to be included. An annotation can be used to hold information (structured or otherwise) for which a place does not exist elsewhere in the schema. See :ref:`Sources and annotations <provenance>` for further guidance.

.. _schema-country:

Country
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Country/description


.. _schema-entity-record:

Entity Statement
----------------

.. json-value:: ../_build_schema/eentity-record.json
   :pointer: /description


.. _schema-identifier:

Identifier
----------

The Identifier object is used to connect a statement to the real-world person or entity that it refers to, using one or more existing known identifiers. See :any:`Real world identifiers <guidance-identifiers>` for technical guidance on when and how to use this object.

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Identifier/description


.. _schema-interest:

Interest
--------

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest/description


.. _schema-interested-party:


Jurisdiction
------------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Jurisdiction/description

.. _schema-name:

Name
----

.. json-value:: ../_build_schema/person-record.json
   :pointer: /$defs/Name/description


.. _schema-relationship-record:

Ownership Or Control Statement
------------------------------

If a person is a beneficial owner of an entity - whether directly or indirectly - and the person or entity is required to declare this beneficial ownership, there MUST be an Ownership-or-control Statement connecting the two which represents the beneficial ownership relationship. See :ref:`representing-bo` for detailed requirements.

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /description


.. _schema-pep-status:

PEP Status Details
------------------

.. json-value:: ../_build_schema/person-record.json
   :pointer: /$defs/PepStatusDetails/description

.. _schema-person-record:

Person Statement
----------------

.. json-value:: ../_build_schema/person-record.json
   :pointer: /description


.. _schema-public-listing:

Public Listing
--------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /$defs/PublicListing/description

.. _schema-publicationdetails:

Publication Details
-------------------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/publicationDetails/description

.. _schema-publisher:

Publisher
---------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/publicationDetails/properties/publisher/description


.. _schema-securities-listing:

Securities Listing
------------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /$defs/SecuritiesListing/description

See :any:`Real world identifiers <guidance-identifiers-other>` for technical guidance on representing securities listings.

.. _schema-share:

Share
-----

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest/properties/share/description

.. _schema-source:

Source
------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Source/description


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


