#!/usr/bin/env python3
#coding: utf-8
### 1st line allows to execute this script by typing only its name in terminal, with no need to precede it with the python command
### 2nd line declaring source code charset should be not necessary but for exemple pydoc request it



__doc__ = "provide converters for numbers"#information describing the purpose of this module
__status__ = "Development"#should be one of 'Prototype' 'Development' 'Production' 'Deprecated' 'Release'
__version__ = "2.0.0"# version number,date or about last modification made compared to the previous version
__license__ = "public domain"# ref to an official existing License
__date__ = "2017"#started creation date / year month day
__author__ = "N-zo syslog@laposte.net"#the creator origin of this prog,
__maintainer__ = "Nzo"#person who curently makes improvements, replacing the author
__credits__ = []#passed mainteners and any other helpers
__contact__ = "syslog@laposte.net"# current contact adress for more info about this file



def to_hex(number):
	"""return a number into its hexadecimal form"""
	return hex(number)[2:]


def to_bin(n):
	"""Convert a number to binary"""
	if n == 0:
		return '0'
	res = ''
	while n != 0:
		res =`n & 1` + res # Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of n is 1, otherwise it's 0. 
		n = n >> 1 # Returns n with the bits shifted to the right 1 time.
	return res


def to_dec(string,base):
	"""Convert a hexadecimal or binary string to decimal number"""
	number=int(string,base)
	return number
