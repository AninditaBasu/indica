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
  - title: Finding conversations in the Rig Veda
    type: tutorial
    url: /topics/how_to_dialogues.html

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

Poetry is always meant to rendered aloud and, during its recitation, it's the _meter_ that sets its rhythm. Consider the following example, and read it out aloud. 

```text
    In the midst of the word he was trying to say,
    In the midst of his laughter and glee,
    He had softly and suddenly vanished away
    For the Snark was a Boojum, you see.

    - Carrol, Lewis. "The Hunting of the Snark".
```

Your vocals will, in all probability, follow the pattern shown with the stress points marked with `/`.

```text
    In the midst / of the word / he was try/ing to say,
    In the midst/ of his laugh/ter and glee,
    He had soft/ly and sud/den ly van/ ish ed away
    For the Snark / was a Boo/jum, you see.

    - Carrol, Lewis. "The Hunting of the Snark".
```

Rig Veda is poetry. Its verses have a certain lilt, beat, rhythm, and meter that turn the words into charming lyrical music when recited aloud. Stressing the incorrect syllable can alter the entire meaning of a mantra. Traditional methods, transmitted orally, teach people which parts of a word must be stressed. In these modern times, printed books also carry this information.  See, for example, this verse, with and without marks on the stress points.

No marks:

```text
    तत्सवितुर्वरेण्यं भर्गो देवस्य धीमहि ।
    धियो यो नः प्रचोदयात् ॥

    - Rig Veda, 3.62.10
```

Marked with `'` to show how the rhythm should flow:

```text
    तत्स॑वि॒तुर्वरे॑ण्यं॒ भर्गो॑ दे॒वस्य॑ धीमहि ।
    धियो॒ यो नः॑ प्रचो॒दया॑त् ॥

    - Rig Veda, 3.62.10
```

This tutorial shows you how to draw a piechart of the vedic meters.

<p style="font-size: 75%;">To see a larger image, click the image.</p>
<a href="../images/meters_pie_chart.png"><img src="../images/meters_pie_chart.png"  alt="pie chart of meter in rig veda" width="75%"></a>

---------

**On this page**

* TOC
{:toc}

---------

## Endpoint to use

```
/meters
```

## API response

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

## Code to plot the pie chart

```python
import json
import matplotlib.pyplot as plt

# API response
data = {
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

# Extract labels and sizes
labels = list(data["meters"].keys())
sizes = list(data["meters"].values())

# Optional: group tiny slices into "Others" for readability
threshold = 30
filtered_labels = []
filtered_sizes = []
other_sum = 0

for label, size in zip(labels, sizes):
    if size < threshold:
        other_sum += size
    else:
        filtered_labels.append(label)
        filtered_sizes.append(size)

if other_sum > 0:
    filtered_labels.append("Others")
    filtered_sizes.append(other_sum)

# Create figure
plt.figure(figsize=(12, 12))

# Plot pie chart
plt.pie(
    filtered_sizes,
    labels=filtered_labels,
    autopct='%1.1f%%',
    startangle=140
)

plt.title("Meters in the Rig Veda")
plt.axis('equal')  # Keeps the pie a perfect circle

# Save image
plt.savefig("meters_pie_chart.png", dpi=300, bbox_inches="tight")

# Show plot
plt.show()

```

The image that is generated by this example code is a bit different from the image at the top of this page, the complete code for which is given in [pie chart of meters](https://github.com/AninditaBasu/indica/blob/master/scripts/pie_plain.py). 

