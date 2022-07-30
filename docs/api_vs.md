---
title: Vedic Society API reference documentation
description: Nouns in vedic literature, including the flora, fauna, geography, food, relationships, and objects.
author: Anindita Basu
og_title: Vedic Society API reference documentation
og_image: images/VS_1.png
---

# Vedic Society API

Nouns in vedic literature, including the flora, fauna, geography, food, relationships, and objects.

!!! danger "Timeout"

    These APIs are offline every night between 9:00 PM IST and 9:00 AM IST.

## Endpoint

`https://api-vs.herokuapp.com/vs/v2/`

## Methods

Only `GET` calls are supported.

### Example request

For the available parameters, see [Parameters](#parameters).
<!--Examples generated through https://curlconverter.com/-->

=== "cURL"

    ```shell
	curl -X 'GET' \
  		'https://api-vs.herokuapp.com/vs/v2/words/ash' \
  		-H 'accept: application/json'
	```

=== "Python"

    ```python
	import requests

	headers = {
	    'accept': 'application/json',
	}

	response = requests.get('https://api-vs.herokuapp.com/vs/v2/words/ash', headers=headers)
	```

=== "Java"

    ```java
	import java.io.IOException;
	import java.io.InputStream;
	import java.net.HttpURLConnection;
	import java.net.URL;
	import java.util.Scanner;

	class Main {

		public static void main(String[] args) throws IOException {
			URL url = new URL("https://api-vs.herokuapp.com/vs/v2/words/ash");
			HttpURLConnection httpConn = (HttpURLConnection) url.openConnection();
			httpConn.setRequestMethod("GET");
	
			httpConn.setRequestProperty("accept", "application/json");
	
			InputStream responseStream = httpConn.getResponseCode() / 100 == 2
					? httpConn.getInputStream()
					: httpConn.getErrorStream();
			Scanner s = new Scanner(responseStream).useDelimiter("\\A");
			String response = s.hasNext() ? s.next() : "";
			System.out.println(response);
		}
	}
    ```

=== "Javascript"

    ```
	fetch('https://api-vs.herokuapp.com/vs/v2/words/ash', {
	    headers: {
	        'accept': 'application/json'
	    }
	});
	```

=== "Node.js"

    ```nodejsrepl
	import fetch from 'node-fetch';

	fetch('https://api-vs.herokuapp.com/vs/v2/words/ash', {
	    headers: {
	        'accept': 'application/json'
	    }
	});
	```

### Example response

```json
[
  {
    "category": "dicing",
    "description": "dice",
    "nagari": "अक्ष",
    "word": "aksh"
  },
  {
    "category": "dicing",
    "description": "a game of dice",
    "nagari": "दीव",
    "word": "div"
  },
  {
    "category": "dicing",
    "description": "a game of dice",
    "nagari": "द्यूत",
    "word": "dyut"
  },
  {
    "category": "dicing",
    "description": "the throw of dice",
    "nagari": "ग्लह",
    "word": "glah"
  },
  {
    "category": "dicing",
    "description": "the throw of dice",
    "nagari": "ग्राभ",
    "word": "grabh"
  },
  {
    "category": "dicing",
    "description": "gambler, one who plays the dice",
    "nagari": "किटव",
    "word": "kitav"
  },
  {
    "category": "dicing",
    "description": "leaving of the dice (as opposed to glahan, taking them up for the throw)",
    "nagari": "शेषण",
    "word": "sheshan"
  },
  {
    "category": "dicing",
    "description": "professional gambler",
    "nagari": "श्वघ्निन",
    "word": "shvaghnin"
  }
]
```

## Parameters

All parameters are path parameters.

### `words`

Returns all nouns, transliterated from Sanskrit to the roman script, that contains the specified word or phrase.
      
The path is like this: `/words/<word>`. For example, `/words/shat` returns the entries for all words that contain `shat`, for example, `kshatriya`, `prishat`, or `shatapati`.

### `descriptions`

Returns all nouns where the meaning contains the specified phrase.

The path is like this: `/descriptions/<description>`. For example, `/descriptions/horse` returns all descriptions that contain the word `horse`.

To get all nouns that contain `horse`, use the `words` parameter instead, and use a Sanskrit word for horse, such as `ashwa`.

### `categories`

Returns all nouns that belong to the specified category. The following categories are available:

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

The path is like this: `/categories/<category>`. For example, `/categories/clothing` returns all nouns that are tagged as an item of clothing.

A noun can belong to more than one category. For example, `aj` is both an `animal` and the name of a `tribe`.

<hr/>

{%include 'common/coffee.md'%}

