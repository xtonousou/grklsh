### grklsh - :greece: + ( :uk: || :us: )

> Greeklish, a portmanteau of the words Greek and English, also known as Grenglish, Latinoellinika/Λατινοελληνικά or ASCII Greek, is the Greek language written using the Latin alphabet.

### What is it about?

`grklsh` is a small script written in python

Its job is to translate any text into Greeklish and|or display it to standard output and|or redirect the translated text to file|s

**NOTE** *Greek can also be translated into Greeklish*

### How can I use it?

##### Greek &#10141; Greeklish

You just have to type ...

```bash
$ grklsh.py
```

##### Any language &#10141; Greeklish

You just have to type but you need to put the `-t` or `--translate` argument first like this,

```bash
$ grklsh.py -t
```

##### Files containing Greek &#10141; New files in Greeklish

OK, this one is a bit tricky :smirk:
You have to put the `-w` or `--write` argument before each filename

The example below shows how to translate a file into Greeklish
It will generate a file `file1.grklsh` which contains the translated text

```bash
$ grklsh.py -w file1
```

If you want to convert multiple files at once,

```bash
$ grklsh.py -w file1 -w file2 -w fileN
```

This will generate three files: `file1.grklsh`, `file2.grklsh` and `fileN.grklsh` which contain the translated text of each file passed as argument

### How can I install it?

#### on Linux or MacOS

```bash
$ git clone https://github.com/xtonousou/grklsh.git
$ cd grklsh/
$ sudo python2 -m pip install -r requirements.txt
```

### on Windows

:unamused: untested

### Changelog

All notable changes to this project will be documented in [this] file.

### License

Copyright (c) 2017 by Sotirios M. Roussis. Some rights reserved.

grklsh is under the terms of the MIT License, following all clarifications stated in the [license] file


<!--- Links -->

[this]: CHANGELOG.md
[license]: LICENSE.md