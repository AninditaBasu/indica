---
title: Rig Veda API reference documentation
description: Endpoints specs, schemas, and parameters for mandal, sukta, poet, deity, meter, and category of the Rig Veda hymns.
summary: Structured metadata for Rig Veda hymns, poets, deities, and metrical traditions.

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

  - title: Finding conversations in the Rig Veda
    type: tutorial
    url: /topics/how_to_dialogues.html

  - title: About the Rig Veda API
    type: explanation
    url: /topics/about_rv.html

  - title: Rig Veda API sandbox
    type: openapi
    url: /topics/openapi_rv.html
---

---

# Rig Veda API reference

<hr/>

This API fetches metadata of the hymns in Rig Veda. The JSON response contains verse-by-verse information on poets, gods, their categories, and the poetic meters.

```json
[
  {
    "mandal": 1,
    "meter": "Gayatri",
    "sukta": 1,
    "sungby": "Madhuchchhanda Vaishwamitra",
    "sungbycategory": "human male",
    "sungfor": "Agni",
    "sungforcategory": "divine male"
  }
]
```

---------

**On this page**

* TOC
{:toc}

---------

## Context

An explanation of the various elements in Rig Veda (and this API) is contained in [About the Rig Veda API](about_rv.md).

## Base URL

`https://indica-1hwj.onrender.com/rv/v2/meta`

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

## Status codes

| Code | Explanation |
| ----   | ------------ | 
| 200   | OK               | 
| 404   | Not found   | 
| 429   | Too many requests | 
| 500   | Internal server error |

## Endpoints

All parameters are path parameters. To form the request URL, the endpoint must be appended to the base URL.

```bash
request URL = base URL + endpoint
```

Some of the endpoints can be expanded for details; such endpoints are usually paginated. For these endpoints, the following query parameters are valid: `?expand=true` and `?expand=true&page=N`.

The following endpoints are available. 

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
      "mandal": 1,
      "sukta": 1,
      "sungby": "Madhuchchhanda Vaishwamitra"
    },
    {
      "mandal": 1,
      "sukta": 12,
      "sungby": "Medhatithi Kanv"
    },
...
```

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

### `/sungby/{poet}/meters`

Returns the count of all meters, separately, employed by the specified poet. For example, `/sungby/Medhatithi Kanv/meters` returns the count of all meters used by Medhatithi Kanv.

```
...
{
  "meters": {
    "Anushtup": 6,
    "Brihati": 3,
...
```

`{poet}` is a string parameter.

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 1,
      "meter": "Gayatri",
      "sukta": 13
    }
  ],
  "sungby": "Medhatithi Kanv",
...
```

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
      "sukta": 13,
      "sungfor": "Tanunapat"
    },
    {
      "mandal": 1,
      "sukta": 13,
      "sungfor": "Grass"
    },
    {
      "mandal": 1,
      "sukta": 13,
      "sungfor": "Ila"
    },
...
```

### `/meters`

Returns the counts of all meters used in all verses of the Rig Veda.

```
{
  "meters": {
    "Abhisarini": 2,
    "Anushtup": 281,
    "Ashti": 6,
    "Atidhriti": 1,
...
```

This endpoint can be queried with `?expand=true` to get further details:

```
...
    {
      "mandal": 8,
      "meter": "Kakup",
      "sukta": 46
    },
    {
      "mandal": 8,
      "meter": "Brihati",
      "sukta": 46
    },
    {
      "mandal": 8,
      "meter": "Anushtup",
      "sukta": 46
    },
...
```

### `/sungforcategories`

Returns the counts of hymns to the categories, separately, of all the gods in the Rig Veda. 

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

### `/poetcategories`

Returns the counts of hymns by the categories, separately, of all the poets in the Rig Veda. 

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

### `/pairs/{god}/{poet}`

Returns all mandal and suktas that contains hymns to the specified god by the specified poet.  For example, `/pairs/agni/Dirghatamas Auchathya` returns all hymns (mandals and suktas) to Agni by Dirghatamas Auchathya.

```
...
    {
      "mandal": 1,
      "sukta": 148
    },
    {
      "mandal": 1,
      "sukta": 149
    }
  ],
  "sungby": "Dirghatamas Auchathya",
  "sungfor": "agni",
...
```

`{god}` and `{poet}` are string parameters.

If the results contain more than one page, this endpoint can be queried with `?expand=true&page=N` to get a specific page:

```
{
  "page": 2,
  "pages": 2,
  "results": [
    {
      "mandal": 1,
      "sukta": 150
    }
  ],
  "sungby": "Dirghatamas Auchathya",
  "sungfor": "agni",
  "total": 11
}
```

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

If the results contain more than one page, this endpoint can be queried with `?expand=true&page=N` to get a specific page.

### `/monologues`

Returns all hymns where the poet is singing to their own self.

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

If the results contain more than one page, this endpoint can be queried with `?expand=true&page=N` to get a specific page.

### `//conversations`

Returns all hymns where the poets and gods are singing to each other.

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

If the results contain more than one page, this endpoint can be queried with `?expand=true&page=N` to get a specific page.

### `/godlist`

Returns a list of all gods in the Rig Veda.

### `/poetlist`

Returns a list of all poets in the Rig Veda.

### `/meterlist`

Returns a list of all meters in the Rig Veda.

### `/godcategorieslist`

Returns a list of all categories of gods in the Rig Veda.

### `/poetcategorieslist`

Returns a list of all categories of poets in the Rig Veda.

## Response parameters

The following response parameters are common to almost all endpoints.

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
-  `sungbycategory`: The category of the poet. 
-  `sungfor`: The god.
-  `sungforcategory`: The category of the god. 


## Live sandbox

See [Rig Veda API: Try it out](openapi_rv.md).
