.. _guidance-identifiers:

Real world identifiers
==================================

Real world identifiers are essential for making beneficial ownership data interoperable. By 'real world identifier' we mean reference strings, issued by authoritative registration schemes, which have gained widespread use in the world. People can use them to verify that the referenced person, entity or item exists.

In BODS, real world identifiers can be published for:

- entities
- people
- stock markets and trading exchanges
- tradable securities

Entity identifiers
-------------------------------

Use an :ref:`Identifier <schema-identifier>` in the ``identifiers`` array of an Entity Statement to supply a company registration number, Legal Entity Identifier (LEI), or other real world identifier.

The value for ``Identifier.scheme`` SHOULD come from `org-id.guide <http://org-id.guide>`_. This resource contains details of company registers and other identifier sources. If the identifier scheme you need to reference is not already listed on org-id.guide `propose a new entry <https://org-idguide-handbook.readthedocs.io/en/latest/contribute/#proposing-a-new-entry>`_.

If it is useful to publish an internal identifier from your data management system, first consider whether it should be used as a :ref:`record identifier <record-identifiers>`. If not, either:

- publish your full list of internal identifiers, and propose it as an entry to `org-id.guide <http://org-id.guide>`_, or
- use ``schemeName`` to identify your system and leave ``scheme`` blank

Person identifiers
----------------------------------

Global identifiers
+++++++++++++++++++

If the system holds identification numbers for a person, and these can be published without privacy or security risks, then these SHOULD be included in the ``identifiers`` array of the Person Statement.

In such cases, the values for ``scheme`` SHOULD be:

{JURISDICTION}-{TYPE}

Where {JURISDICTION} is an `ISO 3-digit country code <https://www.iso.org/iso-3166-country-codes.html>`_ (or one of the extensions in `ICAO Document 9303 §5 <http://www.icao.int/publications/Documents/9303_p3_cons_en.pdf>`_, pages 21-23). And {TYPE} is one of 'PASSPORT', 'TAXID' or 'IDCARD'.

For example, a passport number from Afghanistan would have the ``scheme`` value:

> AFG-PASSPORT

.. warning::
  When making BODS data publicly available, it is important to ensure any person identifiers are suitable for publication under national laws and data protection frameworks.

  Most of the identifier types listed below are not suitable for publication as part of an open dataset.

The following identification types can currently be used in BODS. Suggestions for new types should be made through the `issue tracker <https://github.com/openownership/data-standard/issues>`_.

**PASSPORT**

Passport numbers SHOULD follow the format of the identifier line in a machine-readable passport (see `Appendix B to Part 4 of ICAO Doc 9303 <http://www.icao.int/publications/Documents/9303_p4_cons_en.pdf>`_) including at least the document number.

Parsers should be able to extract the document number from the first 9 characters, and to access any subsequent information supplied according to the ICAO format.

**TAXID**

Taxpayer identification regimes vary from country to country. Where guidance on including numbers from a particular jurisdiction is required, this may be included here in future.

**IDCARD**

ID card systems vary. Where guidance on including numbers from a particular jurisdiction is required, this may be included here in future.

Special case: internal identifiers
+++++++++++++++++++++++++++++++++++

Data management systems may generate internal identifiers for people, or for records about people, or both.

If multiple records in the system are known to relate to the same person, the data management system SHOULD assign a unique identifier to the person, and publish this identifier in the associated records. The identifier SHOULD be included in the ``identifiers`` array with a ``schemeName`` value ‘{publisher name}-{identifier type}’. For example, 'AtlantisCorporateRegister-PersonReference'.

Alternatively, if a known person is only ever represented by one record on the system, then an internal person identifier may serve as the ``recordId``. See :ref:`record-identifiers`.


Market identifier codes (MICs)
----------------------------------------------

See this :ref:`example data <examples-plc>` for a valid use of MICs.

Two properties in an Entity Statement’s :ref:`Securities Listing <schema-securities-listing>` object identify where a security is traded: the ``operatingMarketIdentifierCode`` of the operating market and the ``marketIdentifierCode``. The ``marketIdentifierCode`` SHOULD be the same as the ``operatingMarketIdentifierCode`` if the security is traded on a main exchange. The ``marketIdentifierCode`` will differ where a security is traded on a segment of an exchange.

MICs are standardised, issued and maintained by SWIFT as `ISO 10383 <https://www.iso20022.org/market-identifier-codes>`_. The specification of ``operatingMarketIdentifierCode`` and ``marketIdentifierCode`` is part of the ISO standard.

.. guidance-identifiers-securities:

Tradable security identifiers
---------------------------------------------

See this :ref:`example data <examples-plc>` for a valid use of securities identifiers.

Where a :ref:`Securities Listing <schema-securities-listing>` is supplied, it needs to include a ``ticker`` value. This will allow trades of that security to be tracked on the identified market. However, securities can be traded on several exchanges and therefore supplying a globally unique identifier for the security is RECOMMENDED. Supported identifier schemes for securities are listed on the :ref:`schema reference page <schema-reference>`. Publish the identifier scheme and the security’s ID as ``idScheme`` and ``id`` respectively.






