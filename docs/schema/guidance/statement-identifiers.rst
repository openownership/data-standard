.. _guidance-statement-identifiers:

Statement Identifiers
=====================

Each statement MUST have an entirely unique identifier. There MUST be no possibility of collision between identifiers for different statements. 

This means that:

* Two **different** statements SHOULD never have the same identifier;
* Once an identifier is assigned to a statement, the identifier SHOULD NOT change.

The schema enforces a minimum statement identifier length of 32 characters, and maximum length of 64 characters. 

Publishers MAY use one of the following strategies for creating statement identifiers.



Strategies for identifier creation
----------------------------------

* Generating a `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ for each statement, storing this in internal systems, and updating it whenever the relevant record(s) that make up a statement are updated; 

* Generating a `UUID <https://en.wikipedia.org/wiki/Universally_unique_identifier>`_ as a publisher-related prefix, and appending a local record identifier, and version identifier to it;

* Using an appropriately designed hash function that generates identifiers from a normalised JSON representation of the statement (excluding the `id` field) with a low collision probability.

* Using an internal identifier combined with a unique prefix to avoid collision between identifiers from different publishers


Statement identifiers are generally for creation and internal use within applications. In most circumstances they do not need to be displayed to users. This is in contrast to :ref:`entity or person identifiers <guidance-identifiers>`, which may be useful to display to users. 

