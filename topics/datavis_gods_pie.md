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

This chart is generated from the data returned by the `/rv/v3/mandal/{n}/sungfor` endpoint.

<p style="font-size: 75%;">To see a larger image, click the image.</p>
<a href="../images/gods_pie_chart.png"><img src="../images/gods_pie_chart.png"  alt="pie chart of gods in rig veda" width="75%"></a>

---------

**On this page**

* TOC
{:toc}

---------

## What this chart shows

At first glance, the following things stand out immediately:

-  Indra dominates.
-  Agni is almost as important as Indra.
-  There's a huge `Others` category. So huge, in fact, that the long tail gets exploded into two smaller charts, and still ends up with a large `Others` category.
-  Soma, a drink, is at #3.
-  Vishnu and Rudra rank lower (they appear only in Figure 2a) than the Ashwini twins, who're very visible in Figure 1.
-  The third chart (Figure 2b) is full of things that feel strange as objects of hymns. Subandhu's spirit?!

From this chart, one might be inclined to think rituals (Agni, Soma) matter as much as gods (Indra) and that the central religious theme is situational (objects are gods) rather than god-centered.

## What to explore next

-  Why do some gods dominate?	Fetch all hymns for a specific deity (use the `/sungfor/...` series of endpoints). See whether they cluster in any mandals (use the `mandals/{n}/sungfor` endpoint). See whether those mandals are dominated by any poet family (use the `/sungby/...` series of endpoints, and look for patronymic names).
-  Who are the gods that make up such a long tail, such small slices that each contribute very little to the total on their own but, collectively, are 27% of the corpus where the #1 rankholder is 17%? Minor gods, abstract forces, ancestors, or ritual objects?
-  Why are objects such as doors and grass, gods? Do they have entire suktas to themselves alone, or do they share the honours with others (use the `mandal`-`sukta` combinations in the expanded response to the `/sungfor/...` series of endpoints)?
-  What about pairings? Are some gods always invoked solo or do they always appear along with other specific gods? If they are often paired or grouped, who are these other gods they are invoked along with (use the `mandal`-`sukta` combinations in the expanded response to the `/sungfor/...` series of endpoints)?

## Endpoint to use for this pie chart

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

1.  Aggregate the counts across all collections.
    1.  Initialise an empty map: `total_counts`
    1.  For each collection:
        -  For each `(category, count)` pair:
            -  Add the count to `total_counts[category]`.
1.  Sort the categories by descending frequency, to establish a ranking from the most frequent to the least frequent.
    1.  Convert `total_counts` into a list of `(category, count)` pairs.
    1.  Sort by count in descending order.
1.  Compute the grand total.
1.  Make the first-level grouping (Figure 1):
    1.  Select the primary categories.
    1.  Initialise `main_labels`, `main_values`, `others_labels`, `others_values`.
    1.  For each sorted category, calculate `percentage = count / grand_total × 100`.
    1.  Include in the main chart only if:
        -  It is within the top `N` ranked categories.
        -  Its percentage is greater than or equal to the minimum percentage threshold.
        -  Otherwise move it into the `Others` group.
    1.  Create first remainder bucket:
        1.  Sum all deferred categories: `others_total = sum(others_values)`
        1.  Append `"Others"` (`others_total`) to the main chart.
1.  Make the second-level grouping (Figure 2a):
    1.  Break down the first remainder:
        1.  Take all categories in `Others`.
        1.  Initialise `second_labels`, `second_values`, `others2_labels`, `others2_values`.
        1.  For each category:
            -   If count ≥ second-level threshold, include in the second chart.
            -   Otherwise, move it into `Others2`.
	1.  Create the second remainder bucket:
        1.  Sum the deferred values: `others2_total = sum(others2_values)`
        1.  If non-zero: `append "Others2"`.
1.  Make the third-level grouping (Figure 2b):
    1.  Break down the second remainder:
        1.  Take all categories in `Others2`.
        1.  Initialise `third_labels`, `third_values`, `others3_labels`, `others3_values`.
        1.  For each category:
            -   If count ≥ third-level threshold, include in the third chart.
            -   Otherwise, move it into `Others3`.
	1.  Create the third remainder bucket:
        1.  Sum the deferred values: `others3_total = sum(others3_values)`.
        1.  If non-zero: `append "Others3"`.
1.  Render the charts:
    1.  Create a multi-panel layout containing:
        -  One large left panel for Figure 1.
        -  Two smaller stacked right panels for Figures 2a and 2b.
    1.  From the metadata, render the header (title) and footer.
    1.  Render each pie chart. For each chart:
        1.  Assign colours cyclically.
        1.  Draw pie slices proportionally.
        1.  Apply border styling.
        1.  Add chart title.
    1.  Place the labels. For each slice:
        1.  If the slice is large, place the label inside the slice.
        1.  If the slice is small, place the label outside the slice and connect it with a leader line.
    1.  Generate the legends. For each chart, create a legend showing the category name, raw count, and, for the main chart, percentage.
1.  Draw a border frame around the full visualisation area, flush to the edges.
1.  Export the output. Save the rendered chart as an image file with high resolution.

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

