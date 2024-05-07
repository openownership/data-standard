.. _changelog:

=========
ChangeLog
=========

.. include:: warningbox.rst

[0.4] - 2024-05-08
===============================

Added
-----
* ``recordDetails`` object to contain person, entity or relationship fields within a Statement.
* ``declaration`` and ``declarationSubject`` to support grouping of Statements by parent declaration (filing) or by the declarant
* ``recordId`` and ``recordStatus`` to support information updates
* New documentation pages: 

  * Dates guidance 
  * Generating statements
  * Record identifiers
  * Representing trusts 
  * Representing nominees 
  * Representing record updates

Changed
-------
* All date and date-time fields reviewed to ensure appropriate validation 
* Schema and codelist titles and descriptions updated
* Documentation images and text updated 
* Documentation section 'Data schema' renamed 'Data standard' for clarity
* Guidance pages in 'Data standard' restructured into 'Modelling requirements' and 'System requirements' sub-sections
* 'Ownership-or-control' statements renamed 'Relationship' statements
* Statement fields:

  * ``statementDate`` now required
  * ``statementType`` replaced with ``recordType``
  * ``statementID`` renamed ``statementId``
* Entity fields: 

  * ``entityType`` and ``entitySubtype`` combined into ``entityType``
  * ``securitiesListings`` removed from required fields in ``publicListing``
  * 'nomination' and 'trust' added ``entitySubtype`` codelist
  * prefixes removed from ``entitySubtype`` codelist (e.g. 'stateBody-stateAgency' is now 'stateAgency') 
* Relationship fields:

  * ``Interest.share`` properties and requirements updated. Exact values and ranges are now represented in simpler ways.
  * 'nominee' and 'nominator' added to ``Interest.type`` codelist 
  * ``interestedParty`` and ``subject`` fields now hold a ``recordId`` value (rather than a ``statementId`` value). They may instead take an Unspecified Record object, to represent missing information.
  * ``componentStatementIds`` renamed ``componentRecordIds`` and now holds ``recordId`` values
* Person fields:

  * ``fullName`` is now required 
  * Renamed ``name.type`` code 'individual' to 'legal'
* ``address.country`` is now a Country object not a country code. 

Removed
-------
 * ``placeOfResidence``
 * ``agent``
 * ``replacesStatements``
 * Functional requirements page
 * Sources and annotations page

 
Alterations to schema structure and logic
-----------------------------------------
* Updated the JSON Schema version from draft-04 to 2020-12
* Schema files renamed and contents refactored
* Included as much validation as possible within the schema 
* enum types with one value replaced with const type


[0.3] - 2022-04-15
==================

Added
-----
- Technical guidance (normative) on 'Representing beneficial ownership': providing detailed requirements for the use of ``beneficialOwnershipOrControl``, ``directOrIndirect``, ``componentStatementIDs``, and ``isComponent``.

- Support for describing the traded securities and status of a publicly listed company (PLC): a new ``publicListing`` object has been added to Entity Statements.

- Support for representing state-owned enterprises (SOEs):

  - New codes 'state' and 'stateBody' added to the ``entityType`` codelist.
  - New ``entitySubtype`` property added to Entity Statements. Its value is an object with properties ``generalCategory`` (codelist, see below) and ``localTerm`` (string).
  - New ``entitySubtypeCategory``. Currently only populated with codes related to state bodies.
  - New ``formedByStatute`` property added to Entity Statements. Its value is an object with properties ``name`` and ``date``.
  - Changes (below) to accommodate representation of states and state bodies. 

- Technical guidance (normative) on 'Representing state-owned enterprises': providing modelling requirements.

- The ``interestType`` codelist has had the following new codes added: 'controlViaCompanyRulesOrArticles', 'controlByLegalFramework', 'boardMember', 'boardChair', 'unknownInterest', 'unpublishedInterest', 'enjoymentAndUseOfAssets', 'rightToProfitOrIncomeFromAssets'.


Changed
-------
- The ``interestType`` and ``unspecifiedReason`` codelist codes have been changed from using hyphens to camelCase.

- In the Person Statement, ``hasPepStatus`` and ``pepDetails`` have been wrapped in a ``PoliticalExposure`` object and renamed ``status`` and ``details``.

- ``incorporatedInJurisdiction`` property in Entity Statements renamed to ``jurisdiction`` and description updated.

- ``Jurisdiction.name`` is now a required field (previously it was defined as "MUST" in the description).

- ``Country.name`` is now a required field (previously it was defined as "MUST" in the description).

- 'legalEntity' description in the ``entityType`` codelist updated to remove coverage of government departments (which now fall under 'stateBody').

- Clarified ``Address.country`` is from the ISO 3166-1 list.

- Clarified ``Country.code`` is from the ISO 3166-1 list.

- Clarified ``Jurisdiction.code`` is from the ISO 3166-1 or ISO 3166-2 list.

- Clarified required values for ``statementType``.

- ``interestLevel`` renamed to ``directOrIndirect``.

- The ``interestType`` codelist codes have had 'OfTrust' removed so they refer to any type of legal arrangement. Their descriptions have been edited to reflect these changes. 'beneficiaryOfTrust' has been changed to 'beneficiaryOfLegalArrangement' to avoid ambiguity and 'otherInfluenceOrControlOfTrust' has been removed.


Alterations to schema structure and logic
-----------------------------------------
- ``Annotation`` object refactored.

- Removed reference to codelist in ``statementType``. This fixes issues caused by the way we use this field to select which subschema to use for validation. This should not impact anyone using the compiled schema, but may affect those using the files in the 'schema' directory directly.


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



