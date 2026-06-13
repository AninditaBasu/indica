---
title: About the the Mahabharat API
description: Query the API for details about the characters in the Mahabharat, the places they lived in, the events and journeys that they participated in, their family relationships, their battles and deaths, the armours they carried, and more.
summary: Structured data for the people, places, and events in the Mahabharat.

version: v2
status: stable
base_path: /mb/v1

canonical: https://aninditabasu.github.io/indica/topics/about_mb.html

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

  - title: Mahabharat API reference documentation
    type: reference
    url: /topics/api_mb.html

  - title: Mahabharat API sandbox
    type: openapi
    url: /topics/openapi_mb.html
---

# About the Mahabharat API

<hr/>

This API contains data from the Mahabharat.

The data is from the following books: 

-  [The Mahabharata of Vyasa (K M Ganguli)](https://archive.org/details/TheMahabharataOfKrishna-dwaipayanaVyasa)
-  [Puranic Encyclopedia (Vettam Mani)](https://www.sanskrit-lexicon.uni-koeln.de/scans/PEScan/2020/web/index.php)
-  [Mahabharata: A Cultural Index (M A Mehendale)](https://www.sanskrit-lexicon.uni-koeln.de/scans/MCIScan/2020/web/index.php)
-  [Index to the Names in the Mahabharata (S. Sorensen)](https://www.sanskrit-lexicon.uni-koeln.de/scans/INMScan/2020/web/index.php)
-  [A Classical Dictionary of Hindu Mythology and Religion (John Dowson)](https://archive.org/details/aclassicaldictio00dowsuoft/page/n28/mode/2up)

The JSON structure of the returned data depends on the endpoint you call and the query parameters (when available) you add to the endpoint. The following entity diagram explains the connections between the various data points.

``` mermaid
erDiagram
    PERSON {
        string name PK
        string_array aliases
        string shortDesc
		string gender
		string clan FK
		string fatherReal
		string motherReal
		string fatherAdoptive
		string motherAdoptive
		string_array childrenReal
		string_array childrenAdopted
		string_array spouses
		yes_no_null foughtWar
		yes_no_null aliveAtWarStart
		yes_no_null aliveAtWarEnd
		string_array weapons FK
		string longDesc
    }

    WEAPON {
        string weaponName PK
        string weaponDescription
        string_array weaponAntidote
        string weaponHP
    }
	
	CLAN {
        string clanName PK
        string_array clanAliases
        string_array clanHome FK
        string clanInfo
    }
	
	EVENT {
        string eventName PK
        string_array eventPrecededBy
        string_array eventFollowedBy
        string eventLocation FK
		string_array eventDescription
		string eventPersons FK
    }
	
	PANOPLY {
        string person PK, FK
        string chariotBanner
        string bow
        string sword
		string conch
		string chariotHorses
    }
	
	DEATH {
        string personName PK, FK
        string_array personKilledWhoAll FK
        string_array personKilledByWhom FK
        string personKilledHow
		string personKilledAtEvent FK
    }
	
	PLACE {
        string placeNameEpic PK
        string_array placeAliasEpic
        string_array placeNameHistorical
		string_array placeNameCurrent
		string_array placeCountryCurrent
        string placeType
		string placeInfo
    }
	
	JOURNEY {
        string journeyName PK
        string_array journeyRoute FK
        string_array journeyPersons FK
		string journeyEvent FK
    }
	
	PATH {
        string pathNameEpic PK, FK
        string_array pathCurrent
    }
    
    PERSON }|--|{ WEAPON : owns
	PERSON ||--|| PANOPLY : has
    PERSON ||--|{ CLAN : belongs_to
    PERSON ||--|| EVENT : is_killed_at
	PERSON ||--|| DEATH : dies
	PERSON }|--|{ JOURNEY : undertakes
    EVENT }|--|{ PLACE : happens_at
    EVENT ||--|{ JOURNEY : can_contain
    CLAN ||--|{ PLACE : lives_at
    JOURNEY ||--|{ PATH : contains
    PATH ||--|{ PLACE : passes_through

```
