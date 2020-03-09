Beneficial Ownership Data Standard (BODS)
========================================

[![Documentation Status](https://readthedocs.org/projects/beneficial-ownership-data-standard/badge/?version=latest)](http://standard.openownership.org/en/latest/?badge=latest)

The Beneficial Ownership Data Standard provides a specification for modelling and publishing information on the beneficial ownership and control of companies. 

It has been created by [OpenOwnership](http://www.openownership.org), and is provided under an open license for re-use. 

You can find the latest version of the schema and documentation for review at [http://standard.openownership.org/](http://standard.openownership.org/)

We welcome feedback on the standard through this project's issue tracker.

## Contact

Please direct any correspondence to [support@openownership.org](mailto:support@openownership.org)

# Technical documentation

### Dependencies

The frontend uses **docson** JavaScript library to visualise the JSON schema. BODS uses [a specific patched fork of docson](https://github.com/OpenDataServices/docson/tree/master-bods) (which is different from the patched fork used by other standards). This is included in the `data-standard` repo rather than as part of the [Sphinx theme](https://github.com/openownership/data-standard-sphinx-theme) because it is necessary regardless of which theme is used to build the docs. See [data-standard-sphinx-theme#36](https://github.com/openownership/data-standard-sphinx-theme/issues/36) for the particulars of the patches. The situation with the various branches and patches of docson is in need of serious improvement.

Meanwhile, to include the appropriate version of docson JS after you clone this repo, you need to run:

```
git submodule init
git submodule update
```

### Build the docs locally

Please see https://github.com/openownership/data-standard-sphinx-theme

### Translation

Translation consists of generating strings to be translated from the English docs, pushing them to Transifex, fetching translations back from Transifex, and then you can build the docs in the other languages you need.

To run the steps in the translation workflow, you need to install this repo and its dependencies in your local environment.

```
$ pip install -r requirements.txt
```

You also need to make sure you have `gettext` and `pybabel` installed in whatever environment you're running this in:

```
$ apt-get install gettext
$ apt-get install python-babel
$ apt-get install itstool
```

And you need to get a [Transifex API key](https://www.transifex.com/user/settings/api/), make sure you have access to the [BODS project on Transifex](https://www.transifex.com/OpenDataServices/bods-v01). There are [full instructions for setting up and configuring your local machine for the translation workflow](https://openownership.github.io/bods-dev-handbook/translations.html) in the bods-dev-handbook.

Run the following commands from the root directory unless otherwise specified (eg. sometimes it's less complicated to run them from `docs`).

**When you change text in the docs** you need to do the following so that they can be translated:

1. `cd docs`
2. Run `make gettext` to extract translatable English strings from the docs.

**If you modified the schema** also:

* Run `pybabel extract -F babel_bods_schema.cfg . -o docs/_build/gettext/schema.pot` to extract translatable English strings from the schema.

**If you modified the codelists** also:

* Run `pybabel extract -F babel_bods_codelist.cfg . -o docs/_build/gettext/codelist.pot` to extract translatable English strings from the codelists.

**If you modified an SVG diagram** also:

* Run `itstool -i svg-its-rules.xml -o docs/_build/gettext/svg.pot docs/_assets/*.svg` to extract translatable English strings from the SVGs.

**If you added, deleted or renamed** files or you want to use a **different Transifex project**, run (from root, ie. `cd ../`):

```
rm -f .tx/config
sphinx-intl create-txconfig
sphinx-intl update-txconfig-resources --pot-dir docs/_build/gettext --locale-dir docs/locale --transifex-project-name bods-v01
```

(Replacing `bods-v01` with a different Transifex project name if necessary.)

And then:

3. Run `tx push -s` to **push to Transifex**.

Now the files are ready to be translated in Transifex.

4. **To fetch new translations** when they're done, you need to run `tx pull -a` to fetch all, or `tx pull -l ru` to fetch a particular language.

5. **Commit** the new or updated .po files in `docs/locale`, using a separate commit from your edits to the source (RST, JSON or CSV) files.

6. **Build translated SVGs** for each language using itstool, and commit these (because we can't easily install itstool on readthedocs):

```
pybabel compile --use-fuzzy -d docs/locale -D svg
itstool -m docs/locale/ru/LC_MESSAGES/svg.mo -o docs/_build_svgs/ru docs/_assets/*.svg
```

**To build another language locally** to preview it (pass the language code you want)..

```
$ cd docs
$ sphinx-build -b html -D language=ru . _build/html/ru
```
