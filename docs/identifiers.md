Identifiers
===========


```eval_rst
  .. warning:: This is an old version of the data standard. `See latest version <https://standard.openownership.org/en/latest/>`_.
```


## Statement ids

Each statement must have a unique id. This id must be globally unique: such that no two statements from the same organisation, or from different organisations, could ever have the same identifier. 

Once published, statements must be immutable. This means any time the underlying record changes, a new statement id should be generated. 

Suggested strategies for assigning ids to statements include:

* Generating a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) for each statement, storing this in internal systems, and updating it whenever the relevant record(s) that make up a statement are updated; 

* Generating a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) as a prefix, and appending a local record identifier, and version identifier to it;

* Assigning a [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) in a domain controlled by the publisher to each statement. 

Whilst the schema is agnostic as to the exact strategy that data publishers use to generate statement ids, it enforces a minimum length of 32 characters (the length of a hexidecimal UUID) in order to avoid use of ids that are likely to fail a uniqueness test. 


## Identifying people, companies and other entities

To create a link between statements, and the real-world organisations and people they relate to, statements may include a range of identifying information. We use a common identifier object, with two required properties, and one optional property.

* **scheme** must be a value from a codelist of known identifier sources. Separate codelists exist for entities and persons. 
* **id** must be the value assigned to the relevant entity or person in that scheme;
** **uri** may be used to provide a canonical URI from this scheme.

For example, if a source system holds:

- A registered company number; and
- A VAT number;

for a company, two entries could be created in the ```entities.identifiers``` array, as in the example below:

```json
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
```

### Entity Identifiers

The values for scheme within an entity statement identifier should be drawn from the [http://org-id.guide](http://org-id.guide) codelist. 

Where the publisher is providing an internal identifier, the publisher should either:

* Publish their full list of internal identifiers, and register this list with the [http://org-id.guide](http://org-id.guide) codelist; or
* Use MISC-{Publisher_Name} as the scheme

### Person Identifiers

The values for scheme within a person statement should be based on the following pattern:

{JURISDICTION}-{TYPE}

Where jurisdiction is expressed using thee extended ISO 3-digit country codes list proposed by in [ICAO Document 9303 §5](http://www.icao.int/publications/Documents/9303_p3_cons_en.pdf) (pages 22-29).

For example, a passport number from Afghanistan would have the scheme:

> AFG-PASSPORT-{NUMBER}

Where the publisher is providing an internal identifier, these should use 'MISC-{Publisher_Name}' as the scheme.

```eval_rst
.. warning:: 

  When using BODS to provide open data, it is important to ensure any person identifiers are suitable for publication under national laws and data protection frameworks.

  Most of the identifier types listed below **are not** suitable for publication as part of an open dataset.
```

The following identification types are currently documented. Suggestions for new types should be made through the [issue tracker](https://github.com/openownership/data-standard/issues). 

##### PASSPORT

Passport numbers should follow the format of the identifier (second) line in a machine-readable passport (see [Appendix B to Part 4 of ICAO Doc 9303](http://www.icao.int/publications/Documents/9303_p4_cons_en.pdf)) including at least the document number. 

Parsers should be able to extract the document number from the first 9 characters, and to access any subsequent information supplied according to the ICAO format.

##### IDCARD

Country ID card systems vary. Where specific guidance on including numbers from a particular jurisdiction is required, this may be included here. 







