---
title: Rig Veda API reference documentation
description: Metadata of all the verses in Rig Veda. Contains info on rishis, gods, chhandas.
author: Anindita Basu
og_title: Rig Veda API reference documentation
og_image: images/RV_1.png
---

# Rig Veda API

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

{% include 'common/timeout.md' %}

## Base URL

`https://api-rv.herokuapp.com/rv/v2/meta/`

The request URL is formed by appending an endpoint to the base URL.

## Methods

Only `GET` calls are supported. For the available parameters, see [Endpoints](#endpoints).

=== "Example request"

    ```shell
    curl -X 'GET' \
        'https://api-rv.herokuapp.com/rv/v2/meta//god/ganga' \
        -H 'accept: application/json'
    ```

=== "Example response"

    ```json
	[
  	{
    	"mandal": 10,
	    "meter": "Jagati",
	    "sukta": 75,
	    "sungby": "Sindhukshit Praiyamedh",
	    "sungbycategory": "human male",
	    "sungfor": "Ganga",
	    "sungforcategory": "divine female"
	  }
	]
	```

## Endpoints

All parameters are path parameters, and all of them return a response in the following format:

```json
{
  "mandal": 0,
  "sukta": 0,
  "meter": "string",
  "sungby": "string",
  "sungbycategory": "string",
  "sungfor": "string",
  "sungforcategory": "string"
}
```

The following endpoints are available. To form the request URL, the endpoint must be appended to the base URL.

### `/book/{mandal}`

Returns the metadata of all verses in the specified mandal. For example, `/mandal/4` returns the metadata of all of the verses in the 4th book.

`{mandal}` is an integer parameter.

Valid values for this parameter are 1 through 10 (because there are only 10 mandals in Rig Veda).

### `/chapter/{sukta}`

Returns the metadata of all verses for the specified sukta from all mandals. For example, `/sukta/23` returns the metadata for all suktas numbered 23 from all the 10 mandals.

`{sukta}` is an integer parameter. 

The number of suktas in each mandal is different. For example, mandal 5 contains 87 suktas while mandal 4 contains 58. The highest value possible for this parameter is 191 (which is the number of suktas in the 1st and 10th mandals). The following table lists the number of verses in each book.

| Mandal | Sukta |
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

### `/meter/{meter}`

Returns the metadata of all verses in the specified poetic meter. For example `/meter/tup` returns the metadata for all verses written in any meter that has `tup` in its name, such as `Anushtup` and `Trishtup`.

`{meter}` is a string parameter.

### `/poet/{sungby}`

Returns the metadata of all verses by the specified poet. For example, `tra` returns the metadata of all verses composed by any poet whose name contains `tra`, such as `Vishwamitra` and `Vasishth Maitravaruni`.

`{sungby}` is a string parameter.

### `/poetcategory/{poetcategory}`

Returns the metadata of all verses where the poet belongs to the specified category. The following categories are available:

-  `animal`
-  `demon male`
-  `divine female`
-  `divine male`
-  `human female`
-  `human male`

`{poetcategory}` is a string parameter. 

### `/god/{sungfor}`

Returns the metadata of all verses sung for the specified god. For example, `ni` returns all venerated beings or objects whose name contains `ni`, such as `Nirriti` (god), `Maitravaruni` (human), or `Sinivali` (abstract thing).

`{sungfor}` is a string parameter.

### `/god/{sungfor}/{mandal_number}`

Returns the metadata of all verses in a mandal that are sung for the specified god, for example `Agni` or `plough` in mandal `1`.

`{sungfor}` is a string parameter and `{mandal_number}` an integer parameter.

### `/godbypoet/{sungfor}/{sungby}`

Returns the metadata of all verses sung for the specified god (for example `Agni` or `plough`) by the specified poet (for example, `Vasishth`).

`{sungfor}` and `{sungby}` are string parameter.

### `godcategory/{sungforcategory}`

Returns metadata of all verses where a god belongs to the specified category. The following categories are available:

-  `abstract`
-  `animal`
-  `demon male`
-  `divine female`
-  `divine human`
-  `divine male`
-  `human couple`
-  `human female`
-  `human male`
-  `human unborn`
-  `object`
-  `plant`

`{sungforcategory}` is a string parameter.

### `/godcategorybypoetcategory/{sungforcategory}/{sungbycategory}`

Returns metadata of all verses where the god and the poet belong to specified categories. The following categories are available:

=== "categories of gods"

    -  `abstract`
    -  `animal`
    -  `demon male`
    -  `divine female`
    -  `divine human`
    -  `divine male`
    -  `human couple`
    -  `human female`
    -  `human male`
    -  `human unborn`
    -  `object`
    -  `plant`

=== "categories of poets"

    -  `animal`
    -  `demon male`
    -  `divine female`
    -  `divine male`
    -  `human female`
    -  `human male`

`{sungforcategory}` and `{sungbycategory}` are string parameters.

## Live sandbox

See [Rig Veda API: Try it out](https://aninditabasu.github.io/indica/openapi_rv.html).

## Tutorials

-  [Vedic soliloquies](how_to_soliloquy.md)

<hr/>

{%include 'common/coffee.md'%}
