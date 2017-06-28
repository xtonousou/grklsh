#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author ......: Sotirios M. Roussis aka. xtonousou <xtonousou@gmail.com>
# Date ........: 20170628

"""
    Translate any text into Greeklish, print on stdout, write to file/s
"""

try:
    from sys import argv, platform, stdin
    import locale
    import codecs as cs
    try:
        import dictionaries as d
    except ImportError:
        print 'You must have the \'dictionaries.py\' file in the script\' s directory to continue'
        exit()
    try:
        from googletrans import Translator
    except ImportError:
        if platform == "linux" or platform == "linux2":
            print 'You must run \'sudo python2 -m pip install -r requirements.txt\' first'

        elif platform == "darwin":
            print 'You must run \'sudo pip install -r requirements.txt\' first'

        elif platform == "win32":
            print 'You must run \'pip install -r requirements.txt\' first'
            exit()
except KeyboardInterrupt:
    print '\nexit'
    exit()


SCRIPT_NAME = argv[0].strip('.')[::-1].strip('.')[3:][::-1]
SCRIPT_VERSION = '1.1.0'


def version_message():
    """
        Prints the script's name with the version

        @return: exit()
    """

    print SCRIPT_NAME + ' ' + SCRIPT_VERSION

    return exit()


def help_message():
    """
        Prints all the available script's options

        @return: exit()
    """

    print
    print ' Version: ' + SCRIPT_VERSION
    print
    print ' Usage: ' + SCRIPT_NAME + ' [options]'
    print
    print ' Translate any text into Greeklish, print on stdout, write to file/s'
    print
    print ' Options:'
    print '  -t|--translate translate into Greeklish'
    print '  -w|--write     write to \'.' + SCRIPT_NAME + '\' files'
    print '  -h|--help      output usage information'
    print '  -v|--version   output the version number'
    print

    return exit()


def print_messages(messages):
    """
        Prints out a list line by line

        @param messages: the list to be printed
    """

    for message in messages:
        print message.strip()


def get_arg_list(arg):
    """
        Creates and returns a list of arguments

        @param arg: {'h', 't', 'v', 'w'}
        @return arg_list: a list with the available arguments
    """

    if arg == 'h':
        arg_list = ['-h', '--help']

    elif arg == 't':
        arg_list = ['-t', '--translate']

    elif arg == 'v':
        arg_list = ['-v', '--version']

    elif arg == 'w':
        arg_list = ['-w', '--write']

    return arg_list


def read_file_to_list(file_):
    """
        Reads a file and converts it to a list

        @param file_: the file to be read
        @return [word for ... in line]: the converted word list
    """

    return [word for line in cs.open(file_, 'r', 'utf-8') for word in line]


def read_file_by_char_to_list(file_):
    """old-style-class
        Reads a file char by char and creates a list with those chars

        @param file_: the file to be read
        @return data: a char list
    """

    data = []
    buffer_ = cs.open(file_, 'r', 'utf-8')

    for line in buffer_:
        data.extend(line)

    return data


def to_greeklish(list_):
    """
        Converts a char list to Greeklish using 'dictionaries' file

        @param list_: a char list e.g. list_ = ['a', 'b']
        @return tmp: a char list that contains the translated text
    """

    tmp = [None] * 999999

    for char in xrange(0, len(list_)):

        char_dict = d.get_char_dict()
        uchar = list_[char].encode('utf-8')

        if uchar in char_dict:
            tmp[char] = char_dict.get(uchar)

        else:
            tmp[char] = list_[char]

    return [c for c in tmp if c is not None]


def cat(lang):
    """
        Translate any text into Greeklish by [typing + enter]

        @param lang: a string to check which mode to activate {'greek', anything}
    """

    if lang == 'greek':
        while True:
            try:
                text = raw_input().decode(stdin.encoding
                                          or locale.getpreferredencoding(True))

                new_data = to_greeklish(list(text))
                print ''.join(new_data)
            except KeyboardInterrupt:
                print '\nexit'
                exit()
    else:
        while True:
            try:
                text = raw_input().decode(stdin.encoding
                                          or locale.getpreferredencoding(True))

                translated = Translator().translate(''.join(text), dest='el')
                new_data = to_greeklish(list(unicode(translated.text)))
                print ''.join(new_data)
            except KeyboardInterrupt:
                print '\nexit'
                exit()


def print_or_write_list(arg, flag, count_t):
    """
        Prints list or writes to file/s

        @param arg: each file
        @param flag: boolean value
        @param count_t: how many times a 'translate' argument is passed
        @return flag: the boolean value to keep 'write' sanity between multiple files
        @return messages: a list containing current 'SUCCESS' and 'FAILURE' messages
    """

    messages = []

    try:
        if not flag:
            if count_t > 0:
                data = read_file_to_list(arg)
                translated = Translator().translate(''.join(data), dest='el')
                new_data = to_greeklish(list(unicode(translated.text)))
            elif count_t < 1:
                new_data = to_greeklish(read_file_by_char_to_list(arg))

            print 'File \'' + arg + '\'' + ':' + '\n'
            print ''.join(new_data)
            print '\n' + '----------------------------------------' + '\n'

        elif flag:
            if count_t > 0:
                data = read_file_to_list(arg)
                translated = Translator().translate(''.join(data), dest='el')
                new_data = to_greeklish(list(unicode(translated.text)))
            elif count_t < 1:
                new_data = to_greeklish(read_file_by_char_to_list(arg))

            d.get_color_dict().get('OKGREEN')
            messages.append(d.get_color_dict().get('OKGREEN') + '✓ ' +
                            d.get_color_dict().get('ENDC') + '\'' + arg +
                            '\' file has been translated successfully' + '\n')

            flag = False

            # Write to file/s
            buffer_ = cs.open(str(arg) + '.grklsh', 'w', 'utf-8')

            for char in xrange(0, len(new_data)):
                buffer_.write(new_data[char])
    except IOError as error:
        messages.append(
            d.get_color_dict().get('FAIL') + '✗ ' +
            d.get_color_dict().get('ENDC') + 'I/O error({0}): {1} {2}'
            .format(error.errno, error.strerror, '\'' + arg + '\'')
        )

    return flag, messages


def main(args):
    """
        The main function; parsing command line arguments; write to files

        @param args: all command line arguments after the first e.g. argv[1:]
    """

    all_messages = []
    messages = []
    flag = False
    count_t = 0
    count_w = 0

    if len(args) < 1:
        cat('greek')

    else:
        for arg in args:

            # translate
            if arg in get_arg_list('t'):

                count_t += 1

                if len(args) < 2:
                    cat('other')
                    continue

            # write
            elif arg in get_arg_list('w'):

                if count_t > 0 and len(args) % 2 == 0:
                    print d.get_color_dict().get('WARNING') + \
                        'You need to specify which files to translate' + \
                        d.get_color_dict().get('ENDC')
                    exit()

                count_w += 1

                if len(args) > 1:
                    flag = True
                    continue

                else:
                    print d.get_color_dict().get('WARNING') + \
                        'You need to specify which files to translate' + \
                        d.get_color_dict().get('ENDC')
                    exit()

                flag, messages = print_or_write_list(
                    arg, flag, count_t)
                all_messages += messages

            # help
            elif arg in get_arg_list('h'):
                help_message()

            # version
            elif arg in get_arg_list('v'):
                version_message()

            else:
                flag, messages = print_or_write_list(
                    arg, flag, count_t)
                all_messages += messages

        print_messages(all_messages)

if __name__ == '__main__':
    main(argv[1:])
