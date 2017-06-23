#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import sys
import codecs as cs

py_script_version = '1.0.0'

vowelChars = {
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
	'ω': 'w'
}

consonantChars = {
	'Β': 'B',
	'β': 'b',
	'Γ': 'G',
	'γ': 'g',
	'Δ': 'D',
	'δ': 'd',
	'Ζ': 'Z',
	'ζ': 'z',
	'Θ': 'Th',
	'θ': 'th',
	'Κ': 'K',
	'κ': 'k',
	'Λ': 'L',
	'λ': 'l',
	'Μ': 'M',
	'μ': 'm',
	'Ν': 'N',
	'ν': 'n',
	'Ξ': 'Ks',
	'ξ': 'ks',
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
	'ψ': 'ps'
}

symbolChars = {
	';': '?',
	'·': '-',
	'«': '<<',
	'»': '>>'
}

writeArgChars = {
	'-w': 0,
	'--write': 1
}

helpArgChars = {
	'-h': 0,
	'--help': 1
}

versionArgChars = {
	'-v': 0,
	'--version': 1
}

def version():
	print py_script_version
	
	return sys.exit()


def help():
	print
	print ' Version: ' + py_script_version
	print
	print ' Usage: grklsh [options]? file1 file2 fileN'
	print
	print ' Translate Greek into Greeklish and/or print on the standard output'
	print
	print ' Options:'
	print '  -w, --write   write to \'.grklsh\' files'
	print '  -h, --help    output usage information'
	print '  -v, --version output the version number'
	print
	
	return sys.exit()


def readByCharToList(file_):
	data = []
	f = cs.open(file_, 'r', 'utf-8')
		
	for line in f:
		data.extend(line)
			
	return data


def toGreeklish(list_):
	flag = False
	tmp = [None] * 999999 #TODO fix static malloc

	for char in xrange(0, len(list_)):

		uchar = list_[char].encode('utf-8')

		if uchar in vowelChars:
			tmp[char] = vowelChars.get(uchar)
		elif uchar in consonantChars:
			tmp[char] = consonantChars.get(uchar)
		elif uchar in symbolChars:
			tmp[char] = symbolChars.get(uchar)
		else:
			tmp[char] = list_[char]

		if char == len(list_) - 1:
			flag = True

	return [c for c in tmp if c is not None], flag


def main(args):
	flag = False

	if not len(args) > 0:
		while True:
			try:
				text = raw_input().decode('utf-8')
				newData, isTranlated = toGreeklish(list(text))
				print ''.join(newData)
			except KeyboardInterrupt:
				print 'exit'
				sys.exit()

	for arg in args:
		if arg in writeArgChars:
			if len(args) > 1:
				flag = True
				continue
			else:
				print 'You need to specify which files to translate'
				sys.exit()
		elif arg in helpArgChars:
			help()
		elif arg in versionArgChars:
			version()

		try:
			# Translate list
			newData, isTranlated = toGreeklish(readByCharToList(arg))
			
			if not flag:
				print 'File \'' + arg + '\'' + ':' + '\n'
				print ''.join(newData)
				print '----------------------------------------' + '\n'

			elif flag:
				if isTranlated:
					print '\'' + arg + '\' file has been translated successfully'

				# Write to file/s
				f = cs.open(str(arg) + '.grklsh', 'w', 'utf-8')
				flag = False
				for char in xrange(0, len(newData)):
					f.write(newData[char])
		except IOError as e:
			print "I/O error({0}): {1} {2}"\
				.format(e.errno, e.strerror, '\'' + arg + '\'')


if __name__ == '__main__':
	main(sys.argv[1:])