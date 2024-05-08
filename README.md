Beneficial Ownership Data Standard (BODS)
========================================

[![Documentation Status](https://readthedocs.org/projects/beneficial-ownership-data-standard/badge/?version=latest)](https://standard.openownership.org/en/latest/?badge=latest)

The Beneficial Ownership Data Standard (BODS) is an open standard providing a specification for modelling and publishing information on the beneficial ownership and control of corporate vehicles. 

You can find the latest version of the schema and documentation at [https://standard.openownership.org](https://standard.openownership.org)

## Governance

BODS has been created by [Open Ownership](https://www.openownership.org) in partnership with [Open Data Services](https://opendataservices.coop/), and is provided under an open license for re-use. 

An [open data standard working group](https://standard.openownership.org/en/latest/about/governance.html) of data experts, beneficial ownership specialists and other interested parties also provides advice and helps guide the development of BODS.

The working group is co-chaired by Open Ownership and Open Data Services - and anyone can apply to join the group by [filling out this form](https://docs.google.com/forms/d/e/1FAIpQLSdRSmSUxyyv2t1k3vWXZ_3EhTW_f603MeGxgyjKnbNNE9vvbQ/viewform). Virtual group meetings are held quarterly and communication is coordinated through a [Google group](https://groups.google.com/a/openownership.org/g/data-standard-wg?pli=1).

All changes to the BODS schema and documentation take place this GitHub repo. A [feature tracker](https://github.com/openownership/data-standard/projects/4) is available which documents all new BODS features being researched, proposed or implemented. 

Features currently on the tracker are those adopted for development by the Open Ownership and Open Data Services teams following work with implementers of beneficial ownership reforms and in consultation with the Data Standard Working Group. 

However, anyone can submit a [feature request ticket](https://github.com/openownership/data-standard/issues/new?assignees=&labels=feature+request&template=feature_request.md&title=%5BFeature+request%5D), contribute to a feature development ticket, or make an [implementation proposal](https://github.com/openownership/data-standard/issues/new?assignees=&labels=&template=implementation-proposal-template.md&title=Implementation+proposal%3A+%5BFEATURE+NAME%5D+no.X). The data standard support team at Open Ownership will consider and reply to any submitted feature requests within a month from submission.

See the [project issue tracker](https://github.com/openownership/data-standard/issues) for a list of feature requests and issues.

## Contact

Please direct any correspondence to [support@openownership.org](mailto:support@openownership.org)

# Technical documentation

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
