Beneficial Ownership Data Standard
==================================

This repository contains work in progress for the development of a data specification and standard for publication and consumption of data about Beneficial Ownership.

You can find the latest draft of the schema and documentation for review at [http://beneficial-ownership-data-standard.readthedocs.io/](http://beneficial-ownership-data-standard.readthedocs.io/)

You can share feedback on the standard through this project's issue tracker. 

## About

This work is taking place under the auspices of the Open Ownership project. More details on the project are avaiable at http://www.openownership.org 

The work will be guided by the Data Standard Working Group, and initial phases will take place between December 2016 and March 2017.

### Contact

For more details about the Open Ownership project, please contact the project coordinator, [Zosia Sztykowski](mailto:zosia@openownership.org)

### Partners and funders

The initial development of the Beneficial Ownership Data Standard is funded through support for the Open Ownership project from the UK Department for International Development. Open Ownership is a project of [Transparency International](https://www.transparency.org/), [One](https://www.one.org/international/), the [Open Contracting Partnership](http://www.open-contracting.org), the [World Wide Web Foundation](http://www.webfoundation.org), [Global Witness](https://www.globalwitness.org/en-gb/) and [The B Team](http://bteam.org/)

## Technical documentation

### Virtual Environment Set-up

To set up a virtual environment for the project:

```
virtualenv -p python3 .ve
source .ve/bin/activate
pip install -r requirements.txt
```

### Building the documentation

```
cd docs
make html
```

To serve a copy of the docs locally:

```
cd docs
python -m http.server 
```

And then access at http://localhost:8000/ 

