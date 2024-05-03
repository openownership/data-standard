.. _information-updates:

Information updates
========================================

Systems that collect and manage beneficial ownership information often handle the updating or confirmation of existing records. Depending on how the information is managed, the BODS data that is produced will offer a high or low-resolution picture of the changing nature of a beneficial ownership network. Data management systems handling information updates need to meet the minimal set of requirements below, to offer a low-resolution picture. 


Minimal requirements 
------------------------
A new BODS statement MUST be generated for an element (entity, person or relationship) of a subject's beneficial ownership network when its details are changed or confirmed. See :ref:`generating-statements` for further requirements. 

The ``recordId`` of the subject of each beneficial ownership network MUST be stable over time. That is: when the details of the beneficial ownership network's subject change, or are confirmed, the new Statement generated must contain the same ``recordId`` as in the outdated Statement.

Each BODS statement issued in relation to any element of a subject's declared beneficial ownership network, at any point in time, MUST contain the subject's ``recordId`` as its ``declarationSubject``.

The BODS data producer SHOULD publish guidance for data users explaining how to understand the lifecycle of declared information with reference to the available BODS data. 



Full requirements 
------------------------
The minimal requirements stated above MUST be met.

The lifecycle of a record about an element (entity, person or relationship) within a beneficial ownership network is represented by a series of Statements:

* The ``recordId`` of each element of a beneficial ownership network MUST be stable over time. That is: when the details of an element change, or are confirmed, the new Statement generated must contain the same ``recordId`` as in the outdated Statement.

* The first time a Statement is published about an element within a beneficial ownership network, the ``recordStatus`` MUST be 'new'. When the details of the element change, or are confirmed, in the new Statement ``recordStatus`` MUST be 'updated'. When the element is no longer a part of the beneficial ownership network, in the new Statement ``recordStatus`` MUST be 'closed'.

* When the details of an element have not changed but are confirmed to be accurate, a new Statement SHOULD be generated with the same ``recordId`` as in the outdated Statement and with ``recordStatus`` 'updated'.

Once a series of Statements about a given element is closed, further Statements with the related ``recordId`` MUST NOT be generated.

When the subject or the interested party of a relationship change, the lifecycle of that relationship is considered to have ended. For example, if the owner of a company transfers their interest to a relative, the ``recordStatus`` of the first relationship would be 'closed', and details of a new record would be published.

Requirements for special cases
------------------------------


Error correction
++++++++++++++++

Errors in published data may be due to mistakes at the point of information disclosure, or the incorrect processing of information by the data management system.

In either case, errors SHOULD be corrected by the issuing of new statements including an :any:`annotation <schema-annotation>`, with the ``motivation`` 'correcting' and a ``description`` of the correction, and an updated ``publicationDetails.publicationDate``.

See the example in :any:`guidance-dates`.


Redaction
+++++++++

If sensitive information is accidentally published in a Statement, the Statement MAY be republished with the same statement identifier and updated property values.
