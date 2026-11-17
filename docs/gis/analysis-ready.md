# Analysis-ready data

What you can analyse depends on what a layer is:

| Layer | What it is | Can you analyse it? |
|---|---|---|
| Boundaries (regions, districts, capitals) | Vector data with attributes | Yes: select, join, buffer, overlay, measure, export |
| Community datasets | The files as shared (CSV, GeoPackage, Shapefile, GeoTIFF…) | Yes, in their own format |
| Earth Engine **values** (GeoTIFF) | A raster of real values clipped to Ghana | Yes: zonal statistics, reclassify, raster calculator |
| NASA satellite maps and Earth Engine **map layers** | Pictures for viewing | For looking and comparing, not for calculating |

## A typical analysis

1. In the Earth Engine connector, draw WorldPop population and press **Open values in GIS workspace** (or download the GeoTIFF).
2. Add the Ghana base map from **Ghana Data**.
3. Use **Analyze › Tools** for zonal statistics by district.
4. Export the result as CSV or GeoPackage, or style it as a map and export a layout.

## Coming next

Ready-made analysis layers (population, health-facility access and flood exposure by district, for example) will be published on the portal as analysis-ready datasets, so they can be viewed, downloaded and opened in the workspace like any other dataset.
