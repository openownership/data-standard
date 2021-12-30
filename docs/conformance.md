Conformance and validation
===========================

## Conformance statement

* A conforming implementation **may** use only a subset of this specification’s terms.
* It **must not** use terms from outside this specification’s terms where this specification’s terms would suffice.
* It **may** use terms from outside this specification’s terms where this specification’s terms are insufficient.
* Its usage of this specification’s terms **must** be consistent with the semantics of those terms.
* If an implementation serializes to JSON, its serializations **must** validate against this specification’s JSON Schema.

(Statement [adapted from Popolo Project specification](http://www.popoloproject.com/specs/#conformance))

## Extending the schema

Publishers providing additional properties in their implementations are encouraged to [document these in the project issue tracker](https://github.com/openownership/data-standard/issues/) with the 'extensions' tag, and to re-use [other publisher's extensions](https://github.com/openownership/data-standard/issues?q=is%3Aissue+label%3Aextension) where possible.

## Validation

No public validator available for the beta release is currently available.

The current schema includes minimal validation requirements, and should be treated as a guide to data structure, rather than a full validation schema. 