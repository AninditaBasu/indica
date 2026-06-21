---
title: Visualising Rig Vedic meters
description: Plot a pie graph after querying the API for meters in the hymns of the Rig Veda.
summary: Tutorial for creating a pie graph of vedic meters.

version: v3
status: stable
base_path: /rv/v3

canonical: https://aninditabasu.github.io/indica/topics/datavis_meters_pie.html

tags:
  - sruti
  - rig-veda
  - vedic
  - sanskrit
  - history
  - api
  - liturgy

related:
  - title: Visualising Rig Vedic gods
    type: datavis
    url: /topics/datavis_gods_pie.html

  - title: Finding conversations in the Rig Veda
    type: tutorial
    url: /topics/how_to_dialogues.html

  - title: About the Rig Veda API
    type: explanation
    url: /topics/about_rv.html

  - title: Rig Veda API reference documentation
    type: reference
    url: /topics/api_rv.html

  - title: Rig Veda API sandbox
    type: openapi
    url: /topics/openapi_rv.html
---

# Pie chart: Poetic meters

<hr/>

This chart is generated from the data returned by the `/rv/v3/meters` endpoint.

<p style="font-size: 75%;">To see a larger image, click the image.</p>
<a href="../images/meters_pie_chart.png"><img src="../images/meters_pie_chart.png"  alt="pie chart of meters in rig veda" width="50%"></a>

Rig Veda is poetry. Its verses have a certain lilt, beat, rhythm ( _meter_ ) that turn the words into charming lyrical music when recited aloud.

---------

**On this page**

* TOC
{:toc}

---------

## What this chart shows

At first glance, the following things stand out immediately:

-  Trishtup dominates, accounting for over 40% of the corpus. That makes it the default poetic rhythm of the Rig Veda.
-  Jagati and Gayatri together make up another third of the corpus, meaning that just three meters account for most hymns.
-  Anushtup, which later becomes the dominant meter of classical Sanskrit epics, is relatively minor here.
-  The minor meters together account for only about 17% of the corpus.

From this distribution, one might be inclined to think that Rigvedic poetry relied on a few highly stable rhythmic templates that were used more for structure than for ornamentation or experimentation.

## What to explore next

-  Why does Trishtup dominate? Is it associated with specific gods, poets, or mandals? Use the `/mandal/{n}/meters`, `/sungfor/{god}/meters`, and `/sungby/{poet}/meters` endpoints.
-  Do certain gods prefer certain meters? Use the `/sungfor/{god}/meters` endpoint.
-  Do certain poets prefer certain meters? Use the `/sungby/{poet}/meters` endpoint.
-  Do meters cluster by mandal? Use the `/mandal/{n}/meters` endpoint.
-  Which mandals contain Anushtup, the meter that has only a 9% share here but went on to dominate almost the entire epic literature? Use the `/mandal/{n}/meters` endpoint.

## Endpoint to use for this pie chart

`/meters` returns the following response:

```
{
  "meters": {
    "Abhisarini": 2,
    "Anushtup": 281,
    "Ashti": 6,
    "Atidhriti": 1,
    "Atyashti": 28,
    "Brihati": 91,
    "Dhriti": 4,
    "Gayatri": 469,
    "Jagati": 540,
    "Kakumanyamkushira": 1,
    "Kakup": 9,
    "Kriti": 1,
    "Nyangkusarini": 2,
    "Pankti": 108,
    "Pipilika Madhya": 1,
    "Pragath": 81,
    "Pratishtha": 1,
    "Purastajjyoti": 1,
    "Shakchari": 16,
    "Trishtup": 1230,
    "Uparishtajjyoti": 2,
    "Ushnik": 76,
    "Vardhamana": 2,
    "Virangarupa": 8,
    "Virat": 64
  }
}
```

## Algorithm

### Prerequisites

-  Dataset: A mapping of category to count
-  Threshold: Minimum count for a category to be displayed as a slice
-  Colour palette: List of display colours
-  Chart metadata:
    -  Header text
    -  Footer text
    -  Background and frame styling

### Steps

1.  Extract categories and values.
    1.  Read the input dataset.
    1.  Separate it into:
         -  `labels` = list of category names.
         -  `values` = list of corresponding counts.
1.  Group low-frequency categories so that the chart is not cluttered by numerous tiny slices.
    1.  Initialise:
         -  `filtered_labels` as empty.
         -  `filtered_values` as empty.
         -  `other_total = 0`.
    1.  For each `(label, value)` pair:
         -  If `value < threshold`, add `value` to `other_total`.
         -  Else:
             -  Append `label` to `filtered_labels`.
             -  Append `value` to `filtered_values`.
    1.  After processing all items:
         -  If `other_total > 0`:
             -  Append `"Others"` to `filtered_labels`.
             -  Append `other_total` to `filtered_values`.
1.  Assign colours.
    1.  Generate one colour for each resulting category.
    1.  If the number of categories exceeds the palette size, reuse colours cyclically.
    1.  If an `"Others"` category exists, override its colour with a neutral colour like grey.
1.  Create the chart canvas.
    1.  Initialise a drawing surface with fixed dimensions and background colour.
    1.  Reserve space for header, main chart area, and footer.
1.  Add the metadata. Place the header at the top and the footer at the bottom.
1.  Render the pie chart.
    1.  Draw a pie chart where each slice corresponds to a category and the slice size is proportional to the category count.
    1.  Display the category labels outside or near the slices, and the percentage labels inside the slices.
    1.  Apply visual styling for start rotation angle, slice borders, label distances, and percentage text distances.
    1.  Ensure that the chart uses an equal aspect ratio so that the pie remains circular.
    1.  Draw a border frame around the full visualisation area, flush to the edges.
1.  Export the output. Save the rendered chart as an image file with high resolution and a tight bounding box.
 
## Pseudocode

```
function generatePieChart(data, threshold):

    filtered = []
    other_total = 0

    for each (category, count) in data:
        if count < threshold:
            other_total += count
        else:
            filtered.append(category, count)

    if other_total > 0:
        filtered.append("Others", other_total)

    assign colors to filtered categories
    if "Others" exists:
        set its color to neutral

    create canvas
    add title
    add footer

    draw pie chart using filtered counts
    display labels
    display percentages

    enforce circular aspect ratio
    draw outer frame

    save image
```
