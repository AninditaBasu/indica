---
title: The Indica APIs
---

# The Indica APIs

---

The Indica APIs give you JSON dictionaries of data from ancient India.

Do we know what life was like in ancient India? That depends. To begin with, `ancient` itself is open to several definitions. And secondly, our knowledge of the past is fragmented. We know about ancient India through its songs and stories, transmitted orally for the most part from one generation to the next.

Indologists have sifted through these oral traditions and compiled scholarly books. But, this treasure chest isn't available in a machine-readable, interoperable form. 

These APIs aim to bridge that gap. The APIs speak in JSON, which is a language notation that's understood by almost all machines today.

---------

**On this page**

* TOC
{:toc}

---------

## Authentication

Not needed. These are open APIs.

## License

These APIs are distributed under the [MIT license](https://opensource.org/licenses/MIT).

All content on this website, unless otherwise stated, is distributed under the [Creative Commons (CC-BY-4.0) license](https://creativecommons.org/licenses/by/4.0/).

## Rate limits

The APIs are hosted on the free tier of Render, which has hourly limits. I am neither tracking who makes how many calls to the APIs nor throttling calls on IP-address basis. My only request is, call these APIs in a fair manner so that I have some hours always available to run my other projects.

## Release history

### Rig Veda API

-  2.0.1 (February 2026)
    -  Changed the endpoint to `https://indica-1hwj.onrender.com/rv/v2/meta`
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

### Vedic Society API

-  2.0.1 (February 2026)
    -  Changed the endpoint to `https://indica-1hwj.onrender.com/vs/v2`    
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

### Mahabharat API

-  1.0.0 (February 2026)
    -  First release

## Coffee chat

Why did you make these APIs?
: Because they weren't there.

What can I do with this data?
: You can process the data to make visually appealing or easily consumable information. See the example visualisations.

What is the source of this data?
: See [About the Rig Veda API](topics/about_rv.md), [About the Vedic Society API](topics/about_vs.md), and [About the Mahabharat API](topics/about_mb.md).

I found an error in the data.
: Please log an issue in the [GitHub repository](https://github.com/AninditaBasu/indica).

And you are...?
: [Anindita Basu](https://x.com/anindita_basu).

