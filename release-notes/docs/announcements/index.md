!!! Info "Information"  
    THIS DOCUMENT IS UNDER DEVELOPMENT – THE CONTENTS HAVE NOT YET BEEN FINALISED

# Announcements

Notice of new and planned additions, removals, and deprecations in Dyalog v20.0 compared with Dyalog v19.0.

## Performance Issues with Namespaces

A namespace performance issue was identified in Dyalog v19.0 that was especially noticeable with JSON imports. This has now been resolved, and the suggested workaround of assigning a name to the top-level namespace is no longer required.

## Hash and Lookup Tables

The performance of the set functions has been improved by increasing the amount of workspace allocated to the internal tables used by these functions.

## Legacy Workspaces

Dyalog v20.0 is the last major version that will support workspaces saved using Dyalog v11.0 or Dyalog v12.0 (workspaces saved using earlier versions are already unsupported). From Dyalog v21.0, the minimum version of a workspace that can be loaded will be v12.1.

To resave your Dyalog v11.0 or Dyalog v12.0 workspaces in a later version, you can use `)XLOAD` and `)SAVE`.   

!!! Tip "Hints and Recommendations"  
    Dyalog Ltd recommends that workspaces are saved without any suspended functions on the stack before loading them into a newer interpreter. To achieve this, run `)RESET` before `)SAVE`.
	
## Small-span Component Files

Dyalog v16.0 was the last major version to support creating and updating small-span (32-bit) component files; in Dyalog v17.0 these files became read-only. The ability to access these files even in a read-only state will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

## External Variables

The ability to create and update external variables will be removed in a future release (exact release to be decided, expected to be implemented by the year 2030).

## J0C0 Component Files

Dyalog v20.0 is the last major version that will support creating and updating component files that have both journalling and checksum properties set to `0`; from Dyalog v21.0 component files with this combination of properties will be read-only. The ability to access these files even in a read-only state will be removed in a future release (exact release to be decided, expected to be implemented by the year 2040).

## Dyalog for macOS

Dyalog v19.0 was the last release to be built for Intel-based Mac computers; Dyalog v20.0 is only supported on ARM-based Mac computers.

## Dyalog for Linux

In addition to x86_64, Dyalog is now supported on Linux-based ARM64 platforms and, therefore, on software built on these, such as Raspberry Pi O/S 64-bit and AWS containers. This applies to the Unicode edition only.

Images of docker containers that host Dyalog running on ARM64 Linux are available to download at [https://hub.docker.com/u/dyalog](https://hub.docker.com/u/dyalog).
 
!!! Info "Information"  
    The HTMLRenderer is not currently supported on Linux ARM64.
	
## Dyalog for Raspberry Pi

Dyalog v20.0 is the last release that will be supported on 32-bit Raspberry Pi OS.

## Syncfusion

The Syncfusion library of WPF controls is no longer included with Dyalog. The Syncfusion licence provided with Dyalog v19.0 will continue to be valid for use with Dyalog v19.0, but from Dyalog v20.0 onwards anyone who is using Syncfusion will need to obtain a licence from [https://www.syncfusion.com/](https://www.syncfusion.com/).

## Array Editor

David Liebtag's Array Editor is no longer part of Dyalog. Arrays can now be created and edited using [array notation](../../programming-reference-guide/introduction/arrays/array-notation/).

## Documentation

The process of moving all the documentation into an [open source GitHub project](https://github.com/Dyalog/documentation) has started. The aim of this is two-fold:

- All documentation will be available to view from a single online front-end; this is a long-term goal, and will take several releases to achieve.
- It will be easier for anyone to contribute to the Dyalog documentation set, either by making suggestions or by drafting amendments/enhancements.

To report an error or request a change in the documentation you can now:

- send an email to [docs@dyalog.com](mailto:docs@dyalog.com) – this can be done for any Dyalog document.
- [raise an issue](https://github.com/Dyalog/documentation/issues) directly in the GitHub project – this should only be done if the issue relates to a document that is in the GitHub project.

The GitHub project's [readme file](https://github.com/Dyalog/documentation/blob/main/README.md) includes information on how to contribute by drafting amendments/enhancements.

## New Glyph

A new glyph has been introduced:
  
* Glyph: `⍛` (Classic: `⎕U235B`)  
* Glyph name: Jot Underbar
* Keyboard key location: <kbd>&lt;APL key&gt;</kbd> + <kbd>Shift</kbd> + <kbd>F</kbd>
* Unicode code: U+235B

This glyph is needed for the new [_behind_](../../language-reference-guide/primitive-operators/behind/) operator that is introduced with Dyalog v20.0.

## New APL Font

The Dyalog v20.0 installation images include a preview of a new font, currently called APL387. The default font for APL within Dyalog remains APL385, but if this new font is well received it might become the default for future versions of Dyalog.

The font can be explored within the Microsoft Windows IDE (it can be selected from the drop-down font selection list) or at [https://dyalog.github.io/APL387/](https://dyalog.github.io/APL387/).

The design of APL387 has not yet been finalised, and feedback is welcome. Please email your feedback to [support@dyalog.com](mailto:support@dyalog.com) or raise issues in the APL387 GitHub project ([https://github.com/Dyalog/APL387](https://github.com/Dyalog/APL387)).

!!! Info "Information"  
    Although Dyalog Ltd has commissioned the font, we hope that it will become widely used by the APL community. It is intended to be vendor-agnostic, and we believe that it includes all the APL characters used by all APL dialects. It intentionally has, and will continue to have, an extremely permissive licence.