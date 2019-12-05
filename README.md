# the Indica APIs

At the moment, two APIs are available: 

- `rv`: Data about the gods and poets, their categories, and poem meters used in all of the Rig Veda verses
- `vs`: A descriptions of all the nouns  mentioned in vedic literature (proper nouns aren't included, though)

To help you get an idea of the kind of data available to you, see an interactive demo at https://mybinder.org/repo/AninditaBasu/indica. To run a demo, click an `ipynb` file there. You don't need to clone or download this repo to see the demo :slightly_smiling_face:

## How to use

API documentation is at https://aninditabasu.github.io/indica/.

The APIs are available through `GET` calls over `HTTPS`, and return data in `JSON` or `XML`. You can programmatically process the data to make visually appealing or easily consumable information.

Client libraries are in the folders with the `_SDKs` suffix. These SDKs are generated automatically through Swagger and do not work on their own; you need to create an application that will use the SDK to make API calls. To get started, see the `README.md` file in the SDK. If an SDK in the language of your choice is not included here, you can use the `.yaml` files in `_SDKs` folders to generate one through https://editor.swagger.io.

> If you build an app with these APIs, please let me know. I'll include your implementation on a Gallery page in the documentation, and also include it under `Showcase` on this page.

## Showcase

- Rough-and-ready Vedic Career Advice app (`tarzezindagi.py`) 
  
  ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/flask) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/gunicorn) ![GitHub Pipenv locked dependency version](https://img.shields.io/github/pipenv/locked/dependency-version/AninditaBasu/indica/requests) 

  See [https://pesha.herokuapp.com/](https://pesha.herokuapp.com/). 

- Your app goes here...

## How to contribute

Thank you for wanting to help with this project :heart:

- :bulb: Have an idea for improvement? Open an issue first, and let's talk about it.

- :question: Have a question? See [About this project](https://aninditabasu.github.io/indica/html/about.html), and if your question remains unanswered, open an issue.

- :beetle: Found a bug? Open an issue.

- :tada: Built an app with these APIs? Open an issue to ask it to be showcased in the docs.

The to-do list is organised through labels; therefore, when opening an issue, tag it with the appropriate label (but please just stick to the ones already on the list; don't create any :smiley:).

All interactions in this repository are supposed to follow the [code of conduct](code-of-conduct.md), please.

## Plans

- [ ] Turn the edicts of Asoka into an API
- [ ] Turn the Arthashastra into an API
- [ ] Shall we do a [Mahabharat API](https://dev.to/aninditabasu/building-a-chatbot-with-the-ramp-stack-part-2-designing-the-database-131e) as well?
