---
title: Vedic Society API reference documentation
description: Nouns in vedic literature, including the flora, fauna, geography, food, relationships, and objects.
author: Anindita Basu
og_title: Vedic Society API reference documentation
og_description: Nouns in vedic literature, including the flora, fauna, geography, food, relationships, and objects.
og_image: images/VS_1.png
---

# Vedic Society API

<hr/>

This API fetches the meanings of nouns from vedic literature.  The nouns are categorised as flora, fauna, geography, food, relationships, and more groups. The JSON response contains the word in Nagari script and transliterated roman script, the meaning, and the category.

```json
[
  {
    "category": "law",
    "description": "thief",
    "nagari": "तायु",
    "word": "tayu"
  }
]
```

{% include 'common/timeout.md' %}

## Base URL

`https://api-vs.herokuapp.com/vs/v2/`

## Methods

Only `GET` calls are supported.

=== "Example request"

    For the request parameters, see [Endpoints](#endpoints).

    ```shell
    curl -X 'GET' \
        'https://api-vs.herokuapp.com/vs/v2/words/ash' \
        -H 'accept: application/json'
    ```

=== "Example response"

    For the response parameters, see [Response parameters](#response-parameters).

    ```json
	[
	  {
	    "category": "law",
	    "description": "defendant, mentioned in the list of victims of purushmedh (human sacrifice)",
	    "nagari": "अभिप्रश्निन",
	    "word": "abhiprashnin"
	  },
	  {
	    "category": "plant",
	    "description": "Odina pinnata, Prosopis spicigera, or Mimosa suma",
	    "nagari": "अजशृङ्गी",
	    "word": "ajashringi"
	  },
	  ...
	]
	```

## Endpoints

All parameters are path parameters. To form the request URL, the endpoint must be appended to the base URL.

```bash
request URL = base URL + endpoint
```

The following endpoints are available. 

### `/words/{word}`

Returns all nouns, transliterated from Sanskrit to the Roman script, that contains the specified word or phrase.  For example, `/words/shat` returns the entries for all words that contain `shat`, such as  `kshatriya`, `prishat`, or `shatapati`.

`{word}` is a string parameter.

### `/descriptions/{description}`

Returns all nouns where the meaning contains the specified phrase.  For example, `/descriptions/horse` returns all descriptions that contain the word `horse`.

To get all nouns that contain `horse` (rather than all descriptions that contain `horse`), use the `words` parameter instead, and use a Sanskrit word for horse, such as `ashwa`.

`{description}` is a string parameter.

### `/categories/{category}`

Returns all nouns that belong to the specified category. The following categories are available.

|  Subject to explore | Available categories |
| --- | --- |
| Flora | `grass`, `plant`, `tree` | 
| Fauna | `animal`, `bird`, `cattle`, `fish`, `insect`, `snake`, `worm` | 
| Things | `building`, `chariot`, `food`, `grain`, `metal`, `object`, `ship`, `weapon`, `war` | 
| Measurements | `number`, `distance`, `time`, `weight` | 
| Geography | `mountain`, `place`, `river` | 
| Knowledge | `astronomy`, `disease`, `literature`, `medicine`, `poison`, `subject` | 
| Entertainment | `dicing`, `games`, `music` | 
| Toilette | `clothing`, `hair`, `ornament` | 
| Legal | `law`, `morals` | 
| Societal | `agriculture`, `caste`, `family`, `occupation`, `priest`, `royalty`, `trade`, `tribe` | 

For example, `/categories/clothing` returns all nouns that are tagged as an item of clothing.

A noun can belong to more than one category. For example, `aj` is both an `animal` and the name of a `tribe`.

`{category}` is a string parameter.

## Response parameters

All the endpoints return a response in the following format:

```json
{
  "nagari": "string",
  "word": "string",
  "description": "string",
  "category": "string"
}
```

The `word`, `description`, and `category` parameters are already described in [Endpoints](#endpoints). Here's a description of the `nagari` parameter.

-  `nagari`: The word itself in Sanskrit, represented in the Nagari script. For example, `अजशृङ्गी`.


## Live sandbox

See [Vedic Society API: Try it out](https://aninditabasu.github.io/indica/openapi_vs.html).

## Related

See [Index](tags.md).

<hr/>

{%include 'common/coffee.md'%}

