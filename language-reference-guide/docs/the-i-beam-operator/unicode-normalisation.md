<h1 class="heading"><span class="name">Unicode Normalisation</span> <span class="command">R←X(5581⌶)Y</span></h1>

`Y` is any array. `X` is a character scalar or vector describing the form of normalisation required, from the values in the table below.

The result `R` is the same as `Y` except that all character data within it is normalised as specified. Because normalisation can change the length of character encodings, character data in `R` may be of a different shape and/or rank to that in `Y`.

The Unicode character set includes characters that can be formed from single or multiple code points. Some code points or combinations of code points represent the same character - for example, the character `Ç` is defined as a code point in its own right *and* can be formed from the character `C` with a separate combining cedilla. These two representations are *canonically equivalent*. Some code points or combinations of code points more loosely represent the same character - for example, the characters `5` *and* `⁵` (5 superscript) both represent the same numeric digit but are visually distinct. These two have *compatibilly equivalence*. Unicode normalisation is used to transform all equivalent characters to a single representation. For a full explanation of the different normalisation forms, see <https://unicode.org/reports/tr15/>.

|`X`   |Normalisation form|
|------|---|
|`'D'` |Canonical Decomposition
|`'C'` |Canonical Decomposition followed by Canonical Composition
|`'KD'`|Compatibility Decomposition
|`'KC'`|Compatibility Decomposition followed by Canonical Composition

<h2 class="example">Example</h2>
```apl

      COMBINING_CEDILLA←⎕UCS 807
      'C' (5581⌶) 5 '5⁵' ('C' COMBINING_CEDILLA)
┌→───────────┐
│   ┌→─┐ ┌→┐ │
│ 5 │5⁵│ │Ç│ │
│   └──┘ └─┘ │
└∊───────────┘
      'KC' (5581⌶) 5 '5⁵' ('C' COMBINING_CEDILLA)
┌→───────────┐
│   ┌→─┐ ┌→┐ │
│ 5 │55│ │Ç│ │
│   └──┘ └─┘ │
└∊───────────┘
```

!!! warning
    This I-Beam function is expected to be replaced by a system function in the next Dyalog release and that function may not give results of exactly the same shape or rank for non-vector character data.
