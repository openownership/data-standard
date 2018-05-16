
Provenance information
======================

Provenance information can be attached through use of the ``Source`` object on a ``StatementGroup``, a ``BeneficialOwnershipStatement``, an ``EntityStatement`` or a ``PersonStatement``. 

These can be thought of in a hierarchy:

* Level 1: ``StatementGroup``
  * Level 2: ``BeneficialOwnershipStatement``
    * Level 3: ``EntityStatement`` or ``PersonStatement``

Each level **adds** further provenance information. So, for example, an ``EntityStatement.source`` record would indicate that the details of the entity have been obtained from a officialRegister, whilst the ``BeneficialOwnershipStatement.source`` record would indicate that the relationship between the identified entity, and a person, was asserted through self-declaration, and the ``StatementGroup.source`` would indicate that all this information was brought together by importing from another open dataset. 

### Source object

> ToDo: schema reference table to go here

### Source type codelist

> ToDo: Provide formal definitions of each source type
