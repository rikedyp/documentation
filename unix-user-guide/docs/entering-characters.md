<h1 class="heading"><span class="name"> Entering Characters</span></h1>

It is necessary to select a metakey which is to be used to enter characters. In this document this metakey is represented by the string "APL". In a terminal window under a Linux GUI Dyalog recommends using the Windows key as the metakey to generate APL characters; with PuTTY and the Unicode IME the <kbd>Ctrl</kbd> key is used (similarly to the Windows Unicode edition of Dyalog APL). For example, in a terminal window <kbd>WindowsKey</kbd>+<kbd>a</kbd>generates an `⍺`; when using PuTTY the same APL character is entered by using <kbd>Ctrl</kbd>+<kbd>a</kbd>. 

!!!note 
    Under PuTTY, <kbd>Ctrl</kbd>+<kbd>xcv</kbd> are reserved for the operating system; we shall see later that <kbd>Ctrl</kbd>+<kbd>x</kbd> is used for another purpose. Rather than  <kbd>Ctrl</kbd>+<kbd>xcv</kbd> you must use  <kbd>Shift</kbd>+<kbd>Ctrl</kbd>+<kbd>xcv</kbd>.

Linux Window managers are in generally in a state of flux, so it is best to look at the following article on the Dyalog Forum for the latest information about keyboard configuration:

[https://www.dyalog.com/forum/viewtopic.php?f=20&t=210](https://www.dyalog.com/forum/viewtopic.php?f=20&t=210)

## Recently-added Glyphs

It is currently not possible by default to enter the Behind character as a single key-chord under windows managers under Linux; the updated keyboard mapping file is not yet included in Linux distributions.

Dyalog anticipates that future Linux distributions will have an updated mapping file, but until that time, and for existing versions of Linux distributions the methods available are:

- Update the mapping file. See below for more details
- Define the Operating System's [<kbd>Compose</kbd>](https://en.wikipedia.org/wiki/Compose_key) key and enter *Behind* by pressing <kbd>Compose</kbd> <kbd>Jot</kbd> <kbd>Underscore</kbd>
- In the Session, use the *Insert* command **<IN\>** to change to overstrike mode, enter <kbd>Jot</kbd> <kbd>&larr;</kbd>  <kbd>Underscore</kbd> and enter **<IN\>** again to return to insert mode.
- In Ride, from version 4.6, use the Prefix key and <kbd>F</kbd>


To update the mapping file, edit */usr/share/X11/xkb/symbols/apl*:

- Search for the text **xkb_symbols "dyalog_base"**
- Look for the line<br>
*key <AC04\> { [ underscore		] };	// low line*

- and replace with<br>
*key <AC04\> { [ underscore,	U235b	] };	// low line, jot underbar*

Be aware that there are multiple occurrences of AC04; please ensure that you are editing the Dyalog APL section !

Logout and log back in again.

Be aware that these changes may be lost if you update the operating system.
