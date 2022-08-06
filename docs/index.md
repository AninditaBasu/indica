---
title: The Indica APIs
description: JSON dictionaries of data from ancient India. Includes metadata of all the verses in Rig Veda (rishis, gods, chhandas) and a description of all nouns in vedic literature (including the flora, fauna, geography, food, relationships, and objects).
author: Anindita Basu
og_title: The Indica APIs
og_description: JSON dictionaries of data from ancient India. Includes metadata of all the verses in Rig Veda (rishis, gods, chhandas) and a description of all nouns in vedic literature (including the flora, fauna, geography, food, relationships, and objects).
og_image: images/signboard.png
---

# Indica APIs

<hr/>

The Indica APIs give you JSON dictionaries of data from ancient India.

Do we know what life was like in ancient India? That depends. To begin with, `ancient` itself is open to several definitions. And secondly, our knowledge of the past is fragmented. We know about ancient India through its songs and stories, transmitted orally for the most part from one generation to the next.

Indologists have sifted through these oral traditions and compiled scholarly books on ancient India. But, this treasure chest isn't available in a machine-readable, interoperable form. 

These APIs aim to bridge that gap. The APIs speak in JSON, which is a language notation that's understood by almost all machines today.

=== "Available :material-check-underline:"

    - [Rig Veda API](api_rv.md)
	- [Vedic Society API](api_vs.md)

=== "In the works :material-playlist-edit:"

    - Mahabharat API: A [query service](https://mahabharat.onrender.com) is up but not the API yet.

=== "On the roadmap :material-list-status:"

    - Arthashashtra API
	- Ashokan edicts API

!!! danger "Timeout"

    These APIs are offline every night between 9:00 PM IST and 9:00 AM IST.

## Authentication

Not needed. These are open APIs.

## License

These APIs are distributed under the MIT license. This means you are free to use the data any which way you want, so long as you don't hold me liable and you give me an attribution. See [The MIT License (MIT)](https://opensource.org/licenses/MIT).

All content on this website, unless otherwise stated, is distributed under the Creative Commons license. This means the content is dedicated as-is, without any liability, to the worldwide public domain. See [The Creative Commons Zero v1.0 Universal license](https://wiki.creativecommons.org/wiki/CC0_FAQ).

## Rate limits

The APIs are hosted on Heroku, where I have a limit of 500 hours a month. This limit includes all my apps hosted on Heroku (I have other apps there besides these APIs). I am neither tracking who makes how many calls to the APIs nor throttling calls on IP-address basis. My only request is, call these APIs in a fair manner so that I have some hours always available to run my other projects.

!!! note "Heavy use"

    If you need to use the APIs rather heavily, please let me know. I'll generate for you a free token, which will give you access to an authenticated hosting service that I also use. This authenticated service has a rate limit of 10,000 API calls a month for free accounts.

## Release history

=== "Rig Veda API"

    -  2.0 (July 2022)
	    -  Deprecated all query parameters
		-  Introduced the following path parameters:
		    -  `/book/{mandal}`
		    -  `/meter/{meter}`
		    -  `/poet/{sungby}`
		    -  `/poetcategory/{poetcategory}`
		    -  `/god/{sungfor}`
		    -  `/god/{sungfor}/{mandal}`
		    -  `/godbypoet/{sungfor}/{sungby}`
		    -  `/godcategory/{sungforcategory}`
			-  `/godcategorybypoetcategory/{sungforcategory}/{sungbycategory}`
		-  Changed the endpoint to `https://api-rv.herokuapp.com/rv/v2/meta/`
	-  1.2 (December 2020)
	    -  Changed the endpoint to `https://api-rv.herokuapp.com/rv/v1`
	-  1.1 (October 2018)
	    - Changed the endpoint from `https://sheetlabs.com/RV/` to `https://sheetlabs.com/IND/`
		-  Added the following two parameters: `sungbycategory` and `sungforcategory`
	-  1.0 (August 2018)
	    -  First release

=== "Vedic Society API"

    -  2.0 (July 2022)
	    -  Deprecated all query parameters
		-  Introduced the following path parameters:
		    -  `/words/{word}`
			-  `/descriptions/{description}`
			-  `/categories/{category}`
		-  Changed the endpoint to `https://api-vs.herokuapp.com/vs/v2/`
    -  1.2 (December 2020)
	    -  Changed the endpoint to `https://api-vs.herokuapp.com/vs/v1`
	-  1.1 (October 2018)
	    - Changed the endpoint from `https://sheetlabs.com/RV/` to `https://sheetlabs.com/IND/`
	-  1.0 (August 2018)
	    -  First release

=== "Mahabharat query service"

    - Beta (April 2020)

## Coffee chat :material-coffee:

??? question "Why did you make these APIs?"

    Because they weren't there.

??? question "What can I do with this data?"

    You can process the data to make visually appealing or easily consumable information. See [How-tos and graphics](tags.md).

    Also, I'll be very happy to link back to your implementation or app if you send me a URL.

??? question "What is the source of this data?"

    See [About these APIs](about_mb.md).

??? warning "I found an error in the data."

    Please log an issue in these GitHub repositories:
	
    - [Rig Veda API and Vedic Society API](https://github.com/AninditaBasu/indica/issues)
	- [Mahabharat query service](https://github.com/AninditaBasu/calm-wildwood/issues)

??? info "And you are...?"

    [Anindita Basu](https://twitter.com/@anindita_basu).

<hr/>

{%include 'common/coffee.md'%}