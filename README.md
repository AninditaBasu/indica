# the vedic APIs

These APIs give you two kinds of data: 

- The gods and poets, their categories, and poem meters used in all of the Rig Veda verses
- The descriptions of all the nouns (except proper nouns) mentioned in vedic literature

## How to use

The APIs are available through `GET` calls over `HTTPS`, and return data in `JSON` or `XML`. You can programmatically process the data to make visually appealing or easily consumable information.

To help you get an idea of the kind of data available to you, I've created an interactive demo at https://mybinder.org/repo/AninditaBasu/indica. To run a demo, click an `ipynb` file there. You don't need to clone or download this repo to see the demo :slightly_smiling_face:

Client libraries are in the folders with the `_SDKs` suffix. These SDKs are generated automatically through Swagger and do not work on their own; you need to create an application that will use the SDK to make API calls. To get started, see the `README.md` file in the SDK. If an SDK in the language of your choice is not included here, you can use the `.yaml` files in `_SDKs` folders to generate one through https://editor.swagger.io.

API documentation is at https://aninditabasu.github.io/indica/.

If you build an app with these APIs, please let me know. I'll include your implementation on a Gallery page to showcase it.

## How to contribute

Thank you for wanting to help with this project :heart:

- :bulb: Have an idea for improvement? Open an issue first, and let's talk about it.

- :question: Have a question? See [About this project](https://aninditabasu.github.io/indica/html/about.html), and if your question remains unanswered, open an issue.

- :beetle: Found a bug? Open an issue.

- :tada: Built an app with these APIs? Open an issue to ask it to be showcased in the docs.

We use labels to organize the to-do list; therefore, when opening an issue, tag it with the appropriate label (but please just stick to the ones already on the list; don't create any :smiley:). We'll respond fast (usually within 24 hours).

We'd like all interactions in this repository to follow the [code of conduct](code-of-conduct.md).
