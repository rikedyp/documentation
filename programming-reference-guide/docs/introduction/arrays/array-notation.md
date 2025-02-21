<h1 class="heading"><span class="name">Array Notation</span></h1>


Array notation extends [vector notation](vector-notation.md) to define arrays of higher rank, and namespaces, and lets these definitions span multiple lines:

-   **Parentheses** embrace vector literals and namespace name-value pairs
-   **Square brackets** embrace higher-rank arrays
-   **Diamonds** and **linebreaks** separate array elements and name-value pairs

Some examples show how these work.


## Ordered Arrays

Ordered arrays are indexed by position, as in `vec[3]` or `mat[2 4;5]`.


### Nested Vector { .example }

```apl
      ⍴z← (0 6 1 8 ⋄ 2*0 2 0 2 1
      2 7 1 8 2 8 ⋄ 3 1 4 1 5)
4
      z
┌───────┬─────────┬───────────┬─────────┐
│0 6 1 8│1 4 1 4 2│2 7 1 8 2 8│3 1 4 1 5│
└───────┴─────────┴───────────┴─────────┘
      ('Three'
       'Blind'
       'Mice')
┌─────┬─────┬────┐
│Three│Blind│Mice│
└─────┴─────┴────┘
```

### Matrix { .example }

```apl
      ⍴m←[0 6 1 8 ⋄ 1 4 1 4
       2 7 1 8 ⋄ 3 1 4 2]
4 4
      m
0 6 1 8
1 4 1 4
2 7 1 8
3 1 4 2

      ⍝ short elements are filled
      ⍴mice←['Three'
             'Blind'
             'Mice']
3 5
      mice,'|'
Three|
Blind|
Mice |

      ⍴RC←[0 'OK'
           1 'WS FULL'
           2 'SYNTAX ERROR'
           3 'INDEX ERROR'
           4 'RANK ERROR']
5 2
```

### Column Matrix { .example }

```apl
      (,⊂'Three') ≡ ('Three' ⋄)
1
      ⍴¨cm3←[('Three' ⋄)
             ('Blind' ⋄)
             ('Mice'  ⋄)]
5
5
4
      cm3
┌─────┐
│Three│
├─────┤
│Blind│
├─────┤
│Mice │
└─────┘
```

### Rank-3 Array { .example }

```apl
      ⍴block←[
       [3 1 4 ⋄ 1 5 ]
       [2 7 0 ⋄ 2]
      ]
2 2 3
      block
3 1 4
1 5 0

2 7 0
2 0 0

```


## Namespaces

Namespaces can be thought of as ‘semantic arrays’ (or dictionaries, or objects): unordered, and indexed by names rather than positions.

Array notation allows you to write a namespace literal as zero or more name-value pairs, embraced by parentheses.

```apl
      mt←()              ⍝ empty namespace
      ()()()             ⍝ vector of empty namespaces
      ( () ⋄ () ⋄ () )   ⍝ vector of empty namespaces
      n←(x:'hello')      ⍝ n.x is vector

      (x:['hello'        ⍝ n.x is matrix
        'world'])

      (y:(x:'hello'))    ⍝ nested namespaces

      (
        FirstName:'Wolfgang'
        LastName:'Mozart'
        Age:35
      )
```

### Scoping In Namespace Literals

Array and namespace literals can include value expressions.

```apl
      LUE←(answer:7×6)   ⍝ Life, the Universe, and Everything
```

Any assignments (made with `←`) in a value expression are made *in the scope around the namespace*, and persist there.

```apl
      long←'bobby'
      short←'jack'
      ns←(short:'jill' ⋄ inner:short∘.=short←3↑long)
      ns.inner
1 0 1
0 1 0
1 0 1
      short     ⍝ altered by inner assignment
bob
      ns.short  ⍝ unaffected by inner assignment
jill
```

## Specification

The new syntactic constructs were previously errors in every mainstream APL implementation and therefore introduce no backward incompatibilities.

### Broken Parentheses And Square Brackets

*Broken* here means interrupted by one or more statement separators (diamonds `⋄` or line breaks).

Statement separators encapsulated in a dfn or further contained in array notation do not break a parenthesis or bracket.
For example, in

    ({1=⍵:'y' ⋄ 'n'}?2)

the diamond is part of the dfn and does not break the surrounding parenthesis.


### Empty Round Parentheses

Empty round parentheses `()` create an empty namespace, equivalent to `⎕NS⍬`.

### Broken Round Parentheses

A broken round parenthesis creates a

-   **namespace** if it encapsulates a list of name-value pairs: each pair defines a member of the namespace
-   **vector** if it encapsulates a list of value expressions; the result of each is an element in the vector


A *name-value pair* is a valid APL identifier followed by a colon and a value expression.

!!! warning "Mixing name-value pairs and value expressions is a syntax error."

### Broken Square Brackets

A broken square bracket creates an **array** where the result of each value expression forms a major cell (equivalent to Mix applied to a vector of these), with scalars interpreted as one-element vectors.



### Formal Syntax

The array notation can be described using Extended Backus–Naur form, where `expression` is any traditional APL expression:

    value ::= expression | list | block | space
    list  ::= '(' ( ( value sep )+ value? | ( sep value )+ sep? ) ')'
    block ::= '[' ( ( value sep )+ value? | ( sep value )+ sep? ) ']'
    space ::= '(' sep? ( name ':' value ( sep name ':' value )* )? sep? ')'
    sep   ::= [⋄#x000A#x000D#x0085]+


![Syntax diagram](/img/array-notation-syntax.png)
<!-- Eventually replace weith Mermaid diagram. -->

!!! note "Sep values"

    The list of `sep` values is for illustration purposes and is to match the line breaks recognised by the APL implementation. However, these three values should be handled when reading Unicode text files.
