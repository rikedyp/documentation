!!! Info "Information"  
    THIS DOCUMENT IS STILL UNDER DEVELOPMENT
	
# Minor Updates and Bug Fixes

This page describes minor updates and bug fixes included in Dyalog v20.0.

[`⎕FX`](../../language-reference-guide/system-functions/fx/) – Fix Definition  
The rules around whether a function can be fixed have been tightened to prevent functions with unmatched parentheses from being fixed. This is to accommodate array notation, which changes the meaning of parentheses and brackets that span more than one statement.

!!! Hint "Hints and Recommendations"
    If the enhanced restrictions on `⎕FX` cause problems for you, please contact [support@dyalog.com](mailto:support@dyalog.com) to discuss tools and techniques for mitigation.

[`)SAVE`](../../language-reference-guide/system-commands/save/)  
You can no longer overwrite a workspace that was saved with an earlier version of Dyalog without using the `-force` option. This was already required on Microsoft Windows, but is now required on all supported operating systems.

**&lt;RD>** – The _Reformat_ command  
The ability to reformat JSON text has been extended to also reformat JSON5 text.

 _more coming soon..._