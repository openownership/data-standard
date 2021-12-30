<style><!--
/* override table width restrictions */
.wy-table-responsive table td, .wy-table-responsive table th {
    white-space: normal !important;
}

.wy-table-responsive {
    margin-bottom: 24px;
    max-width: 100%;
    overflow: visible !important;
}


.wy-table-responsive th:nth-of-type(1) {
    width:10%;
}

.wy-table-responsive th:nth-of-type(2) {
    width:10%;
}

.wy-table-responsive th:nth-of-type(3) {
    width:60%;
}

.wy-table-responsive th:nth-of-type(4) {
    width:10%;
}

.wy-table-responsive th:nth-of-type(5) {
    width:10%;
}--></style>


## Provenance Information

Provenance information can be attached through use of the ``Source`` object on a ``StatementGroup``, a ``BeneficialOwnershipStatement``, an ``EntityStatement`` or a ``PersonStatement``. 

These can be thought of in a hierarchy:

* Level 1: ``StatementGroup``
  * Level 2: ``BeneficialOwnershipStatement``
    * Level 3: ``EntityStatement`` or ``PersonStatement``

Each level **adds** further provenance information. So, for example, an ``EntityStatement.source`` record would indicate that the details of the entity have been obtained from a officialRegister, whilst the ``BeneficialOwnershipStatement.source`` record would indicate that the relationship between the identified entity, and a person, was asserted through self-declaration, and the ``StatementGroup.source`` would indicate that all this information was brought together by importing from another open dataset. 

### Source object

The Source object provides the following fields:

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Source.csv
```

### Source type codelist

> ToDo: Provide formal definitions of each source type