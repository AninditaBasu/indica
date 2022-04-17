---
title: The Indica APIs
---

# Indica APIs

Data from ancient India, presented as JSON dictionaries.

=== "Available :material-check-underline:"

    - [Rig Veda API](api_rv.md)
	- [Vedic Society API](api_vs.md)

=== "In the works :material-playlist-edit:"

    - Mahabharat API: [An MVP](https://mb-verse.herokuapp.com/) is up but not the API yet

=== "On the roadmap :material-list-status:"

    - Arthashashtra API
	- Ashokan edicts API

You can programmatically process the data to make visually appealing or easily consumable information (see [Examples](examples.md)).

## Authentication

Not needed. These are open APIs.

!!! danger "Timeout"

    These APIs are offline every night between 9:00 PM IST and 9:00 AM IST.

## License

These APIs are distributed under the MIT license. This means you are free to use the data any which way you want, so long as you don't hold me liable and you give me an attribution. See [The MIT License (MIT)](https://opensource.org/licenses/MIT).

All content on this website, unless otherwise stated, is distributed under the Creative Commons license. This means the content is dedicated as-is, without any liability. to the worldwide public domain. See [The Creative Commons Zero v1.0 Universal license](https://wiki.creativecommons.org/wiki/CC0_FAQ).

## Rate limits

The APIs are hosted on Heroku, where I have a limit of 500 hours a month. This limit includes all my apps hosted on Heroku (I have apps there besides these APIs). I am neither tracking who makes how many calls to the APIs nor throttling calls on IP-address basis. My only request is, call these APIs in a fair manner so that I have some hours always available to run my other projects.

!!! note "Heavy use"

    If you need to use the APIs rather heavily, please let me know. I'll generate for you a free token, which will give you access to an authenticated hosting service that I also use. This authenticated service has rate limits of 10,000 API calls a month.

## Release history

=== "Rig Veda API"

    -  1.2 (December 2020)
	    -  Changed the endpoint to `https://api-rv.herokuapp.com/rv/v1`
	-  1.1 (October 2018)
	    - Changed the endpoint from `https://sheetlabs.com/RV/` to `https://sheetlabs.com/IND/`
		-  Added the following two parameters: `sungbycategory` and `sungforcategory`
	-  1.0 (August 2018)
	    -  First release

=== "Vedic Society API"

    -  1.2 (December 2020)
	    -  Changed the endpoint to `https://api-vs.herokuapp.com/vs/v1`
	-  1.1 (October 2018)
	    - Changed the endpoint from `https://sheetlabs.com/RV/` to `https://sheetlabs.com/IND/`
	-  1.0 (August 2018)
	    -  First release

## Coffee chat

Why did you make these APIs?

:   Because they weren't there.

What can I do with this data?

:   You can make a [fun career advice app](https://github.com/AninditaBasu/indica/blob/master/tarzezindagi.py) or [do a fictional take on the life of a child in vedic times](https://life-ancient-india.herokuapp.com/). Some more use cases are at [Examples](examples.md).

    Also, I'll be very happy to link back to your implementation or app if you send me a URL.

What is the source of this data?

:   Vedic literature comprises the four Vedas (Rig, Saam, Yajur, Atharv). Each Veda is a set of these things:

    -  Samhitas: Hymns or songs to gods
	-  Brahmanas: Instructions on rituals
	-  Upanishads: Philosophical discourses.
	
	For the APIs, the following books were consulted:
	
	-  Main sources:
	    -  Rig Veda Samhita, the English translation according to H. H. Wilson and the Bhashya of Sayanacharya, by Ravi Prakash Arya and K. L. Joshi (Volumes 1 through 4)
	    -  Vedic Index of Names and Subjects, by A. A. Macdonell and A. B. Keith ([Volume 1](https://archive.org/details/in.ernet.dli.2015.284764) and [2](https://archive.org/details/in.ernet.dli.2015.211118))
	-  Additional sources:
	    -  [Vedic Mythology, by A. A. Macdonell](https://archive.org/details/MacdonellArthurVedicMythology1897216P.Scan)
	    -  [The Nighantu and the Nirukta of Sri Yaskacharya, by Lakshman Sarup](https://archive.org/details/nighantuniruktao00yaskuoft)
	    -  [The Practical Sanskrit-English Dictionary, by V. S. Apte](https://dsalsrv04.uchicago.edu/dictionaries/apte/)

I found an error in the data.

:   Please log a [GitHub issue](https://github.com/AninditaBasu/indica/issues).

And you are...?

:   [Anindita Basu](https://twitter.com/@anindita_basu).

<hr/>

<a href="https://whimsy.myinstamojo.com/product/480613/coffee-ddbc0/" data-store-name="whimsy" data-domain="https://whimsy.myinstamojo.com" data-id="480613" rel="im-new-checkout" data-text="Like this API? Buy me a coffee." data-css-style="background:#1273de; color:#ffffff; width:300px; border-radius:30px" data-layout="vertical"></a>
<script src="https://manage.instamojo.com/assets/js/pay_button/button.min.js"></script>