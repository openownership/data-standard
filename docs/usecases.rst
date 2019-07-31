Use cases
=========

The Beneficial Ownership Data Standard beta has been designed with
reference to the requirements of eight use-cases:

-  Data supply
-  Public Registers of Beneficial Ownership
-  Self-submitted data
-  Third-party submitted data
-  Self-published data

-  Data use
-  Procurement & onboarding screening and audit
-  General investigations
-  Data-led investigations
-  Data validation

These use cases are described below.

.. note::

    A full analysis of how far the needs of these use cases are met will take place as part of progress towards a 1.0 Release Candidate of the standard. 

This page builds on the `use case consultation
document <https://docs.google.com/document/d/1s1qqFAK3cDjTGAlCaQvPOb8KzKkssn9xu2HzWeY6amE/edit#>`__
published in December 2016.

Data supply
-----------

*The following cases sketch out ways in which open beneficial ownership
data might be published.*

S1: Public Registers of Beneficial Ownership
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A government or other body creating a public register of beneficial
ownership may want to publish that information as open data that others
can draw on and re-use. This may include publishing bulk data, or
providing an API on the data.

The data that the register should contain is likely to be determined by
national legislation, and there may be existing national guidance on how
to develop open data services or APIs.

Organisations building a register may also be interested in using the
standard to help design their internal data models and data collection
processes.

Possible examples of this case may include the UK Register of Persons of
Significant Control, the Ukraine Beneficial Ownership Register, the
planned register of beneficial ownership in France, and sector-specific
registers from the Extractives Industry Transparency Initiative.

S2: Self-submitted data
~~~~~~~~~~~~~~~~~~~~~~~

An individual or an organisation may make use of online tools to
self-report beneficial ownership information.

For example, `Who Controls It <http://alpha.whocontrolsit.com/>`__ was a
proof-of-concept Beneficial Ownership platform (a precursor to
OpenOwnership.org), designed to test some of the UI issues in the
submission of beneficial ownership data, allowing users to declare their
own ownership of a company, or to report on the ownership structure of a
company.

There are many complex cases a comprehensive system should be able to
deal with, including:

-  Recording economics interests, but without control (e.g. 1% of a
   mining company, which may be valuable, but give little shareholder
   power);

-  Mutual funds, that separate control (the fund manager) from the
   economic interest (the entities that put the money in);

-  `Bonds, preference shares and other
   investments <http://www.investopedia.com/terms/p/preference-shares.asp>`__
   that don’t give control, but do give economic interests. Note that
   sometimes they may have *some* control, such as veto rights, e.g.
   over mergers or asset sales;

-  Control via nominees, particularly when a nominee may act for a
   number of different parties in control of the same company;

-  Contractual control limited to a particular set of circumstances.

The designers of systems capturing self-submitted data may want to use
the standard to express the data they have already collected, and to
plan the collection of other data in future.

S3: Third-party submitted data
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Researchers, journalists or corporate information services may use
filings, reports and other materials to build up structured data about
beneficial ownership.

They may wish to share this data for others to re-use, but with suitable
caveats about the sourcing of the data.

S4: Self-published data
~~~~~~~~~~~~~~~~~~~~~~~

Companies may wish to publish structured data about their own beneficial
ownership on their own websites. This data could be manually curated, or
might come from internal information systems. They may be interested in
doing this to avoid having to manually enter the information into
different systems, so would want the data to be able to be read directly
into platforms like OpenOwnership.

The data may be periodically updated at a single URL, or have regular
releases of data published as part of an annual reporting process, each
time at a new URL.

Data use
--------

*The following cases look at different ways in which stakeholders may
wish to make use of beneficial ownership data.*

U1: Procurement & onboarding screening and audit
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a variety of cases related to onboarding, by which we mean the
process of establishing relationships with new partners: typically new
clients or suppliers (but also joint venture partners, licensees,
Mergers & Acquisitions etc). Each of these new relationships exposes the
onboarding entity (e.g. government, bank, multinational corporation,
etc) to risk (e.g. financial risk, reputational risk, FCPA/Bribery Act
risk, sanctions breaches, etc.), and so they need to understand about
the entity being onboarded.

Information of ownership and control is typically collected by
onboarding entities who then assess the validity of information provided
by cross checking with supplementary data available in open sources. In
high value / high risk transactions, third parties are often employed to
support due diligence processes. Onboarding entities are looking for red
flags (e.g. whether the company is connected with Politically Exposed
Persons or has earned negative media), and for confidence that there are
no red flags they are missing (e.g. that a Beneficial Owner is connected
with a company on a sanctions list). Following an assessment of risks,
an informed judgement call typically determines whether new partnerships
or transactions meet the policy requirements of the business.

As part of an onboarding process, beneficial ownership information might
be integrated alongside other ‘Know Your Customer/Client’ information
and systems. In some cases, having access to documentary evidence to
back up each piece of information given from a beneficial ownership
dataset will be important.

Example user story: *A procurement officer at a multilateral development
bank has to approve the application of a new supplier. They need to
ensure that the company is not on sanctions lists, that the ‘beneficial
owners’ are not PEPs, and that they are not on debarment lists.*

U2: General investigations
~~~~~~~~~~~~~~~~~~~~~~~~~~

There are a number of parties that need to investigate specific
companies or individuals (as opposed to doing data-led
investigations/mappings).

These include:

-  **Journalists** - researching stories on a particular company,
   individual or group of companies

-  **NGO anti-corruption investigation** - finding leads, following them

-  **Law enforcement** - looking to establish a clear evidence base, and
   seeking to establish proof of intent

-  **Asset recovery** - recovering money/assets that are due to a
   client, for example Stolen Assets, proceeds of fraud, or assets
   hidden in divorce settlements

In many ways the processes around such investigations are very similar,
and are less dependent on on who is doing the investigation, and more
about the resources that they have. For example some professional
investigative journalists and even NGOs will have access to proprietary
datasets, whereas many law enforcement officers won’t; some lawyers
performing asset recovery will be able to ask the courts to expose
otherwise hidden data (e.g. dollar transactions). Nevertheless, all are
looking for leads they can follow, and in particular public leads (in
the case of journalists, or NGOs this is possibly all they have access
to or can afford; in the case of law enforcement, lying in public proves
intent).

Tax and accounting investigations are similar, but may be more focused
on corporate structures and direct relationships rather than indirect
and ultimate relationships

Example user story: *A journalist is investigating a politician
including looking at known associates and companies, in both the home
country and other jurisdictions.*

U3: Data-led investigations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

As well as targeted and general purpose investigations, where there is a
specific target for the investigation or a lead that is being pursued,
there are also data-led investigations, which work by analysis or mining
the data as a whole, or combining the data with other datasets. Examples
would be mapping beneficial ownership data to procurement data (for
conflict of interest mapping), as well as mapping to similar data such
as shareholder data from company registers.

To give an example user story: *Data journalists wish to find anomalies
between beneficial ownership disclosures and other public records, to
identify lies*

U4: Data validation
~~~~~~~~~~~~~~~~~~~

Systems collecting beneficial ownership data can benefit from checking
the data they receive against data from other systems. In existing work,
there have been cases where reports under the EITI templates have not
matched with reports to the UK Register of Persons with Significant
Control.

To give an example user story: *National EITI groups may wish to check
reported information against data from national beneficial ownership
registers where those exist, and to be able to address inaccuracies with
the reporting parties. *
