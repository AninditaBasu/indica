---
title: Finding soliloquies in the Rig Veda
description: Read the soliloquies after querying the API for hymns that are monologues.
summary: Tutorial for finding instances of beings, whether human or divine or animal, speaking to themselves or to the world in the Rig Veda.

version: v3
status: stable
base_path: /rv/v3

canonical: https://aninditabasu.github.io/indica/topics/how_to_soliloquy.html

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

  - title: Finding conversations in the Rig Veda
    type: tutorial
    url: /topics/how_to_dialogues.html

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

# HowTo: Vedic soliloquies

<hr/>

A _soliloquy_ is an act of speaking one's thoughts aloud when alone, or regardless of any listeners, especially by a character in a play. When directed to any listeners, a soliloquy is called a _monologue_. 

Here is an example of a soliloquy.

```
    Is this a dagger which I see before me,
    The handle toward my hand? Come, let me clutch thee.
    I have thee not, and yet I see thee still.
    Art thou not, fatal vision, sensible
    To feeling as to sight? or art thou but
    A dagger of the mind, a false creation,
    Proceeding from the heat-oppressed brain?

    - Shakespeare, William. "Macbeth". 
```

And here's an example of a monologue.

```
    I speak not to disprove what Brutus spoke,
    But here I am to speak what I do know.
    You all did love him once, not without cause:
    What cause withholds you then, to mourn for him?
    O judgment! thou art fled to brutish beasts,
    And men have lost their reason. Bear with me;
    My heart is in the coffin there with Caesar,
    And I must pause till it come back to me.

    - Shakespeare, William. "Julius Caesar".
```

Soliloquies and monologues are as old as humankind. People were speaking to themselves, and speaking without waiting for a response, ever since they started speaking. Rig Veda, possibly the oldest book in the world, also has people soliloquising and monologising.

This tutorial shows you how to find the soliloquies and monologues in Rig Veda.

---------

**On this page**

* TOC
{:toc}

---------

## Endpoint to use

```
/monologues
```

## Result

A list of dictionaries with the following structure:

```
...
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

Iterate over the response to pick the mandal and sukta number combination, and look up the poem.

Wikisource is good resource for ancient texts, so you can go read the poems there. The URLs at Wikisource are in the following format: `https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_1/Hymn_2`. Therefore, compose the URLs to match this scheme.

Maybe read the poem in the original Sanskrit?

Wikisource has a Sanskrit site as well, and the URL format for Rig Veda is like this: `https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१.२`.

You can see that the numerals need to be in the Nagari script. So, you'd have to convert the Arabic numerals to Nagari, append them to the URL, and read the poems.

## Obiter dicta

My favourite poem on this list is this one: [https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_125](https://en.wikisource.org/wiki/The_Hymns_of_the_Rigveda/Book_10/Hymn_125).

This is the metadata for this poem:

```
sung by and for: Vagambhrini
category of singer: Human female
meters: Jagati and Trishtup
```

Sanskrit version: [https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.१२५ ](https://sa.wikisource.org/wiki/ऋग्वेदः_सूक्तं_१०.१२५).

A musical rendering:

<iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/4mnYGUG890pny5QTjCaZWr?utm_source=generator" width="100%" height="380" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture"></iframe>

