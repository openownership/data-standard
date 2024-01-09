.. _guidance-identifiers:

Real world identifiers
=============================

The schema reference contains :any:`information about the Identifier object <schema-identifier>`. 

Entity Identifiers
------------------

The values for ``scheme`` within an Entity Statement Identifier SHOULD come from the `http://org-id.guide <http://org-id.guide>`_ codelist. This contains details of company registers and other identifier sources. 

Where the publisher is providing an internal identifier, the publisher SHOULD either:

* Publish their full list of internal identifiers, and register this list with `http://org-id.guide <http://org-id.guide>`_
* Use MISC-{Publisher_Name} as the scheme


Person Identifiers
------------------
f
System Identifiers
++++++++++++++++++

If the source system has assigned a unique identifier to each person, and this identifier can be published, then this SHOULD be included with the scheme 'MISC-{Publisher Name}'.

For example, a beneficial ownership reporting system may maintain a database table of 'person' records, each with its identifier as a primary key. So that users can recognise references to the same person in separate statements, this identifier SHOULD be included in the published data, either in raw form, or modified to ensure a unique value. 


Shared identifiers
++++++++++++++++++

If the source system has collected known identification numbers for a person, and these can be published without privacy or security risks, then these SHOULD also be included in the ``PersonStatement.identifiers`` array. 

In such cases, the values for ``scheme`` SHOULD be:

{JURISDICTION}-{TYPE}

Where jurisdiction is an `ISO 3-digit country code <https://www.iso.org/iso-3166-country-codes.html>`_ or one of the extensions in `ICAO Document 9303 §5 <http://www.icao.int/publications/Documents/9303_p3_cons_en.pdf>`_ (pages 21-23). And type is one of PASSPORT, TAXID or IDCARD.

For example, a passport number from Afghanistan would have the scheme:

> AFG-PASSPORT-{NUMBER}

Where the publisher is providing an internal identifier, use 'MISC-{Publisher_Name}' as the scheme.

.. warning:: 

  When using BODS to provide open data, it is important to ensure any person identifiers are suitable for publication under national laws and data protection frameworks.

  Most of the identifier types listed below **are not** suitable for publication as part of an open dataset.


The following identification types are currently documented. Suggestions for new types should be made through the `issue tracker <https://github.com/openownership/data-standard/issues>`_. 

PASSPORT
++++++++

Passport numbers SHOULD follow the format of the identifier line in a machine-readable passport (see `Appendix B to Part 4 of ICAO Doc 9303 <http://www.icao.int/publications/Documents/9303_p4_cons_en.pdf>`_) including at least the document number. 

Parsers should be able to extract the document number from the first 9 characters, and to access any subsequent information supplied according to the ICAO format.

TAXID
+++++

Country taxpayer identification systems vary. Where specific guidance on including numbers from a particular jurisdiction is required, this may be included here in future.

IDCARD
++++++

Country ID card systems vary. Where specific guidance on including numbers from a particular jurisdiction is required, this may be included here in future.

.. _guidance-identifiers-other:

Other identifiers
-----------------

Market Identifier Codes (MICs)
++++++++++++++++++++++++++++++

See this `company information published as BODS JSON <https://github.com/openownership/data-standard/blob/master/tests/data/entity-statement/valid/valid-entity-statement-plc.json>`_ for an example of a valid use of MICs.

When a company is listed, a ``publicListing`` object can be published within the Entity Statement, containing information about its securities and where they are traded. An array of ``securitiesListings`` MAY be built and, for each security and market on which it is traded, the identifier for the market MAY be published.

Two properties SHOULD be used to accurately identify where a security is traded: the ``operatingMarketIdentifierCode`` of the operating market plus a ``marketIdentifierCode``. The ``marketIdentifierCode`` will be the same as the ``operatingMarketIdentifierCode`` if the security is traded on a main exchange. However the ``marketIdentifierCode`` will differ where a security is traded on a segment of an exchange.

MICs are standardised, issued and maintained by SWIFT as `ISO 10383 <https://www.iso20022.org/market-identifier-codes>`_. The specification of ``operatingMarketIdentifierCode`` and ``marketIdentifierCode`` is part of the ISO standard.

Tradable security identifiers
+++++++++++++++++++++++++++++

See this `company information published as BODS JSON <https://github.com/openownership/data-standard/blob/master/tests/data/entity-statement/valid/valid-entity-statement-plc.json>`_ for an example use of securities identifiers.

Where a ``securitiesListing`` is supplied (see above), it MUST include a ``ticker`` value. This will allow trades of that security to be tracked on the identified market. However, securities can be traded on several exchanges and therefore a globally unique identifier for the security SHOULD also be supplied where possible. Supported identifier schemes for securities are listed on the :any:`schema reference page <schema-codelists>`. The identifier scheme and the security’s ID under that scheme SHOULD be published as ``idScheme`` and ``id`` respectively.






