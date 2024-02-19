.. _conformance:

Conformance and validation
===========================

Conformance
----------------

A comforming implementation of BODS:

* MAY use a subset of the schema's terms

* MAY use terms from outside the schema **only** where the schema's terms are insufficient

* MUST use the schema’s terms consistently with their definitions

A conforming implementation of BODS that serialises to JSON MUST validate against the standard’s JSON schema. 

`Adapted from Popolo Project specification <http://www.popoloproject.com/specs/#conformance>`_

Extending the schema
--------------------
If you need to extend the schema:

* re-use `other publisher's extensions <https://github.com/openownership/data-standard/issues?q=is%3Aissue+label%3Aextension>`_ where possible

* document your extensions `in the project issue tracker <https://github.com/openownership/data-standard/issues/>`_ with the 'extensions' tag


Validation
----------
The BODS JSON schema includes validation checks that are possible to define using JSON schema 2020-12.

The `BODS Data Review Tool <https://datareview.openownership.org/>`_ validates conformance to the JSON schema and to additional requirements that can be validated programmatically but are not included in the schema. For example, it checks that record identifiers in the ``subject`` and ``interestedParty`` fields of Relationship statements appear in at least one statement elsewhere in the BODS JSON array. The Data Review Tool can ingest data serialised as JSON and in tabular form. 



