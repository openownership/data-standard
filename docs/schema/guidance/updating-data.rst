.. _guidance-updating-data:

Updating statements
===================

Statements MUST be treated as immutable: once a statement is published it MUST NOT be republished with the same ``statementID`` and different property values. 

If a particular value needs to be updated, a new statement with a new ``statementID`` MUST be published and the ``replacesStatements`` property used to indicate the statement that is no longer true. 

The ``replacesStatements`` property can be used to indicate that one statement should be considered as a replacement for one or more previous statements.





