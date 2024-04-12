.. _schema-reference:

Schema reference
================

.. include:: warningbox.rst

This is an A - Z guide to the schema's objects and `codelists`_ . For a structured view of how objects fit together in the JSON schema, use the :doc:`Schema browser <schema-browser>`.

The top-level objects are :any:`Statements <schema-statement>`. Each statement contains details of one of three types of system record:

- :any:`Ownership-or-control statements <schema-relationship-record>`
- :any:`Entity statements <schema-entity-record>`
- :any:`Person statements <schema-person-record>`

Statements are built up from a set of nested objects and properties, each of which has a field name, a title and a description that defines how the object or field should be used.

BODS data MAY be published as a valid `JSON document <https://tools.ietf.org/html/rfc8259>`_. See :any:`Serialisation <guidance-serialisation>` for other options.


.. _schema-address:

Address
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Address/description


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

Annotations can apply to a whole statement, part of a statement or a specific field. annotation.statementPointerTarget indicates where the annotation applies. 

.. _schema-country:

Country
-------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Country/description


.. _schema-entity-record:

Entity Record
----------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /description


.. _schema-identifier:

Identifier
----------

The Identifier object connects a statement to the natural person or entity that it refers to. See :any:`Real world identifiers <guidance-identifiers>` for technical guidance on how to use this object.

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


.. _schema-pep-status:

PEP Status Details
------------------

.. json-value:: ../_build_schema/person-record.json
   :pointer: /$defs/PepStatusDetails/description

.. _schema-person-record:

Person Record
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

.. _schema-record-id:

Record Id
---------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/recordId/description


.. _schema-relationship-record:

Relationship Record
-------------------

See :ref:`representing-bo` for detailed requirements.

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /description


.. _schema-securities-listing:

Securities Listing
------------------

.. json-value:: ../_build_schema/entity-record.json
   :pointer: /$defs/SecuritiesListing/description

See :any:`Real world identifiers <guidance-identifiers-other>` for guidance on representing securities listings.

.. _schema-share:

Share
-----

.. json-value:: ../_build_schema/relationship-record.json
   :pointer: /$defs/Interest/properties/share/description

.. _schema-source:

Source
------

.. json-value:: ../_build_schema/components.json
   :pointer: /$defs/Source/description

.. _schema-statement:

Statement
---------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/description

Statement Id
------------

.. json-value:: ../_build_schema/statement.json
   :pointer: /$defs/Statement/properties/statementId/description

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


