---
title: Vedic dialogues
description: Find and read the dialogues in Rig Veda
author: Anindita Basu
og_title: Vedic dialogues
og_description: Find and read the dialogues in Rig Veda
og_image: images/tweet_mockup_2.png
---

# Tutorial: Vedic dialogues

<hr/>

A _dialogue_ is a conversation between two or more people in a book, play, or film. Sometimes, countries also have dialgues amongst themselves, and these instances too can be said to belong to a play or film. Here is an example each.

=== "Normal human dialogue"

    ```
    Bertie: Tell me, Jeeves, were you always like this, or did it come on suddenly?
	Jeeves: Sir? 
	Bertie: The brain, the grey matter. Were you an outstandingly brilliant child?
	Jeeves: My mother thought me intelligent, Sir. Bertie: Well, you can't go by that! My mother thought me intelligent!

    (Woodehouse's Very Good, Jeeves) 
    ```

=== "Nations dialoguing"

    ```
    We have agreed that a conference of United Nations should be called
	to meet at San Francisco in the United States on April 25, 1945, 
	to prepare the charter of such an organization, along the lines proposed 
	in the informal conversations at Dumbarton Oaks.
	
	The Government of China and the Provisional Government of France 
	will be immediately consulted and invited to sponsor invitations to 
	the conference jointly with the Governments of the United States, 
	Great Britain, and the Union of Soviet Socialist Republics. 
	
	As soon as the consultation with China and France has been completed, 
	the text of the proposals on voting procedure will be made public.

    (Yalta Conference Agreement, 1945)
    ```

Rig Veda doesn't contain conversations between countries, but it does contain human conversations.  This tutorial shows you how to find (and read) these conversations.

## Algorithm

All the path parameters in the [Rig Veda API](api_rv.md) return a response in the same JSON structure.

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

In Rig Veda, books (or mandals) contain chapters, and chapters (or suktas) contain verses. If a sukta has more than one verse and if the poets are different in these verses, it's fair to assume that the sukta is a conversation between these poets.

The following algorithm uses the `/book/{mandal}` path parameter to identify such suktas.

## Example code in Python

These steps use the `/book/{mandal}` path parameter.

1.  Make a `GET` call for the first mandal.

    ```python
	headers = {
	    'accept': 'application/json',
	}

	url_suffix = "https://api-rv.herokuapp.com/rv/v2/meta/book/1"

	import json
	
	response = requests.get(url, headers=headers)
	response_json = json.loads(json.dumps(response.json()))
	```

## Results


## What to do next


<hr/>

{%include 'common/coffee.md'%}
