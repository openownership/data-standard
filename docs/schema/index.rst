Data Schema
===========

.. attention:: 
    
    This is v0.2 of the Beneficial Ownership Data Standard. It includes updates to the data model and additional codelist information. Implementers should be aware that future changes are anticipated, before a version 1.0 release. See the :doc:`Changelog <changelog>` and `About <../about>`_ pages for more information.

    **MUST** and **SHOULD** are used in the schema to denote required and recommended elements of the Standard, as defined in `RFC2119 <https://tools.ietf.org/html/rfc2119>`_.

BODS provides a common data model for encapsulating information about the :doc:`beneficial ownership <../primer/whatisbo>` of corporate entities and related arrangements, to facilitate :doc:`sharing of information <../primer/whatisthebods>`. In particular, the :any:`data model <key-concepts>` captures direct and indirect relationships of ownership and control by entities (such as companies) by other entities (including trusts and joint shareholdings) or by natural persons. 

The data model, as specified here in the Data Schema, is intended to represent, or help identify, ultimate beneficial ownership: the natural person(s) who ultimately benefit from, or control, an entity. 

The :doc:`schema browser <schema-browser>` provides a way of digging through the schema's structure, showing how its components and fields fit together. Alternatively, the :doc:`schema reference <reference>` presents these elements and their descriptions in easy-to-reference tables. 

Further considerations regarding the validation, publishing, and lifecycle of data are included in `technical guidance <guidance>`_.

.. toctree::
   :maxdepth: 1

   concepts
   schema-browser
   reference
   guidance/index
   changelog
   conformance


