!!! Info "Information"  
    THIS DOCUMENT IS UNDER DEVELOPMENT – THE CONTENTS HAVE NOT YET BEEN FINALISED

# Announcements

xxx

## Performance Issues with Namespaces

A namespace performance issue was identified in Dyalog v19.0 that was especially noticable with JSON imports. This has now been resovled, and the suggested workaround of assigning a name to the top-level namespace is no longer required.

## Hash and Lookup Tables

The performance of the set functions has been improved by increasing the amount of workspace allocated to the internal tables used by these functions.

## Legacy Workspaces

Dyalog v20.0 is the last major version that will support workspaces saved in Dyalog v11.0 or Dyalog v12.0 (workspaces saved in earlier versions are already unsupported). From Dyalog v21.0, the minimum version of a workspace that can be loaded will be v12.1.

To resave your Dyalog v11.0 or Dyalog v12.0 workspaces in a later version, you can use `)XLOAD` and `)SAVE` after ensuring that there are no suspended functions on the stack.

!!! Info "Information"  
    Performing an `)XLOAD` will refix all functions in the workspace. This could reveal invalid system names.

## Dyalog for macOS

Dyalog v19.0 was the last release to be compiled for Intel-based Macs; Dyalog v20.0 is only supported on ARM-based Macs.

## Syncfusion

The Syncfusion library of WPF controls is no longer included with Dyalog. The Syncfusion licence provided with Dyalog v19.0 will continue to be valid for use with Dyalog v19.0, but from Dyalog v20.0 onwards anyone who is using Syncfusion will need to obtain a licence from [https://www.syncfusion.com/](https://www.syncfusion.com/).

## Array Editor

David Liebtag's Array Editor is no longer part of Dyalog. Arrays can now be created and edited using [array notation](xxxLINKxxx).

## New Glyph

A new glyph has been introduced:
  
* Glyph: `⍛`  
* Glyph name: Jot Underbar
* Keyboard key location: &lt;APL key&gt; + Shift + F
* Unicode code: U+235B

This glyph is needed for the new [_behind_](xxxLINKxxx) operator that is introduced with Dyalog v20.0.

## New APL Font

The Dyalog v20.0 installation images include a preview of a new font, currently called APL387. The default font for APL within Dyalog remains APL385, but if this new font is well received it might become the default for future versions of Dyalog.

The design of APL387 has not yet been finalised, and feedback is welcome. Please email your feedback to support@dyalog.com or raise issues in the [APL387 GitHub project](https://github.com/Dyalog/APL387).

!!! Info "Information"  
    Although Dyalog Ltd has commissioned the font, we hope that it will become widely used by the APL community. It is intended to be vendor-agnostic, and we believe that it includes all the APL characters used by all APL dialects. It intentionally has, and will continue to have, an extremely permissive licence.