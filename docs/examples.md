## Examples

In the [tools folder](https://github.com/openownership/data-standard/) of the schema repository a script is available to generate dummy data, or blank example data files. 

### A single direct owner

The example below represents a single statement, based on a UK PSC disclosure:

```eval_rst

.. literalinclude:: ../examples/1-single-direct.json
    :language: json
   
```
 

### Updating ownership

To update a previous statement, a new beneficial ownership statement, with a ```replacesStatement``` property is required.

> Example to come


### Joint ownership

To model joint ownership, an artificial entity, owned by the two parties responsible for it, should be included within a chain of ownership

> Example to come

### Ownership through an intermediate firm

Ownership through an intermediate firm can be modelled.

> Example to come

### Blank data

If the beneficial owner of Chrinon Ltd had not been identified, a null statement as follows could be used:

```eval_rst

.. literalinclude:: ../examples/null-statement.json
    :language: json
    :emphasize-lines: 33-36
   
```