<h1 class="heading"><span class="name">Unicode Normalisation</span> <span class="command">R←X(5581⌶)Y</span></h1>

!!! warning
    5581⌶ is temporary functionality – it is expected that it will be replaced by a system function in Dyalog v21.0. The replacement system function might not give results of exactly the same shape or rank for non-vector character data.

`Y` can be any array.

`X` must be a scalar or vector character array describing the form of normalisation required. Possible values are shown in the table below.

The result `R` is the same as `Y` except that all character arrays within `Y` are normalised as specified. This means that, because normalisation can change the length of character encodings, character data in `R` can be of a different shape and/or rank to that in `Y`.

The Unicode character set includes characters that can be formed from single or multiple code points. Some code points or combinations of code points represent the same character. For example, the character `Ç` is defined as a code point in its own right (`U+00C7`, or `⎕UCS 199`), and can be formed from two separate code points – that for the character `C` (`U+0043`, or `⎕UCS 67`) followed by the combining cedilla (`U+0327`, or `⎕UCS 807`). These two representations are _canonically equivalent_. Some code points or combinations of code points more loosely represent the same character. For example, the characters `5` *and* `⁵` (superscript 5) both represent the same numeric digit but are visually distinct. These two have _compatibility equivalence_. Unicode normalisation is used to transform all equivalent text to a single representation. For a full explanation of the different normalisation forms, see [Unicode Standard Annex #15](https://unicode.org/reports/tr15/).

|`X`   |Normalisation form|
|------|---|
|`'D'` |Canonical Decomposition
|`'C'` |Canonical Decomposition followed by Canonical Composition
|`'KD'`|Compatibility Decomposition
|`'KC'`|Compatibility Decomposition followed by Canonical Composition

<h2 class="example">Examples</h2>
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

      'BrandTM'≡'Brand™'
0
      'KD'(5581⌶)'Brand™'
BrandTM
      'BrandTM'≡⍥('KD'∘(5581⌶))'Brand™'
1

```

