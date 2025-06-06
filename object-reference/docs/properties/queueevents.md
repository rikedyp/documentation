<h1 class="heading"><span class="name">QueueEvents</span> <span class="right">Property</span></h1>



**Applies To:** [OCXClass](../objects/ocxclass.md), [OLEClient](../objects/oleclient.md)

**Description**


The QueueEvents property specifies whether or not incoming events generated by an COM object are queued. It is a Boolean value where the (default) value 1 specifies that events are queued, and 0 that they are not.


If QueueEvents is 1, the result (if any) of your callback function is not passed back to the COM object but is discarded. Thus you cannot, for example, inhibit or modify the default processing of the event by the COM object.


If QueueEvents is 0, the following applies.

- The callback function attached to the event is executed immediately, even if there are other APL events before it in the internal event queue. This immediate execution means that your callback can fire during the execution of any other function, including a callback function on an APL event. You must therefore take care that the callback makes no references to objects that may be shadowed.
- The result of your callback function is then passed back to the COM object. In this situation, it is essential that the callback is not interrupted by other events from the same, or another instance, of an COM object.
- To prevent APL itself from yielding to Windows, the Yield property is temporarily set to 0 while the callback is run. For the same reason, the tracing of a callback function, that is run immediately in this way, is disabled.


However, you must yourself also ensure that your own code does not yield. This means that you may not perform any operation in your callback that would yield to Windows; these include:

- `⎕DL`

- certain uses of `⎕NA`
- external function calls to Auxiliary Processors


If your callback does yield to Windows, thereby allowing another COM object event to arrive, this second event and any subsequent events that arrive during the execution of the callback are queued and will be processed later. These events may therefore not be modified by their callback functions.



