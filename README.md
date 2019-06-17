Beneficial Ownership Data Standard
==================================

This repository contains work in progress for the development of a data specification and standard for publication and consumption of data about Beneficial Ownership.

You can find the latest draft of the schema and documentation for review at [http://standard.openownership.org/](http://standard.openownership.org/)

You can share feedback on the standard through this project's issue tracker.

## About

This work is taking place under the auspices of the Open Ownership project. More details on the project are available at http://www.openownership.org

The work will be guided by the Data Standard Working Group, and initial phases will take place between December 2016 and March 2017.

### Contact

For more details about the Open Ownership project, please contact the project coordinator, [Zosia Sztykowski](mailto:zosia@openownership.org)

### Partners and funders

The initial development of the Beneficial Ownership Data Standard is funded through support for the Open Ownership project from the UK Department for International Development. Open Ownership is a project of [Transparency International](https://www.transparency.org/), [One](https://www.one.org/international/), the [Open Contracting Partnership](http://www.open-contracting.org), the [World Wide Web Foundation](http://www.webfoundation.org), [Global Witness](https://www.globalwitness.org/en-gb/) and [The B Team](http://bteam.org/)

## Technical documentation

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
```

And you need to get a [Transifex API key](https://www.transifex.com/user/settings/api/), make sure you have access to the [BODS project on Transifex](https://www.transifex.com/OpenDataServices/bods-v01)

Run the following commands from the root directory unless otherwise specified (eg. sometimes it's less complicated to run them from `docs`).

**When you change text in the docs** you need to do the following so that they can be translated:

1. `cd docs`
2. Run `make gettext` to extract translatable English strings from the docs.

**If you modified the codelists** also:

1. Run `pybabel extract -F babel_bods_schema.cfg . -o docs/_build/gettext/schema.pot` to extract translatable English strings from the schema.

**If you modified the schema** also:

1. Run `pybabel extract -F babel_bods_codelist.cfg . -o docs/_build/gettext/codelist.pot` to extract translatable English strings from the codelists.

**If you added, deleted or renamed** files or you want to use a **different Transifex project**, run (from root, ie. `cd ../`):

```
rm -f .tx/config
sphinx-intl create-txconfig
sphinx-intl update-txconfig-resources --pot-dir docs/_build/gettext --locale-dir docs/locale --transifex-project-name bods-v01
```

(Replacing `bods-v01` with a different Transifex project name if necessary.)

And then:

2. Run `tx push -s` to **push to Transifex**.

Now the files are ready to be translated in Transifex.

**To fetch new translations** when they're done, you need to:

1. Run `tx pull -a` to fetch all, or `tx pull -l ru` to fetch a particular language.
2. Compile the schema and codelist translations:

```
$ pybabel compile --use-fuzzy -d docs/locale -D schema
$ pybabel compile --use-fuzzy -d docs/locale -D codelist
```

**Commit** the new or updated .po files in `docs/locale`, using a separate commit from your edits to the source (RST, JSON or CSV) files.

**TEMPORARILY** also commit `schema.mo` and `codelist.mo` for each language. You'll need to force add these as usually git ignores .mo files. This is a quick fix for readthedocs, and this stage will be going away soon (see [#190](https://github.com/openownership/data-standard/issues/190)). ie (replacing `ru` for any other languages and repeating):

```
git add -f docs/locale/ru/LC_MESSAGES/schema.mo
git add -f docs/locale/ru/LC_MESSAGES/codelist.mo
```

**To build another language locally** (pass the language code you want)..

```
$ cd docs
$ sphinx-build -b html -D language=ru . _build/html/ru
```
