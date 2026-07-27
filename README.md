Beneficial Ownership Data Standard (BODS)
========================================

[![Documentation Status](https://readthedocs.org/projects/beneficial-ownership-data-standard/badge/?version=latest)](https://standard.openownership.org/en/latest/?badge=latest)

The Beneficial Ownership Data Standard (BODS) is an open standard providing a specification for modelling and publishing information on the beneficial ownership and control of corporate vehicles. 

- The latest version of the schema and documentation is at [standard.openownership.org](https://standard.openownership.org)
- Details of the project, its governance, and development of the standard are at [standard.openownership.org/en/main/about](https://standard.openownership.org/en/main/about/index.html)
- A handbook for those developing BODS is at [github.com/openownership/bods-dev-handbook](https://github.com/openownership/bods-dev-handbook)

## Current status of BODS 

BODS v0.4 was [released](https://standard.openownership.org/en/latest/standard/changelog.html) in May 2024. The documentation on the release branch (`0.4.0`) builds at [standard.openownership.org/en/0.4.0/](https://standard.openownership.org/en/0.4.0/), via ReadTheDocs. The release was translated into Spanish, French and Russian.

Subsequent to the release, non-normative documentation updates were made to the Primer, About and Governance pages. (These updates were not translated.) The updates were merged into the `main` branch and not back-ported to the `0.4.0` release branch.

So that readers benefit from the latest documentation updates, the default (standard.openownership.org) and latest (standard.openownership.org/latest) documentation URLs direct users to the documentation on the `main` branch [standard.openownership.org/en/main](https://standard.openownership.org/en/main).

The BODS schema is not in active development at the moment. Implementers should be aware that future changes may be made before a version 1.0 release.

## Contact

Please direct any correspondence to [support@openownership.org](mailto:support@openownership.org)

# Basic technical documentation

The following is a brief guide to technical setup and use. See the [dev handbook](https://github.com/openownership/bods-dev-handbook) for a complete account.

### Installation & setup

First, clone this repository so that you can work locally on your machine.

The frontend uses **docson** JavaScript library to visualise the JSON schema. BODS uses [a specific patched fork of docson](https://github.com/OpenDataServices/docson/tree/master-bods) (which is different from the patched fork used by other standards). This is included in the `data-standard` repo rather than as part of the [Sphinx theme](https://github.com/openownership/data-standard-sphinx-theme) because it is necessary regardless of which theme is used to build the docs. See [data-standard-sphinx-theme#36](https://github.com/openownership/data-standard-sphinx-theme/issues/36) for the particulars of the patches. The situation with the various branches and patches of docson is in need of serious improvement.

Meanwhile, to include the appropriate version of docson JS after you clone this repo, you need to change directory into the cloned repository and run:

```
git submodule init
git submodule update
```
Create a Python Virtual Environment. It should be python3.9 to match our build server.

    python3 -m virtualenv -p python3.9 .ve

(If you don't have python3.9 installed [see here](https://launchpad.net/~deadsnakes/+archive/ubuntu/ppa).)

Activate the virtual environment:

    source .ve/bin/activate

Install Python libraries:

    pip install -r requirements_test.txt


### Building the documentation locally

(Note if you need to change the theme you must instead use https://github.com/openownership/data-standard-sphinx-theme . If you only need to change the content, read on).

Once you have followed the installation and setup instructions above, you just need to change directory to that of your local repository and activate the virtual environement:

    source .ve/bin/activate

To actually build the docs:

    sphinx-build  docs/ _build

To see the docs, open a new terminal window and run a development webserver:

    cd _build
    python3 -m http.server

Leave this command running, and you can now go to http://127.0.0.1:8000/ to see the docs.

Edit source files as needed. Return to your original window and rerun the build command above. Reload in web browser. Repeat!

To build another language, instead use this build command:

    sphinx-build  -D language=ru  docs/ _build

### Running schema and json tests

Once you have followed the installation and setup instructions above, you just need to change directory to that of your local repository and activate the virtual environement:

    source .ve/bin/activate
    
To run the tests:

    pytest tests

### Managing the translation workflow

Translation consists of generating strings to be translated from the English docs, pushing them to Transifex, fetching translations back from Transifex, and then you can build the docs in the other languages you need. There are [full instructions for the translation workflow](https://openownership.github.io/bods-dev-handbook/translations.html) in the bods-dev-handbook.
