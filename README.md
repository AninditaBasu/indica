# the Indica APIs

As of now, the following two APIs are available: 

- `rv`: Data about the gods and poets, their categories, and poem meters used in all of the Rig Veda verses
- `vs`: A descriptions of all the nouns  mentioned in vedic literature (proper nouns aren't included, though)

<hr/>

## Contents
-  [Documentaion](#documentation)
-  [How to use](#how-to-use)
-  [Showcase](#showcase)
-  [How to contribute](#how-to-contribute)
-  [Resources](#resources)
-  [Plans](#plans-for-indica)

<hr/>

## Documentation

API reference documentation is at:

- [rv YAML](https://raw.githack.com/AninditaBasu/indica/master/rv_SDKs/rv_redoc.html)
- [vs YAML](https://raw.githack.com/AninditaBasu/indica/master/vs_SDKs/vs_redoc.html)

Detailed documentation is at [Indica documentation](https://aninditabasu.github.io/indica/). 

## How to use

The APIs are openly available through `GET` calls over `HTTPS`, and return data in the `JSON` format. You can programmatically process the data to make visually appealing or easily consumable information.

For an interactive demo, use the `.ipynb` files in this repo. Or, use these gists that you can open with Google Colab and use interactively:

-  [gist for rv](https://gist.github.com/AninditaBasu/e7baf92b307a8d125243350fc02eafa9)
-  [gist for vs](https://gist.github.com/AninditaBasu/d6107cb10fdb385baad09db497dba4a7)

> If you build an app with these APIs, please let me know. I'll include your implementation on a `Gallery` page in the documentation, and also include it under `Showcase` on this page.

What can you do with this data, you ask? This repo contains the code for two sample apps:

- `tarzezindagi.py`, a fun app for vedic career advice. Clone this repo and run the code locally to see the app in function (I ran out of free Heroku hours to host it).
- `life.py`, an app that introduces a fictional child from the vedic times. Here's a Heroku-hosted version as [Life in ancient India](https://life-ancient-india.herokuapp.com/).
 
Am sure you'll have your own ideas as well. 

## Showcase

- [Vedic Career Advice](tarzezindagi.py)  ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/flask) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/gunicorn) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/requests)
- [Intro by an ancient child](life.py) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/flask) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/gunicorn) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/requests)
- _...Link to your app or implementation goes here..._

## How to contribute

Thank you for wanting to help with this project :heart:

- :bulb: Have an idea for improvement? Open an issue, and let's talk about it.

- :question: Have a question? See [About this project](https://aninditabasu.github.io/indica/html/about.html), and if your question remains unanswered, open an issue.

- :beetle: Found a bug? Open an issue.

- :tada: Built an app with these APIs? Open an issue to ask it to be showcased in the docs.

The to-do list is organised through labels; therefore, when opening an issue, tag it with the appropriate label (but please just stick to the ones already on the list; don't create any more :smiley:).

All interactions in this repository are supposed to follow the [code of conduct](code-of-conduct.md), please.

## Resources

Client libraries are in the folders with the `_SDKs` suffix. These SDKs are generated automatically through Swagger and do not work on their own; you need to create an application that will use the SDK to make API calls. To get started, see the `README.md` file in the SDK. If an SDK in the language of your choice is not included here, you can use the `.yaml` files in `_SDKs` folders to generate one through https://editor.swagger.io.

If something doesn't work or is broken, it might be that I didn't update it. The latest documentation is at [Indica](https://aninditabasu.github.io/indica/); head over there and RTFM?

## Plans for Indica

- [ ] Turn the edicts of Asoka into an API
- [ ] Turn the Arthashastra into an API
- [ ] Shall we do a Mahabharat API as well? An info-bot is up at [MBverse](https://mb-verse.herokuapp.com/) but the API is yet to be built.