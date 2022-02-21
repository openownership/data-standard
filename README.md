Beneficial Ownership Data Standard (BODS)
========================================

[![Documentation Status](https://readthedocs.org/projects/beneficial-ownership-data-standard/badge/?version=latest)](https://standard.openownership.org/en/latest/?badge=latest)

The Beneficial Ownership Data Standard provides a specification for modelling and publishing information on the beneficial ownership and control of companies. 

It has been created by [OpenOwnership](https://www.openownership.org), and is provided under an open license for re-use. 

You can find the latest version of the schema and documentation for review at [https://standard.openownership.org/](https://standard.openownership.org/)

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

### Build & test the docs locally

(Note if you need to change the theme you must instead use https://github.com/openownership/data-standard-sphinx-theme . If you only need to change the content, read on).

Clone this repository and change to the directory of this repository.

Create a Python Virtual Environment. It should be python3.8 to match our build server.

    python3 -m virtualenv -p python3.8 .ve

(If you don't have python3.8 installed [see here](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).)

Activate the virtual environment:

    source .ve/bin/activate

Install Python libraries:

    pip install -r requirements_test.txt

To actually build the docs:

    sphinx-build  docs/ _build

To see the docs, open a new terminal window and run a development webserver:

    cd _build
    python3 -m http.server

Leave this command running, and you can now go to http://127.0.0.1:8000/ to see the docs.

Edit source files as needed.  Return to your original window and rerun the build command above. Reload in web browser. Repeat!

To run the tests:

    pytest tests

To build another language, instead use this build command:

    sphinx-build  -D language=ru  docs/ _build

### Translation

Translation consists of generating strings to be translated from the English docs, pushing them to Transifex, fetching translations back from Transifex, and then you can build the docs in the other languages you need.

To run the steps in the translation workflow, you need to install this repo and its dependencies in your local environment.

```
$ pip install -r requirements.txt
```

You also need to make sure you have `gettext`, `pybabel` and (for SVGs) `itstool` installed in whatever environment you're running this in:

```
$ apt-get install gettext
$ apt-get install python-babel
$ apt-get install itstool
```

And you need to get a [Transifex API key](https://www.transifex.com/user/settings/api/), make sure you have access to the [BODS project on Transifex](https://www.transifex.com/OpenDataServices/bods-v01). There are [full instructions for setting up and configuring your local machine for the translation workflow](https://openownership.github.io/bods-dev-handbook/translations.html) in the bods-dev-handbook.

Run the following commands from the root directory unless otherwise specified (eg. sometimes it's less complicated to run them from `docs`).

0. *Before you start*, run `tx-pull -a` to make sure you have the most up to date translations in your local environment.

**When you change text in the docs** you need to do the following so that they can be translated:

1. `cd docs`
2. Run `make gettext` to extract translatable English strings from the docs. (This generates `.pot` files into `docs/_build/gettext/`.)

**If you modified the schema** also:

* Run `pybabel extract -F babel_bods_schema.cfg . -o docs/_build/gettext/schema.pot` to extract translatable English strings from the schema.

**If you modified the codelists** also:

* Run `pybabel extract -F babel_bods_codelist.cfg . -o docs/_build/gettext/codelist.pot` to extract translatable English strings from the codelists.
* If you change (add, remove, rename) a column heading in a codelist CSV, you must also edit the `babel_bods_codelist.cfg` file to match.

**If you modified an SVG diagram** also:

* Run `itstool -i svg-its-rules.xml -o docs/_build/gettext/svg.pot docs/_assets/*.svg` to extract translatable English strings from the SVGs.

**If you added, deleted or renamed** files or you want to use a **different Transifex project**, run (from root, ie. `cd ../`):

```
rm -f .tx/config
sphinx-intl create-txconfig
sphinx-intl update-txconfig-resources --pot-dir docs/_build/gettext --locale-dir docs/locale --transifex-project-name bods-test
```

(Replacing `bods-test` with a different Transifex project name.)

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
