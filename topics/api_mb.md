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

The following endpoints are available. 

## Helper lists

These return lists of available entity names.

| Method | Endpoint          | Description            |
| ------ | ----------------- | ---------------------- |
| GET    | `/persons/names`  | List all person names  |
| GET    | `/weapons/names`  | List all weapon names  |
| GET    | `/clans/names`    | List all clan names    |
| GET    | `/journeys/names` | List all journey names |
| GET    | `/events/names`   | List all event names   |
| GET    | `/places/names`   | List all place names   |

## Persons

| Method | Endpoint                   | Description                         |
| ------ |------------------------|-----------------------------|
| GET    | `/persons`                 | List persons                        |
| GET    | `/persons/{name}`          | Get the details of a specific person     |
| GET    | `/persons/{name}/armour`   | Get the panoply of a specific person |
| GET    | `/persons/{name}/journeys` | Get the journeys that a specific person went on  |

Query parameters are available for `/persons` and `/persons/{name}`:

| Parameter | Values                      | Meaning                  |
| ----------- | ---------------------- | -------------------- |
| `fields`  | `basic` (default) or `full` | Controls returned fields |
| `expand`  | `true` or  `false`           | Expands related data     |

If `expand` is `true`, full details are returned for `armour`, `clan`, and `deaths`.

## Explore

| Method | Endpoint               | Description                                               |
| -------- |--------------------|------------------------------------------|
| GET    | `/explore/{name}`  | List all events, journeys, armour, clan, places, deaths connected with the specified person   |

## Weapons

| Method | Endpoint                 | Description                        |
| ------ | ------------------------ | ---------------------------------- |
| GET    | `/weapons`               | List all weapons                   |
| GET    | `/weapons/{name}`        | Get details of a specific weapon                 |
| GET    | `/weapons/{name}/owners` | List the persons who have the specified weapon |

## Events

| Method | Endpoint         | Description       |
| ------ | ---------------- | ----------------- |
| GET    | `/events`        | List all events   |
| GET    | `/events/{name}` | Get the details of a specific event |

The following query parameters are available:

| Parameter | Values                      | Meaning                  |
| ----------- | ---------------------- | -------------------- |
| `fields`  | `basic` (default) or `full` | Controls returned fields |
| `expand`  | `true` or  `false`           | Expands related data     |

If `expand` is `true`, `eventPersons` and `eventLocations` contain full details.

## Clans

| Method | Endpoint        | Description      |
| ------ | --------------- | ---------------- |
| GET    | `/clans`        | List all clans   |
| GET    | `/clans/{name}` | Get the details of a specific clan |

## Journeys

| Method | Endpoint           | Description         |
| ------ | ------------------ | ------------------- |
| GET    | `/journeys`        | List all journeys       |
| GET    | `/journeys/{name}` | Get the details of a specific journey |

The following query parameters are available:

| Parameter       | Description                             |
| --------------- | --------------------------------------- |
| `expand=true`   | Expand route + persons                  |
| `person={name}` | Filter journeys containing a person     |
| `place={place}` | Filter journeys passing through a place |

## Places

| Method | Endpoint         | Description            |
| ------ | ---------------- | ---------------------- |
| GET    | `/places`        | List all places        |
| GET    | `/places/{name}` | Get the details of a specific place |


## Live sandbox

See [Mahabharat API: Try it out](openapi_mb.md).
