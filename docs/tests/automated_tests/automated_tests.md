# Instructions

All folders specified in `tests/automated_tests/test_folder_list` are assumed to hold folders for testing various scripts. These folders must be relative to the project root, any other structure is not supported at the moment. Each subfolder under these specified folders will be searched for python files of the form `*_test.py`. Here is an eaxmple directory structure:

```
src/autopi/tests/
  - script1/
    - input/           # Directories are optional and are ignored by the test framework
    - output/          # However, the directories can be accessed by test files if desired...
    - scripty_test.py  # This is the only required file, note the '*_test.py' name.
    - testscript.py    # This is not a test and will not be treated as such.
    - random_file      # Arbitrary files will not disrupt the test framework
```

The following is an example of good practice directory structure:

```
src/autopi/tests/
  - script1/
    - input/          # Optional; use this directory for input files needed by a test
    - output/         # Optional; use this directory for any output examples needed by a test
    - script_test.py  # This is the only required file, note the '*_test.py' name.
```

Each test file will be treated as containing unit tests as expected by the 'unittest' framework. These have the following form:

```python
import unittest

class REPLACEWITHGROUPTESTNAME(unittest.TestCase):
    def TESTFUNCTION(self):
        ... # test code
    def MOARTEST(self):
        ... # test code

class REPLACEWITHGROUPTESTNAME2(unittest.TestCase):
    ... # more tests like above

... # more classes
```

Each function will be executed exactly as expected for 'unittest'. If you want to know how to do something test-wise, look up documentation for 'unittest'. Group tests into different `*_test.py` files as you think makes logical sense, group into classes as makes logical sense. Keep tests for particular scripts in the same folder. If you want input files/configuration files/etc., feel free to add subdirectories or other files to a folder as you wish. As long as you do not want a file to be treated as a test, don't name it like one. 

The current working directory will be the test's folder. The script is loaded in such a way that every folder in the path (except the first) is treated as a module, enabling relative/package imports to work. For example, specifying the folder `src/autopi/tests` for the example structure above, results in the test script being loaded as the module `autopi.tests.script1.scripty_test`. This allows the test script to be treated as a module under the `autopi` package. This way, imports can be done in the following way:
```python3
import autopi.util.config
import ...util.config
```
Notice that the `src` folder is not part of the package, because the first step in the path is not treated as part of the package. Note that the entire rest of the path will be. 

No execution order for test files or tests in a file is guaranteed.

Test folders should be named with the stem of the script name. That is, `get_ip.py` test folder should be named `get_ip`. Non-compliance will be punished severely...
