Representing alternative languages
==================================

Beneficial ownership information may need to be provided in different languages or scripts. BODS provides options for representing translated or transliterated information. 

To represent:

* people’s names, use an entry in the names array with ``name.type`` ‘translation’ or ‘transliteration’ 

* entity names, use an entry in the ``alternativeNames`` array

* entity types use ``entityType.details``

* legal forms use ``legalForm.code``, where known: the ELF code list gives each legal form's names in the official languages of its jurisdiction

* interest types use ``interest.details``

For other fields or entire records, use an annotation. 

In the annotation:

* ``motivation`` MUST be ‘transformation’

* ``description`` SHOULD explain the type of transformation (e.g. ‘translation’) 

* ``transformedContent`` MUST contain the transformed content

