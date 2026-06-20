---
title: Rig Veda API reference documentation
description: Endpoints specs, schemas, and parameters for mandal, sukta, poet, god, meter, and category of the Rig Veda hymns.
summary: Structured metadata for Rig Veda hymns, poets, gods, and metrical traditions.

version: v3
status: stable
base_path: /rv/v3

canonical: https://aninditabasu.github.io/indica/topics/api_rv.html

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

  - title: Visualising Rig Vedic gods
    type: datavis
    url: /topics/datavis_gods_pie.html

  - title: About the Rig Veda API
    type: explanation
    url: /topics/about_rv.html

  - title: Rig Veda API sandbox
    type: openapi
    url: /topics/openapi_rv.html
---

# Rig Veda API reference

<hr/>

This API fetches metadata of the hymns in Rig Veda. The JSON response contains information on poets, gods, and meters.

The following table is a snapshot of the available endpoints and the questions they answer.

| Endpoint  | Question that's answered by the default mode    | Question that's answered by the expanded mode  |
| ---------- | -------------------------------------------- | ---------------------------------------------- |
| `/mandal/{n}`  | How many hymns are there in this mandal?  | -  |
| `/mandal/{n}/meters`  | What meters occur in this mandal, and how many times?  | -  |
| `/mandal/{n}/sungfor`  | Which gods are praised in this mandal, and how many hymns are for each? | -  |
| `/mandal/{n}/sungby`  | Which poets composed hymns in this mandal, and how many hymns did each compose? | -  |
| `/sungfor/{god}/mandals` | In which mandals is this god praised, and how many hymns in each mandal? | Which specific hymns (mandal+sukta) are sung for this god? |
| `/sungfor/{god}/meters`   | What meters are used in hymns for this god, and how often? | Which specific hymns for this god use which meter?  |
| `/sungfor/{god}/sungby`  | Which poets sang for this god, and how many hymns did each compose? | For each poet who sang for this god, what metrical distribution do their hymns have? |
| `/sungby/{poet}/mandals` | In which mandals does this poet appear, and how many hymns in each mandal? | Which specific hymns (mandal+sukta) were composed by this poet? |
| `/sungby/{poet}/meters` | What meters does this poet use, and how often? | Which specific hymns by this poet use which meter, and for whom were they sung? |
| `/sungby/{poet}/sungfor` | Which gods does this poet sing for, and how many hymns for each? | Which specific hymns by this poet are addressed to which god, and in what meter? |
| `/meters`  | What meters exist in the corpus, and how often does each occur?  | -   |
| `/sungforcategories`  | What god-categories exist in the corpus, and how many hymns belong to each? | Which specific hymns belong to each god-category? |
| `/sungbycategories`  | What poet-categories exist in the corpus, and how many hymns belong to each? | Which specific hymns belong to each poet-category? |
| `/hymns`  | Which hymns match the given filters? | -  |
| `/pairs/{god}/{poet}`   | -    | Which hymns represent this sungfor + sungby pair, and in what meter?  |
| `/pairs/{godcategory}/{poetcategory}` | - | Which hymns match this sungforcategory + sungbycategory pair?  |
| `/monologues`  | Which hymns are self-addressed ? | - |
| `/conversations`  | Which hymns contain overlapping speakers and addressees?   | -  |
| `/godlist`  | Who are all distinct gods in the corpus?  | -  |
| `/poetlist`  | Who are all distinct poets in the corpus?  | -  |
| `/meterlist` | What are all distinct meters in the corpus?  | - |
| `/godcategorieslist`  | What are all valid god categories? | -  |
| `/poetcategorieslist`  | What are all valid poet categories?  | -  |

---------

**On this page**

* TOC
{:toc}

---------

## Context

An explanation of the various elements in Rig Veda (and this API) is contained in [About the Rig Veda API](about_rv.md).

## Base URL

`https://indica-1hwj.onrender.com/rv/v3`

The request URL is formed by appending an endpoint to the base URL.

## Methods

Only `GET` calls are supported.

### Example request

For the request parameters, see [Endpoints](#endpoints).

```shell
    curl -X 'GET' \
        'https://indica-1hwj.onrender.com/rv/v3/meters' \
        -H 'accept: application/json'
```

### Example response

For the response parameters, see [Response parameters](#response-parameters).

```json
{
  "meters": {
    "Abhisarini": 2,
    "Anushtup": 281,
...
    "Virangarupa": 8,
    "Virat": 64
  }
}
```

## Status codes

| Code | Explanation |
| ----   | ------------ | 
| 200   | OK               | 
| 404   | Not found   | 
| 429   | Too many requests | 
| 500   | Internal server error |

## Endpoints

To form the request URL, the endpoint must be appended to the base URL.

```bash
request URL = base URL + endpoint
```

Some endpoints need a path parameter. Some other don't, but might need a query parameter.

Some of the endpoints can be expanded for details. If there are more than 27 results, the response is paginated. For such endpoints, the following query parameters are valid: `?expand=true` and `?expand=true&page={n}`.

### `/mandal/{n}`

Returns the number of verses in the specified mandal. For example, `/mandal/4` returns the numer of verses in the 4th book.

```
{
  "hymns": 58,
  "mandal": 4
}
```

`{n}` is an integer parameter. Valid values for this parameter are 1 through 10 (because there are only 10 mandals in Rig Veda).

### `/mandal/{n}/meters`

Returns the counts of all meters in the specified mandal. For example `/mandal/4/meters` returns the counts of all meters found in the 4th book.

```
{
  "mandal": 4,
  "meters": {
    "Anushtup": 15,
    "Ashti": 1,
...
  }
}
```

`{n}` is an integer parameter.  is a string parameter.

### `/mandal/{n}/sungfor`

Returns the count of verses, separately, to all gods in the specified mandal. For example, `/mandal/4/sungfor` returns all gods in the 4th book along with the count of verses sung to them.

```
{
  "mandal": 4,
  "sungfor": {
    "Aditya": 1,
    "Agni": 22,
	...
```

`{n}` is an integer parameter.

### `/mandal/{n}/sungby`

Returns the count of all verses, separately, by all poets in the specified mandal. For example, `/mandal/4/sungby` returns all poets in the 4th book along with the count of verses composed by them.

```
{
  "mandal": 4,
  "sungby": {
    "Aditi": 1,
    "Ajamil Sauhotra": 2,
    "Indra": 1,
    "Purumil Sauhotra": 2,
    "Trasadasyu Paurukutsya": 3,
    "Vamadev Gautam": 107
  }
}
```

`{n}` is an integer parameter. 

### `/sungfor/{god}/mandals`

Returns the count of verses, separately, in all mandals, to the specified god. For example, `/sungfor/agni/mandals` returns the count of all hymns to Agni in all the mandals.

```
...
{
  "mandals": {
    "1": 68,
    "10": 55,
    "2": 13,
...
```
`{god}` is a string parameter.

This endpoint can be queried with `?expand=true` to get the mandals and suktas of these hymns:

```
...
    {
      "mandal": 1,
      "sukta": 22
    },
    {
      "mandal": 1,
      "sukta": 23
    }
  ],
  "sungfor": "agni",
  "total": 304
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/sungfor/{god}/meters`

Returns the count of all meters, separately, used in hymns to the specified god. For example, `/sungfor/agni/meters` returns the count of all meters used in all hymns to Agni.

```
...
{
  "meters": {
    "Anushtup": 48,
    "Ashti": 1,
    "Atidhriti": 1,
...
```
`{god}` is a string parameter.

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 1,
      "meter": "Trishtup",
      "sukta": 79
    },
    {
      "mandal": 1,
      "meter": "Ushnik",
      "sukta": 79
    }
  ],
  "sungfor": "agni",
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/sungfor/{god}/sungby`

Returns the count of all poets, separately, who've composed hymns to the specified god. For example, `/sungfor/agni/sungby` returns the count of all poets who've sung to Agni.

```
...
{
  "sungby": {
    "Agastya Maitravaruni": 3,
    "Agni": 7,
    "Arun Vaitahavya": 2,
...
```
`{god}` is a string parameter.

This endpoint can be queried with `?expand=true` to get further details:

```
...
"results": [
    {
      "meters": {
        "Jagati": 1,
        "Trishtup": 1
      },
      "poet": "Chitramaha Vasishth"
    },
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/sungby/{poet}/mandals`

Returns the count of all mandals, separately, that contain hymns of the specified poet. For example, `/sungby/Medhatithi Kanv/mandals` returns the count of all hymns by Medhatithi Kanv in all mandals separately.

```
...
{
  "mandals": {
    "1": 12,
    "8": 5,
    "9": 3
  },
  "sungby": "Medhatithi Kanv"
}
...
```

`{poet}` is a string parameter.

This endpoint can be queried with `?expand=true` to get further details:

```
...
      "mandal": 1,
      "sukta": 20
    },
    {
      "mandal": 1,
      "sukta": 21
    }
  ],
  "sungby": "Medhatithi Kanv",
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/sungby/{poet}/meters`

Returns the count of all meters, separately, employed by the specified poet. For example, `/sungby/Dirghatamas Auchathya/meters` returns the count of all meters used by Medhatithi Kanv.

```
...
{
  "meters": {
    "Anushtup": 16,
    "Jagati": 19,
...
```

`{poet}` is a string parameter.

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 1,
      "meter": "Anushtup",
      "sukta": 142,
      "sungfor": "Ila"
    },
  ],
  "sungby": "Dirghatamas Auchathya",
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/sungby/{poet}/sungfor`

Returns the count of all gods, separately, that the specified poet has composed hymns for. For example, `/sungby/Medhatithi Kanv/sungfor` returns the count of all gods sung to by Medhatithi Kanv.

```
...
"sungfor": {
    "Aditya": 1,
    "Agnayi": 1,
    "Agni": 9,
    "Apah": 3,
...
```

`{poet}` is a string parameter.

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 1,
      "meter": "Gayatri",
      "sukta": 13,
      "sungfor": "Usha"
    },
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/meters`

Returns the counts of all meters used in all verses of the Rig Veda. This endpoint does not take any path parameters.

```
{
  "meters": {
    "Abhisarini": 2,
    "Anushtup": 281,
    "Ashti": 6,
    "Atidhriti": 1,
...
```

### `/sungforcategories`

Returns the counts of hymns to the categories, separately, of all the gods in the Rig Veda.  This endpoint does not take any path parameters.

```
...
"sungforcategories": {
    "abstract": 36,
    "animal": 35,
    "demon male": 1,
...
```

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 1,
      "sukta": 6,
      "sungforcategory": "divine male"
    },
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/poetcategories`

Returns the counts of hymns by the categories, separately, of all the poets in the Rig Veda.  This endpoint does not take any path parameters.

```
...
 "sungbycategories": {
    "animal": 1,
    "demon male": 1,
...
```

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 10,
      "sukta": 144,
      "sungbycategory": "human male"
    },
    {
      "mandal": 10,
      "sukta": 145,
      "sungbycategory": "divine female"
    },
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/hymns`

Returns the count of all hymns that match the specified query parameters. Requires at least one query parameter and can take up to four from among these: `sungby`, `sungfor`, `mandal`, and `meter`.

For example, `/rv/v3/hymns?sungfor=agni&meter=gayatri` returns all hymns to Agni in the Gayatri meter, like this:

```
{
  "count": 18,
  "hymns": [
    {
      "mandal": 1,
      "sukta": 1
    },
    {
      "mandal": 1,
      "sukta": 12
    },
...
 ],
  "mandal": 1,
  "meter": "gayatri",
  "sungfor": "agni"
}
```

### `/pairs/{god}/{poet}`

Returns all mandal and suktas that contains hymns to the specified god by the specified poet.  For example, `/pairs/agni/Vishwamitra Gathin` returns all hymns (mandals and suktas) to Agni by Dirghatamas Auchathya.

```
...
    {
      "mandal": 3,
      "meter": "Jagati",
      "sukta": 29
    },
    {
      "mandal": 3,
      "meter": "Trishtup",
      "sukta": 57
    }
  ],
  "sungby": "Vishwamitra Gathin",
  "sungfor": "agni",
...
```

`{god}` and `{poet}` are string parameters.

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/pairs/{godcategory}/{poetcategory}`

Returns all mandal and suktas that contains hymns to the specified category of gods by the specified category of poets.  For example, `/pairs/human male/divine female` returns all hymns (mandals and suktas) to human males by divine females.

```
{
  "page": 1,
  "pages": 1,
  "results": [
    {
      "mandal": 3,
      "sukta": 33
    },
    {
      "mandal": 4,
      "sukta": 18
    },
    {
      "mandal": 10,
      "sukta": 95
    }
  ],
  "sungbycategory": "divine female",
  "sungforcategory": "human male",
  "total": 3
}
```

`{godcategory}` and `{poetcategory}` are string parameters.

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/monologues`

Returns all hymns where the poet is singing to their own self. This endpoint does not take any parameters.

```
...
    {
      "mandal": 4,
      "sukta": 42,
      "sungby": "Trasadasyu Paurukutsya",
      "sungbycategory": "human male"
    },
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/conversations`

Returns all hymns where the poets and gods are singing to each other. This endpoint does not take any parameters.

```
...
    {
      "mandal": 3,
      "participants": [
        {
          "participant": "Vishwamitra Gathin",
          "participantcategory": "human male",
          "role": "sungby"
        },
        {
          "participant": "Rivers",
          "participantcategory": "divine female",
          "role": "sungfor"
        },
        {
          "participant": "Rivers",
          "participantcategory": "divine female",
          "role": "sungby"
        },
        {
          "participant": "Vishwamitra Gathin",
          "participantcategory": "human male",
          "role": "sungfor"
        }
      ],
      "sukta": 33
    },
...
```

If the result runs into several pages, use the `?expand=true&page={n}` query parameter.

### `/godlist`

Returns a list of all gods in the Rig Veda. This endpoint does not take any parameters.

### `/poetlist`

Returns a list of all poets in the Rig Veda. This endpoint does not take any parameters.

### `/meterlist`

Returns a list of all meters in the Rig Veda. This endpoint does not take any parameters.

### `/godcategorieslist`

Returns a list of all categories of gods in the Rig Veda. This endpoint does not take any parameters.

### `/poetcategorieslist`

Returns a list of all categories of poets in the Rig Veda. This endpoint does not take any parameters.

## Response parameters

Depending on the endpoint, the response can contain the following parameters:

-  `mandal`: The book number. Rig Veda has 10 books.
-  `sukta`: The chapter number. Books contain chapters. The number of chapters in each book is different. For example, mandal 5 contains 87 suktas while mandal 4 contains 58. The highest value possible for this parameter is 191 (which is the number of suktas in the 1st and 10th mandals). The following table lists the number of chapters in each book.
	
	| Mandal (book) | Sukta (chapter) |
	| --- | --- |
	| 1 | 191 |
	| 2 | 43 |
	| 3 | 62 |
	| 4 | 58 |
	| 5 | 87 | 
	| 6 | 75 |
	| 7 | 104 |
	| 8 | 103 |
	| 9 | 114 |
	| 10 | 191 |

-  `meter`: The poetic meter.
-  `sungby`: The poet.
-  `sungfor`: The god.

## Live sandbox

See [Rig Veda API: Try it out](openapi_rv.md).
