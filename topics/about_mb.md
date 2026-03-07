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
-  [Index to the Names in the Mahabharata](https://www.sanskrit-lexicon.uni-koeln.de/scans/INMScan/2020/web/index.php)
-  [A Classical Dictionary of Hindu Mythology and Religion (John Dowson)](https://archive.org/details/aclassicaldictio00dowsuoft/page/n28/mode/2up)

The JSON structure of the returned data depends on the endpoint you call and the query parameters (when available) you add to the endpoint. The following entity diagram explains the connections between the various data points.

``` mermaid
erDiagram
  person }|--|{ weapon : has
  person ||--|{ clan : belongs_to
  person ||--|| event : is_killed_at
  event }|--|{ place : happens_at
  event ||--|{ journey : can_contain
  clan ||--|{ place : lives_at
  journey ||--|{ path : contains
  path ||--|{ place : passes_through
```
