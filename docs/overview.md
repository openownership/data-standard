Overview (stub)
========


```eval_rst
  .. warning:: This is an old version of the data standard. `See latest version <https://standard.openownership.org/en/latest/>`_.
```


The beneficial ownership data standard will be made up of two parts:

* A data schema that sets out how beneficial ownership data MUST or SHOULD be formatted for interoperability, and that describes the fields of data that systems MUST or SHOULD provide. 

* A set of implementation recommendations that describe the way in which beneficial ownership data SHOULD be collected and published. 

MUST and SHOULD are used as defined by [RFC2119](https://tools.ietf.org/html/rfc2119).

This documentation currently contains a draft of the **schema**, with some initial (though non-exhaustive) **implementation recommendations**.

### Scope

* The standard is concerned with relationships of **ownership** and **control**

* The schema will describe relationships between a **legal entity** such as a company, trust, partnership, or person acting as a nominee, and a **natural person**. These may be direct relationships, or may be indirect through intermediate legal entities. 

* **Ownership** is understood as *"the right to receive profits, income, interest, etc. from a property or investment"* (NOTE:  Definition of “beneficial ownership” from the Cambridge Business English Dictionary) and may operate through a range of mechanisms, including share ownership and contractual rights. 

The standard does not set any threshold on levels of shareholding or rights required in order to beneficial ownership to be present, leaving this decision to individual implementers. i.e. it will be possible to represent shareholdings of 0.1% or less using the standard, but individual implementers may choose to set thresholds for the levels of ownership they will require before they collect, produce or consume such data.  

* **Control** is understood as the ability to direct or influence the actions of a **legal entity**, and may operate through a range of mechanisms, including, but not limited to, ownership of shares with voting rights, or contractual agreements. 

As with ownership, the standard does not set any threshold on levels of control that can be represented. 

* We use the concept of **beneficial ownership** to cover both **ownership** (economic benefit) and **control**. 

* Relationships of **ownership** and **control** may be **direct**, **indirect**, operating through intermediate entities, or may be declared as ultimate beneficial ownership, without information on whether the relationship is direct or indirect. 

* In cases of indirect relationships, the schema will support inclusion of the **intermediate relationships** between **legal entities**. *E.g.* information on company ownership structures will be captured within the scope of the standard. The implementation guidance will recommend that this information is collected and published wherever possible. 

* In order to allow clear identification of beneficial owners the schema will provide means of describing attributes of **natural persons**, including, but not limited to, their name, nationality, country of residence, date of birth, and any public identification numbers. 

* Where particular information cannot be published for legal or privacy reasons, the implementation guidance will recommend placeholder entries are published, with reasons for non-publication or redaction clearly explained using the schema. 

* The schema does not seek to provide globally unique identifiers to natural persons or legal entities, though it will allow reuse of existing identifiers. Consuming applications will be required to perform their own matching and deduplication on both legal entity and natural person components where their use-cases require this.  

* In order allow clear identification of the entities owned or controlled, or involved in indirect ownership and control chains, the schema will provide means of describing the attributes of **legal entities**, including the nature of the entity, names, addresses and registration details. 

* Complex arrangements, such as trusts, consortia, and individuals acting as a nominee for another, will be included within the definition of a **legal entity**. 

* The schema will incorporate **provenance** information for ownership and control statements, and for descriptions of legal entities and natural persons. This will include links to **documents** that provide evidence for statements made. Such documents will need to be stored externally. 

* The schema is intended for exchange of **open data**. Data publishers and consumers will need to independently consider the legal regime around the publication or use of any personally identifying information covered by the standard. 

* The implementation guidance will describe how to provide **bulk data** and **API access** to aggregated beneficial ownership information. It will not describe advanced API patterns such as querying, or retrieval of a sub-set of all records (with the exception of fetching all records changed since a given date). 