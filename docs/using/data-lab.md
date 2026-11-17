# Data Lab (SQL)

The Data Lab runs SQL in your browser with DuckDB: nothing to install, and your queries never leave your computer. It needs a free account.

## Tables

| Table | What it holds |
|---|---|
| `region` | The 16 regions: p-code, name, capital, number of districts, area, centre |
| `district` | The 260 districts: p-code, name, region, capital, area, centre |
| `indicator` | National indicator values: code, country, year, value |
| `indicator_meta` | What each indicator code means, and its unit |
| `dataset` | The portal's catalogue |

## Examples

```sql
-- The ten largest districts
SELECT name, region, round(area_km2) AS km2
FROM district
ORDER BY area_km2 DESC
LIMIT 10;
```

```sql
-- Ghana's inflation, newest first
SELECT year, round(value, 1) AS inflation
FROM indicator
WHERE code = 'FP.CPI.TOTL.ZG' AND country = 'GHA'
ORDER BY year DESC;
```

Results show as a sortable table or a chart, download as CSV, and a query can be shared as a link.
