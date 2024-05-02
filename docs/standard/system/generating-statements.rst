.. _generating-statements:

Generating statements
=====================

Statements SHOULD be treated as immutable: once a Statement is published it SHOULD NOT be republished with the same statement identifier (``statementId``) and different property values. See :ref:`information-updates` for more information.

Each Statement MUST have a unique statement identifier. There MUST NOT be a possibility of collision between identifiers for different Statements. 

This means that:

* two **different** Statements SHOULD never have the same identifier
* once an identifier is assigned to a Statement, the identifier SHOULD NOT change.

The schema enforces a minimum statement identifier length of 32 characters, and maximum length of 64 characters. 

Statement identifiers are generally for internal use within applications. In most circumstances they do not need to be displayed to users. This is in contrast to :ref:`entity or person identifiers <guidance-identifiers>`, which are useful to display to users. 

Strategies for statement identifier creation
-------------------------------------------------------------------------------

Publishers MAY use one of the following strategies to create statement identifiers.

* Generate a `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ for the first Statement for a record. Store this in the data management system. Update it whenever the relevant record is updated. 
* Generate a `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ as a publisher-related prefix. Append the relevant ``recordId``, and a version identifier to it.
* Use an appropriately designed hash function that generates identifiers from a normalised JSON representation of the statement (excluding the ``statementId`` field) with a low collision probability.
* Use an internal identifier combined with a unique prefix to avoid collision between identifiers from different publishers.


