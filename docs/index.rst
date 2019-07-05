.. toctree::

   Home <the Vedic APIs>
   Endpoints
   Resources

the Vedic APIs
==============

Two APIs are available:

- rv (rig veda), for the gods, poets, and poem meters in the Rig Veda
- vs (vedic society), for a descriptions of the nouns in vedic literature

These are open APIs. No authentication is needed.

The APIs are distributed under the MIT license. This means you are free to use the data any which way you want, so long as you don't hold me liable and you give me an attribution. See `The MIT License (MIT) <https://opensource.org/licenses/MIT>`_.

Endpoints
-----------------

JSON output is returned by the following endpoints:

- ``https://sheetlabs.com/IND/rv``, for gods, poets, and meters.
- ``https://sheetlabs.com/IND/vs``, for descriptions of nouns.

To get output in the XML format, append .xml to the endpoint, like this: ``https://sheetlabs.com/IND/rv.xml``.

Resources
-----------------

The following resources are available:

- rv: ``mandal``, ``sukta``, ``sungby``, ``sungbycategory``, ``sungfor``, ``sungforcategory``, and ``meter``
- vs: ``word``, ``nagari``, ``description``, and ``category``

The mandals and suktas of the ``rv`` API are integers; the remaining parameters of the ``rv`` API and all of the parameters of the ``vs`` API are strings.
