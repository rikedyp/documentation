<h1 class="heading"><span class="name">UUID Generator</span> <span class="command">R←120⌶Y</span></h1>

This function generates a UUID (Universally Unique IDentifier) according to the [RFC 9562](https://datatracker.ietf.org/doc/html/rfc9562) specification. 

`Y` specifies the UUID Version required, from the table below. The result `R` is a vector containing the generated 36-character UUID.

|Version|Description|
|---|--------------------------------------|
| 4 | Randomly or pseudorandomly generated |
| 7 | Unix Epoch time-based                |

Other values are either unsupported, undefined or reserved.

UUIDs are also known as GUIDs (Globally Unique IDentifiers); the terms are equivalent.

<h2 class="example">Example</h2>
```apl
      120⌶4
32cd549f-eb33-4457-bf45-babf26dc2b53
```
