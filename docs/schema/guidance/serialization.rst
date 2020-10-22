.. _guidance-serialization:

Serialization
=============

The canonical serialization of BODS data is as a `JSON document <https://tools.ietf.org/html/rfc8259>`_. A JSON BODS file SHOULD consist of a series of ordered statement objects within a top-level array. JSON Lines MAY also be used when creating large files.

Each of the :ref:`entityStatements <schema-entity-statement>` or :ref:`personStatements <schema-person-statement>` referenced by a particular :ref:`ownershipOrControlStatement <schema-ownership-or-control-statement>`  MUST appear before that particular ownership-or-control statement in the ordered array. 

BODS data MAY also be serialized in tabular form, with each row representing a statement. Columns SHOULD represent statement fields and column titles SHOULD use the relevant relative JSON Pointer from the statement root. 

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


