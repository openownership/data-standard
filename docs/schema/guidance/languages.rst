Representing alternative languages
==================================

Beneficial ownership information may need to be provided in different languages or scripts. BODS provides options for representing translated or transliterated information. 

To represent:

* people’s names, use an entry in the names array with ``name.type`` ‘translation’ or ‘transliteration’ 

* entity names, use an entry in the ``alternativeNames`` array

* entity types use ``entitySubtype.localTerm``

* interest types use ``interest.details``

For other fields or entire records, use an annotation. 

In the annotation:

* ``motivation`` MUST be ‘transformation’

* ``description`` SHOULD explain the type of transformation (e.g. ‘translation’) 

* ``transformedContent`` MUST contain the transformed content

Translation converts text from one language to another, preserving the meaning of the text. For example the Russian word “Здравствуйте” can be translated to “hello” in English. 

Transliteration converts a word from one alphabet to another. The word sounds the same after transliteration. For example the Russian word “Здравствуйте” is transliterated to “Zdravstvuyte”. 

