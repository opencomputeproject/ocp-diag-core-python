# ocptv.output.config module

This module contains output channel configuration for the OCPTV library.


### _class_ ocptv.output.config.StdoutWriter()
A simple writer that prints the json to stdout.

This type can be instantiated by user code directly.


### _class_ ocptv.output.config.Writer()
Abstract writer interface for the lib. Should be used as a base for
any output writer implementation (for typing purposes).
NOTE: Writer impls must ensure thread safety.


### ocptv.output.config.config(\*, writer=None, enable_runtime_checks=None, timezone=<object object>)
Configure how the ocptv.output lib behaves.


* **Parameters**

    
    * **writer** (`Optional`[`Writer`]) – if provided, set the output channel writer.


    * **enable_runtime_checks** (`Optional`[`bool`]) – if provided, enables or disables runtime type checks.


    * **timezone** (`Optional`[`tzinfo`]) – if provided, sets the timezone for the output formatted datetime fields.
    To reset to local timezone, None value should be used.
