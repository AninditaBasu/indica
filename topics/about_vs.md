---
title: About the Vedic Society API
description: Query the API for meanings of all nouns, except proper nouns, from the entire vedic corpus (Rig Veda, Sama Veda, Yajur Veda, and Atharv Veda).
summary: Structured data for all nouns in the vedic corpus.

version: v2
status: stable
base_path: /vs/v2

canonical: https://aninditabasu.github.io/indica/topics/about_vs.html

tags:
  - vedic
  - sanskrit
  - history
  - material culture
  - api

related:
  - title: Building curses from vedic nouns
    type: tutorial
    url: /topics/how_to_curses.html

  - title: Visualising the frequency of terms in the vedic corpus
    type: datavis
    url: /topics/datavis_wordcloud.html

  - title: Vedic society API reference documentation
    type: reference
    url: /topics/api_vs.html

  - title: Vedic society API sandbox
    type: openapi
    url: /topics/openapi_vs.html
---

# About the Vedic Society API

<hr/>

This API contains the meanings of all nouns, except proper nouns, from the entire vedic corpus. Vedic literature comprises four vedas (Rig, Sama, Yajur, and Atharv). Each veda is a set of the following books:

-  Samhitas: Hymns or songs to gods
-  Brahmanas: Instructions on rituals
-  Upanishads: Philosophical discourses
	
All of these are reckoned for this API. The data is from the following books: :
	
-  Vedic Index of Names and Subjects, by A. A. Macdonell and A. B. Keith ([Volume 1](https://archive.org/details/in.ernet.dli.2015.284764) and [Volume 2](https://archive.org/details/in.ernet.dli.2015.211118))
-  [Vedic Mythology, by A. A. Macdonell](https://archive.org/details/in.ernet.dli.2015.47343/page/n5/mode/2up)
-  [The Nighantu and the Nirukta of Sri Yaskacharya, by Lakshman Sarup](https://archive.org/details/nighantuniruktao00yaskuoft)
-  [The Practical Sanskrit-English Dictionary, by V. S. Apte](https://dsal.uchicago.edu/dictionaries/apte/)

The data is returned in the following format:

```json
    {
      "nagari": "string",
      "word": "string",
      "description": "string",
      "category": "string"
    }
```

Here's an example response:

```json
	{
    	"category": "law",
    	"description": "thief",
    	"nagari": "तायु",
    	"word": "tayu"
  	}
```

The nouns are categorised into flora, fauna, geography, food, relationships, and more groups. The JSON response contains the word in the Nagari script, the word transliterated into the Roman script, the meaning of the word, and the category the word belongs to.

