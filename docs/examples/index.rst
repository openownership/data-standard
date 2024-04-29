Examples
========

These fictional examples highlight key elements of how ownership and control information is built up through the use of statements.

A single, direct beneficial owner
----------------------------------------------------------------

Three statements (Entity, Person and Relationship) that describe the beneficial ownership (and 100% legal ownership) of Profitech Ltd by Jennifer Hewitson-Smith. 

.. literalinclude:: ../../examples/bods-package.json
    :language: json

Updating information over time 1 (Tecido scenario)
------

This example demonstrates a gradual transfer of ownership from a single owner to an employee owned trust. In this example, a beneficial owner must be disclosed when they own at least 25% of the company. The trust arrangement itself is not disclosed.

`Example JSON <https://github.com/openownership/data-standard/tree/0.4.0/examples/tecido.json>`__ 

| **20th January 2019** 
| Tecido is registered with one person as owner and director. 
|
| **25th September 2021**
| 60% of shares are transferred to a corporate trustee company, Shear Trust.
|
| **25th September 2022**
| An additional 10% of shares are transferred to the trustee company, which now holds 70% of the shares. 
|
| **3rd March 2023**
| An additional 10% of shares are transferred to the trustee company, which now holds 80% of the shares. The original owner is now below the threshold for reporting and is no longer disclosed as a beneficial owner. 

Updating information over time 2 (Fermcat scenario)
-------

This example demonstrates how a confirmation process and changes in ownership are represented in BODS. 

`Example JSON <https://github.com/openownership/data-standard/tree/0.4.0/examples/fermcat.json>`__ 

| **11th September 2019**
| Fermcat is registered as having two beneficial owners who each own 50% of the company. 
|
| **11th September 2020**
| The yearly confirmation process is completed. There have been no changes in beneficial ownership. 
|
| **11th September 2021**
| In April 2021 one of the owners dies and his shares are transferred to his next of kin. When the yearly confirmation process is started, this prompts Fermcat's accountant to update the register with this change. After updating the register she files the confirmation statement. 
|
| **21st January 2022**
| One of the co-owners is bought out by the other. Fermcat's accountant updates the register to reflect this change. 

Levent Trust 
------------

This example demonstrates how the beneficial ownership of a trust-like arrangement can be represented using BODS. 

`Example JSON <https://github.com/openownership/data-standard/tree/0.4.0/examples/levent.json>`__

| **19th September 2020**
| A fiducie is registered with information about the settlor and trustees disclosed. The beneficiary is exempt from disclosure. 

Other examples
--------------

There are additional examples of valid BODS JSON files in the standard repository. These examples include representing indirect ownership, use of annotations, and representing state owned enterprises. 

Example data (`v0.4 <https://github.com/openownership/data-standard/tree/0.4.0/examples>`__ | `v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/examples>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/examples>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/examples>`__ )

In 0.4, test files are used to validate the schema. Each test file represents a feature of the schema. 

Test data (`v0.4 <https://github.com/openownership/data-standard/tree/0.4.0/tests/data/valid-statements>`__  | `v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/tests/data/>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/tests/data/>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/tests/data/>`__ )

