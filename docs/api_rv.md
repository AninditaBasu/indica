---
title: Rig Veda API reference documentation
description: Metadata of all the verses in the Rig Veda. Contains info on rishis, gods, chhandas.
author: Anindita Basu
og_title: Rig Veda API reference documentation
og_image: images/RV_1.png
---

# Rig Veda API

Metadata of all the verses in the Rig Veda. Contains info on poets, gods, their categories, and the poetic meters.

!!! danger "Timeout"

    These APIs are offline every night between 9:00 PM IST and 9:00 AM IST.

## Endpoint

`https://api-rv.herokuapp.com/rv/v2/meta/`

## Methods

Only `GET` calls are supported.

### Example request

For the available parameters, see [Parameters](#parameters).
<!--Examples generated through https://curlconverter.com/-->

=== "cURL"

    ```shell
	curl -X 'GET' \
  	'https://api-rv.herokuapp.com/rv/v2/meta/sukta/3' \
  	-H 'accept: application/json'
	```

=== "Python"

    ```python
	import requests

	headers = {
    	'accept': 'application/json',
	}

	response = requests.get('https://api-rv.herokuapp.com/rv/v2/meta/sukta/3', headers=headers)
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
    		URL url = new URL("https://api-rv.herokuapp.com/rv/v2/meta/sukta/3");
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

    ```js
	fetch('https://api-rv.herokuapp.com/rv/v2/meta/sukta/3', {
	    headers: {
	        'accept': 'application/json'
	    }
	});
	```

=== "Node.js"

    ```nodejsrepl
	import fetch from 'node-fetch';

	fetch('https://api-rv.herokuapp.com/rv/v2/meta/sukta/3', {
	    headers: {
	        'accept': 'application/json'
	    }
	});
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

## Path parameters

All parameters are path parameters.

### `mandal`

Returns the metadata of all verses in the specified mandal.

This is an integer parameter. The path is like this: `/mandal/<mandal_number>`. For example, `/mandal/4` returns the metadata of all of the verses in the 4th book.

Valid values for this parameter are 1 through 10 (because there are only 10 mandals in the Rig Veda).

### `sukta`

Returns the metadata of all verses for the specified sukta from all mandals.

This is an integer parameter. The path is like this: `/sukta/<sukta_number>`. For example, `/sukta/23` returns the metadata for all suktas numbered 23 from all the 10 mandals.

The number of suktas in each mandal is different; for example, mandal 5 contains 87 suktas while mandal 4 contains 58. The highest value possible for this parameter is 191 (which is the number of suktas in the 1st and 10th mandals). The following table lists the number of verses in each book.

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

### `meter`

Returns the metadata of all verses in the specified poetic meter, for example, `gayatri`.

This is a string parameter. The path is like this: `/meter/<string>`. For example `/meter/tup` returns the metadata for all verses written in any meter that has `tup` in its name, such as `Anushtup` and `Trishtup`.

### `sungby`

Returns the metadata of all verses by the specified singer, for example, `Bharadwaj`.

This is a string parameter. The path is like this: `/sungby/<string>`. For example, `tra` returns the metadata of all verses composed by any singer whose name contains `tra`, such as `Vishwamitra` and `Vasishth Maitravaruni`.

### `sungbycategory`

Returns the metadata of all verses where the singer belongs to the specified category. The following categories are available:

-  `animal`
-  `demon male`
-  `divine female`
-  `divine male`
-  `human female`
-  `human male`

This is a string parameter. The path is like this:  `/sungbycategory/<specific_string>`. 

### `sungfor`
Returns the metadata of all verses sung for the specified god, human, or object, for example `Agni` or `plough`.

This is a string parameter. The path is like this:  `/sungfor/<string>`. For example, `ni` returns all venerated beings or objects whose name contains `ni`, such as `Nirriti` (god), `Maitravaruni` (human), or `Sinivali` (abstract thing).

### `sungforcategory`

Returns metadata of the verses where the subject belongs to the specified category. The following categories are available:

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

This is a string parameter. The path is like this: `/sungforcategory/<specific_string>`.

## Live sandbox

See [Rig Veda API: Swagger sandbox](https://aninditabasu.github.io/indica/rv_meta_openapi3.html).

<hr/>

{%include 'common/coffee.md'%}
