# Block identifier
The following block identifier is to be used for the identification of blocks within a Vinyard.

    89636749924-abouriou-47-northblock-12-40
    ----------- -------- -- ---------- -- --
      |           |       |         |   |  |
      |           |       |         |   |  Number of rows in block
      |           |       |         |   |
      |           |       |         |   Starting row number of the block 
      |           |       |         |
      |           |       |        Block name
      |           |      GI_NUMBER
      |         Variety
      ABN
      
 The block identifier is comprised of 5 sections.
 
 | ID | Name | Type | Description | Links |
 | -- | ---- | ---- | ----------- | ----- |
 | 1  | ABN | `Text` | The ***ABN*** of the vineyard where the block is located (as provided by ATO/visible on wine company contract) | [ABN Format and verification](https://abr.business.gov.au/Help/AbnFormat) |
 | 2  | GrapeVine Variety Code | `Text` | The ***Variety*** code for the variety as provided by Wine Australia - lowercase, spaces removed | xx |
 | 3  | Geographic Indicator Region Number | `Integer` | The ***Geographic Indicator Region*** GI_NUMBER (i.e 47) of the block as provided by Wine Australia [Website Link] | [Open Data Hub](https://wineaustralia-opendata-wineaustralia.hub.arcgis.com/maps/ede7ffb0e73b4504a5ed613965b11e0f/about). The data is made available in GeoJSON format and can be accessed through a API call to the ARCGIS data service. [Full Growing Regions Geo JSON](https://services6.arcgis.com/s8j6JbJJCqmhNgh7/arcgis/rest/services/Wine_Geographical_Indications_Australia_2022v1/FeatureServer/1/query?where=1%3D1&outFields=*&outSR=4326&f=json) [API Explorer](https://wineaustralia-opendata-wineaustralia.hub.arcgis.com/datasets/ede7ffb0e73b4504a5ed613965b11e0f/api?layer=1) |
 | 4  | Block Name | `Text` | The ***Block Name*** of the block as provided by the grower - lower case, spaces replaced with underscores. | xx |
 | 5  | Starting row number | `Integer` | The ***starting row number*** of the block -Integer - Numbering starts from 0  | xx |
 | 6  | Number of rows | `Integer` | The ***number of rows*** in the block | xx |
