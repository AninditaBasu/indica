---
title: The Rig Veda API reference
---

# Rig Veda API

Poets and gods in the Rig Veda, presented with the mandal and sukta numbers, and the meters the verses are composed in.

!!! danger "Timeout"

    These APIs are offline every night between 9:00 PM IST and 9:00 AM IST.

## Endpoint

`https://api-rv.herokuapp.com/rv/v2/meta/`

## Methods

Only `GET` calls are supported.

### Example request

For the available parameters, see [Parameters](#parameters).

=== "cURL"

    ```shell
	curl https://api-rv.herokuapp.com/rv/v2/meta/sukta/150
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
			URL url = new URL("https://api-rv.herokuapp.com/rv/v1/resources?sukta=150");
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

    ```js
	fetch('https://api-rv.herokuapp.com/rv/v1/resources?sukta=150');
	```

=== "Node.js"

    ```nodejsrepl
	var request = require('request');

	var options = {
    	url: 'https://api-rv.herokuapp.com/rv/v1/resources?sukta=150'
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
    "mandal": 1,
    "meter": "Ushnik",
    "sukta": 150,
    "sungby": "Dirghatamas Auchathya",
    "sungbycategory": "human male",
    "sungfor": "Agni",
    "sungforcategory": "divine male"
  },
  {
    "mandal": 10,
    "meter": "Brihati",
    "sukta": 150,
    "sungby": "Mrilik Vasishth",
    "sungbycategory": "human male",
    "sungfor": "Agni",
    "sungforcategory": "divine male"
  },
  {
    "mandal": 10,
    "meter": "Jagati",
    "sukta": 150,
    "sungby": "Mrilik Vasishth",
    "sungbycategory": "human male",
    "sungfor": "Agni",
    "sungforcategory": "divine male"
  },
  {
    "mandal": 10,
    "meter": "Uparishtajjyoti",
    "sukta": 150,
    "sungby": "Mrilik Vasishth",
    "sungbycategory": "human male",
    "sungfor": "Agni",
    "sungforcategory": "divine male"
  }
]
```

## Parameters

All parameters are path parameters.

### `mandal`

Returns all verses in that mandal.

This is an integer parameter. The path is like this: `/mandal/<mandal_number>`. For example, `/mandal/4` returns all of the verses in the 4th book.

Valid values for this parameter are 1 through 10 (because there are only 10 mandals in the Rig Veda).

### `sukta`

Returns the sukta bearing that number from all the mandals.

This is an integer parameter. The path is like this: `/sukta/<sukta_number>`. For example, `/sukta/23` returns all the suktas that are numbered 23 from all the 10 mandals.

The number of suktas in each mandal is different; for example, mandal 5 contains 87 suktas. The highest value possible for this parameter is 191 (which is the number of suktas in the 1st and 10th mandals). The following table lists the number of verses in each book.

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

### `sungby`

Returns all verses sung by that person.

This is a string parameter. The path is like this:  `/sungby/<string>`. For example, `//sungby/tra` returns all composers whose name contains `tra`, for example `Vishwamitra`.

### `sungbycategory`

Returns all verses composed by that category of composer, for example, `human male`. The following categories are available:

-  `animal`
-  `demon male`
-  `divine female`
-  `divine male`
-  `human female`
-  `human male`

This is a string parameter. The path is like this:  `/sungbycategory/<string>`. For example `/sungbycategory/ale` returns all of the verses composed by all males and females, whether human or divine.

### `sungfor`

Returns all verses sung for that subject, for example, `Agni` or `plough`.

This is a string parameter. The path is like this:  `/sungfor/<string>`. For example, `/sungfor/ni` returns all venerated beings or objects whose name contains `ni`, like Nirriti (god), Maitravaruni (human) or Sinivali (abstract thing).

### `sungforcategory`

Returns all verses sung for that category, for example, `object`. The following categories are available:

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

This is a string parameter. The path is like this: `/sungforcategory/<string>`. For example `/sungforcategory/animal` returns all animals.

### `meter`

Returns all verses that are composed in that meter.

This is a string parameter. The path is like this: `/meter/<string>`. For example `/meter/tup` returns all meters that contain `tup`, such as Anushtup and Trishtup.

## Sandbox

See [Interactive API](https://aninditabasu.github.io/indica/rv_meta_openapi3.html).

<hr/>

<a href="https://whimsy.myinstamojo.com/product/480613/coffee-ddbc0/" data-store-name="whimsy" data-domain="https://whimsy.myinstamojo.com" data-id="480613" rel="im-new-checkout" data-text="Like this API? Buy me a coffee." data-css-style="background:#1273de; color:#ffffff; width:300px; border-radius:30px" data-layout="vertical"></a>
<script src="https://manage.instamojo.com/assets/js/pay_button/button.min.js"></script>