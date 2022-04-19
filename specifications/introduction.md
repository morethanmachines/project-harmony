# Introduction
The Wine Australia project harmony object model and interaction schema is organised around [REST](http://en.wikipedia.org/wiki/Representational_State_Transfer). The artifacts have been designed to align to predictable resource oriented URLs, accept [form-encoded](https://en.wikipedia.org/wiki/POST_(HTTP)#Use_for_submitting_web_forms) request bodies, returns [JSON-encoded](http://www.json.org/) responses and uses standard http response codes.

The object model is designed to provide a reference architecture for the movement of viticultural data between systems.

We have started by specifying the object model and interaction schema for [blocks](https://github.com/morethanmachines/project-harmony/blob/develop/specifications/block/documents/block.md#block-draft) and [rows](https://github.com/morethanmachines/project-harmony/blob/develop/specifications/block/documents/row.md#vine-row-draft).

Where possible the object model will align to international data models and existing standards to ensure alignment with international specifications. Additionally the specification has been designed to support emerging requirements. For example by providing for the inclusion of spatial features (and aligning these to geojson standards).
