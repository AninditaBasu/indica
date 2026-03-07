---
title: Mahabharat API reference documentation
---

# Mahabharat API reference

{hr/}

This API fetches information from Mahabharat. The JSON response contains data about people and events.


---------

**On this page**

* TOC
{:toc}

---------

## Context

An explanation of the various endpoints in this API is contained in [About the Mahabharat API](about_mb.md).

## Base URL

`https://indica-1hwj.onrender.com/mb/v1`

The request URL is formed by appending an endpoint to the base URL.

## Methods

Only `GET` calls are supported.

## Endpoints

Parameters are path parameters and, optionally, query parameters. To form the request URL, the endpoint must be appended to the base URL.

```bash
request URL = base URL + endpoint
```

For some endpoints, the following query parameters are available.

| Parameter | Values                      | Meaning                  |
| ----------- | ---------------------- | -------------------- |
| `fields`  | `basic` (default) or `full` | Controls returned fields |
| `expand`  | `true` or  `false`           | Expands related data     |

The following endpoints are available. 

### Helper lists

These endpoints return lists of available entity names, for use in other endpoints.

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | `/persons/names`  | List all person names  |
| GET    | `/weapons/names`  | List all weapon names  |
| GET    | `/clans/names`    | List all clan names    |
| GET    | `/journeys/names` | List all journey names |
| GET    | `/events/names`   | List all event names   |
| GET    | `/places/names`   | List all place names   |

### Persons

| Method | Endpoint                   | Description                         |
| ------ |------------------------|-----------------------------|
| GET    | `/persons`                 | List persons                        |
| GET    | `/persons/{name}`          | Get the details of a specific person     |
| GET    | `/persons/{name}/armour`   | Get the panoply of a specific person |
| GET    | `/persons/{name}/journeys` | Get the journeys that a specific person went on  |

Query parameters are available for `/persons` and `/persons/{name}`. If `expand` is `true`, full details are returned for `armour`, `clan`, and `deaths`.

The response schema is like this:

```
[
  {
    "name": "string",
    "aliases": [
      "string"
    ],
    "shortDesc": "string",
    "gender": "string",
    "clan": "string",
    "fatherReal": "string",
    "motherReal": "string",
    "fatherAdoptive": "string",
    "motherAdoptive": "string",
    "childrenReal": [
      "string"
    ],
    "childrenAdopted": [
      "string"
    ],
    "spouses": [
      "string"
    ],
    "foughtWar": "string",
    "aliveAtWarStart": "string",
    "aliveAtWarEnd": "string",
    "weapons": [
      "string"
    ],
    "longDesc": "string"
  }
]

```

### Explore

| Method | Endpoint               | Description                                               |
| -------- |--------------------|------------------------------------------|
| GET    | `/explore/{name}`  | List all events, journeys, armour, clan, places, deaths connected with the specified person   |

The response schema is like this:

```
{
  "person": "string",
  "clan": {
    "clanName": "string",
    "clanAliases": [
      "string"
    ],
    "clanHome": [
      "string"
    ],
    "clanInfo": "string"
  },
  "armour": {
    "weapons": [
      {
        "weaponName": "string",
        "weaponDescription": "string",
        "weaponAntidote": [
          "string"
        ],
        "weaponHP": "string"
      }
    ],
    "panoplies": [
      {
        "person": "string",
        "chariotBanner": "string",
        "bow": "string",
        "sword": "string",
        "conch": "string",
        "chariotHorses": "string"
      }
    ]
  },
  "events": [
    {
      "eventName": "string",
      "eventPrecededBy": [
        "string"
      ],
      "eventFollowedBy": [
        "string"
      ],
      "eventLocation": [
        "string"
      ],
      "eventDescription": "string",
      "eventPersons": [
        "string"
      ]
    }
  ],
  "journeys": [
    {
      "journeyName": "string",
      "journeyRoute": [
        "string"
      ],
      "journeyPersons": [
        "string"
      ],
      "journeyEvent": "string"
    }
  ],
  "places": [
    "string"
  ],
  "death": [
    {
      "personName": "string",
      "personKilledWhoAll": [
        "string"
      ],
      "personKilledByWhom": [
        "string"
      ],
      "personKilledHow": "string",
      "personKilledAtEvent": "string"
    }
  ]
}
```

### Weapons

| Method | Endpoint                 | Description                        |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/weapons`               | List all weapons                   |
| GET    | `/weapons/{name}`        | Get details of a specific weapon                 |
| GET    | `/weapons/{name}/owners` | List the persons who have the specified weapon |

The response schema is like this:

```
[
  {
    "weaponName": "string",
    "weaponDescription": "string",
    "weaponAntidote": [
      "string"
    ],
    "weaponHP": "string"
  }
]
```

### Events

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/events`        | List all events   |
| GET    | `/events/{name}` | Get the details of a specific event |

If the `expand` query parameter is `true`, `eventPersons` and `eventLocations` contain full details.

The response schema is like this:

```
[
  {
    "eventName": "string",
    "eventPrecededBy": [
      "string"
    ],
    "eventFollowedBy": [
      "string"
    ],
    "eventLocation": [
      "string"
    ],
    "eventDescription": "string",
    "eventPersons": [
      "string"
    ]
  }
]
```

### Clans

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | `/clans`        | List all clans   |
| GET    | `/clans/{name}` | Get the details of a specific clan |

The response schema is like this:

```
[
  {
    "clanName": "string",
    "clanAliases": [
      "string"
    ],
    "clanHome": [
      "string"
    ],
    "clanInfo": "string"
  }
]
```

### Journeys

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | `/journeys`        | List all journeys       |
| GET    | `/journeys/{name}` | Get the details of a specific journey |

In addition to `expand=true`, which expands routes and persons, the following query parameters are also available:

- `person={name}`:  Filter journeys containing the specific person
- `place={place}`: Filter journeys passing through a specific place

The response schema is like this:

```
[
  {
    "journeyName": "string",
    "journeyRoute": [
      "string"
    ],
    "journeyPersons": [
      "string"
    ],
    "journeyEvent": "string"
  }
]
```

### Places

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| GET    | `/places`        | List all places        |
| GET    | `/places/{name}` | Get the details of a specific place |

The response schema is like this:

```
[
  {
    "placeNameEpic": "string",
    "placeAliasEpic": [
      "string"
    ],
    "placeNameHistorical": [
      "string"
    ],
    "placeNameCurrent": [
      "string"
    ],
    "placeCountryCurrent": [
      "string"
    ],
    "placeType": "string",
    "placeInfo": "string"
  }
]
```

## Live sandbox

See [Mahabharat API: Try it out](openapi_mb.md).
