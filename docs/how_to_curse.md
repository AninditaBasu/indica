---
title: Vedic curses
description: Find and read the soliloquies and monologues in Rig Veda
author: Anindita Basu
og_title: Vedic curses
og_image: images/VS_2.png
---

# Tutorial: Vedic curses

<hr/>

A _curse_ is a word or phrase that's uttered with complete seriousness, with the intention to invoke a supernatural power that can cause harm or injury to someone or something.

Curses are born of human emotions and, therefore, are as old as humanity itself. The vedas, which are among the oldest text in a Indo-European language, contain interesting curses (in addition to the solemn hymns to gods, for which they're better known).  Atharva Veda is, in fact, more a compendium of curses than of grateful hymns to gods. Here's an example curse from Atharva Veda.

```text
Whoever shall curse us not cursing, 
And whoever shall curse us cursing, 
Like a tree smitten by a thunderbolt, 
Let him dry up from the root.

- Atharva Veda, 7.59
```

This tutorial shows you how to curse like you were living in the vedic times.

## Possible paths

All the path parameters in the Vedic Society API return a response in the same JSON structure.

```json
{
  "nagari": "string",
  "word": "string",
  "description": "string",
  "category": "string"
}
```

First, you find words that from those categories that have an element of evil or of suffering in them. And then, you string those words together to form sentences. 

Here's a pseudocode example:

```bash

where /categories/{category} == 'disease':
	get word
	get description
where /categories/{category} == 'family':
	get word
	get description
curse = 'May your ' + <family_word> + ' be blighted with ' + <disease_word> + '.

```

## Example code in Python

1.  Make a `GET` call for words in the `disease` category.

    ```python
	headers = {
	    'accept': 'application/json',
	}

	url = "https://api-vs.herokuapp.com/vs/v2/categories/disease"

	response = requests.get(url, headers=headers)
	response_json = json.loads(json.dumps(response.json()))
	```

1.  Loop through the returned JSON, and append the values of the `word` and `description` parameters to a dictionary.

    ```python hl_lines="5"
	import json
	diseases = {}
	
	for entry in response_json:
        diseases.update({entry['word']:entry['description']})
	```

1.  Repeat the two previous steps to generate a similar dictionary for families.
    1.  Make a `GET` call for words in the `family` category.
	1.  Make a dictionary for the values of the `word` and `description` parameters.
1.  Pick a random entry from both the dictionaries. You'll use these entries to compose a sentence.

    ```python
	import random
	disease, disease_meaning = random.choice(list(diseases.items()))
	family, family_meaning = random.choice(list(families.items()))
	```
	
1.  Compose the curse. Here's an example:

    ```python
	curse = 'May your ' + family + ' be blighted with ' + disease + '.'
	```

## Results

You should now be able to see a random curse like this:

```bash
May your didhishu be blighted with suram.
```

## What to do next

Maybe make the curses multilingual? If you also pick the `nagari` parameter when looping through the JSON data, you can generate curses like this:

```shell
May your बाल  be blighted with अर्शस.
बाल = bal (boy)
अर्शस = arshas (haemorrhoids)
```

Or, maybe make the curses more colourful? You could compose entire verses by picking random entries from the following categories: `snake`, `worm`, `insect`, `weapon`, `medicine`, `poison`.


<hr/>

{%include 'common/coffee.md'%}
