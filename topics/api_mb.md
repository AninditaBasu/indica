---
title: Mahabharat API reference documentation
description: Endpoints specs, schemas, and parameters for the characters in the Mahabharat, the places associated with them, the events and journeys that they participated in, their family relationships, their battles and deaths, the armours they carried, and more.
summary: Structured data for the people, places, and events in the Mahabharat.

version: v2
status: stable
base_path: /mb/v2

canonical: https://aninditabasu.github.io/indica/topics/api_mb.html

tags:
  - itihasa
  - sanskrit
  - history
  - epic
  - ancient-india
  - api

related:
  - title: Visualising the weapons in Mahabharat and the Harry Potter world
    type: tutorial
    url: /topics/datavis_sankey_mbhp.html

  - title: Visualising the Mahabharat timeline
    type: datavis
    url: /topics/datavis_timeline.html

  - title: Visualising the route map of the Jarasandh episode in the Mahabharat
    type: datavis
    url: /topics/datavis_routemap.html

  - title: About the the Mahabharat API
    type: explanation
    url: /topics/about_mb.html

  - title: Mahabharat API sandbox
    type: openapi
    url: /topics/openapi_mb.html
---

# Mahabharat API reference

<hr/>

This API returns structured data from the Mahabharat. The JSON response contains data about people, places, and events.

---------

**On this page**

* TOC
{:toc}

---------

## Context

An explanation of the connection between the fields of the several endpoints in this API is contained in [About the Mahabharat API](about_mb.md).

## Base URL

`https://indica-1hwj.onrender.com/mb/v2`

The request URL is formed by appending an endpoint to the base URL.

## Methods

Only `GET` calls are supported.

## Status codes

| Code | Explanation |
| ----   | ------------ | 
| 200   | OK               | 
| 404   | Not found   | 
| 429   | Too many requests | 
| 500   | Internal server error |

## Pagination

Response for the following collection endpoints are paginated:

-  `/persons`
-  `/persons/{name}/journeys`
-  `/weapons`
-  `/weapons/{name}/owners`
-  `/events`
-  `/clans`
-  `/journeys`
-  `/places`

The available query parameters are:

| Parameter | Type    | Default | Meaning   |
| --------- | ------- | ------: | ------------- |
| `page`    | integer |     `1` | Page number  |
| `limit`   | integer |    `10` | Number of items on a page (max: 50) |

When a response is paginated, it has the following structure:

```
{
  "meta": {
    "page": 1,
    "limit": 10,
    "total": 125,
    "pages": 13,
    "hasNext": true,
    "hasPrev": false
  },
  "data": []
}
```

## Endpoints

Parameters are path parameters and, optionally, query parameters. To form the request URL, the endpoint must be appended to the base URL.

```bash
request URL = base URL + endpoint
```

For some endpoints, the following query parameters are available.

| Parameter | Values                      | Meaning                  |
| ----------- | ---------------------- | -------------------- |
| `fields`  | `basic` (default) or `details` | Controls returned fields |
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

Query parameters are available for `/persons` and `/persons/{name}`. If `expand` is `true`, full details are given inline for `armour`, `clan`, and `deaths`.

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
  "armour": {
    "panoplies": [],
    "weapons": []
  },
  "clan": {
    "clanAliases": [],
    "clanHome": [
      "forests"
    ],
    "clanInfo": "",
    "clanName": ""
  },
  "death": [
    {
      "personKilledAtEvent": "",
      "personKilledByWhom": [],
      "personKilledHow": "",
      "personKilledWhoAll": [],
      "personName": ""
    }
  ],
  "events": {
    "data": [],
    "meta": {
      "hasNext": false,
      "hasPrev": false,
      "limit": integer,
      "page": integer,
      "pages": integer,
      "total": integer
    }
  },
  "journeys": {
    "data": [],
    "meta": {
      "hasNext": boolean,
      "hasPrev": boolean,
      "limit": integer,
      "page": integer,
      "pages": integer,
      "total": integer
    }
  },
  "person": "",
  "places": []
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

Query parameters are available for both `/events` and `/events/{name}`. If the `expand` query parameter is `true`, `eventPersons` and `eventLocations` contain full details.

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

The query parameter `expand=true` expands `journeyRoute` into full path objects and `journeyPersons` into full person objects.

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
