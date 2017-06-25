### grklsh
#### :greece: :link: :us:

> Greeklish, a portmanteau of the words Greek and English, also known as Grenglish, Latinoellinika/Λατινοελληνικά or ASCII Greek, is the Greek language written using the Latin alphabet.

### What is it about?

A small Python2 script that translates any text into Greeklish.

#### Features

* File translation
* `cat` like functionality

*Greek can also be translated into Greeklish*

### How can I use it?

##### Greek &#10141; Greeklish

You just have to type,

```bash
$ grklsh.py
```

##### Any language &#10141; Greeklish

You need to put the `-t` or `--translate` argument first like this,

```bash
$ grklsh.py -t
```

##### Files containing Greek &#10141; New files in Greeklish

OK, this one is a bit tricky :smirk:
You have to put the `-w` or `--write` argument before each filename

The example below shows how to translate a file into Greeklish and generate a file `file1.grklsh` which contains the translated text

```bash
$ grklsh.py -w file1
```

If you want to convert multiple files at once,

```bash
$ grklsh.py -w file1 -w file2 -w file3
```

This will generate three files: `file1.grklsh`, `file2.grklsh` and `file3.grklsh` which contain the translated text of each file passed as argument

##### Files containing Greek &#10141; New files in Greeklish (PARTIALLY)

Hmmm? :confused:

You can use the functionality of printing the translated text on stdout and the functionality of writing to files simultaneously

The example below shows the implementation of the above,

```bash
$ grklsh.py -w file1 file2 -w file3 -w file4
```

This will print on stdout the translated text of the file `file2` but it will also generate three files: `file1.grklsh`, `file3.grklsh` and `file4.grklsh` which contain the translated text of each file

### How can I use it?

#### on :penguin: Linux or :apple: MacOS

You only need `git` and of course `python2`

```bash
$ git clone https://github.com/xtonousou/grklsh.git
$ cd grklsh/
$ sudo python2 -m pip install -r requirements.txt
```

#### on Windows :unamused:

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

* It would be nice to be able to run Python from any location without having to constantly reference the full installation path name. This can by done by adding the Python installation path to Windows' `PATH` `ENVIRONMENT VARIABLE`
  * In **Windows 7, 8, 8.1 and 10**, simply searching for "environment variables" will present the option to `Edit the system environment variables`. This will open the `System Properties / Advanced` tab
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
    Python 2.7.8 (default, Jun 30 2014, 16:03:49) [MSC v.1500 32 bit (Intel)] on win
    32
    Type "help", "copyright", "credits" or "license" for more information.
    >>>
    ```


### Changelog

All notable changes to this project will be documented in [this] file

### License

Copyright (c) 2017 by Sotirios M. Roussis. Some rights reserved.

grklsh is under the terms of the MIT License, following all clarifications stated in the [license] file


<!--- Links -->

[here]: https://www.python.org/downloads/windows/
[this]: CHANGELOG.md
[license]: LICENSE.md