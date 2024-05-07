.. _examples:

Examples
========

These fictional examples highlight key elements of how ownership and control information is built up through the use of statements.

.. _examples-simple-bo:

A single, direct beneficial owner
---------------------------------

Three statements (Entity, Person and Relationship) that describe the beneficial ownership (and 100% legal ownership) of Profitech Ltd by Jennifer Hewitson-Smith. 

.. literalinclude:: ../../examples/bods-package.json
    :language: json

.. _examples-trust:

A trust-like arrangement
------------------------

This example demonstrates how the beneficial ownership of a trust-like arrangement can be represented using BODS. A fiducie is registered with information about the settlor and trustees disclosed. The beneficiary is exempt from disclosure.

.. literalinclude:: ../../examples/levent.json
    :language: json

.. _examples-plc:

An entity statement for a listed company
-----------------------------------------

This statement demonstrates how the details of a listed company can be published in BODS format.

.. literalinclude:: ../../examples/plc-entity-statement.json
    :language: json

Updating information over time 1
--------------------------------

This example demonstrates a gradual transfer of ownership from a single owner to an employee owned trust. In this example, a beneficial owner must be disclosed when they own at least 25% of the company. The trust arrangement itself is not disclosed.

`Example JSON <https://github.com/openownership/data-standard/tree/0.4.0/examples/tecido.json>`__ 

**Timeline**

.. list-table::
    :widths: 15 25 65
    :header-rows: 1
    
    * - Statement Date
      - Declaration
      - Description
    * - 2019-01-20
      - bo-jtc-8755982746
      - Tecido is registered with Maria Esteves as sole beneficial owner, legal owner and director.
    * - 2021-09-25
      - bo-tjf-7435753839
      - 60% of shares are transferred to a corporate trustee company, Shear Trust.
    * - 2022-09-25
      - bo-kks-9337584037
      - An additional 10% of shares are transferred to the trustee company, which now holds 70% of the shares.
    * - 2023-03-03
      - bo-tns-6849443385
      - An additional 10% of shares are transferred to the trustee company, which now holds 80% of the shares. The original owner is now below the threshold for reporting and is no longer disclosed as a beneficial owner.
      
Updating information over time 2
--------------------------------

This example demonstrates how a confirmation process and changes in beneficial ownership information are represented in BODS. 

`Example JSON <https://github.com/openownership/data-standard/tree/0.4.0/examples/fermcat.json>`__ 

**Timeline** 

.. list-table::
    :widths: 15 75
    :header-rows: 1
    
    * - Statement Date 
      - Description
    * - 2019-09-11 
      - Fermcat is registered as having two beneficial owners who each own 50% of the company.
    * - 2020-09-11
      - The yearly confirmation process is completed. There have been no changes in beneficial ownership.
    * - 2021-09-11
      - In April 2021 one of the owners dies and his shares are transferred to his next of kin. When the yearly confirmation process is started, this prompts Fermcat's accountant to update the register with this change. After updating the register she files the confirmation statement. 
    * - 2022-01-21
      - One of the co-owners is bought out by the other. Fermcat's accountant updates the register to reflect this change.
      
Other examples
--------------

There are additional examples of valid BODS JSON files in the standard repository. These examples include representing indirect ownership, use of annotations, and representing state owned enterprises. 

Example data (`v0.4 <https://github.com/openownership/data-standard/tree/0.4.0/examples>`__ | `v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/examples>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/examples>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/examples>`__ )

