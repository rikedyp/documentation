<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FTIE FTIE
</div>






<h1 class="heading"><span class="name">Exclusive File Tie</span> <span class="command">{R}←X ⎕FTIE Y</span></h1>


## Access code 2


`Y` must be 0 or a simple 1 or 2 element integer vector containing an available file tie number to be associated with the file for further file operations, and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The tie number must not already be associated with a share tied or exclusively tied file.


`X` must be a simple character scalar or vector which specifies the name of the file to be exclusively tied.  The file must be named in accordance with the operating system's conventions, and may be a relative or absolute pathname. If no file extension is supplied, the set of extensions specified by the  **CFEXT** parameter are tried one after another until the file is found or the set of extensions is exhausted. See [ CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).


The file must exist and  the user must have write access to it.  It may not already be tied by another user.



## Automatic Tie Number Allocation


A tie number of 0 as argument to a create, share tie or exclusive tie operation, allocates the first (closest to zero) available tie number, and returns it as an explicit result. This allows you to simplify code. For example:


from:
```apl
      tie←1+⌈/0,⎕FNUMS ⍝ With next available number,
      file ⎕FTIE tie   ⍝ ... tie file.
```


to:
```apl
      tie←file ⎕FTIE 0 ⍝ Tie with first available number.
```



The shy result of `⎕FTIE` is the tie number of the file.

<h2 class="example">Examples</h2>
```apl
      'SALES' ⎕FTIE 1
 
      '../budget/COSTS' ⎕FTIE  2
 
      '../budget/expenses' ⎕FTIE 0
3
```
# Variant Options
## Mode

The Mode variant option can be used to specify that the file being tied will only be read, or must be writable.

Writing to a component file is not always permitted - for example:

* The operating system permissions may not allow it.
* The file properties may not allow it.

By default, the mode specifies that the file should be tied as permitted (`P`) - for write access if possible, but a file that is only readable will be tied for read access only, and any subsequent attempt to write to it will fail.

If read mode (`R`) is specified the file will always be tied for read access and any subsequent attempt to write to it will fail.

If write mode (`W`) is specified, a file that is not writable will fail to tie.

Mode is independent of any file access controls managed using an access matrix.

<h3 class="example">Example</h3>

```apl
      'cf' (⎕FSTIE⍠'Mode' 'W') 1
FILE ACCESS ERROR: cf.dcf: File is not writable
      'cf'(⎕FSTIE⍠'Mode' 'W')1
                ∧
```