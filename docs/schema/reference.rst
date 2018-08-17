.. _schema-reference:

Schema reference
================

.. attention:: 
    
    This is **beta 2** of the Beneficial Ownership Data Standard. It includes updates to the data model and additional codelist information. Implementers should be aware that future changes are anticipated, before a version 1.0 release. See the :doc:`Changelog <changelog>` and `About <../about>`_ pages for more information.

    **MUST** and **SHOULD** are used in the schema to denote required and recommended elements of the Standard, as defined in `RFC2119 <https://tools.ietf.org/html/rfc2119>`_.


The following is an A - Z guide to the objects of the Data Standard's schema. Details of each object's properties are provided in a table generated from the JSON schema. (For a structured view of how objects fit together in the JSON schema, use the :doc:`Schema browser <schema-browser>`.)

The top-level objects are `statements <key-concepts>`:

- `Beneficial ownership statements <#schema-ownership-or-control-statement>`_
- `Entity statements <#schema-entity-statement>`_
- `Person statements <#schema-person-statement>`_


Serialization
-------------

The canonical serialization of BODS data is as a `JSON document <https://tools.ietf.org/html/rfc8259>`_. A JSON BODS file SHOULD consists of a series of ordered statements within a top-level array. 

Each of the `entityStatements <#entitystatement>`_ or `personStatements <#personstatement>`_ referenced by a particular `ownershipOrControlStatement <#ownershiporcontrolstatement>`_  MUST appear before that particular statement in the ordered array. 

BODS data MAY also be serialized in tabular form, using the relative JSON Pointer from the statement root for each relevant field as the column header. 

For example, the extract:

.. code-block:: json
   
   [
    {
      "statementID": "e3c07f34-1810-4eed-b845-4d9f4d97f9d5",
      "statementType": "entityStatement",
      "identifiers": [
        {
          "scheme": "GB-COH",
          "id": "07444723"
        }
      ]
    },
    {
      "statementID":"a2b485be-e3b6-4fd7-8a6a-930e46cf9957",
      "statementType":"personStatement",
      "identifiers":[
        {
          "scheme":"MX-RFC",
          "id":"ABC680524P-76"
        }
      ]
    },
    {
      "statementID":"34b479f2-1681-4064-ab51-1e703fbafa",
      "statementType":"ownershipOrControlStatement"
    }
   ]

may be serialized in a table as:

.. list-table:: 
   :header-rows: 1

   * - statementID 
     - statementType 
     - identifiers/0/scheme 
     - identifiers/0/id
   * - e3c07f34-1810-4eed-b845-4d9f4d97f9d5
     - entityStatement
     - GB-COH
     - 07444723
   * - a2b485be-e3b6-4fd7-8a6a-930e46cf9957
     - personStatement
     - MX-RFC
     - ABC680524P-76

   * - 34b479f2-1681-4064-ab51-1e703fbafa
     - ownershipOrControlStatement
     - 
     - 


.. _id:

Statement Identifiers
---------------------

Each statement MUST have an entirely unique identifier. There MUST be no possibility of collision between identifiers for different statements. 

Publishers MAY use a guid or uuid as the statement identifier, a reproducible hash of the statement or unique components thereof, or an internal identifier combined with a unique prefix to avoid collision between identifiers from different publishers. 

The schema enforces a minimum statement identifier length of 32 characters, and maximum length of 64 characters. 

See :ref:`guidance on statement identifiers <guidance-statement-identifiers>` for more information.

Component Reference
-------------------

Statements are built up from a set of nested objects and properties, each of which has a field name, a title and a description that defines how the object or field should be used. 

**Statements:** `Ownership or control statements <#schema-ownership-or-control-statement>`_; `Entity statements <#schema-entity-statement>`_ `Person statements <#schema-person-statement>`_

**Components:** 



.. _schema-ownership-or-control-statement:

OwnershipOrControlStatement
+++++++++++++++++++++++++++

.. json-value:: ../../schema/ownership-or-control-statement.json
   :pointer: /description


.. jsonschema:: ../../schema/ownership-or-control-statement.json
    :collapse: interests,source,annotations,interestedParty

.. _schema-entity-statement:

EntityStatement
+++++++++++++++

.. json-value:: ../../schema/entity-statement.json
   :pointer: /description

.. jsonschema:: ../../schema/entity-statement.json
   :collapse: identifiers,addresses,source,incorporatedInJurisdiction,annotations

.. _schema-person-statement:

PersonStatement
+++++++++++++++

.. json-value:: ../../schema/person-statement.json
   :pointer: /description

.. jsonschema:: ../../schema/person-statement.json
   :collapse: names,identifiers,source,placeOfResidence,placeOfBirth,addresses,nationalities,annotations,pepStatus

.. _schema-interest:

Interest
++++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Interest/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Interest
   :collapse: share,annotations

.. _schema-interested-party:

InterestedParty
+++++++++++++++

.. json-value:: ../../schema/ownership-or-control-statement.json
   :pointer: /definitions/InterestedParty/description

.. jsonschema:: ../../schema/ownership-or-control-statement.json
   :pointer: /properties/interestedParty
   :collapse: 

.. _schema-share:

Share
+++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Interest/properties/share/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Interest/properties/share

.. _schema-jurisdiction:

Jurisdiction
++++++++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Jurisdiction/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Jurisdiction

.. _schema-country:

Country
+++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Country/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Country

.. _schema-name:

Name
++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Name/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Name

.. _schema-pep-status:

PEPStatus
+++++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/PepStatus/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/PepStatus
   :collapse: jurisdiction

.. _schema-identifier:

Identifier
++++++++++

The identifier component is used to connect a statement to the real-world person or entity that it refers to, using one or more existing known identifiers. See [Real world identifiers](identifiers.md) for technical guidance on when and how to use this component.

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Identifier/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Identifier

.. _schema-address:

Address
+++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Address/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Address


.. note::

    Due to the diversity of address formats used across systems, and the extent to which data is inconsistently entered across these data fields in source systems and legacy datasets, the schema uses a very simple address format for data exchange - relying upon consuming systems to parse addresses before carrying out any structured comparison. However, designers of new data collection systems are encouraged to choose an appropriate structured format, with reference to established standards, and awareness of the need to accomodate addresses from across the world. See `issue 18 <https://github.com/openownership/data-standard/issues/18>`_ for more details.

.. _schema-source:

Source
++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Source/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Source
   :collapse: assertedBy


See :any:`the provenance pages <provenance>` for a discussion of provenance modelling.

.. _schema-agent:

Agent
++++++

.. json-value:: ../../schema/components.json
   :pointer: /definitions/Agent/description

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Agent
   :collapse:


.. _schema-annotation:

Annotation
++++++++++

The annotation property currently allows for an array of simple annotation objects. This is a placeholder which could be extended in future to include structured information qualifying the nature of the interest held.

.. jsonschema:: ../../schema/components.json
   :pointer: /definitions/Annotation

.. _schema-statement-date:

StatementDate
+++++++++++++

Dates MUST be provided according to `ISO 8601 <https://en.wikipedia.org/wiki/ISO_8601>`_ in one of the following formats:

* A full datetime string (YYYY-MM-DDTHH:MM:SSZ)
* A year, month and day (YYYY-MM-DD)
* A year and month (YYYY-MM)
* A year (YYYY)


.. _schema-replaces-statements:

ReplacesStatements
++++++++++++++++++

``replacesStatements``

.. json-value:: ../../schema/components.json
   :pointer: /definitions/ReplacesStatements/description

See :any:`handling changing data <guidance-updating-data>` for technical guidance on working with updates to date. 

.. _schema-codelists:

Codelists
---------

AddressType
+++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/addressType.csv


AnnotationMotivation
++++++++++++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/annotationMotivation.csv


EntityType
++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/entityType.csv


InterestLevel
+++++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/interestLevel.csv


InterestType
++++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/interestType.csv


NameType
++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/nameType.csv


PersonType
++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/personType.csv


SourceType
++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/sourceType.csv


StatementType
+++++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/statementType.csv


UnspecifiedReason
+++++++++++++++++

.. csv-table::
   :header-rows: 1
   :class: codelist-table
   :file: ../../schema/codelists/unspecifiedReason.csv


Normative references
--------------------

* JSON: https://tools.ietf.org/html/rfc8259 

