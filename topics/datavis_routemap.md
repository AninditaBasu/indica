---
title: Route map of the Jarasandh episode in the Mahabharat
description: Plot a route map after querying the API for details about places in the journey that Krishna, Bheem, and Arjuna undertook to kill Jarasandh, the king of Magadh in the Mahabharat.
summary: Tutorial for building a datavis of the journey undertaken to kill Jarasandh.

version: v1
status: stable
base_path: /mb/v1

canonical: https://aninditabasu.github.io/indica/topics/datavis_routemap.html

tags:
  - itihasa
  - sanskrit
  - history
  - epic
  - ancient-india
  - api

related:
  - title: Visualising the weapons in Mahabharat and the Harry Potter world
    type: tutorial
    url: /topics/datavis_sankey_mbhp.html

  - title: Visualising the Mahabharat timeline
    type: datavis
    url: /topics/datavis_timeline.html

  - title: About the Mahabharat API
    type: explanation
    url: /topics/about_mb.html

  - title: Mahabharat API reference documentation
    type: reference
    url: /topics/api_mb.html

  - title: Mahabharat API sandbox
    type: openapi
    url: /topics/openapi_mb.html
---

# Route map: Jarasandh killing

<hr/>

This route map is generated from data returned by `/mb/v1/journeys/{name}` endpoint, with full details (`?expand=true`) where `{name}` = `Jarasandh killing`.

<p style="font-size: 75%;">To see a larger image, click the image.</p>
<a href="../images/map_jarasandh_killing.png"><img src="../images/map_jarasandh_killing.png"  alt="Route map for Jarasandh killing" width="50%"></a>

---------

**On this page**

* TOC
{:toc}

---------

## What this map shows

At first glance, what stands out immediately is the circular route:

-  The onward journey is through a northern, lesser travelled route bordering on the Himalayan terai region.
-  The return journey is through a straight route on the Gangetic plains.

From this map, it is evident that the travellers went out of their way to conceal their travel till they reached their destination (Magadh).

## What to explore next

-  What events preceded and followed this killing? Use the `/events` series of endpoints.
-  What other journeys did the travellers on this route go on? Use the `/journeys/{name}` endpoint.
-  What were the places along this route like? Do they exist today, and if they do, what are their names today? Use the `/places/{name}` endpoint. 
-  Were the places along this route frequent pitstops for other journeys too? Use the `/journeys?place={place}` endpoint.

## Endpoint to use for this map

`/mb/v1/journeys/Jarasandh killing` returns the following response:

```json
{
  "journeyEvent": "Rajasuya yagya",
  "journeyName": "Jarasandh killing",
  "journeyPersons": [
    "Arjun",
    "Bheem",
    "Krishna"
  ],
  "journeyRoute": [
    "Indraprastha",
    "Kurujangal to Kalakuta",
    "Kalakuta to the east to Mithila",
    "Mithila to Magadh",
    "Girivraj",
    "Girivraj to Indraprastha"
  ]
}
``` 

It's the `journeyRoute` list that is of interest here. To get detailed route information, use the `?expand=true` query parameter.

```json
...
  "journeyRoute": [
    "Indraprastha",
    "Kurujangal to Kalakuta",
    "Kalakuta to the east to Mithila",
    "Mithila to Magadh",
    "Girivraj",
    "Girivraj to Indraprastha"
  ],
  "journeyRouteFull": [null, {
      "pathCurrent": [
        "Hapur (India)",
        "Garhmukteshwar (India)",
        "Gajraula (India)",
        "Dhampur (India)",
        "Kalagarh (India)"
      ],
      "pathNameEpic": "Kurujangal to Kalakuta"
    },
    {
      "pathCurrent": [
        "Kalagarh (India)",
        "Kashipur (India)",
        "Pantnagar (India)",
        "Pilibhit (India)",
        "Lakhimpur Kheri (India)",
        "Bahraich (India)",
        "Shravasti (India)",
        "Kapilvastu (Nepal)",
        "Kudiya (Nepal)",
        "Bagaha (Nepal)",
        "Birganj (Nepal)",
        "Mithila (Nepal)"
      ],
      "pathNameEpic": "Kalakuta to the east to Mithila"
    },
    {
      "pathCurrent": [
        "Mithila (Nepal)",
        "Janakpur (Nepal)",
        "Madhubani (India)",
        "Darbhanga (India)",
        "Samastipur (India)",
        "Patna (India)",
        "Rajgir (India)"
      ],
      "pathNameEpic": "Mithila to Magadh"
    },
    null, {
      "pathCurrent": [
        "Rajgir (India)",
        "Varanasi (India)",
        "Kaushambi (India)",
        "Mathura (India)",
        "New Delhi (India)"
      ],
      "pathNameEpic": "Girivraj to Indraprastha"
    }
  ]
...
```

## Cartographic libraries

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

## Algorithm

1.  Geocode the place names (`GeoPy`).
1.  Create point geometries from the coordinates (`Shapely`).
1.  Store the geometries in a geospatial data frame (`GeoPandas`).
1.  Create the figure and axes (`Matplotlib`).
1.  Add the terrain basemap tiles (`Contextily`).
1.  Plot the locations and export the image (`GeoPandas` + `Matplotlib`).

