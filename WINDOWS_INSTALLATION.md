# grklsh Installation on Windows

## Table Of Contents

* [Python 2.7 installation]
  * [Environment Variables for python (optional)]
* [PIP Installation]
  * [Environment Variables for pip (optional)]
* [grklsh Installation] :arrow_left:

### Python 2.7 installation

Installation of Python itself should be fairly straight-forward

* Download and execute the latest Python 2.* installation package from [here]

* Verify a successful installation by opening a command prompt window and navigating to your Python installation directory (default is `C:\Python27`). Type `python` from this location to launch the Python interpreter

	```
	Microsoft Windows [Version 6.2.9200]
	(c) 2012 Microsoft Corporation. All rights reserved.

	C:\Users\Username>cd C:\Python27

	C:\Python27>python
	Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win
	32
	Type "help", "copyright", "credits" or "license" for more information.
	>>>
	```

#### Environment Variables for python (optional)

* It would be nice to be able to run Python from any location without having to constantly reference the full installation path name. This can by done by adding the Python installation path to Windows' `PATH` `ENVIRONMENT VARIABLE`

  * In Windows 7, 8, 8.1 and 10, simply searching for "environment variables" will present the option to `Edit the system environment variables`. This will open the `System Properties / Advanced` tab

  * In Windows XP, right click on `My Computer->Properties` to open `System Properties` and click on the `Advanced` tab.

1. On the `System Properties / Advanced` tab, click `Environment Variables` to open `User Variables` and `System Variables`

2. Create a new `System Variable` named Variable name: `PYTHON_HOME` and  Variable value: `c:\Python27` (or whatever your installation path was)

3. Find the system variable called `Path` and click `Edit`

4. Add the following text to the end of the Variable value: `;%PYTHON_HOME%\;%PYTHON_HOME%\Scripts\`

5. Verify a successful environment variable update by opening a new command prompt window (important!) and typing `python` from any location
  ```
  Microsoft Windows [Version 6.2.9200]
  (c) 2012 Microsoft Corporation. All rights reserved.
  
  C:\Users\Username>python
  Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win 32
  Type "help", "copyright", "credits" or "license" for more information.
  >>>
  ```

### PIP Installation

The easiest way to install the `grklsh` python modules and keep them up-to-date is with a Python-based package manager called [Pip](http://en.wikipedia.org/wiki/Pip_(package_manager))

There are many methods for getting Pip installed, but my preferred method is the following:

* Download [get-pip.py](https://bootstrap.pypa.io/get-pip.py) to a folder on your computer. Open a command prompt window and navigate to the folder containing `get-pip.py`. Then run `python get-pip.py`. This will install `pip`.

* Verify a successful installation by opening a command prompt window and navigating to your Python installation's script directory (default is `C:\Python27\Scripts`).  Type `pip freeze` from this location to launch the Python interpreter.  
_`pip freeze` displays the version number of all modules installed in your Python non-standard library;  On a fresh install, `pip freeze` probably won't have much info to show but we're more interested in any errors that might pop up here than the actual content_

    ```
    Microsoft Windows [Version 6.2.9200]
    (c) 2012 Microsoft Corporation. All rights reserved.
    
    C:\Users\Username>cd c:\Python27\Scripts
    
    c:\Python27\Scripts>pip freeze
    antiorm==1.1.1
    enum34==1.0
    requests==2.3.0
    virtualenv==1.11.6
    ```

#### Environment Variables for pip (optional)

* It would be nice to be able to run Pip from any location without having to constantly reference the full installation path name. If you followed the Python installation instructions above, then you've already got the pip install location (default = `C:\Python27\Scripts`) in your Windows' `PATH` `ENVIRONMENT VARIABLE`. If you did not follow those steps, refer to them above now.

* Verify a successful environment variable update by opening a new command prompt window (important!) and typing `pip freeze` from any location

    ```
    Microsoft Windows [Version 6.2.9200]
    (c) 2012 Microsoft Corporation. All rights reserved.
    
    C:\Users\Username>pip freeze
    antiorm==1.1.1
    enum34==1.0
    requests==2.3.0
    virtualenv==1.11.6
    ```


### grklsh Installation

OK, now that you have installed python, pip and you tweaked the environment variables you are ready to proceed

1. Download the latest release of `grklsh` from [here]

2. Extract the downloaded file `grklsh-*.*.*.*`

3. Navigate to the newly created directory `grklsh-*.*.*.*/`

4. <kbd>Shift</kbd> + Right click on whitespace and select the option `Open PowerShell window here` or `Open command window here` (depends)

5. Now, you can use **grklsh** by typing `python grklsh.py` and then press <kbd>Enter</kbd>

6. To see the available options, type `python grklsh.py -h` and then press <kbd>Enter</kbd>

<!--- Links -->

[here]: https://github.com/xtonousou/grklsh/releases
[Python 2.7 installation]: #python-27-installation
[Environment Variables for python (optional)]: #environment-variables-for-python-optional
[PIP Installation]: #pip-installation
[Environment Variables for pip (optional)]: #environment-variables-for-pip-optional
[grklsh Installation]: #grklsh-installation