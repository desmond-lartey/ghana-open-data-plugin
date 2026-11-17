# For developers

Everything on the portal has a stable web address. The portal's **Developers** page has the full list of files and copy-and-paste examples.

## Files

```text
https://ghana-open-data.vercel.app/data/reference/gha_admin0.geojson     national border
https://ghana-open-data.vercel.app/data/reference/gha_admin1.geojson     16 regions
https://ghana-open-data.vercel.app/data/reference/gha_admin2.geojson     260 districts
https://ghana-open-data.vercel.app/data/reference/gha_admincapitals.geojson
```

## National indicators

```text
GET https://ghana-open-data.vercel.app/api/series?code=NY.GDP.MKTP.KD.ZG&countries=GHA,NGA
```

Each point is `[year, value]`, with `"imf"` as a third element where the figure comes from the IMF.

=== "Python"

    ```python
    import geopandas as gpd, requests

    districts = gpd.read_file("https://ghana-open-data.vercel.app/data/reference/gha_admin2.geojson")
    series = requests.get("https://ghana-open-data.vercel.app/api/series",
                          params={"code": "SP.POP.TOTL", "countries": "GHA"}).json()
    ```

=== "R"

    ```r
    library(sf); library(jsonlite)
    districts <- st_read("https://ghana-open-data.vercel.app/data/reference/gha_admin2.geojson")
    series <- fromJSON("https://ghana-open-data.vercel.app/api/series?code=SP.POP.TOTL&countries=GHA")
    ```

=== "DuckDB"

    ```sql
    INSTALL spatial; LOAD spatial;
    SELECT adm1_name, count(*) FROM ST_Read('https://ghana-open-data.vercel.app/data/reference/gha_admin2.geojson') GROUP BY 1;
    ```

## Linking to a map

Any page can open the GIS workspace on a given map. The portal's Developers page builds such links; the parameters are `layers`, `eo` (a satellite layer), `bbox`, `date` and `title`.
