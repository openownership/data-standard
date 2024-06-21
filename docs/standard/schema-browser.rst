.. _schema-browser:

Schema browser
==============

.. include:: warningbox.rst

The draft Beneficial Ownership Data Standard schema is defined using `JSON Schema 2020-12 <https://json-schema.org/>`_.

A BODS dataset is an array of Statements. Each Statement contains ``recordDetails`` for one of three beneficial ownership elements. The structure of these objects can be explored using the viewers below. (Click on object buttons to reveal their properties.)

* :ref:`schema-browser-statement`
* :ref:`schema-browser-entity`
* :ref:`schema-browser-person`
* :ref:`schema-browser-relationship`

For an A - Z guide to the the Data Standard's schema objects and codelists, see the :ref:`schema-reference`.

.. _schema-browser-statement:

Statements array
----------------

View the `Statements JSON schema <../_static/statement.json>`_ or explore it using the viewer below.

.. raw:: html

    <script src="../_static/docson/widget.js" data-schema="../statement.json"></script>

.. _schema-browser-entity:

Record details (entity)
------------------------

View the `Entity record details JSON schema <../_static/entity-record.json>`_ or explore it using the viewer below.

.. raw:: html

    <script src="../_static/docson/widget.js" data-schema="../entity-record.json"></script>


.. _schema-browser-person:

Record details (person)
------------------------

View the `Person record details JSON schema <../_static/person-record.json>`_ or explore it using the viewer below.

.. raw:: html

    <script src="../_static/docson/widget.js" data-schema="../person-record.json"></script>

.. _schema-browser-relationship:

Record details (relationship)
------------------------------

View the `Relationship record details JSON schema <../_static/relationship-record.json>`_ or explore it using the viewer below.

.. raw:: html

    <script src="../_static/docson/widget.js" data-schema="../relationship-record.json"></script>
