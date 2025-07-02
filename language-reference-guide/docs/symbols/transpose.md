---
search:
  exclude: true
---
<h1 class="heading"><span class="name">Circle Backslash</span> <span class="command">⍉</span></h1>

Monadic Transpose means
[Transpose](../primitive-functions/transpose-monadic.md)
```apl
      mat
1 2 3
4 5 6

      ⍉ mat
1 4
2 5
3 6
```

Dyadic Transpose means
[Dyadic Transpose](../primitive-functions/transpose-dyadic.md)
```apl
      2 1 ⍉ mat
1 4
2 5
3 6
      1 1 ⍉ mat     ⍝ leading diagonal
1 5
```
[Language Elements](./language-elements.md)


