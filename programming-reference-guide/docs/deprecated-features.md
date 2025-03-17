<h1 class="heading"><span class="name">Deprecated Features</span></h1>

Over time, certain features supplied by Dyalog, be they part of the language, functionality within the development environments, or the supplied samples or Tools, may become obsolete or cease to be useful. There are many reasons why this may happen; some examples are:

* A superior alternative has been introduced. For example, Dyalog now recommends using `⎕UCS` instead of `⎕TC` (which generates only the newline, backspace and tabstop characters).
* The feature was originally implemented as an I-beam but has since been superseded by a formal addition to Dyalog APL. For example `⎕JSON` replaced an earlier I-beam.
* The feature is associated with hardware or technology which is itself becoming obsolete - such as 32-bit processes and address spaces limited to 4GB in size.

In such circumstances the feature becomes **deprecated**; it is unlikely to be developed or extended further and its use in new developments may be discouraged, and in some cases Dyalog may even announce that it will be removed in a specific version. (Such announcements are included in the [Release Notes](xxxLINKxxx).)

## Identifying uses of deprecated features

In cases when removing the feature is considered to be sufficiently significant, Dyalog will enable the ability to identify where the feature is being used.

To use this, Dyalog can be configured to log the feature's use to a file. Logging must be configured and enabled/disabled in each APL process - information about logging is not retained.  

Two steps are necessary before logging to a file will begin:  you must call [`109⌶`](../../../language-reference-guide/the-i-beam-operator/log-file-for-deprecations) to specify the name of the file into which the JSON5 log messages will be written, and you must call [`13⌶`](../../../language-reference-guide/the-i-beam-operator/deprecated-features) to specify which specific features should be logged.

To specify the log file, use `109⌶` with a right argument of 0; for example 

```apl
      'deprecated_log.json'(109⌶)0
```

Note: If you do not set the name of the log file, then all logging information will be silently discarded.

To select which features should be logged call `13⌶`. The right argument is a list of the names by which the features are identified.  This list will appear in the [Release Notes](xxxLINKxxx) for the appropriate version of Dyalog APL. There are two reserved names which can be used: `'All'` is used to enable logging of all such features, and `'None'` can the used to disable all logging.

Each time `13⌶` is called, the new list of features _replaces_ the existing list: if the list is empty then all logging will be disabled.

Every subsequent use of the selected features is logged and each line in the file contains a complete JSON5 object which includes a description of the feature and the SI Stack at the point it was called.

The log file can be examined using any text editor, or from within Dyalog:

```apl
      log_entries←(⎕JSON⍠('Dialect' 'JSON5')('Compact' 0))⍣2¨⊃⎕NGET 'deprecated_log.json5' 1
```

If an error occurs when writing to the log file, further logging is suspended. `109⌶` with a right argument of 1 checks whether this happened and the result is non-zero with an error description if it did; for example

```apl
      (109⌶)1
┌─┬┐
│0││
└─┴┘
```

