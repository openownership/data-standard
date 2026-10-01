.. _guidance-serialisation:

Serialisation
=============

The canonical serialisation of BODS data is as a JSON document. Equivalent specifications of JSON are given by `IETF RFC 8256 <https://tools.ietf.org/html/rfc8259>`_ and by `ECMA 404 <https://ecma-international.org/publications-and-standards/standards/ecma-404/>`_. It is RECOMMENDED that publishers:

- Use UTF-8 for maximal interoperability (section 8.1 of RFC 8259);
- Escape characters that might cause problems when ingesting data (for example: &, <).

See Section 9 of the ECMA-404 JSON specification which deals with strings, encoding and escaping.

JSON Lines MAY also be used when creating large files.

.. _serialisation-missing-values:

Missing values
--------------

Where a publisher has no value for an optional field, that field MUST be omitted from the statement. A field MUST NOT be present with a value of ``null``: the schema does not permit ``null`` for any field, so a statement containing one will fail validation. Empty strings SHOULD NOT be used to stand in for a missing value.

For example, an Entity statement for which no founding date or identifiers are known omits those fields:

.. code-block:: json

   {
     "recordDetails": {
       "isComponent": false,
       "entityType": {
         "type": "registeredEntity"
       },
       "name": "Example Ltd"
     }
   }

The following will not validate:

.. code-block:: json

   {
     "recordDetails": {
       "isComponent": false,
       "entityType": {
         "type": "registeredEntity"
       },
       "name": "Example Ltd",
       "foundingDate": null,
       "identifiers": null
     }
   }

Omitting a field says nothing about *why* the value is missing. Where the reason matters, the standard provides fields for it: ``unspecifiedEntityDetails`` and ``unspecifiedPersonDetails`` on Entity and Person statements, an :ref:`schema-unspecified-record` in place of a ``recordId`` in a Relationship statement, and ``missingInfoReason`` on political exposure details. Publishers SHOULD use these rather than an empty or placeholder value.

Systems which emit every field, leaving missing ones blank, will need to strip those fields before publishing BODS data. Converters from tabular data SHOULD treat an empty cell as an omitted field (see :ref:`serialisation-tabular`).

Statement order
---------------

A JSON BODS file MUST consist of a series of ordered Statement objects within a top-level array. 

Specifically, the ``interestedParty`` and ``subject`` values of a Relationship statement, when they are a ``recordId`` value, MUST match the ``recordId`` value of at least one other *prior* Statement in the array.

.. _serialisation-tabular:

Alternative tabular form
------------------------

BODS data MAY also be serialised in tabular form, with each row representing a statement. Columns SHOULD represent statement fields and column titles SHOULD use the relevant relative JSON Pointer from the statement root. An empty cell means that the field is omitted from that statement (see :ref:`serialisation-missing-values`).

For example, the extract:

.. code-block:: json
   
   [
    {
      "statementId": "e3c07f34-1810-4eed-b845-4d9f4d97f9d5",
      "recordId": "1810-4eed-b845-4d9f4d97f9d5",
      "recordType": "entity",
      "recordDetails": {
        "identifiers": [
          {
            "scheme": "GB-COH",
            "id": "07444723"
          }
        ]
      }
    },
    {
      "statementId":"a2b485be-e3b6-4fd7-8a6a-930e46cf9957",
      "recordId": "e3b6-4fd7-8a6a-930e46cf9957",
      "recordType":"person",
      "recordDetails": {
        "identifiers":[
          {
            "scheme":"MX-RFC",
            "id":"ABC680524P-76"
          }
        ]
      }
    },
    {
      "statementId":"34b479f2-1681-4064-ab51-1e703fbafa",
      "recordId": "1681-4064-ab51-1e703fbafa",
      "recordType":"relationship"
    }
   ]

may be serialised in a table as:

.. list-table:: 
   :header-rows: 1
    
   * - statementId 
     - recordId
     - recordType 
     - recordDetails/identifiers/0/scheme 
     - recordDetails/identifiers/0/id
   * - e3c07f34-1810-4eed-b845-4d9f4d97f9d5
     - 1810-4eed-b845-4d9f4d97f9d5
     - entity
     - GB-COH
     - 07444723
   * - a2b485be-e3b6-4fd7-8a6a-930e46cf9957
     - e3b6-4fd7-8a6a-930e46cf9957
     - person
     - MX-RFC
     - ABC680524P-76
   * - 34b479f2-1681-4064-ab51-1e703fbafa
     - 1681-4064-ab51-1e703fbafa
     - relationship
     - 
     - 


