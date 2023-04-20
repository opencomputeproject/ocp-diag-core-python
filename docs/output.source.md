# ocptv.output.source module


### _class_ ocptv.output.source.SourceLocation(filename, line_number)
The `SourceLocation` instances are coordinates in user diagnostic code, used
for documenting where an `Error`, `Log` or `Diagnosis` artifacts were emitted from.

For functions taking a `source_location` parameter, eg. the ones making error messages,
the default value is `SourceLocation.CALLER`. Thi special instance is used to tell the
library to try to guess the location in user code based on the call stack.

However, the `source_location` can also be manually specified if needed.

Usage:

```python
import ocptv.output as tv
run = tv.TestRun(name="test", version="1.0")
# default source_location=SourceLocation.CALLER on the following line
# will result in the fields identifying the next line itself
run.add_log(LogSeverity.DEBUG, "Some interesting message.")
```

Specification reference:
- [https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#sourcelocation](https://github.com/opencomputeproject/ocp-diag-core/tree/main/json_spec#sourcelocation)

This type can be instantiated by user code directly.


#### \__init__(filename, line_number)

* **Parameters**

    
    * **filename** (`str`) – diagnostic package source filename being referenced.


    * **line_number** (`int`) – line number inside the diagnostic package source file.



### _class_ ocptv.output.source.NullSourceLocation()
This is an internal specialization of `SourceLocation` that will result in the
`source_location` message fields not to be emitted by virtue of translating into a None.
