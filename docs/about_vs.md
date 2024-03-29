---
title: About the Vedic Society API
description: Nouns from the vedic corpus.
author: Anindita Basu
og_title: About the Vedic Society API
og_description: Nouns from the vedic corpus.
og_image: images/signboard.png
---

# About the Vedic Society API

<hr/>

This API contains the meanings of all nouns, except proper nouns, from the entire vedic corpus. Vedic literature comprises four vedas (Rig, Sama, Yajur, and Atharv). Each veda is a set of these articles:

-  Samhitas: Hymns or songs to gods
-  Brahmanas: Instructions on rituals
-  Upanishads: Philosophical discourses
	
All of these are reckoned for this API. The data is from the following books: :
	
-  Vedic Index of Names and Subjects, by A. A. Macdonell and A. B. Keith ([Volume 1](https://archive.org/details/in.ernet.dli.2015.284764) and [Volume 2](https://archive.org/details/in.ernet.dli.2015.211118))
-  [Vedic Mythology, by A. A. Macdonell](https://archive.org/details/in.ernet.dli.2015.47343/page/n5/mode/2up)
-  [The Nighantu and the Nirukta of Sri Yaskacharya, by Lakshman Sarup](https://archive.org/details/nighantuniruktao00yaskuoft)
-  [The Practical Sanskrit-English Dictionary, by V. S. Apte](https://dsal.uchicago.edu/dictionaries/apte/)

The data is returned in the following format:

=== "Schema"

    ```json
    {
      "nagari": "string",
      "word": "string",
      "description": "string",
      "category": "string"
    }
    ```

=== "Example response"

    ```json
	{
    	"category": "law",
    	"description": "thief",
    	"nagari": "तायु",
    	"word": "tayu"
  	}
	```

The nouns are categorised into flora, fauna, geography, food, relationships, and more groups. The JSON response contains the word in the Nagari script, the word transliterated into the Roman script, the meaning of the word, and the category the word belongs to.

## Related

-  [Vedic Society API reference](api_vs.md)
-  [Tutorial: Vedic curses](how_to_curse.md)
-  [Dataviz: Word cloud](datavis_wordcloud.md)

<hr/>

{%include 'common/coffee.md'%}