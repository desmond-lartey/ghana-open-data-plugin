# Map explorer

The Map explorer shows one indicator at a time across Ghana's **260 districts** or **16 regions**, the way statistical offices present their data: as a coloured map, a sortable table or a ranking.

[Open the Map explorer](https://www.ghanaopendata.com/explorer.html){ .md-button .md-button--primary }

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

## Points of interest on the map

Besides the coloured statistics, the map can show the places themselves: clinics, schools, cafés, shops, hotels, churches and mosques, bus stations and more, from Overture Maps.

- Open **Layers** on the map and tick **Places from Overture**, then choose the groups you want. Choosing a *Places* indicator turns its group on for you.
- Zoomed out, places are merged into rings. Each ring shows how many places it holds, and its colours show the mix of groups. Click a ring to zoom in.
- Once the view is about a degree across (roughly one district), each place appears as a coloured point. Hover over it, or tap it on a phone, for its name and type.
- The filter box under the groups finds places by name or type, for example *school*, *cafe*, *pharmacy* or *hotel*. It applies when you are zoomed in.

Only named places that Overture is reasonably confident about are drawn, so the map shows fewer places than the district counts, which include every open place.

!!! note "Read with care"
    Open map data is uneven: some districts are mapped in more detail than others, and listings of places depend on what partners have collected. A high count can mean more activity, or simply better mapping. The figures are a starting point for analysis, not official statistics.

## Taking the data further

- **Download CSV** saves exactly what you see (needs a free account).
- **Copy link to this view** gives a link that opens the explorer with the same selection.
- **Open in GIS workspace** opens the same map in the workspace: the districts or regions coloured with the explorer's classes, with **every indicator as an attribute**, plus the places you have switched on as point layers. From there you can restyle, query, join, buffer, or count points in polygons, and export the result. The workspace layer holds the latest monthly release.
- The full table, every district and every month, is the dataset *Ghana district statistics from Overture Maps* in the data browser.
