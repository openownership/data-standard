Examples
========

The examples below highlight key elements of how ownership and control information is built up through the use of statements.

You can also find examples of valid BODS JSON files in the standard repository:

- Example data (`v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/examples>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/examples>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/examples>`__ )
- Test data (`v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/tests/data/entity-statement/valid>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/tests/data/entity-statement/valid>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/tests/data/entity-statement/valid>`__ )

For a visual rendering of these examples, use the `BODS Visualiser <https://www.openownership.org/visualisation/visualisation-tool/>`_.


A single direct owner
---------------------

The example below presents three statements (Entity, Person and OwnershipOrControl) that describe the 100% beneficial ownership of Chrinon Ltd by Chris Taggart. 

-0.3 JSON EXAMPLE REMOVED SO DOCS BUILD-

Joint ownership
---------------

To model joint ownership, an artificial 'arrangement', owned by the two parties responsible for it, should be included within a chain of ownership.

.. literalinclude:: ../../examples/joint-ownership.json
    :language: json


Updating ownership
------------------

To update a previous statement, a new beneficial ownership statement, with a ``replacesStatement`` property is required.

In the (fictional) example below, the previous statement that Chris Taggart has 100% ownership of Chrinon Ltd is replaced by a new statement showing 50% ownership. A separate statement declares that the owner of the other 50% has not yet been identified.

Note that only **changed statements** need to have new statement identifiers. 

-0.3 JSON EXAMPLE REMOVED SO DOCS BUILD-

When a data file is provided, all the person or entity statements referenced from an ownershipOrControl statement ``subject`` or ``interestedParty`` field should be included in the file.
