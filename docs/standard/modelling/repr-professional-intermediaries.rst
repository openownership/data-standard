.. _representing-professional-intermediaries:

Representing professional intermediaries
========================================

.. highlights::

    **Key requirements:** A professional intermediary SHOULD only be the ``interestedParty`` of a Relationship statement if they hold or exercise an interest in the subject, whether on their own account or on behalf of a client. Providing a service to an entity or to its beneficial owners is not, in itself, an interest in BODS.

    Where an intermediary makes a declaration on behalf of a declaring subject, they SHOULD be named in ``source.assertedBy``.

Overview
--------

Companies and legal arrangements are often set up and run with the help of professionals: formation agents, registered agents, trust and company service providers, lawyers, notaries, accountants, auditors, tax advisers and introducers. In this documentation they are called *professional intermediaries*.

Users of beneficial ownership data, such as investigative journalists, often want to tell these professionals apart from the beneficial owners they act for. For example, the `Offshore Leaks database <https://offshoreleaks.icij.org/>`_ published by the International Consortium of Investigative Journalists (ICIJ) records who acted as the intermediary or registered agent for each offshore entity.

Professional intermediaries are different from the *intermediary entities* described in the :ref:`representing-bo` guidance. An intermediary entity is a company or arrangement in an ownership chain, through which a beneficial owner holds an interest indirectly. A professional intermediary is a person or entity that acts *for* someone else.

How a professional intermediary is represented depends on what they do. They may:

1. hold an interest on behalf of a client, as a nominee or a trustee
2. exercise a power over the subject on behalf of a client, such as a power of attorney
3. make a declaration on behalf of a client
4. provide a service, with no interest in the subject

Each of these is covered below. Only the first two are interests, and only those are represented by Relationship statements.

Requirements
------------

Holding an interest on behalf of a client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Formation agents and service providers often supply nominee shareholders and nominee directors. These MUST be represented using a nominee arrangement, following the :ref:`representing-nominations` guidance. The intermediary is connected to the arrangement by a Relationship statement with ``interest.type`` 'nominee'. The client is connected by a Relationship statement with ``interest.type`` 'nominator'.

Professional trustees and protectors, including trust companies, MUST be represented following the :ref:`representing-trusts` guidance, using the ``interest.type`` 'trustee' or 'protector'. ``interest.details`` MAY be used to record that the trustee acts in a professional capacity (e.g. "professional trustee").

Exercising a power on behalf of a client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

An intermediary may hold a power over an entity without holding shares or a board seat. Examples include a lawyer acting under a power of attorney, or a legal representative who can bind the entity. Where this power is disclosed, it SHOULD be represented by a Relationship statement between the entity (``subject``) and the intermediary (``interestedParty``), with:

* ``interest.type`` 'rightsGrantedByContract' where the power comes from a contract or instrument such as a power of attorney, or 'otherInfluenceOrControl' otherwise
* ``interest.details`` giving the role as it is named in the source data (e.g. "attorney-in-fact" or "authorised signatory")
* ``beneficialOwnershipOrControl`` set to 'false', unless the definition of beneficial owner in operation treats the role as beneficial ownership

The person on whose behalf the intermediary acts SHOULD be represented by their own Relationship statement with the entity, following the :ref:`representing-bo` guidance.

.. code-block:: json
   
   {
     "subject": "c-0001",
     "interestedParty": "p-0002",
     "interests": [
       {
         "type": "rightsGrantedByContract",
         "details": "Power of attorney",
         "directOrIndirect": "direct",
         "beneficialOwnershipOrControl": false,
         "startDate": "2016-03-01"
       }
     ]
   }

Making a declaration on behalf of a client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In many jurisdictions, beneficial ownership information is filed by an agent of the company, such as a registered agent or a company secretary. The agent is not an interested party: they are the source of the information.

Where an intermediary makes a declaration on behalf of a declaring subject:

* ``source.type`` SHOULD include 'selfDeclaration', because the information was provided by the declaring subject's authorised representative
* ``source.assertedBy`` SHOULD name the intermediary, with a ``uri`` that identifies them where one is available
* ``source.description`` MAY explain the capacity in which they made the declaration

.. code-block:: json
   
   {
     "source": {
       "type": ["selfDeclaration"],
       "description": "Filed by the company's registered agent on its behalf.",
       "assertedBy": [
         {
           "name": "Example Corporate Services Ltd",
           "uri": "https://example.com/register/agents/1234"
         }
       ]
     }
   }

Providing a service with no interest
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Registered agents, registered office providers, formation agents, accountants, auditors, legal and tax advisers, and introducers usually have no ownership or control of the entities they serve. These relationships SHOULD NOT be represented as Relationship statements, and SHOULD NOT be represented as arrangements. A Relationship statement says that the ``interestedParty`` has an interest in the ``subject``. Users who follow Relationship statements to find who owns or controls an entity would wrongly include the service provider.

BODS does not currently have a structured way to represent a service relationship (see `Limitations`_). Until it does, publishers who need to share this information MAY:

* add an Annotation to the Entity statement, with ``motivation`` 'commenting', describing the service relationship, or with ``motivation`` 'linking' and a ``url`` to the intermediary's record in another dataset
* publish the service relationships in a separate dataset that refers to the BODS records by their ``recordId`` or by entity identifiers

.. code-block:: json
   
   {
     "annotations": [
       {
         "statementPointerTarget": "",
         "motivation": "linking",
         "description": "Registered agent of this entity from 2009-04-14.",
         "url": "https://example.com/register/agents/1234"
       }
     ]
   }

Where the same person or company is both a service provider and holds an interest, for example a formation agent that also supplies a nominee director, the interest MUST be represented as described above, and the service relationship MAY be annotated.

Worked example: ICIJ Offshore Leaks roles
-----------------------------------------

The Offshore Leaks database records many roles that link people and companies to offshore entities. The table shows how some of the roles that describe professional intermediaries map to BODS. Role names are given as they appear in the data.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Offshore Leaks role
     - BODS representation
   * - nominee name of; nominated person of; nominee shareholder
     - Nominee arrangement, with the intermediary as 'nominee'. See :ref:`representing-nominations` for the pattern.
   * - trustee of; protector of; co-trustee of
     - Trust, with ``interest.type`` 'trustee' or 'protector'. See :ref:`representing-trusts` for the pattern.
   * - director of; secretary; officer of
     - 'boardMember' for a director. Where the director acts for a client, use a nominee arrangement. A company secretary or other officer has no interest unless the source shows control.
   * - power of attorney; attorney-in-fact; authorised signatory of
     - Relationship statement with 'rightsGrantedByContract' and ``beneficialOwnershipOrControl`` 'false'.
   * - legal representative of
     - Relationship statement with 'otherInfluenceOrControl' where the representative can bind the entity, otherwise a service relationship.
   * - registered agent of; registered office service provider
     - Service relationship. Name the agent in ``source.assertedBy`` where they filed the information.
   * - intermediary of; intermediary / eligible introducer of
     - Service relationship.
   * - accountant; auditor; tax advisor of; attorney at law of
     - Service relationship.

The full list of roles, and how they are mapped to the FollowTheMoney data model, can be seen in the `OpenSanctions crawler configuration for Offshore Leaks <https://github.com/opensanctions/opensanctions/blob/main/datasets/_global/icij_offshoreleaks/icij_offshoreleaks.yml>`_. FollowTheMoney represents service relationships with a separate ``Representation`` schema (agent and client), alongside ``Ownership`` and ``Directorship``. BODS has no equivalent.

Limitations
-----------

BODS 0.4 cannot represent the following as structured data:

* a service relationship between a professional intermediary and an entity or person, with no ownership or control
* the type of service provided (registered agent, formation agent, accountant, auditor, legal adviser, introducer)
* the regulated status of an intermediary, such as a licence to act as a trust and company service provider
* a link from ``source.assertedBy`` to the intermediary's own Person or Entity record

These needs are being considered as part of the work on describing interests (`issue #466 <https://github.com/openownership/data-standard/issues/466>`_). Feedback and examples from publishers and users are welcome on `issue #626 <https://github.com/openownership/data-standard/issues/626>`_.
