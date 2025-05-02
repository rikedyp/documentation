<h1 class="heading"><span class="name">Scan For Deprecated Files</span> <span class="command">R←{X}(3535⌶)Y</span></h1>

Scans a directory (and, optionally, subdirectories) for deprecated component files and external variables. For an overview of deprecated features see [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` is the name of the directory to scan.

`X` specifies whether subdirectories within `Y` should also be scanned. If `X` is omitted or has the value 0 subdirectories will be ignored and if 1 they will be scanned.

`R` is a two-column matrix identifying the files which are deprecated, with one filename per row.

The files in `Y`, and optionally subdirectories of `Y`, are examined and only the names of files which are deprecated or cannot be checked are included in `R`. The first column contains the names and the second contains a vector of one or more labels which indicate why the file is deprecated. These labels may be:

| Label | Meaning |
|-------|---------|
| J0C0  | File is a component file with both the Journalling (J) and Checksumming (C) properties set to 0.
| S32   | File is a small span component file.
| ⎕XT   | File is an external variable file.
| ?     | File could not be read and its content is unknown.

The rows in `R` are not sorted.

<h2 class="example">Example</h2>

```apl
      1(3535⌶)'.'
 ./J0C0.dcf             J0C0
 ./XT.dxv               ⎕XT
 ./subdir/S32J0C0.dcf   J0C0  S32
```

See also [Log use of deprecated features](deprecated-features.md).