<style><!--
/* override table width restrictions */
.wy-table-responsive table td, .wy-table-responsive table th {
    white-space: normal !important;
}

.wy-table-responsive {
    margin-bottom: 24px;
    max-width: 100%;
    overflow: visible !important;
}


.wy-table-responsive th:nth-of-type(1) {
    width:10%;
}

.wy-table-responsive th:nth-of-type(2) {
    width:10%;
}

.wy-table-responsive th:nth-of-type(3) {
    width:60%;
}

.wy-table-responsive th:nth-of-type(4) {
    width:10%;
}

.wy-table-responsive th:nth-of-type(5) {
    width:10%;
}--></style>

# Specification

The beneficial ownership standard is made up of two parts:

* A data schema that sets out how beneficial ownership data MUST or SHOULD be formatted for interoperability, and that describes the fields of data that systems MUST or SHOULD provide. 

* A set of implementation recommendations that describe the way in which beneficial ownership data SHOULD be collected and published. 

```eval_rst 

.. attention:: 
    
    This is the **beta** of the schema. This version is ready for test implementations. 

    Implementers should be aware that future changes are anticipated, before a version 1.0 release. However, from this beta release onwards, any structural changes, or major definitional changes will only take place following consultation, with a clear changelog provided, and with the documentation of previous versions maintained in archive form. 

    The schema contains a draft **structure** and **fields** but does not yet specify substantial constraints or explicit required fields. 

```

## Conceptual model

The conceptual model for the standard was developed in late 2016/early 2017 and [is documented here](https://github.com/openownership/data-standard/issues/7).

We model information on beneficial ownership in terms of a collection of statements. Each statement represents the assertions made by a particular agent at a particular point in time.

It is up to data consumers to decide which statements to trust, and to reconcile the identity of the entities and persons described in those statements based on the identifying information contained within each statement. 

![Conceptual Model](_assets/ConceptualModel-March2017.png)

This abstraction is important to represent the reality of how data is provided, to support integration of data from different systems and [bi-temporal modelling](https://en.wikipedia.org/wiki/Bitemporal_Modeling), and to recognise that any dataset may contain overlapping or conflicting claims about ownership and control that need to be resolved in application specific ways. 

## Schema browser

The draft Beneficial Ownership Data Standard is defined using [JSON Schema 0.4](http://json-schema.org/). The structured schema can be [accessed here](_static/beneficial-ownership-statements.json) or explored using the viewer below.

<script src="_static/docson/widget.js" data-schema="../beneficial-ownership-statements.json"></script>

## Serializations

We have currently modelled the schema with the option for:

* (1) Entity, person and provenance statements to be nested inside a beneficial ownership statement;
* (2) Each kind of statement to be provided at the same level of heiarchy, with a cross-reference between them;

This second option is sketched out with a view of serialisations that may make use of the [JSON Lines](http://jsonlines.org/) format for sharing or streaming large quantities of statements, rather than enclosing all statements ot be exchanged in a single object. 

## Sections

The following tables are generated from the schema, and outline the different components of the data model. 

### Statement Groups

At the top level of any structured file is always an array of ```statementGroups```.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/statementGroup.csv
```

Each statementGroup MUST include an array of one or more ```beneficialOwnershipStatements``` and, where a cross-reference publication pattern is followed, may include arrays of other statements.

--- 

### BeneficialOwnershipStatement

A beneficial ownership statement is made up of statements about an entity, an interestedParty (either an entity, a person or null party), and details of the interest. Additionally, annotations on the interest, provenance and versioning information can be provided. 

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/BeneficialOwnershipStatement.csv
```

#### Interest

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Interest.csv
```

#### Annotation

The annotation property currently allows for an array of simple annotation objects. This is a placeholder which could be extended in future to include structured information qualifying the nature of the interest held.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Annotation.csv
```

#### Share

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Share.csv
```


---

### EntityStatement

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/EntityStatement.csv
```

---

### PersonStatement

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/PersonStatement.csv
```


#### AlternateName

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/AlternateName.csv
```


---


### NullParty

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/NullParty.csv
```



---
### Source

See [the provenance pages](provenance.md) for a discussion of provenance modelling.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Source.csv
```

---

### EntityStatementReference

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/EntityStatementReference.csv
```

### PersonStatementReference

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/PersonStatementReference.csv
```


---

### Common components

The following components are used at a number of points in the schema

#### Address

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Address.csv
```

#### Identifier

The identifier component is used to connect a statement to the person or entity that it refers to, using one or more existing known identifiers.

```eval_rst
.. csv-table::
   :header-rows: 1
   :widths: 20 65 15
   :file: docs/_schema_tables/Identifier.csv
```


#### Date

See https://github.com/openownership/data-standard/issues/12 for a discussion of handling fuzzy dates.

Our current schema uses a regular expression to allow YYYY, YYYY-MM, YYYY-MM-DD or full datetimes. 

#### ID

Publishers MUST generate globally unique and persisent identifiers for each statement.

These SHOULD start with a [uuid](https://en.wikipedia.org/wiki/Universally_unique_identifier) to avoid any clash between identifiers from different publishers, and MAY be suffixed with additional characters to distinguish versions of a statement as required by local implementations.

In many implementation scenarios, it will be appropriate to simply generate a distinct uuid for each statement. 

## Publication and use considerations

This section outlines considerations for publishers and consumers of the data

### Immutability of statements

Statements are considered immutable. If a field is updated, this should be considered to create a new statement, with a new identifier. 

### Updating statements

Where a ```statementGroup``` or ```statement``` replaces a previous statement this should be explicitly declared using a ```replacesStatementGroup``` or ```replacesStatement``` property. 



