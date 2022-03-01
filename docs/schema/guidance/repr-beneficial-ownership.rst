.. _representing-bo:

Representing beneficial ownership
========================================

.. highlights::

    **Key requirement:** If a person is a beneficial owner of an entity - whether directly or indirectly - and the person or entity is required to declare this beneficial ownership, there MUST be an Ownership-or-control Statement connecting the two which represents the beneficial ownership relationship.


Overview
------------------------

Beneficial owners can exercise ownership-or-control *directly* in an entity (expected to be a company) or *indirectly*, via intermediary entities (such or arrangements or other companies). It must be clear in a BODS dataset which people are declared as beneficial owners of which companies (and which entities are intermediaries). And it must be clear what overall control or ownership beneficial owners have (regardless whether it is direct or indirect).

.. figure:: ../../_assets/RepresentingChainsBODS-RealWorld.svg
   :alt: Person 1 indirectly holds a 15 percent shareholding in Company E, via an intermediary: Company A. Person 2 directly holds 32 precent of Company E's shares.
   :figwidth: 65%
   :align: center

In the above situation, Person 1 *indirectly* benefits from a 15% shareholding in Company E and Person 2 has a *direct* 32% shareholding in Company E. In a jurisdiction where people with a shareholding (direct or indirect) of over 10% in a company should be disclosed as beneficial owners, both Person 1 and Person 2’s interests would be declared. Additionally, the jurisdiction may require that details of Person 1’s indirect interest are disclosed. That is: that some details of the chain Company E - Company A - Person 1 are also disclosed. 

In BODS, the following properties are used to represent such information disclosure:

* ``beneficialOwnershipOrControl`` (See :ref:`schema-interest`)
* ``directOrIndirect`` (See :ref:`schema-interest`)
* ``componentStatementIDs`` (See :ref:`schema-ownership-or-control-statement`)
* ``isComponent`` (See :ref:`schema-entity-statement`)

Requirements
------------------------

Representing beneficial ownership
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If a person is a beneficial owner of an entity, entity X, whether directly or indirectly, and one of them is required to declare this beneficial ownership:

1. There MUST be a *primary* Ownership-or-control Statement connecting the two which represents the beneficial ownership relationship. In particular: 

   a. the entity’s Statement MUST be the ``subject``;
   b. the person’s Statement MUST be the ``interestedParty``;
   c. ``isComponent`` MUST be false;
   d. the ``interests`` which make the person meet the criteria for their being declared a beneficial owner MUST be included in this primary Ownership-or-control Statement if known; and
   e. the ``interests`` in (d) MUST have ``beneficialOwnershipOrControl`` set to 'true'.

2. If beneficial ownership is known to be exercised indirectly, via intermediary entities then ``directOrIndirect`` MUST be ‘indirect’. If it is known to be exercised directly then ``directOrIndirect`` MUST be ‘direct’. Otherwise ``directOrIndirect`` MUST be ‘unknown’.

Representing intermediaries
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Where beneficial ownership is known to be exercised indirectly, via known intermediary entities, this SHOULD be represented in addition to the above. In particular:

1. The chain of known intermediary entities SHOULD be represented by *secondary* Entity Statements, Ownership-or-control Statements and Person Statements.
2. These secondary statements SHOULD link the beneficial owner’s Statement to entity X’s statement indirectly.
3. These secondary statements SHOULD all have ``isComponent`` set to 'true'.
4. These secondary statements SHOULD all have their ``statementID`` values listed in the ``componentStatementIDs`` array of the primary Ownership-or-control Statement.
5. When the primary Ownership-or-control Statement is published in a BODS file:

   a. all secondary statements referenced from ``componentStatementIDs`` MUST also be published in that file;
   b. all secondary statements must appear before the primary Ownership-or-control Statement in the list of statements.

Example
--------

In the following example, Person 1 is a beneficial owner of Company E. They exercise that beneficial ownership via an intermediary company, Company A. (Note: abbreviated statement IDs are used for brevity and clarity of explanation. Short IDs like ‘ooc-2’ are not valid in BODS.)

.. figure:: ../../_assets/RepresentingChainsBODS-Statements.svg
   :alt: Person Statements, Entity Statements and Ownership-or-control Statements are linked, representing the company ownership structure. Statement property values are given as follows. Person 1's Statement: statementID is p-1, isComponent is false. Intermediary Company A's Statement: statementID is e-2, isComponent is true. Company E's Statement: statementID is e-1, isComponent is false. Ownership-or-control Statement connecting Person 1 and Company A: statementID is ooc-3, directOrIndirect is direct, isComponent is true, beneficialOwnershipOrControl is false. Ownership-or-control Statement connecting Company A and Company E: statementID is ooc-2, directOrIndirect is direct, isComponent is true, beneficialOwnershipOrControl is false. Ownership-or-control Statement connecting Person 1 and Company E: statementID is ooc-1, isComponent is false, componentStatementIDs are ooc-2 and e-2 and ooc-3; and its interests have directOrIndirect as indirect and beneficialOwnershipOrControl as true.
   :figwidth: 90%
   :align: center

Statement order
^^^^^^^^^^^^^^^^
An example of valid statement order for the above would be: p-1, e-1, e-2, ooc-3, ooc-2, ooc-1.

