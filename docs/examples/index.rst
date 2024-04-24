Examples
========

The examples below highlight key elements of how ownership and control information is built up through the use of statements. These examples are synthetic data. 

There are additional examples of valid BODS JSON files in the standard repository:

Example data (`v0.4 <https://github.com/openownership/data-standard/tree/0.4.0/examples>`__ | `v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/examples>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/examples>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/examples>`__ )

Test data demonstrates individual features of the schema:

Test data (`v0.4 <https://github.com/openownership/data-standard/tree/0.4.0/tests/data/valid-statements>`__  | `v0.3 <https://github.com/openownership/data-standard/tree/0.3.0/tests/data/>`__  |  `v0.2 <https://github.com/openownership/data-standard/tree/0.2.0/tests/data/>`__  | `v0.1 <https://github.com/openownership/data-standard/tree/0.1.0/tests/data/>`__ )

A single direct owner
---------------------

The example below presents three statements (Entity, Person and Relationship) that describe the 100% beneficial ownership of Profitech Ltd by Jennifer Hewitson-Smith. 

.. literalinclude:: ../../examples/bods-package.json
    :language: json

Fermcat
-------

This example demonstrates how a confirmation process and changes in ownership are represented in BODS. 

`Example JSON <https://github.com/openownership/data-standard/tree/0.4.0/examples/fermcat.json>`__ 

*11th September 2019*
Fermcat is registered with the beneficial ownership register. There are 2 owners who each own 50% of the company. 

*11th September 2020*
The yearly confirmation process is completed. There have been no changes in ownership. 

*11th September 2021*
In April 2021 one of the owners dies and his shares are transferred to his next of kin. 

When the yearly confirmation process is started this prompts Fermcat's accountant to update the register with this change. After updating the register she files the confirmation statement. 

*21st January 2022* 
One of the co-owners is bought out by the other. Fermcat's accountant updates the register to reflect this change. 

Tecido
------


