---
title: Vedic soliloquies
description: Find and read the soliloquies and monologues in Rig Veda
author: Anindita Basu
og_title: Vedic soliloquies
og_description: Find and read the soliloquies and monologues in Rig Veda
og_image: images/tweet_mockup_2.png
tags:
  - Rig Veda API
---

# Tutorial: Vedic soliloquies

<hr/>

A _soliloquy_ is an act of speaking one's thoughts aloud when alone, or regardless of any listeners, especially by a character in a play. When directed to any listeners, a soliloquy is called a _monologue_. Here is an example each.

=== "Soliloquy"

    ```
    Is this a dagger which I see before me,
    The handle toward my hand? Come, let me clutch thee.
    I have thee not, and yet I see thee still.
    Art thou not, fatal vision, sensible
    To feeling as to sight? or art thou but
    A dagger of the mind, a false creation,
    Proceeding from the heat-oppressed brain?

    (Shakespeare's Macbeth. Act 2, Scene 1.) 
    ```

=== "Monologue"

    ```
    I speak not to disprove what Brutus spoke,
    But here I am to speak what I do know.
    You all did love him once, not without cause:
    What cause withholds you then, to mourn for him?
    O judgment! thou art fled to brutish beasts,
    And men have lost their reason. Bear with me;
    My heart is in the coffin there with Caesar,
    And I must pause till it come back to me.

    (Shakespeare's Julius Caesar. Act 3, Scene 2.)
    ```

Soliloquies and monologues are as old as humankind. People were speaking to themselves, and speaking without waiting for a response, ever since they started speaking. Rig Veda, possibly the oldest book in the world, also has people soliloquising and monologising.

This tutorial shows you how to find (and read) the soliloquies and monologues in Rig Veda.

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

Because you're interested in people talking to themselves, you need the verses where `sungby` is the same as `sungfor`. To do so, you can use any of the path parameters to get all verses in all books, and then programmatically extract only those verses where the poet is the same as the god.

The steps for getting this filtered list verses will depend on the path parameter that you use. The following pseudocodes show the steps with 3 different path parameters.

=== "/book/{mandal}"

    Use the `/book/{mandal}` path parameter.
	
      1.  Start a counter from 1.
	  1.  Create an empty list to store the results.
	  1.  Get all verses of the mandal, where `{mandal}` is equal to the counter value.
	  1.  Loop through the returned JSON and find verses where `sungby` is the same as `sungfor`. Append those verses to the list.
      1.  Increase the counter by 1.
      1.  Repeat the previous steps till counter value is 11.
	  1.  Remove duplicate entries from the list.
	  1.  Iterate over this list, pick the mandal and sukta number combination, and use your favourite search engine to look up the poem.

=== "/poetcategory/{poetcategory}"

    Use the `/poetcategory/{poetcategory}` path parameter.
	
	  1.  Create a list where the list items are the available categories.
	  1.  Create an empty list to store the results.
	  1.  Loop through the category list to get all verses where `{poetcategory}` is equal to the category list item.
	  1.  Loop through the returned JSON and find verses where `sungby` is the same as `sungfor`. Append those verses to the empty list.
      1.  Pick up the next item from the category list, and repeat steps 2, 3, and 4.
      1.  Repeat the previous steps till there are no more items in the category list.
	  1.  Remove duplicate entries from the generated result list.
	  1.  Iterate over this list, pick the mandal and sukta number combination, and use your favourite search engine to look up the poem.

=== "/godcategory/{sungforcategory}"
		
    Use the `/godcategory/{sungforcategory}` path parameter.
   
    The steps are the same as that for the `/poetcategory/{poetcategory}`. The only difference is, in step 1, the available categories in the `/godcategory/{sungforcategory}` list is different from the ones in `/poetcategory/{poetcategory}`.

## Example code in Python

These steps use the `/poetcategory/{poetcategory}` path parameter.

1.  Create a list of all available categories.

    ```python
	categories = ["animal", "demon male", "divine female", "divine male", "human female", "human male"]
	```

1.  Iterate over this list and make a `GET` call for each category to the `/poetcategory/{poetcategory}` path parameter.

    ```python
	headers = {
	    'accept': 'application/json',
	}

	url_suffix = "https://api-rv.herokuapp.com/rv/v2/meta/poetcategory/"

	import json
	for item in category:
		url = url_suffix + item
		response = requests.get(url, headers=headers)
		response_json = json.loads(json.dumps(response.json()))
	```

1.  Loop through the returned JSON and find verses where `sungby` is the same as `sungfor`. Append those verses to the result list.

    ```python
	soliloquy = []
	
	for entry in response_json:
        if entry['sungby'] == entry['sungfor']:
            soliloquy.append(entry)
	```

1.  Clean the result list of duplicate entries.

	```python
	soliloquy_unique = []
	
	for entry in soliloquy:
       if entry in soliloquy_unique:
           continue
       else:
           soliloquy_unique.append(entry)
	```
	
1.  Iterate over this list, pick the mandal and sukta number combination, and look up the poem.

Wikisource is good resource for ancient texts, so you can go read the poems there. The URLs at Wikisource are in the following format: `https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_1/Hymn_2`. Therefore, compose the URLs to match this scheme.

	```python
	for item in soliloquy_unique:
        poem = "Mandala_" + str(item['mandal']) + "/Hymn_" + str(item['sukta'])
        poem_list.append(poem)

	for item in poem_list:
    	url = url_suffix + item
    	print(url)
	```

## Results

You now have a list of URLs for the soliloquies and monologues in Rig Veda.

```
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_159
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_48
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_49
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_50
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_53
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_79
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_80
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_124
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_140
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_125
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_4/Hymn_42
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_119
https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_139

Process finished with exit code 0
```

## What to do next

Maybe read the poem in the original Sanskrit?

Wikisource has a Sanskrit site as well, and the URL format for Rig Veda is like this: `https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१.२`.

You can see that the numerals need to be in the Nagari script. So, you'd have to convert the Arabic numerals to Nagari, append them to the URL, and read the poems.

## Obiter dicta

My favourite poem on this list is this one: [https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_125](https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_10/Hymn_125).

This is the metadata for this poem:

```
sung by and for: Vagambhrini
category of singer: Human female
meters: Jagati and Trishtup
```

Sanskrit version: [https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.१२५ ](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.१२५).

A musical rendering:

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4mnYGUG890pny5QTjCaZWr?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

<hr/>

{%include 'common/coffee.md'%}
