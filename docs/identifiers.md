Identifiers
===========

## Identifying statements

Each statement must have a unique identifier. This identifier must be globally unique: such that no two statements from the same organisation, or from different organisations, could ever have the same identifier. 

Once published, statements must be immutable. This means any time the underlying record changes, a new statement identifier should be generated. 

Suggested strategies for assigning identifiers to statements include:

* Generating a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) for each statement, storing this in internal systems, and updating it whenever the relevant record(s) that make up a statement are updated; 

* Generating a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) as a prefix, and appending a local record identifier, and version identifier to it;

* Assigning a [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) in a domain controlled by the publisher to each statement. 

Whilst the schema is agnostic as to the exact strategy that data publishers use to generate statement identifier, it enforces a minimum length of 32 characters (the length of a hexidecimal UUID) in order to avoid use of identifiers that are likely to fail a uniqueness test. 


## Identifying people, companies and other entities

### Entity Identifiers




### Person Identifiers


