# Map explorer

The Map explorer shows one indicator at a time across Ghana's **260 districts** or **16 regions**, the way statistical offices present their data: as a coloured map, a sortable table or a ranking.

[Open the Map explorer](https://ghana-open-data.vercel.app/explorer.html){ .md-button .md-button--primary }

## Choosing what to see

| Control | What it does |
|---|---|
| **Indicator** | What to map, grouped by theme: land and boundaries, elections, settlements, roads, places and land cover |
| **Measure** | A total, a density (per km²) or, for land cover, the share of the district's area |
| **Level** | Districts or regions |
| **Area** | Zoom into one region and compare only its districts |
| **Release** | For indicators refreshed every month, the month to show |

Hover over a district to see its value; select it for its rank, a trend across releases, a link to its region profile and a button to open it in the GIS workspace.

## The indicators

| Theme | Indicators | Source |
|---|---|---|
| Land and boundaries | Area | OCHA Common Operational Dataset (2021) |
| Elections, 2024 | Constituencies, polling stations | Electoral Commission of Ghana |
| Settlements | Buildings | Overture Maps (OpenStreetMap, Google, Microsoft and others) |
| Roads | Road length, by class | Overture Maps (OpenStreetMap and others) |
| Places | Points of interest: health care, education, shopping, food, lodging and more | Overture Maps (Meta, Microsoft, Foursquare and others) |
| Land cover | Forest, cropland, grassland, built-up and more, as a share of area | Overture Maps, from ESA WorldCover satellite data |

The Overture figures are refreshed every month and earlier months are kept, so you can follow change over time. Each building, road or place is counted in the district that holds the centre of its outline.

!!! note "Read with care"
    Open map data is uneven: some districts are mapped in more detail than others, and listings of places depend on what partners have collected. A high count can mean more activity, or simply better mapping. The figures are a starting point for analysis, not official statistics.

## Taking the data further

- **Download CSV** saves exactly what you see (needs a free account).
- **Copy link to this view** gives a link that opens the explorer with the same selection.
- **Open in GIS workspace** takes the district into the workspace for deeper analysis.
- The full table, every district and every month, is the dataset *Ghana district statistics from Overture Maps* in the data browser.
