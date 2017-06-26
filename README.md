### grklsh

> Greeklish, a portmanteau of the words Greek and English, also known as Grenglish, Latinoellinika/Λατινοελληνικά or ASCII Greek, is the Greek language written using the Latin alphabet.

### About

`grklsh` is a small script written in **Python 2** that translates any text into Greeklish. It reads from stdin or from the arguments and prints on stdout or writes to files.

<a href="https://en.wikipedia.org/wiki/Greeklish">
    <img src="/imgs/banner.jpg" alt="grklsh logo"
         title="Greeklish Banner" align="right"
         		width="80%"/>
</a>

#### Features

* <kbd>Type</kbd> and <kbd>Enter</kbd> translation (Any language &#10141; Greeklish)
* File translation (Currently only Greek &#10141; Greeklish)

### Installation

#### on Linux and on MacOS

You only need `git` and of course `python2`

```bash
$ git clone https://github.com/xtonousou/grklsh.git
$ cd grklsh/
$ sudo python2 -m pip install -r requirements.txt
```

#### on Windows

You can read this [guide]

### Usage

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

### Changelog

All notable changes to this project will be documented in [this] file

### License

Copyright (c) **2017** by **Sotirios M. Roussis**. Some rights reserved.

`grklsh` is under the terms of the MIT License, following all clarifications stated in the [license] file


<!--- Links -->

[banner]: /imgs/banner.jpg
[here]: https://www.python.org/downloads/windows/
[guide]: WINDOWS_INSTALLATION.md
[this]: CHANGELOG.md
[license]: LICENSE.md