---
title: Finding conversations in the Rig Veda
description: Read the dialogues after querying the API for hymns that are conversations.
summary: Tutorial for finding instances of beings, whether human or divine or animal, talking with each other in the Rig Veda.

version: v3
status: stable
base_path: /rv/v3

canonical: https://aninditabasu.github.io/indica/topics/how_to_dialogues.html

tags:
  - sruti
  - rig-veda
  - vedic
  - sanskrit
  - history
  - api
  - liturgy

related:
  - title: Visualising Rig Vedic meters
    type: datavis
    url: /topics/datavis_meters_pie.html

  - title: Finding soliloquies in the Rig Veda
    type: tutorial
    url: /topics/how_to_soliloquy.html

  - title: About the Rig Veda API
    type: explanation
    url: /topics/about_rv.html

  - title: Rig Veda API reference documentation
    type: reference
    url: /topics/api_rv.html

  - title: Rig Veda API sandbox
    type: openapi
    url: /topics/openapi_rv.html
---

# HowTo: Vedic dialogues

<hr/>

A _dialogue_ is a conversation between two or more people in a book, play, or film. Sometimes, countries also have dialgues amongst themselves, and these instances too can be said to belong to a play or film.

Here's an example of a normal human dialogue:

```bash
    Bertie: Tell me, Jeeves, were you always like this, or did it come on suddenly?
    Jeeves: Sir? 
    Bertie: The brain, the grey matter. Were you an outstandingly brilliant child?
    Jeeves: My mother thought me intelligent, Sir. 
    Bertie: Well, you can't go by that! My mother thought me intelligent!

    - Woodehouse, P. G. "Very Good, Jeeves".
```

And, here's an example of nations dialoguing:

<pre>
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
</pre>

Rig Veda doesn't contain conversations between countries, but it does contain human conversations.  This tutorial shows you how to find these conversations.

---------

**On this page**

* TOC
{:toc}

---------

## Endpoint to use

```
/conversations
```

## Result

A list of dictionaries with the following structure:

```
{
      "mandal": 4,
      "participants": [
        {
          "participant": "Trasadasyu Paurukutsya",
          "participantcategory": "human male",
          "role": "sungby"
        },
        {
          "participant": "Trasadasyu Paurukutsya",
          "participantcategory": "human male",
          "role": "sungfor"
        },
        {
          "participant": "Indra",
          "participantcategory": "divine male",
          "role": "sungfor"
        },
        {
          "participant": "Varun",
          "participantcategory": "divine male",
          "role": "sungfor"
        }
      ],
      "sukta": 42
},
{
      "mandal": 5,
      "participants": [
        {
          "participant": "Atri Bhaum",
          "participantcategory": "human male",
          "role": "sungby"
        },
        {
          "participant": "Indra",
          "participantcategory": "divine male",
          "role": "sungfor"
        },
        {
          "participant": "Surya",
          "participantcategory": "divine male",
          "role": "sungfor"
        },
        {
          "participant": "Surya",
          "participantcategory": "divine male",
          "role": "sungby"
        },
        {
          "participant": "Atri Bhaum",
          "participantcategory": "human male",
          "role": "sungfor"
        }
      ],
      "sukta": 40
},
```

## What to do next

Read the verse, maybe? Wikisource is good resource for ancient texts, so you can go read the poems there. The URLs at Wikisource are in the following format: `https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_1/Hymn_2`. Therefore, compose the URLs to match this scheme, and look up the verses.

## Obiter dicta

My favourite conversation in Rig Veda is in the tenth mandal and contained in veser 95: [https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_95](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_95).

It's a conversation between a king named Pururava Aila and his queen Urvashi.

