Schema reference
================

```eval_rst 

.. attention:: 
    
    This is the **beta** of the schema. This version is ready for test implementations. 

    Implementers should be aware that future changes are anticipated, before a version 1.0 release. However, from this beta release onwards, any structural changes, or major definitional changes will only take place following consultation, with a clear changelog provided, and with the documentation of previous versions maintained in archive form. 

    The schema contains a draft **structure** and **fields** but does not yet specify substantial constraints or explicit required fields. 

```

The following is an A - Z guide to the components of the Data Standard's schema. Details of each component's properties are provided in a table generated from the JSON schema. (For a structured view of how components fit together in the JSON schema, use the [Schema browser](data-schema-browser.md).)

The top-level components are:

* [Beneficial ownership statements](#beneficialownershipstatement)
* [Entity statements](#entitystatement)
* [Person statements](#personstatement)
* [Arrangement statements]()

These top-level components must be packaged up in a [statement package](#statement-packages) for a [data release](building-data-releases.md).



## Address

Due to the diversity of address formats used across systems, and the extent to which data is inconsistently entered across these data fields in source systems and legacy datasets, the schema uses a very simple address format for data exchange - relying upon consuming systems to parse addresses before carrying out any structured comparison. However, designers of new data collection systems are encouraged to choose an appropriate structured format, with reference to established standards, and awareness of the need to accomodate addresses from across the world. See [issue 18](https://github.com/openownership/data-standard/issues/18) for more details.

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Address
```


## AlternateName

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/AlternateName
```


## Annotation

The annotation property currently allows for an array of simple annotation objects. This is a placeholder which could be extended in future to include structured information qualifying the nature of the interest held.

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Annotation
```


## AssertingParty

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/AssertingParty
```


## BeneficialOwnershipStatement

A beneficial ownership statement is made up of statements about an entity, an interestedParty (either an entity, a person or null party), and details of the interest. Additionally, annotations on the interest, provenance and versioning information can be provided.

```eval_rst
.. jsonschema:: ../schema/beneficial-ownership-statement.json
    :collapse: interestedParty,interests,source,subject/entity
```

## EntityStatement

```eval_rst
.. jsonschema:: ../schema/entity-statement.json
   :collapse: identifiers,addresses,source
```

## Identifier

The identifier component is used to connect a statement to the real-world person or entity that it refers to, using one or more existing known identifiers. See [Real world identifiers](identifiers.md) for technical guidance on when and how to use this component.


```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Identifier
```


## Interest

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Interest
   :collapse: share,annotations
```


## PersonStatement

```eval_rst
.. jsonschema:: ../schema/person-statement.json
   :collapse: alternateNames,identifiers,source,placeOfResidence,placeOfBirth,addresses
```


## ReplacesStatement
See [Updating statements](updating-statements.md) for technical guidance on when and how to use this property.


## Share

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Interest/properties/share
```

## Source

See [the provenance pages](provenance.md) for a discussion of provenance modelling.

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Source
```

## StatementDate

See https://github.com/openownership/data-standard/issues/12 for a discussion of handling fuzzy dates.

Our current schema uses a regular expression to allow YYYY, YYYY-MM, YYYY-MM-DD or full datetimes. 


## Statement packages

At the top level of any structured file are arrays (packages) of statements. All the statements in a package must be the same type of object; that is, all ```beneficialOwnershipStatements```, all ```entityStatements```, all ```beneficialOwnershipStatements```, or similar. See [Building a release package](building-release-package.md) for technical guidance.

```eval_rst
.. jsonschema:: ../schema/bods-package.json
```

## StatementReference

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/StatementReference
```

## Unspecified

```eval_rst
.. jsonschema:: ../schema/components.json
   :pointer: /definitions/Unspecified
```




