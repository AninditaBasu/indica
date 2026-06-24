---
title: Change log of the Indica API
description: Detailed release notes of the three Indica APIs, namely, Rig Veda API, Vedic Society API, and Mahabharat API.
summary: Release notes of the Indica API.

status: stable
canonical: https://aninditabasu.github.io/indica/topics/changelog.html

tags:
  - vedic
  - itihasa
  - sanskrit
  - mythology
  - ancient-india
  - material-culture
  - liturgy
  - lexicon
  - api

related:
  - title: Vedic hymns metadata
    type: explanation
    url: /topics/about_rv.html

  - title: Nouns in the Vedic corpus
    type: explanation
    url: /topics/about_vs.html

  - title: Mahabharat data
    type: explanation
    url: /topics/about_mb.html
---

# Change log

---------

**On this page**

* TOC
{:toc}

---------

## Rig Veda API

-  3.0.0 (June 2026)
    -  Deprecated all parameters of v2.0
	-  Introduced the following path parameters:
	    -  `/mandal/{n}`
	    -  `/mandal/{n}/meters`
	    -  `/mandal/{n}/sungfor`
	    -  `/mandal/{n}/sungby`
	    -  `/sungfor/{god}/mandals`
	    -  `/sungfor/{god}/meters`
	    -  `/sungfor/{god}/sungby`
	    -  `/sungby/{poet}/mandals`
	    -  `/sungby/{poet}/meters`
	    -  `/sungby/{poet}/sungfor`
	    -  `/meters`
	    -  `/sungforcategories`
	    -  `/sungbycategories`
		-  `/hymns`
	    -  `/pairs/{god}/{poet}`
	    -  `/pairs/{godcategory}/{poetcategory}`
	    -  `/monologues`
	    -  `/conversations`
	    -  `/godlist`
	    -  `/poetlist`
	    -  `/meterlist`
	    -  `/godcategorieslist`
	    -  `/poetcategorieslist`
	- Introduced pagination and expansion
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

## Vedic Society API

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

## Mahabharat API

-  2.0.0 (June 2026)
    -  Introduced query parameters for pagination and the number of responses on a page 
-  1.0.0 (February 2026)
    -  First release
