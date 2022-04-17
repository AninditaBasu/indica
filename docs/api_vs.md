---
title: The Vedic Society API reference
---

# Vedic Society API

Nouns in vedic literature, including the flora, fauna, geography, food, relationships, and objects.

!!! danger "Timeout"

    These APIs are offline every night between 9:00 PM IST and 9:00 AM IST.

## Endpoint

`https://api-vs.herokuapp.com/vs/v1/resources?`

## Methods

Only `GET` calls are supported.

### Example request

Querying on more than one parameter in a single API request is not supported. Querying on the `nagari` parameter is not supported. For the available parameters, see [Query parameters](#query-parameters).

=== "cURL"

    ```shell
	curl https://api-vs.herokuapp.com/vs/v1/resources?category=dicing
	```

=== "Python"

    ```python
	import requests

	params = {
		'sukta': '150',
	}

	response = requests.get('https://api-rv.herokuapp.com/rv/v1/resources', params=params)
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
			URL url = new URL("https://api-vs.herokuapp.com/vs/v1/resources?category=dicing");
			HttpURLConnection httpConn = (HttpURLConnection) url.openConnection();
			httpConn.setRequestMethod("GET");

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
	fetch('https://api-vs.herokuapp.com/vs/v1/resources?category=dicing');
	```

=== "Node.js"

    ```nodejsrepl
	var request = require('request');

	var options = {
    	url: 'https://api-vs.herokuapp.com/vs/v1/resources?category=dicing'
	};

	function callback(error, response, body) {
    	if (!error && response.statusCode == 200) {
        console.log(body);
    	}
	}

	request(options, callback);
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

## Query parameters

All the parameters are string parameters. Querying on more than one parameter in a single API request is not supported.

### `word`

Returns all nouns, in Sanskrit, transliterated into the roman script, that contains the word.

The query is like this: `/resources?word=<string>`. For example, `/resources?word=shat` returns all words that contain `shat`, for example, kshatriya, prishat, or shatapati.

### `nagari`

Returns the noun in the Nagari script, for example, `आल`. Querying on this parameter is not supported.

### `description`

Returns all nouns that contain the string in the description of the noun.

The query is like this: `/resources?description=<string>`. For example, `/resources?description=horse` returns all descriptions that contain the word `horse`.

To get all nouns that contain `horse`, use the `word` parameter instead and use a Sanskrit word for horse, such as `ashwa`.

### `category`

Returns all nouns that belong to that category. The following categories are available:

-  Flora: `grass`, `plant`, `tree`
-  Fauna: `animal`, `bird`, `cattle`, `fish`, `insect`, `snake`, `worm`
-  Things: `building`, `chariot`, `food`, `grain`, `metal`, `object`, `ship`, `weapon`, `war`
-  Measurements: `number`, `distance`, `time`, `weight`
-  Geography: `mountain`, `place`, `river`
-  Knowledge: `astronomy`, `disease`, `literature`, `medicine`, `poison`, `subject`
-  Entertainment: `dicing`, `games`, `music`
-  Toilette: `clothing`, `hair`, `ornament`
-  Legal: `law`, `morals`
-  Societal: `agriculture`, `caste`, `family`, `occupation`, `priest`, `royalty`, `trade`, `tribe`

The query is like this: `/resources?category=<string>`. For example, `/resources?category=clothing` returns all nouns that are tagged as an item of clothing. A noun can belong to more than one category. For example, `aj` is both an `animal` and the name of a `tribe`.

<hr/>

<a href="https://whimsy.myinstamojo.com/product/480613/coffee-ddbc0/" data-store-name="whimsy" data-domain="https://whimsy.myinstamojo.com" data-id="480613" rel="im-new-checkout" data-text="Like this API? Buy me a coffee." data-css-style="background:#1273de; color:#ffffff; width:300px; border-radius:30px" data-layout="vertical"></a>
<script src="https://manage.instamojo.com/assets/js/pay_button/button.min.js"></script>

