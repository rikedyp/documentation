# Minor Updates and Bug Fixes

This page describes minor updates and bug fixes included in Dyalog v20.0.

[`)SAVE`](../../language-reference-guide/system-commands/save/)  
You can no longer overwrite a workspace that was saved with an earlier version of Dyalog without using the `-force` option. This was already required on Microsoft Windows, but is now required on all supported operating systems.

**&lt;RD>** – The _Reformat_ command  
The ability to reformat JSON text has been extended to also reformat JSON5 text.

**.aplf** Files  
The interpreter now assumes that a file with the **.aplf** extension contains a function definition unless there are explicit instructions indicating otherwise within the file.

Microsoft Windows IDE

* The [**Find Objects** tool](https://dyalog.github.io/documentation/20.0/windows-ui-guide/find-objects-tool/) now allows a user to select and copy mulitple entries from the results.
* When applying a caption to a label, exceeding 1,023 characters now gives a `LIMIT ERROR` rather than crashing the interpreter (64-bit only).

.NET Framework v4.x  
Dyalog no longer crashes if you call `⎕CLEAR` after creating a link and using `-watch=both`.