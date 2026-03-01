---
title: The Indica APIs
---

# The Indica APIs

---

The Indica APIs give you JSON dictionaries of data from ancient India.

Do we know what life was like in ancient India? That depends. To begin with, `ancient` itself is open to several definitions. And secondly, our knowledge of the past is fragmented. We know about ancient India through its songs and stories, transmitted orally for the most part from one generation to the next.

Indologists have sifted through these oral traditions and compiled scholarly books. But, this treasure chest isn't available in a machine-readable, interoperable form. 

These APIs aim to bridge that gap. The APIs speak in JSON, which is a language notation that's understood by almost all machines today.

- [Rig Veda API](topics/api_rv.md)
- [Vedic Society API](topics/api_vs.md)

## Authentication

Not needed. These are open APIs.

## License

These APIs are distributed under the MIT license. This means you are free to use the data any which way you want, so long as you don't hold me liable and you give me an attribution. See [The MIT License (MIT)](https://opensource.org/licenses/MIT).

All content on this website, unless otherwise stated, is distributed under the Creative Commons license. This means the content is dedicated as-is, without any liability, to the worldwide public domain. See [The Creative Commons Zero v1.0 Universal license](https://wiki.creativecommons.org/wiki/CC0_FAQ).

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

## Coffee chat

{% include admonition.html
   type="note"
   title="Why did you make these APIs?"
   content="Because they weren't there."
%}

{% include admonition.html
   type="tip"
   title="What can I do with this data?"
   content="You can process the data to make visually appealing or easily consumable information. See the example visualisations."
%}

{% include admonition.html
   type="note"
   title="What is the source of this data?"
   content="See [About the Rig Veda API](topics/about_rv.md) and [About the Vedic Society API](topics/about_vs.md)."
%}

{% include admonition.html
   type="warning"
   title="I found an error in the data."
   content="Please log an issue in the [GitHub repository](https://github.com/AninditaBasu/indica)."
%}

{% include admonition.html
   type="note"
   title="And you are...?"
   content="[Anindita Basu](https://x.com/anindita_basu)."
%}

-----------

![logo](images/logo.png)