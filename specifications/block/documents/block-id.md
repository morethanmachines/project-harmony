# Block identifier
The following block identifier is to be used for the identification of blocks within a Vinyard.

    89636749924-abouriou-47-northblock-12
    ----------- -------- -- ---------- --
      |           |       |         |   |
      |           |       |         |   Row number in the block 
      |           |       |         |
      |           |       |        Block name
      |           |      GI_NUMBER
      |         Variety
      ABN
      
 The block identifier is comprised of 5 sections.
 
 1. The ***ABN*** of the vineyard where the block is located (as provided by ATO/visible on wine company contract).
 2. The ***Variety*** code for the variety as provided by Wine Australia - lowercase, spaces removed
 3. The ***Geographic Indicator Region*** GI_NUMBER (i.e 47) of the block as provided by Wine Australia [Website Link](https://www.wineaustralia.com/labelling/register-of-protected-gis-and-other-terms/geographical-indications) - [Open Data Hub](https://wineaustralia-opendata-wineaustralia.hub.arcgis.com/maps/ede7ffb0e73b4504a5ed613965b11e0f/about).
 4. The ***Block Name*** of the block as provided by the grower - lower case, spaces removed.
 5. The row number in the block

The GI regions can be found as a geojson representation as part of the [collabraculture](https://www.wineaustralia.com/research/projects/collabriculture-an-open-and-collaborative-approach-to-technology-in-the-wine-industry) project [here](https://github.com/CollabricultureOrg/geographical-indications-of-australia/blob/master/data/geojson/Wine_GI_Regions_2021.geojson)
