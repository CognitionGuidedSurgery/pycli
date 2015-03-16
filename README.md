# pyclictk


[![Circle CI](https://circleci.com/gh/CognitionGuidedSurgery/pyclictk.svg?style=svg)](https://circleci.com/gh/CognitionGuidedSurgery/pyclictk)
[![Documentation Status](https://readthedocs.org/projects/pyclictk/badge/?version=latest)](https://readthedocs.org/projects/pyclictk/?badge=latest)


    Author: Alexander Weigl <Alexander.Weigl@student.kit.edu>
    License: LGPLv3
 
Support for CTK's Command Line Interface

**Install over pip** `pip install pyclictk`

## Features

* Parse CLI XML into Python model
* Create CLI XML from Python model
* Create `argparse.ArgumentParser` or a `docopt` description for a CLI model
* Invoke CLI executable with arguments


### Parse CLI XML into Python model

```
>>> from clictk import Executable
>>> exe1 = Executable.from_exe("myexecutable")
>>> exe2 = Executable.from_xml("myexecutable.xml")
```

### Create CLI XML from Python model

```
>>> from clictk import Executable, ParameterGroup, Parameter
>>> exe = Executable(executable=sys.argv[0], 
                     category="example",
                     title="My Super App",
                     description="This is just awesome",
                     version="1.0",
                     license=None, 
                     contributor=None, 
                     acknowledgements=None, 
                     documentation_url=None,
                     parameter_groups=[
                        ParameterGroup(
                          label="FirstGroup",
                          description="Test",
                          parameters=[
                            Parameter("imagefile", "image", "test.png", 
                                      description="image file",
                                      channel="input",,
                                      label="Image", 
                                      flag="i", 
                                      file_ext=".png")
                          ]
                        )
                     ]):
>>> exe.as_xml()
```

### Create `argparse.ArgumentParser` or a `docopt` description for a CLI model

```
>>> ap = build_argument_parser(exe)
>>> ap.parse_args() 
```

### Invoke CLI executable with arguments

  >>> exe.run(imagefile="abc.png")
