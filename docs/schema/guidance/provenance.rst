.. _provenance:

Sources and annotations
=======================

It is important to indicate clearly where data has come from, and any changes to it that have been made since it was originally collected.

Each statement SHOULD contain information on its source, and whether or not the information it contains has been verified. (For example, a statement may be taken from official records, or self declaration, and it may or may not have been checked through some process to verify that the information provided is accurate.)

The ``source`` property of each statement MAY be used to provide provenance information.

The ``annotations`` property of each statement MAY be used to provide additional contextual information at the level of a whole statement, a sub-object, or an individual property. For example an annotation might be used to include structured information detailing the nature of the interest held by a natural person in a company. In some cases, systems processing BODS data may make changes to clean, enhance or otherwise update the data, such as reconciling company names against identifiers. In this case, details of these changes SHOULD be recorded as annotations, to allow users to clearly understand the provenance of information.


