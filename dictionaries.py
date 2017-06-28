#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# Author ......: Sotirios M. Roussis aka. xtonousou <xtonousou@gmail.com>
# Date ........: 20170628


"""
    Dictionary library for grklsh.py
"""


def get_char_dict():
    """
        Returns char dictionary

        @return char_dict: Greek <-> Greeklish character dictionary
    """

    char_dict = {
        'Ά': 'A',
        'Α': 'A',
        'ά': 'a',
        'α': 'a',
        'Έ': 'E',
        'Ε': 'E',
        'έ': 'e',
        'ε': 'e',
        'Ή': 'H',
        'Η': 'H',
        'ή': 'h',
        'η': 'h',
        'Ϊ': 'I',
        'Ί': 'I',
        'Ι': 'I',
        'ΐ': 'i',
        'ϊ': 'i',
        'ί': 'i',
        'ι': 'i',
        'Ό': 'O',
        'Ο': 'O',
        'ό': 'o',
        'ο': 'o',
        'Ϋ': 'Y',
        'Ύ': 'Y',
        'Υ': 'Y',
        'ΰ': 'y',
        'ϋ': 'y',
        'ύ': 'y',
        'υ': 'y',
        'Ώ': 'W',
        'Ω': 'W',
        'ώ': 'w',
        'ω': 'w',
        'Β': 'B',
        'β': 'b',
        'Γ': 'G',
        'γ': 'g',
        'Δ': 'D',
        'δ': 'd',
        'Ζ': 'Z',
        'ζ': 'z',
        'Θ': '8',
        'θ': '8',
        'Κ': 'K',
        'κ': 'k',
        'Λ': 'L',
        'λ': 'l',
        'Μ': 'M',
        'μ': 'm',
        'Ν': 'N',
        'ν': 'n',
        'Ξ': '3',
        'ξ': '3',
        'Π': 'P',
        'π': 'p',
        'Ρ': 'R',
        'ρ': 'r',
        'Σ': 'S',
        'σ': 's',
        'ς': 's',
        'Τ': 'T',
        'τ': 't',
        'Φ': 'F',
        'φ': 'f',
        'Χ': 'X',
        'χ': 'x',
        'Ψ': 'Ps',
        'ψ': 'ps',
        ';': '?',
        '·': ';',
        '«': '<<',
        '»': '>>',
        '…': '...'
    }

    return char_dict


def get_color_dict():
    """
        Returns colors dictionary

        @return color_dict: dictionary containing all available colors
    """

    color_dict = {
        'HEADER': '\033[95m',
        'OKBLUE': '\033[94m',
        'OKGREEN': '\033[92m',
        'WARNING': '\033[93m',
        'FAIL': '\033[91m',
        'ENDC': '\033[0m',
        'BOLD': '\033[1m',
        'UNDERLINE': '\033[4m'
    }

    return color_dict
