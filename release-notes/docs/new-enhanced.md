!!! Info "Information"  
    THIS DOCUMENT IS STILL UNDER DEVELOPMENT

# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v20.0 compared with Dyalog v19.0.

## Language Changes

### Primitive Functions/Operators

A new primitive operator, [_behind_](../../language-reference-guide/primitive-operators/behind/), has been added. This completes the set of [function composition](../../language-reference-guide/primitive-operators/operator-syntax/#function-composition) operators, which allow functions to be glued together to build up more complex functions:

- Glyph: `⍛` (Classic: `⎕U235B`)
- Derived function equivalence:
    - monadic: `(f Y) g Y`
	- dyadic: `(f X) g Y`

### System Functions

The following system functions have been added:

- [`⎕SHELL`](../../language-reference-guide/system-functions/shell/)  
This enables execution of external programs with more control and options than [`⎕SH`](../../language-reference-guide/system-functions/start-unix-auxiliary-processor/)/[`⎕CMD`](../../language-reference-guide/system-functions/start-windows-auxiliary-processor/).
- [`⎕VGET`](../../language-reference-guide/system-functions/vget/)  
This enables values to be read for names in a source namespace/namespaces.
- [`⎕VSET`](../../language-reference-guide/system-functions/vset/)  
This enables values to be set for names in a target namespace/namespaces.

The following system functions have been enhanced:

- [`⎕DT`](../../language-reference-guide/system-functions/dt/)  
Additional conversion types have been added:
    - 15 – Go UnixMicro
	- 16 – Go UnixNano
	- 17 – APL+Win and APL64 workspace timestamp
	- 21 – Apollo NCS UUID
	- 22 – OSF DCE UUID
	- 70  – AmigaOS
- [`⎕FSTIE`](../../language-reference-guide/system-functions/fstie/)  
A new variant option, **Mode**, has been added. This specifies the intended purpose of the tie, and can affect when/how errors are generated.
- [`⎕FTIE`](../../language-reference-guide/system-functions/ftie/)  
A new variant option, **Mode**, has been added. This specifies the intended purpose of the tie, and can affect when/how errors are generated.
- [`⎕MKDIR`](../../language-reference-guide/system-functions/mkdir/)  
A new variant option, **Unique**, has been added. This specifies whether the base name in the right argument is modified so that the name is unique.
- [`⎕NINFO`](../../language-reference-guide/system-functions/ninfo/)  
    - Several of the properties can now be set by extending the appropriate element in the left argument from a `propertyNumber` to a `(propertyNumber newValue)` pair.
    - A new variant option, **ProgressCallBack**, has been added. This causes `⎕NINFO` to invoke an APL callback function as a file operation (for example, a query relating to a file's size, name, or modification date) proceeds.
- [`⎕NS`](../../language-reference-guide/system-functions/ns/)  
    - The left argument `X` has been extended to allow references to namespaces to be specified. It can also now be an array in which each element identifies a namespace. 
	- The right argument `Y` has been extended to  allow references to namespaces to be specified. It can also now be an array produced by the [`⎕OR`](../../language-reference-guide/system-functions/or/) of a namespace.
	- A new variant option, **Trigger**, has been added. This specifies whether any triggers should be run for the modified variables in the target namespace that have triggers attached.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I-Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

The following I-beams have been added:

- [`13⌶`](../../language-reference-guide/the-i-beam-operator/deprecated-features/) – Deprecated Features  
Records information in the log file set by `109⌶` about the specified deprecated feature names or keywords
- [`43⌶`](../../language-reference-guide/the-i-beam-operator/monadic-operator-generator/) – Monadic Operator Generator  
Generates a monadic operator with specified functionality. The functionality is currently limited to creating a .NET-specific operator that can create concrete versions of generic classes and execute generic methods.
- [`109⌶`](../../language-reference-guide/the-i-beam-operator/log-file-for-deprecations/) – Log File for Deprecations  
Manages the file used to log the use of deprecated features.
- [`120⌶`](../../language-reference-guide/the-i-beam-operator/generate-uuid/) – Generate UUID  
Generates a UUID (Universally Unique IDentifier) according to the RFC 9562 specification.
- [`3535⌶`](../../language-reference-guide/the-i-beam-operator/scan-for-deprecated-files/) – Scan For Deprecated Files  
Scans the specified directory (and, optionally, sub-directories) for deprecated saved workspaces, component files, and external variables.
- [`5581⌶`](../../language-reference-guide/the-i-beam-operator/unicode-normalisation/) – Unicode Normalisation  
Applies the specified Unicode normalisation form to given character data.  

    !!! Info "Information"  
        `5581⌶` is a temporary I-beam – it is expected that it will be superseded by a system function in Dyalog v21.0.
		
- [`8373⌶`](../../language-reference-guide/the-i-beam-operator/shell-process-control/) – Shell Process Control  
Provides a way to determine the process IDs of processes started by `⎕SHELL`, as well as enabling the sending of signals to any of those processes.

The following I-beams have been removed:

- `819⌶` – Case Convert (introduced in Dyalog v15.0)  
The functionality provided by this I-beam is available through the [`⎕C`](../../language-reference-guide/system-functions/c/) system function.
- `8468⌶` – Hash Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.
- `8469⌶` – Lookup Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.

## Syntax Changes

### Array Notation

[Array notation](../../programming-reference-guide/introduction/arrays/array-notation/) is a literal syntax for most arrays (including nested and high-rank arrays) and namespaces. With array notation, arrays can be entered and displayed over multiple lines.

## User Interface Changes

### Configuration Parameters

The following configuration parameters have been added:

- `DYALOG_SHELL_SUBPROCESS`  
This improves the performance of `⎕SHELL` on AIX. When set to `1` (the default on AIX), `⎕SHELL` uses another mechanism for running/executing its command, which can improve performance on some operating systems.

### Home and End Keys

The actions of the <kbd>Home</kbd> and <kbd>End</kbd> keys have been enhanced to provide finer granularity.

When the cursor is placed in a line in the Session:

- <kbd>Home</kbd> moves the cursor left to whichever of these it encounters first from its starting position:
    - the start of the content of the line
    - the six space prompt (except when in the **Editor**, in which case this is skipped)
    - the left edge of the session
- <kbd>End</kbd> moves the cursor right to whichever of these it encounters first from its starting position:
	- the end of the content of the line excluding space characters
    - the end of the content of the line including space characters
    - the six space prompt (only when the cursor is on a blank line)

Pressing <kbd>Home</kbd> or <kbd>End</kbd> multiple times progresses through the list in the order shown.

### Microsoft Windows IDE

The following changes have been made to the Microsoft Windows IDE:

- A new menu, **Layout**, provides options for the location (or undocking) of the **Debugger** window.
- A new keyboard shortcut has been added to toggle inline tracing:
    - key code: **&lt;IT&gt;**
	- keystroke: <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Enter</kbd>
- A new icon (xxxIMAGExxx) has been added to the **Session** menu to toggle the use of array notation.
- The Session caption can now include the current thread by adding the `{TID}` field to the `⎕SE.Caption` property.
	
### TTY Interface

The following changes have been made to the TTY interface:

- A new keyboard shortcut has been added to toggle inline tracing:
    - key code: **&lt;IT&gt;**
	- keystroke – terminal emulator under Linux GUIs: _&lt;undefined&gt;_
	- keystroke – PuTTY terminal emulator: <kbd>Ctrl</kbd> + <kbd>Alt</kbd> + <kbd>Enter</kbd>

## Interfaces and Libraries

### PCRE Library

The Perl Compatible Regular Expressions (PCRE) library used by the interpreter has been upgraded from PCRE v8.45 to PCRE2 v10.45.

!!! Warning "Warning"
    Some semantic changes introduced with this upgrade could result in unexpected results when using `⎕R`, `⎕S`, or the search functionality within the Microsoft Windows IDE (and all tools that build on these) compared to results in Dyalog v19.0.
	
### .NET Interface

In .NET, a generic class is a class that has type parameters, which must be given values to create a concrete version of the class. Similarly, a generic method has type parameters which must be specified before the method can be called. 

The .NET interface now supports creating concrete versions of generic classes, instantiating them, and calling generic methods. For more information, see the [_.NET Interface Guide_](https://docs.dyalog.com/latest/dotNET_Interface_Guide.pdf).

The .NET Framework interface does not support generics.