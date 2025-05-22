<h1 class="heading"><span class="name">Files and Directories</span></h1>

## Unicode and Classic Editions

Dyalog APL continues to be available in two separate editions; *Unicode* and *Classic*.

- The *Unicode* edition is intended for users who need to develop
    Unicode applications now, and are prepared to make the necessary (usually
    small) changes to existing applications in order to support new Unicode
    character types.
- The *Classic* edition is intended for customers who want to take
    advantage of other product enhancements, but do not wish to use Unicode at
    this time.

The two different editions are maintained from the same source code, and
every effort will be made to ensure that they are identical except for the
handling of character arrays, and the transfer of data into and out of the
workspace.

## 32-Bit and 64-Bit Versions

Two separate versions of Dyalog for Microsoft Windows are available. The 32-bit version will run on both 32-bit and 64-bit Operating Systems; the 64-bit version will only run on a 64-bit Operating System.

## Files

The following tables show files that are included in the different versions and editions under Microsoft Windows.  These are referred to in the remainder of this document and in other documents by the name shown in the first column of the tables.

With the exception of the following all these files may be distributed as part of end-user applications, under the terms and conditions of a Dyalog APL Run-Time Agreement. Please contact Dyalog or your distributor, or see the Dyalog web page for more information.

## Non-Distributable Development Components

- Development EXE
- Development DLL
- Array Editor

|Name               |File                                    |
|-------------------|----------------------------------------|
|32-bit Unicode { .shaded }    |Dyalog APL {{ version_majmin }} Unicode\\ { .shaded }|
|Development EXE    |`dyalog.exe`                            |
|Development DLL    |`dyalog{{ version_maj }}_32_unicode.dll`|
|Shell Script Engine|`dyascript.exe`                         |
|Array Editor       |`dlaedit32.dll`                         |
|Run-Time EXE       |`dyalogrt.exe`                          |
|Run-Time DLL       |`dyalog{{ version_maj }}rt_unicode.dll` |
|Bridge DLL         |`bridge{{ version_maj }}_unicode.dll`   |
|Dyalog DLL         |`dyalog32.dll`                          |
|DyaRes DLL         |`dyares{{ version_maj }}_32.dll`        |
|DyalogProvider DLL |`dyalogprovider.dll`                    |
|DyalogNet DLL      |`dyalognet.dll`                         |
|APLScript Compiler |`dyalogc_unicode.exe`                   |
|For Conga and Ride |`conga34ssl32.dll`                      |
|For Conga and Ride |`conga34_32.dll`                        |
|&nbsp;             |`exestub.dll`                           |
|&nbsp;             |`dllstub.dll`                           |
|SQAPL INI          |`sqapl.ini`                             |
|SQAPL ERR          |`sqapl.err`                             |
|SQAPL DLL          |`cwdya64u32w.dll`                       |
|APLUNICD INI       |`aplunicd.ini`                          |
|&nbsp;             |`sharpplot.dll`                         |
|&nbsp;             |`sharpplot.xml`                         |

|Name               |File                                    |
|-------------------|----------------------------------------|
|32-bit Classic { .shaded }     |Dyalog APL {{ version_majmin }} Classic\\  { .shaded }|
|Development EXE    |`dyalog.exe`                            |
|Development DLL    |`dyalog{{ version_maj }}_32.dll`        |
|Shell Script Engine|`dyascript.exe`                         |
|Array Editor       |`dlaedit32.dll`                         |
|Run-Time EXE       |`dyalogrt.exe`                          |
|Run-Time DLL       |`dyalog{{ version_maj }}rt.dll`         |
|Bridge DLL         |`bridge{{ version_maj }}.dll`           |
|Dyalog DLL         |`dyalog32.dll`                          |
|DyaRes DLL         |`dyares{{ version_maj }}_32.dll`        |
|DyalogProvider DLL |`dyalogprovider.dll`                    |
|DyalogNet DLL      |`dyalognet.dll`                         |
|APLScript Compiler |`dyalogc.exe`                           |
|For Conga and Ride |`conga34ssl32.dll`                      |
|For Conga and Ride |`conga34_32.dll`                        |
|&nbsp;             |`exestub.dll`                           |
|&nbsp;             |`dllstub.dll`                           |
|SQAPL INI          |`sqapl.ini`                             |
|SQAPL ERR          |`sqapl.err`                             |
|SQAPL DLL          |`cwdya64c32w.dll`                       |
|APLUNICD INI       |`aplunicd.ini`                          |
|&nbsp;             |`sharpplot.dll`                         |
|&nbsp;             |`sharpplot.xml`                         |

|Name               |File                                       |
|-------------------|-------------------------------------------|
|64-bit Unicode { .shaded }     |Dyalog APL-64 {{ version_majmin }} Unicode\\  { .shaded }|
|Development EXE    |`dyalog.exe`                               |
|Development DLL    |`dyalog{{ version_maj }}_64_unicode.dll`   |
|Shell Script Engine|`dyascript.exe`                            |
|Array Editor       |`dlaedit64.dll`                            |
|Run-Time EXE       |`dyalogrt.exe`                             |
|Run-Time DLL       |`dyalog{{ version_maj }}_64rt_unicode.dll` |
|Bridge DLL         |`bridge{{ version_maj }}-64_unicode.dll`   |
|Dyalog DLL         |`dyalog64.dll`                             |
|DyaRes DLL         |`dyares{{ version_maj }}_64.dll`           |
|DyalogProvider DLL |`dyalogprovider.dll`                       |
|DyalogNet DLL      |`dyalognet.dll`                            |
|APLScript Compiler |`dyalogc64_unicode.exe`                    |
|For Conga and Ride |`conga34ssl64.dll`                         |
|For Conga and Ride |`conga34_64.dll`                           |
|&nbsp;             |`exestub.dll`                              |
|&nbsp;             |`dllstub.dll`                              |
|SQAPL INI          |`sqapl.ini`                                |
|SQAPL ERR          |`sqapl.err`                                |
|SQAPL DLL          |`cwdya64u64w.dll`                          |
|APLUNICD INI       |`aplunicd.ini`                             |
|&nbsp;             |`sharpplot.dll`                            |
|&nbsp;             |`sharpplot.xml`                            |

|Name               |File                                       |
|-------------------|-------------------------------------------|
|64-bit Classic { .shaded }     |Dyalog APL-64 {{ version_majmin }} Classic\\ { .shaded }|
|Development EXE    |`dyalog.exe`                               |
|Development DLL    |`dyalog{{ version_maj }}_64.dll`           |
|Shell Script Engine|`dyascript.exe`                            |
|Array Editor       |`dlaedit64.dll`                            |
|Run-Time EXE       |`dyalogrt.exe`                             |
|Run-Time DLL       |`dyalog{{ version_maj }}_64rt.dll`         |
|Bridge DLL         |`bridge{{ version_maj }}-64.dll`           |
|Dyalog DLL         |`dyalog64.dll`                             |
|DyaRes DLL         |`dyares{{ version_maj }}_64.dll`           |
|DyalogProvider DLL |`dyalogprovider.dll`                       |
|DyalogNet DLL      |`dyalognet.dll`                            |
|APLScript Compiler |`dyalogc64.exe`                            |
|For Conga and Ride |`conga34ssl64.dll`                         |
|For Conga and Ride |`conga34_64.dll`                           |
|&nbsp;             |`exestub.dll`                              |
|&nbsp;             |`dllstub.dll`                              |
|SQAPL INI          |`sqapl.ini`                                |
|SQAPL ERR          |`sqapl.err`                                |
|SQAPL DLL          |`cwdya64c64w.dll`                          |
|APLUNICD INI       |`aplunicd.ini`                             |
|&nbsp;             |`sharpplot.dll`                            |
|&nbsp;             |`sharpplot.xml`                            |

## File Naming Conventions

The following file naming conventions have been adopted for the various files distributed with and used by Dyalog APL.

|Extension|Description                     |
|---------|--------------------------------|
|.dws     |Dyalog APL Workspace            |
|.dse     |Dyalog APL Session              |
|.dcf     |Dyalog APL Component File       |
|.DXV     |Dyalog APL External Variable    |
|.din     |Dyalog APL Input Table          |
|.dot     |Dyalog APL Output Table         |
|.dft     |Dyalog APL Format File          |
|.DXF     |Dyalog APL Transfer File        |
|.dlf     |Dyalog APL Session Log File     |
|.dyalog  |Dyalog APL SALT file            |
|.dyapp   |Dyalog APL SALT application file|

!!! note
    Some of these extensions, notably .dcf, .dlf, .dot and .DXF, are not unique to Dyalog and conflict with the same extensions used by other software applications. Although all the above file extensions are associated with Dyalog during its installation, these associations may subsequently be changed by the installation of other software or by a Windows System restore.
