---
search:
  exclude: true
---





<h1 class="heading"><span class="name">Back Slash</span> <span class="command">\</span></h1>


## Used as a Function


Monadic Back Slash is not defined

### Dyadic Back Slash means


[Expand](../primitive-functions/expand.md)
```apl

      3 ¯2 4 \ 7 8
7 7 7 0 0 8 8 8 8

      1 0 1 0 1 \ 'Hat'
H a t
```

## Used as an Operator


Back Slash is a Monadic operator with a Dyadic operand

#### Operator Back Slash means


[Scan](../primitive-operators/scan.md)
```apl

      +\ 1 2 3 4 5
1 3 6 10 15

      mat
1  2  3  4
5  6  7  8
9 10 11 12
      
      +\ mat
1  3  6 10
5 11 18 26
9 19 30 42

      +\[1] mat
 1  2  3  4
 6  8 10 12
15 18 21 24

```


[Language Elements](./language-elements.md)


