<h1 class="heading"><span class="name">Log use of deprecated features</span> <span class="command">{R}←(13⌶)Y</span></h1>

Controls which deprecated features are logged when logging is enabled.

For an overview of deprecated features see [Deprecated features](../../../../programming-reference-guide/deprecated-features) within the Programming Reference Guide.

`Y` is a character vector, or a vector of character vectors, each containing the name of a deprecated feature, or one of the names defined in the table below. The list of deprecated feature names varies with each version of Dyalog and is listed in the [Release Notes](xxxLINKxxx).

Subsequent uses of the selected deprecated features will be logged, provided that [109⌶](log-file-for-deprecations.md) has been called to set the name of the log file.

If `13⌶` is called again, the list of features which are logged is replaced; to disable all logging `Y` can have the value `'None'` or can be an empty vector.

The result `R` is a vector of zero or more names, per the table below.

|Value(s) in Y|Meaning                                          |Value(s) in R                                           |
|---------------|-----------------------------------------------|--------------------------------------------------------|
|*Feature names*|Enable logging of the specified features       |Names of features for which logging is enabled (shy)    |
|`'All'`        |Enable logging of all deprecated features      |Names of features for which logging is enabled (non-shy)|
|`'None'`       |Enable logging of no deprecated features       |                                                        |
|`'Enabled'`    |List all features for which logging is enabled |_                                                      _|
|`'List'`       |List names all possible features               |Names of all deprecated features (non-shy)              |

Before any logging information is created, the log file must also be configured using [109⌶](log-file-for-deprecations.md). Without selecting a log file, all logging is silently discarded.

Each log entry is a complete JSON5 object definition which includes the following items:

* `TS`: a timestamp.
* `Type`: a description of the entry type (always `'Warning'`).
* `Message`: a message associated with the log entry (always `'Use of deprecated feature'`).
* `Feature`: a description of the deprecated feature.
* `ExtraInfo`: feature-specific additional information (may be an empty string).
* `WSID`: the name of the workspace in which the feature was used.
* `Stack`: an array of strings indicating the SIstack at the point the feature was used.

<h2 class="example">Example</h2>

```apl
      13⌶'List'
 This  That  TheOther 
      13⌶'Enabled'

      13⌶'That' 'This'
      13⌶'Enabled'
 This  That
      13⌶'All'
      13⌶'Enabled'
 This  That  TheOther
```

See also [Deprecated feature log file](log-file-for-deprecations.md).