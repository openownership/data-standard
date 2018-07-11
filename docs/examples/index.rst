Examples
========

The following examples highlight key elements of how ownership and control information is built up through the use of statements.

A single direct owner
---------------------

The example below presents three statements (Entity, Person and OwnershipOrControl) that describe the 100% beneficial ownership of Chrinon Ltd by Chris Taggart. 

.. literalinclude:: ../../examples/1-single-direct.json
    :language: json

Joint ownership
---------------

To model joint ownership, an artificial 'arrangement', owned by the two parties responsible for it, should be included within a chain of ownership.

.. literalinclude:: ../../examples/3-joint-ownership.json
    :language: json


Updating ownership
------------------

To update a previous statement, a new beneficial ownership statement, with a ``replacesStatement`` property is required.

In the (fictional) example below, the previous statement that Chris Taggart has 100% ownership of Chrinon Ltd is replaced by a new statement showing 50% ownership. A separate statement declares that the owner of the other 50% has not yet been identified.

Note that only **changed statements** need to new statement identifiers. 

.. literalinclude:: ../../examples/2-single-update.json
    :language: json

When a data file is provided, all the person or entity statements referenced from an ownershipOrControl statement ``subject`` or ``interestedParty`` field should be included in the file.