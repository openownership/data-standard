.. _guidance-identifiers:

Real world identifiers
=============================

To create a link between statements, and the real-world organisations and people they relate to, statements may include a range of identifying information. We use a common :any:`Identifier object <schema-identifier>` with the following properties:

* ``scheme`` should be a value from a codelist of known identifier sources. Separate codelists exist for entities and persons. See below.

* ``id`` should be the value assigned to the relevant entity or person in that scheme.

* ``uri`` may be used to provide a canonical URI for the entity or person within the scheme.

* ``schemeName`` should be the name of the list, registry or ID system.

A good-quality Identifier will contain ``scheme`` and ``id`` values which will uniquely identify an entity or person. Where these are not available, ``schemeName`` can be used to refer to the registration system in which the person or entity is known to be represented. When publishing an Identifier object, a value for either ``scheme`` or ``schemeName`` MUST be present.


Multiple Identifiers
--------------------

A source system might hold the following identifying information for a single company:

- A registered company number; and
- A VAT number;

In this case, two entries can be created in the Entity statement's ``identifiers`` array:

.. code-block:: json

    [
        {
            "scheme":"GB-COH",
            "id":"012345678"
        },
        {
            "scheme":"GB-VAT",
            "id":"65251235"
        }
    ]

Person Statements may also hold an array of Identifiers.


Entity Identifiers
------------------

The values for ``scheme`` within an Entity Statement Identifier should be drawn from the `http://org-id.guide <http://org-id.guide>`_ codelist. This contains details of hundreds of company registers and other identifier sources. 

Where the publisher is providing an internal identifier, the publisher should either:

* Publish their full list of internal identifiers, and register this list with the `http://org-id.guide <http://org-id.guide>`_ codelist; or
* Use MISC-{Publisher_Name} as the scheme


Person Identifiers
------------------

System Identifiers
++++++++++++++++++

If the source system has assigned a unique identifier to individual persons, and this identifier can be published, then this should be included with the scheme 'MISC-{Publisher Name}'.

For example, a beneficial ownership reporting system may maintain a database table of 'person' records, each with its identifier as a primary key. So that users can recognise references to the same person mentioned in separate statements, this identifier should be included in the published data, either in raw form, or modified to ensure a unique value. 


Shared identifiers
++++++++++++++++++

If the source system has collected one or more known identification numbers for a person, and these can be published without privacy or security risks, then these should also be included in the ``PersonStatement.identifiers`` array. 

In such cases, the values for ``scheme`` should be based on the following pattern:

{JURISDICTION}-{TYPE}

Where jurisdiction is expressed using the extended ISO 3-digit country codes list proposed by in `ICAO Document 9303 §5 <http://www.icao.int/publications/Documents/9303_p3_cons_en.pdf>`_ (pages 22-29).

For example, a passport number from Afghanistan would have the scheme:

> AFG-PASSPORT-{NUMBER}

Where the publisher is providing an internal identifier, these should use 'MISC-{Publisher_Name}' as the scheme.

.. warning:: 

  When using BODS to provide open data, it is important to ensure any person identifiers are suitable for publication under national laws and data protection frameworks.

  Most of the identifier types listed below **are not** suitable for publication as part of an open dataset.


The following identification types are currently documented. Suggestions for new types should be made through the `issue tracker <https://github.com/openownership/data-standard/issues>`_. 

PASSPORT
++++++++

Passport numbers should follow the format of the identifier (second) line in a machine-readable passport (see `Appendix B to Part 4 of ICAO Doc 9303 <http://www.icao.int/publications/Documents/9303_p4_cons_en.pdf>`_) including at least the document number. 

Parsers should be able to extract the document number from the first 9 characters, and to access any subsequent information supplied according to the ICAO format.

TAXID
+++++

Country taxpayer identification systems vary. Where specific guidance on including numbers from a particular jurisdiction is required, this may be included here in future.

IDCARD
++++++

Country ID card systems vary. Where specific guidance on including numbers from a particular jurisdiction is required, this may be included here in future.







