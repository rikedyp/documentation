!!! Info "Information"  
    THIS DOCUMENT IS STILL UNDER DEVELOPMENT

# New Features, Changes, and Enhancements

This page describes the changes and new features in Dyalog v20.0 compared with Dyalog v19.0.

## Language Changes

### System Functions

#### New System Functions

The following system functions have been added:

- [`⎕SHELL`](xxxLINKxxx)  
This extends [`⎕SH`](xxxLINKxxx)/[`⎕CMD`](xxxLINKxxx). It executes an external program, either directly or using the operating system's shell.

#### Enhanced System Functions

The following system functions have been enhanced:

- [`⎕DT`](xxxLINKxxx)  
Additional conversion types have been added:
    - 15 – Go UnixMicro
	- 16 – Go UnixNano
	- 17 – APL+Win and APL64 workspace timestamp
	- 21 – Apollo NCS UUID
	- 22 – OSF DCE UUID
	- 70  – AmigaOS
- [`⎕FSTIE`](xxxLINKxxx)  
A new variant option, **Mode**, has been added. This specifies the intended purpose of the tie, and can affect when/how errors are generated.
- [`⎕FTIE`](xxxLINKxxx)  
A new variant option, **Mode**, has been added. This specifies the intended purpose of the tie, and can affect when/how errors are generated.
- [`⎕MKDIR`](xxxLINKxxx)  
A new variant option, **Unique**, has been added. This specifies whether the base name in the right argument is modified so that the name is unique.
- [`⎕NINFO`](xxxLINKxxx)  
    - Several of the properties can now be set by extending the appropriate element in the left argument from a `propertyNumber` to a `(propertyNumber newValue)` pair.
    - A new variant option, **ProgressCallBack**, has been added. This causes `⎕NINFO` to invoke an APL callback function as the file operation proceeds.

### I-beams

!!! Warning "Warning"  
    Any service provided using an I-Beam should be considered as "experimental" and subject to change – without notice - from one release to the next. Any use of I-Beams in applications should, therefore, be carefully isolated in cover-functions that can be adjusted if necessary.

#### New I-beams

The following I-beams have been added:

- [`13⌶`](xxxLINKxxx) – Deprecated Features  
Records information in the log file set by `109⌶` about the specified deprecated feature names or keywords
- [`43⌶`](xxxLINKxxx) – Monadic Operator Generator  
Generates a monadic operator with specified functionality. The functionality is currently limited to creating a .NET-specific operator that can create concrete versions of generic classes and execute generic methods.
- [`109⌶`](xxxLINKxxx) – Log File for Deprecations  
Manages the file used to log the use of deprecated features.
- [`120⌶`](xxxLINKxxx) – Generate UUID  
Generates a UUID (Universally Unique IDentifier) according to the RFC 9562 specification.
- [`3535⌶`](xxxLINKxxx) – Scan For Deprecated Files  
Scans the specified directory (and, optionally, sub-directories) for deprecated saved workspaces, component files, and external variables.
- [`5581⌶`](xxxLINKxxx) – Unicode Normal Forms  
Applies the specified Unicode normalisation form to given character data.
This is a temporary I-beam – it is expected that it will be superseded by a system function in Dyalog v21.0.
- [`8373⌶`](xxxLINKxxx) – Shell Process Control  
Provides a way to determine the process IDs of processes started by `⎕SHELL`, as well as enabling the sending of signals to any of those processes.

#### Removed I-beams

The following I-beams have been removed:

- `819⌶` – Case Convert (introduced in Dyalog v15.0)  
The functionality provided by this I-beam is available through the [`⎕C`](xxxLINKxxx) system function.
- `8468⌶` – Hash Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.
- `8469⌶` – Lookup Table Size (introduced in Dyalog v19.0)  
Temporary functionality used for identification of potential side-effects of a change that has now been implemented. No longer relevant.

## User Interface Changes

xxx

## Other Changes

### PCRE Library

The Perl Compatible Regular Expressions (PCRE) library used by the interpreter has been upgraded from PCRE v8.45 to PCRE2 v10.45.

!!! Warning "Warning"
    Some semantic changes introduced with this upgrade could result in unexpected results when using `⎕R`, `⎕S`, or the search functionality within the Microsoft Windows IDE (and all tools that build on these) compared to results in Dyalog v19.0.