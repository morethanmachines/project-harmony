# Introduction
The Wine Australia project harmony object model and interaction schema is organised around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). The artifacts have been designed to align to predictable resource oriented URLs, accept [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns [JSON-encoded](http://www.json.org/) responses and uses standard http response codes.

The object model is designed to provide a reference architecture for the movement of viticultural data between systems.

We have started by specifying the [object model](https://github.com/morethanmachines/project-harmony/blob/91115c89e3743c6d6e42381bba9c6886d723027e/specifications/block/data_model/data_model.png) and interaction schema for [blocks](https://github.com/morethanmachines/project-harmony/blob/develop/specifications/block/documents/block.md#block-draft) and [rows](https://github.com/morethanmachines/project-harmony/blob/develop/specifications/block/documents/row.md#vine-row-draft).

Where possible the object model will align to international data models and existing standards to ensure alignment with international specifications. Additionally the specification has been designed to support emerging requirements. For example by providing for the inclusion of spatial features (and aligning these to [geojson standards](https://geojson.org/)).

The docmentation contained in the schema aligns closely to the conventions in use by the [Internet Engineering Task Force](https://www.ietf.org/).

## Notes on documentation style
### Requirements language
The keywords "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT",
"SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and
"OPTIONAL" in this document are to be interpreted as described in
[RFC2119](https://datatracker.ietf.org/doc/html/rfc2119).

### Conventions used
* The ordering of the members of any JSON object defined in this
document MUST be considered irrelevant, as specified by [RFC7159](https://datatracker.ietf.org/doc/html/rfc7159).

* Some examples use the combination of a JavaScript single-line comment
(//) followed by an ellipsis (...) as placeholder notation for
content deemed irrelevant by the authors.  These placeholders must of
course be deleted or otherwise replaced, before attempting to
validate the corresponding JSON code example.

* Whitespace is used in the examples inside this document to help
illustrate the data structures, but it is not required.  Unquoted
whitespace is not significant in JSON.

### Versioning
* The schema is explicitly versioned. A specification that alters the
semantics of schema objects or otherwise modifies the format does
not create a new version of this format; instead, it defines an
entirely new format that MUST NOT be identified as the Wine Australia Spray Diary schema.

### Security Considerations
* The Wine Australia Spray Diary schema shares security issues common to all JSON content types.  See
[RFC7159, Section 12](https://datatracker.ietf.org/doc/html/rfc7159#section-12) for additional information. 

* The Wine Australia Spray Diary schema does not currently provide privacy or integrity services.  If sensitive data requires privacy or integrity protection, those must be provided by the transport -- for example, Transport Layer Security (TLS) or HTTPS.  There will be cases in which stored data needs protection,
which is out of scope for this document.
