Representing alternative languages
==================================

Beneficial ownership information may need to be provided in different languages or scripts. BODS provides options for representing translated or transliterated information. 

To represent:

* people’s names, use an entry in the names array with ``name.type`` ‘translation’ or ‘transliteration’ 

* entity names, use an entry in the ``alternativeNames`` array

* entity types use ``entityType.details``

* interest types use ``interest.details``

For other fields or entire records, use an annotation. 

In the annotation:

* ``motivation`` MUST be ‘transformation’

* ``description`` SHOULD explain the type of transformation (e.g. ‘translation’) 

* ``transformedContent`` MUST contain the transformed content

