---
title: Route map: Jarasandh killing
---

# Route map: Jarasandh killing

<hr/>

This route map is generated from data returned by `/mb/v1/journeys/{name}` endpoint, with full details (`?expand=true`) where `{name}` = `Jarasandh killing`.

![Route map for Jarasandh killing](../images/map_jarasandh_killing.png)

The summary journey route is this:

```json
"journeyRoute": [
    "Indraprastha",
    "Kurujangal to Kalakuta",
    "Kalakuta to the east to Mithila",
    "Mithila to Magadh",
    "Girivraj",
    "Girivraj to Indraprastha"
  ]
```

The detailed route information was obtained by using the `?expand=true` query parameter.

The following components were used to generate the map:

- Country boundary dataset from [Natural Earth](https://www.naturalearthdata.com/),  used for determining the geographic extent of India and surrounding regions
- Geocoding by using [Nominatim](https://nominatim.org/)
- Terrain and physical basemap tiles from [Esri](https://www.esri.com/en-us/home) (World Physical Map layer)
- Python libraries:
    - `GeoPy`, for converting place names to geographic coordinates
    - `Shapely`, for creating point geometries for the locations
    - `GeoPandas`, for handling geospatial data structures and plotting the points
    - `Matplotlib`, for creating the figure and exporting the `.png` image
    - `Contextily`, for adding the terrain basemap tiles

The workflow is as follows:

1. Geocode the place names (`GeoPy`)
1. Create point geometries from the coordinates (`Shapely`)
1. Store the geometries in a geospatial data frame (`GeoPandas`)
1. Create the figure and axes (`Matplotlib`)
1. Add the terrain basemap tiles (`Contextily`)
1. Plot the locations and export the image (`GeoPandas` + `Matplotlib`)

