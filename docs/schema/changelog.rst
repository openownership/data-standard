.. _changelog:

=========
ChangeLog
=========

.. attention:: 
   
    This is v0.2 of the Beneficial Ownership Data Standard. It includes updates to the data model and additional codelist information.

    Implementers should be aware that future changes are anticipated, before a version 1.0 release. However, from this v0.2 release onwards, any structural changes, or major definitional changes will only take place following consultation, with a clear changelog provided, and with the documentation of previous versions maintained in archive form.

    The schema specifies a **structure**, **fields** and **codelists** but does not yet enforce validation constraints on most fields.

[Unreleased]
============

Added
-----
- Support for describing the traded securities and status of a publicly listed company (PLC): a new ``publicListing`` object has been added to Entity Statements.
- Support for representing state-owned enterprises (SOEs):

  - New codes 'state' and 'stateBody' added to the ``entityType`` codelist.
  - New ``entitySubtype`` property added to Entity Statements. Its value is an object with properties ``generalCategory`` (codelist, see below) and ``localTerm`` (string).
  - New ``entitySubtypeCategory`` codelist add. Currently only populated with codes related to state bodies.
  - New ``formedByStatute`` property added to Entity Statements. Its value is an object with properties ``name`` and ``date``.
  - Changes, listed below, to accommodate representation of states and state bodies. 

- ``Country.name`` is now a required field (previously it was defined as "MUST" in the description).
- ``Jurisdiction.name`` is now a required field (previously it was defined as "MUST" in the description).
- ``SecuritiesListing.stockExchangeJurisdiction`` has minimum and maximum lengths to match the two lists that values could be from.
- Annotations have ``oneOfEnumSelectorField`` added to provide hints to validation code which will produce better error messages.

Changed
-------
- The ``interestType`` and ``unspecifiedReason`` codelist codes have been changed from using hyphens to camelCase.
- ``hasPepStatus`` and ``pepDetails`` are replaced with ``politicalExposure`` object  that contains ``status`` and ``details`` properties.
- ``incorporatedInJurisdiction`` property in Entity Statements renamed to ``jurisdiction`` and description updated.
- 'legalEntity' description in the ``entityType`` codelist updated to remove coverage of government departments (which now fall under 'stateBody').
- Required fields `statementPointerTarget` and `motivation` are moved from inside the `anyOf` statement to the top level, as they apply to all motivation types.
- Clarified ``Address.country`` is from the ISO 3166-1 list (previously it was unclear which ISO list was meant and used "digit" when it meant "letter").
- Clarified ``Country.code`` is from the ISO 3166-1 list (previously it was unclear which ISO list was meant and used "digit" when it meant "letter").
- Clarified ``Jurisdiction.code`` is from the ISO 3166-1 or ISO 3166-2 list (previously it was unclear which ISO list was meant and used "digit" when it meant "letter").
- Clarified ``SecuritiesListing.stockExchangeJurisdiction`` is from the ISO 3166-1 or ISO 3166-2 list (previously it was unclear which ISO list was meant and used "digit" when it meant "letter").
- Annotations changes from a ``anyOf`` to a ``oneOf``. This is technically correct and also is needed to improve validation messages.
- Descriptions of ``statementType``.
- Do not reference codelists in ``statementType`` - fixes issues caused by the way we use this field to select which subschema to use for validation. This should have no change for anyone using the compiled schema but may affect anyone using the files in ``schema/`` directly.
- ``interestLevel`` renamed to ``directOrIndirect``.


[0.2] - 2019-06-30
==================

Added
-----
- Support for representing details of indirect beneficial ownership relationships (where a beneficial owner owns or controls an entity through intermediaries):

  - A required ``isComponent`` property has been added to all three Statement objects. It takes a boolean value and indicates whether a Statement represents part of a primary indirect ownership-or-control relationship.
  - A ``componentStatementIDs`` property has been added to Ownership-or-control Statements. It takes an array of Statement IDs, indicating which component statements provide detail about the parent Ownership-or-control Statement.

- A required ``publicationDetails`` property has been added to all three Statement objects. It represents metadata for Statements: information about their original publisher. Sub-properties (and their sub-properties) are:

  - ``publicationDate``\*
  - ``bodsVersion``\*
  - ``license``
  - ``publisher``\* (``name``, ``url``)

  \* required

- A ``hasPepStatus`` property (taking a boolean value) has been added to Person Statements. It is only to be used where disclosure requirements require that Politically Exposed Persons are flagged.

- PEP Status objects now have the additional properties ``missingInfoReason`` and ``source``.

- A ``taxResidencies`` property has been added to Person Statements. It takes an array of Country objects.

- Support for more structured accounts of missing and anonymised data:

  - ``unspecifiedPersonDetails`` has been added to Person Statements (with a required ``reason`` sub-property)
  - ``unspecifiedEntityDetails`` has been added to Entity Statements (with a required ``reason`` sub-property)

  The ``reason`` sub-property draws on the Unspecified Reason codelist (as does the Ownership-or-control Statement's ``interestedParty.unspecified`` property).

Changed
-------
- The ``pepStatus`` property of Person Statements has been renamed ``pepStatusDetails`` (and still references an array of PEP Status objects).

- The ``personType`` property of Person Statements is now required.

- If ``Annotation.motivation`` is 'linking', ``Annotation.url`` is required.

- The Interest Type codelist has been amended:

  - 'influence-or-control' is renamed 'other-influence-or-control'
  - 'rights-to-surplus-assets' is renamed 'rights-to-surplus-assets-on-dissolution'
  - 'rights-granted-by-contract' has been added
  - 'conditional-rights-granted-by-contract' has been added

- The Address Type codelist has been amended:

  - 'home' has been removed (since 'residence' can be used instead)
  - 'business' has been added

- The Name Type codelist has been amended:

  - 'alias', 'aka', and 'nick' have all been removed. They are replaced by 'alternative'
  - 'transliteration' has been added

- The Unspecified Reason codelist has been amended:

  - 'information-unknown-to-publisher' has been added

- All codelist codes now have descriptions.

Removed
-------
- The ``missingInfoReason`` property has been removed from Person and Entity Statements. It has been replaced with ``unspecifiedPersonDetails`` and ``unspecifiedEntityDetails`` respectively.

[0.1] - 2018-12-12
==================

Added
-----
- ``beneficialOwnershipOrControl`` property added to Interest object. Takes a boolean value. Can be used to assert that an interest between a natural person and an entity makes that person a beneficial owner.
- ``pepStatus`` property added to Person Statement object. Allows a natural person to be recorded as a politically exposed person (with a related reason, jurisdiction, start date and end date).
- ``annotations`` property added to all three types of statement. Annotations provide a way of including additional (structured) data or transforming existing data in a targeted way.
- An ``unspecified`` property replaces the ``nullParty`` option for interested parties.  An unspecifiedReason codelist provides options for describing why an interested party is not recorded. 

Changed
-------
- The interestType codelist has been extended to include interests in trusts.
- The structure of BODS-formatted data has been flattened, to remove extraneous nesting and facilitate serialization using JSON Lines.
- 'Beneficial ownership statements' have been renamed 'Ownership-or-control statements' to reflect the scope of their use.

Removed
-------
- Arrays of ``statementGroup`` objects (each object with its own statement group id) are no longer used to package arrays of statements. This reflects a flattening of the structure of BODS formatted data. 
- The ``nullParty`` option for interested parties. See ``unspecified`` property in the Added section above.



