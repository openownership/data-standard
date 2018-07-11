.. _guidance-statement-identifiers:

Statement Identifiers
=====================

**Publishers MUST generate globally unique and persistent identifiers for each statement.**

This means that:

* No two **different** statements should ever have the same identifier;
* Once an identifier is assigned to a statement, the identifier should not change.
  
Statement identifiers should generally be created and used internally within applications, but in most circumstances do not need to be displayed to users. (Note: this does not apply to organisation or person identifiers, which may be useful to display to users).

Each publishers should identifier an appropriate strategy for creating and maintaining identifiers. The standard enforces a minimum identifier length of 32 characters, and a maximum length of 64 characters. 

Possible strategies for identifier creation
-------------------------------------------

* Generating a `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ for each statement, storing this in internal systems, and updating it whenever the relevant record(s) that make up a statement are updated; 

* Generating a `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ as a publisher-related prefix, and appending a local record identifier, and version identifier to it;

* Using an appropriately designed hash function that generates identifiers from a normalised JSON representation of the statement (excluding the `id` field) with a low colision probability. 

