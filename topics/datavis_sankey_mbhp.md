---
title: Visualising the weapons in Mahabharat and the Harry Potter world through a Sankey diagram
description: Draw a Sankey diagram after querying the API for the relationship between the weapons in the Mahabharat and Potterworld.
summary: Tutorial for building a datavis of Mahabharat and Potterworld weapons.

config:
  sankey:
    showValues: false

version: v2
status: stable
base_path: /mb/v1

canonical: https://aninditabasu.github.io/indica/topics/datavis_sankey_mbhp.html

tags:
  - itihasa
  - sanskrit
  - history
  - epic
  - ancient-india
  - api

related:
  - title: Visualising the route taken in the Jarasandh episode in the Mahabharat
    type: tutorial
    url: /topics/datavis_routemap.html

  - title: Visualising the Mahabharat timeline
    type: datavis
    url: /topics/datavis_timeline.html
	
  - title: About the Mahabharat API
    type: explanation
    url: /topics/about_mb.html

  - title: Mahabharat API reference documentation
    type: reference
    url: /topics/api_mb.html

  - title: Mahabharat API sandbox
    type: openapi
    url: /topics/openapi_mb.html
---

# Sankey diagram: Mahabharat weapons in Potterworld

<hr/>

This diagram is generated from the data returned by `/mb/v1/weapons`.

```mermaid
sankey-beta
Mahabharat,Potterworld,Value
Adityastra,Hot-air charm,1
Agneyastra,Incendio,1
Antardhan,Disillusionment charm,1
Bhargavastra,Incendio,1
Bhaskarastra,Lumos,1
Brahmashir,Avada kedavra,1
Brahmastra,Incendio,1
Jyotish,Lumos,1
Nag,Locomotor Mortis,1
Narayanastra,FiendFyre curse,1
Paash,Petrificus Totalus,1
Parjanyastra,Aguamenti,1
Pragnyastra,Rennervate,1
Pramohanastra,Stupefy,1
Sahasraghni,Sectumsempra,1
Salilastra,Aguamenti,1
Sammohan,Stupefy,1
Saurastra,Incendio,1
Shakti,Avada kedavra,1
Sudarshan chakra,Avada kedavra,1
Tvashtr,Polyjuice potion,1
Vaishnavastra,Avada kedavra,1
Vajra,Duro,1
Varunastra,Aguamenti,1
Vayavyastra,Deprimo,1
Vishoshan,Hot-air charm,1
```

