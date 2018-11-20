.. _guidance-updating-data:

Updating statements
===================

Statements MUST be treated as immutable: once a statement is published it MUST NOT be republished with the same ``statementID`` and different property values. The ``replacesStatements`` property can be used to indicate that one statement should be considered as a replacement for one or more previous statements.

Therefore, if a particular value needs to be updated, a new statement with a new ``statementID`` MUST be published and the ``replacesStatements`` property used to reference the old, out-of-date statement. 







