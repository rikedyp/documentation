<!-- Hidden search keywords -->
<div style="display: none;">
  ⎕FSTIE FSTIE
</div>






<h1 class="heading"><span class="name">File Share Tie</span> <span class="command">{R}←X ⎕FSTIE Y</span></h1>



`Y` must be 0 or a simple 1 or 2 element integer vector containing an available file tie number to be associated with the file for further file operations, and an optional passnumber.  If the passnumber is omitted it is assumed to be zero.  The tie number must not already be associated with a tied file.


`X` must be a simple character scalar or vector which specifies the name of the file to be tied.  The file must be named in accordance with the operating system's conventions, and may be specified with a relative or absolute pathname. If no file extension is supplied, the set of extensions specified by the  **CFEXT** parameter are tried one after another until the file is found or the set of extensions is exhausted. See [ CFEXT](../../../windows-installation-and-configuration-guide/configuration-parameters/configuration-parameters).


The file must exist and be accessible by the user.  If it is already tied by another task, it must not be tied exclusively.


The shy result of `⎕FSTIE` is the tie number of the file.



## Automatic Tie Number Allocation


A tie number of 0 as argument to a create, share tie or exclusive tie operation, allocates the first (closest to zero) available tie number and returns it as an explicit result. This allows you to simplify code. For example:


from:
```apl
      tie←1+⌈/0,⎕FNUMS  ⍝ With next available number,
      file ⎕FSTIE tie   ⍝ ... share tie file.
```


to:
```apl
      tie←file ⎕FSTIE 0 ⍝ Tie with 1st available number.
```


<h2 class="example">Example</h2>
```apl
      'SALES' ⎕FSTIE 1
 
      '../budget/COSTS' ⎕FSTIE 2
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

Mode is independent of any [file access controls managed using an access matrix](../programming-reference-guide/component-files/component-files/#file-access-control).

<h3 class="example">Example</h3>

```apl
      'cf' (⎕FSTIE⍠'Mode' 'W') 1
FILE ACCESS ERROR: cf.dcf: File is not writable
      'cf'(⎕FSTIE⍠'Mode' 'W')1
                ∧
```