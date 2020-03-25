'''
Copyright (c) <'2020'> <'Alrick Grandison'>

This software is provided 'as-is', without any express or implied
warranty. In no event will the authors be held liable for any damages
arising from the use of this software.

Permission is granted to anyone to use this software for any purpose,
including commercial applications, and to alter it and redistribute it
freely, subject to the following restrictions:

1. The origin of this software must not be misrepresented; you must not
   claim that you wrote the original software. If you use this software
   in a product, an acknowledgment in the product documentation would be
   appreciated but is not required.
2. Altered source versions must be plainly marked as such, and must not be
   misrepresented as being the original software.
3. This notice may not be removed or altered from any source distribution.

'''

'''
	text_to_c.py [pathfile] [...options]

	[pathfile] :	input filename with path
				mandatory
	[...option] :	not mandatory; default values used
					adjust behaviour by adding additional options
'''

'''
	This scripts takes any text and converts it to a string to be used in a C program. The string
	is generated in the form of 'lines-of-strings' where you have one string block followed by another in which
	each string block represents a line in the text: '"..." "..." "..."'.  C automatically amalgamates these into
	one string at compile time.	The text you provide could also be another C program which would be then turned 
	into a string.	The transformation from text to string is done in such a way that when the string is written
	to a file, that file is equivalent to the original text.  You can format the string to be used
	as a define ('define=on') or to be used as a format string ('param=on' and/or escape='on').  All quotes '"' in the
	text is guarded against using a backslash '\'.  The newline '\n' is automatically inserted at the end
	of each 'line-of-string' but this can be turned off ('line=off') as well.
	The resulting string is written to the file 'output.txt'.  Copy the contents to any file you want.
	WARNING: There should be no spaces between the option, the equal sign '=' and the value.
	That is, it must be exactly '[option]=on' or '[option]=off'.  Also, you can use 'true' instead of 'on' and
	'false' instead of 'off'.  The cases of the options or the values do not matter.
'''

import sys

PARAM = 'param'
ESCAPE = 'escape'
DEFINE = 'define'
LINE = 'line'
ON = ['on', 'true']
OFF = ['off', 'false']
EQU = '='
OR = '/'
SYM_PARAM = '%'
SYM_ESCAPE = '\\'
SYM_DEFINE = '\\'
SYM_LINE = '\\n'
SYM_SPACE = ' '
SYM_QUOTE = '"'

STATE = {
	PARAM:False,
	ESCAPE:True,
	DEFINE:False,
	LINE:True
}

def read(file):
	with open(file, "r") as stream:
		return stream.read()

def readlines(file):
	with open(file, "r") as stream:
		return stream.readlines()

def write(file, content):
	with open(file, "w") as stream:
		stream.write(content)

def string_is_a_member(string, stringList):
	for item in stringList:
		if item.lower() == string.lower(): return True
	return False

def apply_options():
	for option in sys.argv[2:]:
		pair = option.split(EQU)
		if len(pair) == 2:
			if pair[0].lower() == PARAM.lower():
				if string_is_a_member(pair[1], ON):
					STATE[PARAM] = True
				elif string_is_a_member(pair[1], OFF):
					STATE[PARAM] = False
			elif pair[0].lower() == ESCAPE.lower():
				if string_is_a_member(pair[1], ON):
					STATE[ESCAPE] = True
				elif string_is_a_member(pair[1], OFF):
					STATE[ESCAPE] = False
			elif pair[0].lower() == DEFINE.lower():
				if string_is_a_member(pair[1], ON):
					STATE[DEFINE] = True
				elif string_is_a_member(pair[1], OFF):
					STATE[DEFINE] = False
			elif pair[0].lower() == LINE.lower():
				if string_is_a_member(pair[1], ON):
					STATE[LINE] = True
				elif string_is_a_member(pair[1], OFF):
					STATE[LINE] = False

def genc(string):
	newstring = ''
	for i, c in enumerate(string):
		if c == '"':
			newstring += '\\"'
		elif STATE[PARAM] and c == SYM_PARAM:
			newstring += (SYM_PARAM + SYM_PARAM)
		elif STATE[ESCAPE] and c == SYM_ESCAPE:
			newstring += (SYM_ESCAPE + SYM_ESCAPE)
		else:
			if i < len(string) - 1:
				newstring += c
			else:
				if c == '\n': continue ## ignore trailing newline at the end of lines
				newstring += c
	return newstring

def content_from_lines(lines, separator=''):
	content = ''
	for line in lines:
		content += (line + separator)
	return content

def genclines(rawlines):
	clines = []
	for i, line in enumerate(rawlines):
		trail = SYM_QUOTE
		if i < len(rawlines) - 1:
			if STATE[LINE]: trail = (SYM_LINE + SYM_QUOTE)
			if STATE[DEFINE]: trail += (SYM_SPACE + SYM_DEFINE)
		string = SYM_QUOTE + genc(line) + trail
		clines.append(string)
	return clines

def main():
	argc = len(sys.argv)
	if(argc > 1):
		rawlines = readlines(sys.argv[1])
		if(argc > 2): apply_options()
		clines = genclines(rawlines)
		content = content_from_lines(clines, '\n')
		write("output.txt", content)
	else:
		print "text_to_c.py", "[pathfile]", "([...options])", '\n'
		print "USE-OPTION:", "[option]=on,", "[option]=off", '\n'
		print "OPTIONS:", PARAM+",", ESCAPE+",", DEFINE+",", LINE, '\n'
		print PARAM, "ON: doubles every '%'"+",", "OFF: [nothing]"+",", "[DEFAULT 'OFF']"
		print ESCAPE, "ON: doubles every '\\'"+",", "OFF: [nothing]"+",", "[DEFAULT 'ON']"
		print DEFINE, "ON: adds a trailing ' \\'"+",", "OFF: [nothing]"+",", "[DEFAULT 'OFF']"
		print LINE, "ON: inserts a '\\n' at the end of the string"+",", "OFF: [nothing]"+",", "[DEFAULT 'ON']"


#Script starts
main()



### REFERENCES
'''
	https://www.stechies.com/unboundlocalerror-local-variable-referenced-before-assignme/
	https://www.datacamp.com/community/tutorials/python-dictionary-comprehension?utm_source=adwords_ppc&utm_campaignid=1455363063&utm_adgroupid=65083631748&utm_device=c&utm_keyword=&utm_matchtype=b&utm_network=g&utm_adpostion=&utm_creative=278443377095&utm_targetid=aud-438999696719:dsa-473406574715&utm_loc_interest_ms=&utm_loc_physical_ms=1009016&gclid=CjwKCAjw3-bzBRBhEiwAgnnLCmb2NiAhDV3LT3UpmbGzxPcQ-LPckibrHcBI_A3wLDRmxEssSuNcrRoCns4QAvD_BwE
	https://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison
	https://www.w3schools.com/python/ref_string_split.asp
	https://stackoverflow.com/questions/6148619/start-index-for-iterating-python-list/6148636
	https://www.edureka.co/blog/substring-in-python/
	https://thispointer.com/python-how-to-iterate-over-the-characters-in-string/
	https://www.tutorialspoint.com/python/file_readlines.htm
'''

