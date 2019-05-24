.. _changelog:

=========
ChangeLog
=========

.. attention:: 
   
    This is v0.1 of the Beneficial Ownership Data Standard. It includes updates to the data model and additional codelist information.

    Implementers should be aware that future changes are anticipated, before a version 1.0 release. However, from this v0.1 release onwards, any structural changes, or major definitional changes will only take place following consultation, with a clear changelog provided, and with the documentation of previous versions maintained in archive form.

    The schema specifies a **structure**, **fields** and **codelists** but does not yet enforce validation constraints on most fields. 


[0.2] - 2019-05-29
==================

Added
-----
- A ``hasPepStatus`` property (taking a boolean value) has been added to Person Statements. It is only to be used where disclosure requirements require that Politically Exposed Persons are flagged.
- PEP Status objects now have the additional properties ``missingInfoReason`` and ``source``.

Changed
-------
- The interestType codelist has been amended:
 - 'rights-to-surplus-assets' is renamed 'rights-to-surplus-assets-on-dissolution'
 - 'rights-granted-by-contract' has been added
 - 'conditional-rights-granted-by-contract' has been added

- The ``pepStatus`` property of Person Statements has been renamed ``pepStatusDetails`` (and still references an array of PEP Status objects).

Removed
-------
-


[0.1] - 2018-12-12
==================

Added
-----
- ``beneficialOwnershipOrControl`` property added to Interest object. Takes a boolean value. Can be used to to assert that an interest between a natural person and an entity makes that person a beneficial owner.
- ``pepStatus`` property add to Person Statement object. Allows a natural person to be recorded as a politically exposed person (with a related reason, jurisdiction, start date and end date).
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



