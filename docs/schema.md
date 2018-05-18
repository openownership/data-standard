Schema reference
================



**NO LONGER NEEDED?**

The beneficial ownership standard is made up of two parts:

* A data schema that sets out how beneficial ownership data MUST or SHOULD be formatted for interoperability, and that describes the fields of data that systems MUST or SHOULD provide. 

* A set of implementation recommendations that describe the way in which beneficial ownership data SHOULD be collected and published. 

**/NO LONGER NEEDED?**

```eval_rst 

.. attention:: 
    
    This is the **beta** of the schema. This version is ready for test implementations. 

    Implementers should be aware that future changes are anticipated, before a version 1.0 release. However, from this beta release onwards, any structural changes, or major definitional changes will only take place following consultation, with a clear changelog provided, and with the documentation of previous versions maintained in archive form. 

    The schema contains a draft **structure** and **fields** but does not yet specify substantial constraints or explicit required fields. 

```




The following tables are generated from the schema, and outline the different components of the data model. 

## Statement packages

At the top level of any structured file are arrays (packages) of statements. All the statements in a package must be the same type of object; that is, all ```beneficialOwnershipStatements```, all ```entityStatements```, all ```beneficialOwnershipStatements```, or similar.

```eval_rst
.. jsonschema:: ../schema/bods-package.json
```

--- 

## BeneficialOwnershipStatement

A beneficial ownership statement is made up of statements about an entity, an interestedParty (either an entity, a person or null party), and details of the interest. Additionally, annotations on the interest, provenance and versioning information can be provided.

```eval_rst
.. jsonschema:: ../schema/beneficial-ownership-statement.json
    :collapse: interestedParty,interests,source,subject/entity
```


## Interest

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Interest
```

## Annotation

The annotation property currently allows for an array of simple annotation objects. This is a placeholder which could be extended in future to include structured information qualifying the nature of the interest held.

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Annotation
```

## Share

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Interest/share
```


---

## EntityStatement

```eval_rst
.. jsonschema:: ../schema/entity-statement.json
   :collapse: identifiers,addresses,source
```

---

## PersonStatement

```eval_rst
.. jsonschema:: ../schema/person-statement.json
   :collapse: alternateNames,identifiers,source,placeOfResidence,placeOfBirth,addresses
```


## AlternateName

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/AlternateName
```


---


## Unspecified

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Unspecified
```



---
## Source

See [the provenance pages](provenance.md) for a discussion of provenance modelling.

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Source
```

## AssertingParty

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/AssertingParty
```


---

## StatementReference

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/StatementReference
```


---

<h2>Common components</h2>

The following components are used at a number of points in the schema

## Address

Due to the diversity of address formats used across systems, and the extent to which data is inconsistently entered across these data fields in source systems and legacy datasets, the schema uses a very simple address format for data exchange - relying upon consuming systems to parse addresses before carrying out any structured comparison. However, designers of new data collection systems are encouraged to choose an appropriate structured format, with reference to established standards, and awareness of the need to accomodate addresses from across the world. See [issue 18](https://github.com/openownership/data-standard/issues/18) for more details.

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Address
```

## Identifier

The identifier component is used to connect a statement to the real-world person or entity that it refers to, using one or more existing known identifiers.

```eval_rst
.. jsonschema:: ../schema/components.json#/definitions/Identifier
```

## StatementDate

See https://github.com/openownership/data-standard/issues/12 for a discussion of handling fuzzy dates.

Our current schema uses a regular expression to allow YYYY, YYYY-MM, YYYY-MM-DD or full datetimes. 




