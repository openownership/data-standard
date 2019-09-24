## Examples


```eval_rst

  .. warning:: This is an old version of the data standard. `See latest version <https://standard.openownership.org/en/latest/>`_.
```


In the [tools folder](https://github.com/openownership/data-standard/) of the schema repository a script is available to generate dummy data, or blank example data files. 

The following manually constructed examples highlight key elements of how beneficial ownership statements can be constructed.

### A single direct owner

The example below represents a single statement, based on a UK PSC disclosure tha asserts 100% ownership of Chrinon Ltd by Chris Taggart. 

```eval_rst

.. literalinclude:: ../examples/1-single-direct.json
    :language: json
   
```
 

### Updating ownership

To update a previous statement, a new beneficial ownership statement, with a ```replacesStatement``` property is required.

In the (fictional) example below, the previous statement that Chris Taggart has 100% ownership of Chrinon Ltd is replaced by a new statement showing 50% ownership. A separate statement in the statementGroup declares a new owner of the other 50%, although notes that this owner has not yet been identified such that their information can be disclosed.

Note that only **changed statements** need to new statement identifiers (assuming that the same orignal submissions of data are being used).

```eval_rst

.. literalinclude:: ../examples/2-single-update.json
    :language: json
    :emphasize-lines: 8, 72, 77-118
```


### Joint ownership

To model joint ownership, an artificial 'arrangement', owned by the two parties responsible for it, should be included within a chain of ownership.

```eval_rst

.. literalinclude:: ../examples/3-joint-ownership.json
    :language: json
```

### Ownership via trust

To model ownership via a trust:

```eval_rst

.. literalinclude:: ../examples/4-ownership-via-trust.json
    :language: json
```


### Blank data

If the beneficial owner of Chrinon Ltd had not been identified, a null statement as follows could be used:

```eval_rst

.. literalinclude:: ../examples/null-statement.json
    :language: json
    :emphasize-lines: 33-36
   
```