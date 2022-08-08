---
title: Vedic dialogues
description: Find and read the dialogues in Rig Veda
author: Anindita Basu
og_title: Vedic dialogues
og_description: Find and read the dialogues in Rig Veda
og_image: images/tweet_mockup_2.png
tags:
  - Rig Veda API
  - Tutorial
---

# HowTo: Vedic dialogues

<hr/>

A _dialogue_ is a conversation between two or more people in a book, play, or film. Sometimes, countries also have dialgues amongst themselves, and these instances too can be said to belong to a play or film. Here is an example each.

=== "Normal human dialogue"

    ```
    Bertie: Tell me, Jeeves, were you always like this, or did it come on suddenly?
	Jeeves: Sir? 
	Bertie: The brain, the grey matter. Were you an outstandingly brilliant child?
	Jeeves: My mother thought me intelligent, Sir. 
	Bertie: Well, you can't go by that! My mother thought me intelligent!

    - Woodehouse, P. G. "Very Good, Jeeves".
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

    - Yalta Conference Agreement, 1945
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

In Rig Veda, books (or mandals) contain chapters, and chapters (or suktas) contain verses. If a sukta has more than one verse, and if the poets are different in these verses, it's fair to assume that the sukta is a conversation between these poets.

!!! note "Entity relationship"

    For information on how mandals, suktas, poets, and gods are connected to each other, see the entity-relationship diagram at [About Rig Veda](about_rv.md).

The following algorithm uses the `/book/{mandal}` path parameter to identify such suktas.

1.  Fetch all the verses in a mandal.
1.  For each verse, make a `sukta`-`sungby` string and add it to a list.

    ```bash
	...
	8-Trishira Tvashtra
	9-Trishira Tvashtra
	9-Trishira Tvashtra
	10-Yami Vaivasvati
	10-Yama Vaivasvat
	11-Havirdhan Angi
	11-Havirdhan Angi
	...
	```
	
1.  Clean this list of duplicates.

    ```bash
	...
	8-Trishira Tvashtra
	9-Trishira Tvashtra
	10-Yami Vaivasvati
	10-Yama Vaivasvat
	11-Havirdhan Angi
	...
	```
	
1.  Iterate over this list to find instances where the same `sukta` occurs more than once (that is, the same `sukta` is tagged to more than one `sungby`). These are the verses that have more than one poet.

    ```bash
	...
	10-Yami Vaivasvati
	10-Yama Vaivasvat
	...
	```

## Example code in Python

These steps use the `/book/{mandal}` path parameter.

1.  Make a `GET` call for any mandal. The following example makes a call to the first mandal.

    ```python
	headers = {
	    'accept': 'application/json',
	}

	url = "https://api-rv.herokuapp.com/rv/v2/meta/book/1"

	import json
	
	response = requests.get(url, headers=headers)
	response_json = json.loads(json.dumps(response.json()))
	```

1.  Loop through the returned JSON and find the number of verses in the mandal. You'll use this number to run a counter in a later step.

    ```python
	sukta_numbers = []
	
	for entry in response_json:
        sukta_numbers.append(entry['sukta'])
	number_of_suktas = max(sukta_numbers)
	number_of_suktas = max(sukta_numbers)
	print("mandal", mandal, "has", number_of_suktas, "suktas")
	```

1.  Loop through the returned JSON again, pick `sukta` and `sungby`, and add them to a list. This is the list of all verses_by_poets in the mandal.

    ```python
	poet_list = []
	
	for entry in response_json:
        for entry in entry_full:
		text = str(entry['sukta']) + "-" + entry['sungby']
		poet_list.append(text)
	#print("poet list", len(poet_list), poet_list)
	```

1.  Clean the result list of duplicate entries. Because, the same poet might have sung all verses in a sukta, but if there are 5 verses in the sukta, the list will have 5 entries.

	```python
	unique = []
	duplicates = []
	for entry in poet_list:
		if entry in unique:
			duplicates.append(entry)
		else:
			unique.append(entry)
	```

1.  Iterate over this clean list, and pick the verses that have more than one entry. These are the dialogue verses.

	```python
	print("==========================")
	print("mandal " + str(mandal) + " conversations")
	print("==========================")
	counter = 1
	conversation_count = 0
	while counter <= number_of_suktas:
		text_to_search = str(counter) + '-'
		conversation = sum(word.startswith(text_to_search) for line in unique for word in line.split())
		if conversation > 1:
			print(conversation, "poets in sukta", counter)
			conversation_count = conversation_count + 1
		counter = counter + 1
	if conversation_count == 0:
    print("No conversations in this book")
	```

## Results

You now have a list of the dialogue verses in the mandal.

=== "Mandal has dialogue hymns"

    ```bash
    mandal 1 has 191 suktas
    ==========================
    mandal 1 conversations
    ==========================
    5 poets in sukta 100
    3 poets in sukta 126
    3 poets in sukta 165
    2 poets in sukta 170
    3 poets in sukta 179
    ```

=== "Mandal doesn't have dialogue hymns"

    ```bash
    mandal 6 has 75 suktas
    ==========================
    mandal 6 conversations
    ==========================
    No conversations in this book
    ```



## What to do next

Read the verse, maybe? Wikisource is good resource for ancient texts, so you can go read the poems there. The URLs at Wikisource are in the following format: `https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_1/Hymn_2`. Therefore, compose the URLs to match this scheme, and look up the verses.

## Obiter dicta

My favourite conversation in Rig Veda is in the tenth mandal and contained in chapter 95: [https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_95](https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_95).

It's a conversation between a king named Pururava Aila and his queen Urvashi.

## More HowTo-s

See [Index](tags.md).

<hr/>

{%include 'common/coffee.md'%}
