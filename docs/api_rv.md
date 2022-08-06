---
title: Rig Veda API reference documentation
description: Metadata of all the verses in Rig Veda. Contains info on rishis, gods, chhandas.
author: Anindita Basu
og_title: Rig Veda API reference documentation
og_description: Metadata of all the verses in Rig Veda. Contains info on rishis, gods, chhandas.
og_image: images/RV_1.png
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

{% include 'common/timeout.md' %}

## Context

An explanation of the various elements in Rig Veda (and this API) is contained in [About the Rig Veda API](about_rv.md).

## Base URL

`https://api-rv.herokuapp.com/rv/v2/meta/`

The request URL is formed by appending an endpoint to the base URL.

## Methods

Only `GET` calls are supported.

=== "Example request"

    For the request parameters, see [Endpoints](#endpoints).

    ```shell
    curl -X 'GET' \
        'https://api-rv.herokuapp.com/rv/v2/meta/god/ganga' \
        -H 'accept: application/json'
    ```

=== "Example response"

    For the response parameters, see [Response parameters](#response-parameters).

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

All parameters are path parameters. To form the request URL, the endpoint must be appended to the base URL.

```bash
request URL = base URL + endpoint
```

The following endpoints are available. 

### `/book/{mandal}`

Returns the metadata of all verses in the specified mandal. For example, `/book/4` returns the metadata of all of the verses in the 4th book.

`{mandal}` is an integer parameter.

Valid values for this parameter are 1 through 10 (because there are only 10 books in Rig Veda).

### `/meter/{meter}`

Returns the metadata of all verses in the specified poetic meter. For example `/meter/tup` returns the metadata for all verses written in any meter that has `tup` in its name, such as `Anushtup` and `Trishtup`.

`{meter}` is a string parameter.

### `/poet/{sungby}`

Returns the metadata of all verses by the specified poet. For example, `/poet/tra` returns the metadata of all verses composed by any poet whose name contains `tra`, such as `Vishwamitra` and `Vasishth Maitravaruni`.

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

Returns the metadata of all verses sung for the specified venerated being or object. For example, `/god/ni` returns all venerated beings or objects whose name contains `ni`, such as `Nirriti` (god), `Maitravaruni` (human), or `Sinivali` (abstract thing).

`{sungfor}` is a string parameter.

### `/god/{sungfor}/{mandal}`

Returns the metadata of all verses in a book that are sung for the specified venerated being or object. For example, `/god/agni/1` returns the metadata of all verses to Agni in book 1.

`{sungfor}` is a string parameter and `{mandal}` an integer parameter.

### `/godbypoet/{sungfor}/{sungby}`

Returns the metadata of all verses sung for the specified venerated being or object (for example `Agni` or `plough`) by the specified poet (for example, `Vasishth`).

`{sungfor}` and `{sungby}` are string parameter.

### `/godcategory/{sungforcategory}`

Returns metadata of all verses where a venerated being or object belongs to the specified category. The following categories are available:

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

Returns metadata of all verses where the venerated being or object, and the poet, belong to specified categories. The following categories are available:

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

## Response parameters

All the endpoints return a response in the following format:

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

Here's a description of these parameter.

-  `mandal`: The book number. Rig Veda has 10 books.
-  `sukta`: The chapter number. Books contain chapters. The number of chapters in each book is different. For example, mandal 5 contains 87 suktas while mandal 4 contains 58. The highest value possible for this parameter is 191 (which is the number of suktas in the 1st and 10th mandals). The following table lists the number of chapters in each book.

    ??? note "Click to show/hide the table"
	
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
-  `sungbycategory`: The category of the poet. For a list of categories, see [/poetcategory/{poetcategory}](#godcategorybypoetcategorysungforcategorysungbycategory).
-  `sungfor`: The god.
-  `sungforcategory`: The category of the god. For a list of categories, see [/godcategory/{sungforcategory}](#godcategorybypoetcategorysungforcategorysungbycategory).

## Live sandbox

See [Rig Veda API: Try it out](https://aninditabasu.github.io/indica/openapi_rv.html).

## Related

See [Index](tags.md).

<hr/>

{%include 'common/coffee.md'%}
