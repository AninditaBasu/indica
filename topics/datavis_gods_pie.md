---
title: Visualising Rig Vedic gods
description: Plot a pie graph after querying the API for all gods in the Rig Veda.
summary: Tutorial for creating a pie graph of vedic gods.

version: v3
status: stable
base_path: /rv/v3

canonical: https://aninditabasu.github.io/indica/topics/datavis_gods_pie.html

tags:
  - sruti
  - rig-veda
  - vedic
  - sanskrit
  - history
  - api
  - liturgy

related:
  - title: Visualising Rig Vedic meters
    type: datavis
    url: /topics/datavis_meters_pie.html

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

# Pie chart: Gods

<hr/>

This tutorial shows you how to draw a piechart of gods in Rig Veda.

<p style="font-size: 75%;">To see a larger image, click the image.</p>
<a href="../images/gods_pie_chart.png"><img src="../images/gods_pie_chart.png"  alt="pie chart of gods in rig veda" width="75%"></a>

---------

**On this page**

* TOC
{:toc}

---------

## Endpoint to use

Fetch, and save, the results for all mandals one by one by using `/mandal/{n}/sungfor`.

```
{
  "mandal": 3,
  "sungfor": {
    "Aditi": 1,
    "Aditya": 4,
    "Agni": 43,
...
}
```

## Algorithm

Aggregates category counts across multiple source collections, ranks them by frequency, and progressively decomposes low-frequency categories into successive levels of detail by using a cascade of pie charts. A 3-level hierarchical visualisation is created.

1. Primary chart: Top categories + aggregated remainder
2. Secondary chart: Breakdown of the remainder above a second threshold
3. Tertiary chart: Further breakdown of the secondary remainder above a third threshold

### Prerequisites

-  Collections: A list of grouped datasets, where each set contains category to count mappings.
-  Top `N`: Maximum number of categories shown in the first chart
-  Minimum percentage: Minimum share required for inclusion in the first chart
-  Second-level minimum count: Threshold for inclusion in the second chart
-  Third-level minimum count: Threshold for inclusion in the third chart
-  Colour palette: List of display colours
-  Chart metadata:
    -  Header text
    -  Footer text
    -  Background and frame styling

### Procedure

1.  Aggregate counts across all collections (`total_counts[category] = sum of all occurrences across all collections`).
    1.  Initialise an empty map: `total_counts`
    1.  For each collection:
      -  For each `(category, count)` pair:
          -  Add the count to `total_counts[category]`.
2.  Sort categories by descending frequency, to establishe ranking from most frequent to least frequent.
    1.  Convert `total_counts` into a list of `(category, count)` pairs.
    1.  Sort by count in descending order.
3.  Compute the grand total.
4.  Draw the first-level grouping (Figure 1):
    1.  Select the primary categories.
    1.  Initialise `main_labels`, `main_values`, `others_labels`, `others_values`.
    1.  For each sorted category, calculate `percentage = count / grand_total × 100`.
    1.  Include in the main chart only if:
      -  It is within the top `N` ranked categories.
      -  Its percentage is greater than or equal to the minimum percentage threshold.
	 Otherwise move it into the `Others` group.
    1.  Create first remainder bucket:
      1.  Sum all deferred categories: `others_total = sum(others_values)`
	  1.  Append `"Others"` (`others_total`) to the main chart.
5.  Draw the second-level grouping (Figure 2a):
    1.  Break down the first remainder:
      1.  Take all categories inside `Others`.
	  1.  Initialise `second_labels`, `second_values`, `others2_labels`, `others2_values`.
	  1.  For each category:
          -  If count ≥ second-level threshold, include in second chart.
          -  Otherwise, defer into `Others2`.
	1.  Create the second remainder bucket:
        1. Sum deferred values: `others2_total = sum(others2_values)`
        1. If non-zero: `append "Others2"`.
6. Draw the third-level grouping (Figure 2b):
    1.  Break down the second remainder:
      1.  Take all categories inside `Others2`.
      1.  Initialise `third_labels`, `third_values`, `others3_labels`, `others3_values`.
	  1.  For each category:
          -  If count ≥ third-level threshold, include in third chart.
          -  Otherwise, defer into `Others3`.
	1.  Create the third remainder bucket:
        1. Sum deferred values: Sum the deferred values: `others3_total = sum(others3_values)`
        1. If non-zero: `append "Others3"`
7. Render the charts:
    1.  Create multi-panel layout, with a canvas containing:
      -  One large left panel for Figure 1.
      -  Two smaller stacked right panels for Figures 2a and 2b.
    1.  From the metadata, render the header (title) and footer.
    1.  Render each pie chart. For each chart:
        1. Assign colours cyclically.
        1. Draw pie slices proportionally.
        1. Apply border styling.
        1. Add chart title.
    1.  Place labels adaptively. For each slice:
        1. If the slice is large, place the label inside the slice.
        1. If the slice is small, place the label outside the slice and connect it with a leader line.
    1.  Generate the legends. For each chart, create a legend showing the category name, raw count, and percentage (for the main chart).
8.  Draw a border frame around the full visualisation area, flush to the edges.
9.  Export the output. Save the rendered chart as an image file with high resolution and a tight bounding box.

## Pseudocode

```
function generateHierarchicalPieCharts(collections):

    total_counts = empty map

    # Aggregate all counts
    for each collection in collections:
        for each (category, count) in collection:
            total_counts[category] += count

    # Sort descending
    sorted_counts = sort total_counts by count descending

    grand_total = sum(all counts)

    --------------------------------------------------
    # LEVEL 1
    --------------------------------------------------

    main = []
    others = []

    for each ranked (category, count):
        percentage = count / grand_total * 100

        if rank < TOP_N and percentage >= MIN_PERCENT:
            main.append(category, count)
        else:
            others.append(category, count)

    main.append("Others", sum(others))

    --------------------------------------------------
    # LEVEL 2
    --------------------------------------------------

    second = []
    others2 = []

    for each (category, count) in others:
        if count >= SECOND_LEVEL_MIN_COUNT:
            second.append(category, count)
        else:
            others2.append(category, count)

    if others2 is not empty:
        second.append("Others2", sum(others2))

    --------------------------------------------------
    # LEVEL 3
    --------------------------------------------------

    third = []
    others3 = []

    for each (category, count) in others2:
        if count >= THIRD_LEVEL_MIN_COUNT:
            third.append(category, count)
        else:
            others3.append(category, count)

    if others3 is not empty:
        third.append("Others3", sum(others3))

    --------------------------------------------------
    # VISUALISATION
    --------------------------------------------------

    create canvas with 3-panel layout

    add global title
    add footer

    render pie chart for main
    render pie chart for second
    render pie chart for third

    for each chart:
        assign colours
        place labels
        add legends

    draw outer frame

    save image
```

An example code in Python is given in [pie chart of gods](https://github.com/AninditaBasu/indica/blob/master/examples/pie_3step_cascade.py). 

## What to do next

Draw similar charts for poets.

<p style="font-size: 75%;">To see a larger image, click the image.</p>
<a href="../images/rishis.png"><img src="../images/rishis.png"  alt="bubble chart of rishis in the rig veda" width="50%"></a>

