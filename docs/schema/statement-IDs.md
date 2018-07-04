Statement IDs
=============

**Publishers MUST generate globally unique and persisent identifiers for each statement.**

Each statement must have a unique id. This id must be globally unique: such that no two statements from the same organisation, or from different organisations, could ever have the same identifier. To avoid any clash between identifiers from different publishers, they should start with a publisher-related [uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier), and may be suffixed with additional characters to distinguish versions of a statement as required by local implementations.

Once published, statements must be immutable. This means any time the underlying record changes, a new statement id should be generated. 

Therefore, suggested strategies for assigning ids to statements include:

* Generating a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) for each statement, storing this in internal systems, and updating it whenever the relevant record(s) that make up a statement are updated; 

* Generating a [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) as a publisher-related prefix, and appending a local record identifier, and version identifier to it;

* Assigning a [URI](https://en.wikipedia.org/wiki/Uniform_Resource_Identifier) in a domain controlled by the publisher to each statement. 

Whilst the schema is agnostic as to the exact strategy that data publishers use to generate statement ids, it enforces a minimum length of 32 characters (the length of a hexidecimal UUID) in order to avoid use of ids that are likely to fail a uniqueness test. 

