---
title: Finding conversations in the Rig Veda
description: Read the dialogues, monologues, and soliloquies after querying the API for hymns that are conversations, whether with one's own self or with some other being.
summary: Tutorial for finding instances of beings, whether human or divine or animal, talking to themselves or with each other in the Rig Veda.

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

  - title: Visualising Rig Vedic gods
    type: datavis
    url: /topics/datavis_gods_pie.html

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

A _dialogue_ is a conversation between two or more people in a book, play, or film. 

```bash
    Bertie: Tell me, Jeeves, were you always like this, or did it come on suddenly?
    Jeeves: Sir? 
    Bertie: The brain, the grey matter. Were you an outstandingly brilliant child?
    Jeeves: My mother thought me intelligent, Sir. 
    Bertie: Well, you can't go by that! My mother thought me intelligent!

    - Woodehouse, P. G. "Very Good, Jeeves".
```

A _soliloquy_ is an act of speaking one's thoughts aloud when alone, or regardless of any listeners, especially by a character in a play. When directed to any listeners, a soliloquy is called a _monologue_. 

Here is an example of a soliloquy.

```
    Is this a dagger which I see before me,
    The handle toward my hand? Come, let me clutch thee.

    - Shakespeare, William. "Macbeth". 
```

And here's an example of a monologue.

```
    I speak not to disprove what Brutus spoke,
    But here I am to speak what I do know.

    - Shakespeare, William. "Julius Caesar".
```

Rig Veda contains not only conversations between gods and poets but also monologues and soliloquies.  This tutorial shows you how to find these conversations.

---------

**On this page**

* TOC
{:toc}

---------

## Endpoints to use

- `/conversations`
- `/monologues`


## API response

For conversations, a list of dictionaries, with the following structure, is returned:

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

For monologues, the result looks something like this:

```
{
  "page": 1,
  "pages": 2,
  "results": [
    {
      "mandal": 4,
      "sukta": 42,
      "sungby": "Trasadasyu Paurukutsya",
      "sungbycategory": "human male"
    },
    {
      "mandal": 10,
      "sukta": 48,
      "sungby": "Indra Vaikunth",
      "sungbycategory": "divine male"
    },
...
```

## What to do next

Read the verse, maybe? Wikisource is good resource for ancient texts, so you can go read the poems there. The URLs at Wikisource are in the following format: `https://en.wikisource.org/wiki/The_Rig_Veda/Mandala_1/Hymn_2`. Therefore, compose the URLs to match this scheme, and look up the verses.

## Obiter dicta

My favourite conversation in Rig Veda is in the tenth mandal and contained in veser 95: [https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_95](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_95).

It's a conversation between a king named Pururava Aila and his queen Urvashi.

And my favourite soliloquy is this one: [https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_125](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_125).

This is the metadata for this poem:

```
{
      "mandal": 10,
      "sukta": 125,
      "sungby": "Vagambhrini",
      "sungbycategory": "human female"
}
```

Sanskrit version: [https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.१२५ ](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.१२५).

A musical rendering:

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4mnYGUG890pny5QTjCaZWr?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>



