---
title: About the Mahabharat API
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
		gender
		clan FK
		fatherReal
		motherReal
		fatherAdoptive
		motherAdoptive
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
    EVENT }|--|{ PLACE : happens_at
    EVENT ||--|{ JOURNEY : can_contain
    CLAN ||--|{ PLACE : lives_at
    JOURNEY ||--|{ PATH : contains
	JOURNEY ||--|{ PERSON : contains
	JOURNEY ||--|| EVENT : happens_because
    PATH ||--|{ PLACE : passes_through

```
