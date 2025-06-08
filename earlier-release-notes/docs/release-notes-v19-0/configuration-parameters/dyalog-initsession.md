<h1 class="heading"><span class="name">DYALOG_INITSESSION</span></h1>

This Boolean parameter governs whether (1) or not (0) Dyalog performs Session Initialisation on start-up. See [Session Initialisation](../../../windows-ui-guide/the-session-object/session-initialisation).

The default is 1 for development and shell script versions, and 0 for run-time versions.

Session initialisation makes Link, SALT and other things available. These features depend on DYALOG_INITSESSION being 1 (explicitly or by default).
