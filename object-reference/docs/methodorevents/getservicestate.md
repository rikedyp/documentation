<h1 class="heading"><span class="name">GetServiceState</span> <span class="right">Method 92</span></h1>

**Applies To:** [Root](../objects/root.md)

**Description**

This method is used to obtain the current state of a Dyalog APL service running under Windows. See [APL Application as a Service](../../../windows-installation-and-configuration-guide/apl-application-as-a-service).

The GetServiceState method is niladic.

The result of the method is a 7-element numeric vector corresponding to the `SERVICE_STATUS` structure which is described in C++ as follows:
```c
typedef struct _SERVICE_STATUS {
  DWORD dwServiceType;
  DWORD dwCurrentState;
  DWORD dwControlsAccepted;
  DWORD dwWin32ExitCode;
  DWORD dwServiceSpecificExitCode;
  DWORD dwCheckPoint;
  DWORD dwWaitHint;
} SERVICE_STATUS, *LPSERVICE_STATUS;
```

For further details, see the on-line documentation for `SERVICE_STATE` and the function `HashDefine` in the sample workspace `aplservice`.
