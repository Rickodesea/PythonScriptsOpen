'''
Binary_to_C
	Converts any binary data to an array of 'char' type to be used inside of a C program.
	The reason to want to do that, is to emulate a 'Windows Resource System' on Linux.
	Linux does not allow inclusion of binary data in application (I am OK with that, I like that actually).
	Windows, however, does.  On that system it is called resource; See 'http://www.winprog.org/tutorial/resources.html'
	for details.  Sometimes, though a Linux programmer, may want the binary data to be apart of the application
	so that end users do not tamper with it.  This script will make that possible.

	python binary_to_c.py [file] ([commands])

	commands
		* -output=[file] : 		outputs the data to a file; default is the screen
		* -column=[number] :	sets the number of column the array should have (that is, break before making a new row); 
								0 gives an single row with a infinitly long column;
								default is 10.
		* -hex=[0, 1, or 2]:	0=decimal, 1=lower-case-hex, 2=upper-case-hex

'''

import sys
import os

## defines
COLUMN = 'column'
OUTPUT = 'output'
HEX = 'hex'
SPACE = ' '
LINE = '\n'
TAB = '\t'
COMMA = ','
DEFAULT_COLUMN = 10
DEFAULT_OUTPUT = sys.stdout
DEFAULT_HEX = 0

## structs
Config = {
	COLUMN: DEFAULT_COLUMN,
	OUTPUT: DEFAULT_OUTPUT,
	HEX: DEFAULT_HEX
}

## functions
def printUse():
	print "python binary_to_c.py " + "[file] ([commands])"
	print "commands"
	print "\t-" + OUTPUT + "=[file] : outputs the data to a file; default is the screen"
	print "\t-" + COLUMN + "=[number] : sets the number of column the array should have (that is, break before making a new row);"
	print "\t" + ' ' * len(COLUMN + "\"=[number]\"") + ": 0 gives an single row with a infinitly long column;"
	print "\t-" + HEX + "=[0, 1, or 2] : 0=decimal, 1=lower-case-hex, 2=upper-case-hex"

def configReset():
	if Config[OUTPUT] != sys.stdout:
		Config[OUTPUT].close()

	Config[COLUMN] = DEFAULT_COLUMN
	Config[OUTPUT] = DEFAULT_OUTPUT
	Config[HEX] = DEFAULT_HEX

def checkParam():
	if(os.path.isfile(sys.argv[1]) == False):
		print sys.argv[1] + " is not a file"
		printUse()
		sys.exit()

def configReadParam():
	for i in range(len(sys.argv)):
		if i == 0: continue #name of program
		if i == 1: continue #file reading binary from

		Command = sys.argv[i]

		if OUTPUT in Command:
			List = Command.split('=')
			if len(List) < 2:
				print "Error in " + OUTPUT + " command: ", '-' + OUTPUT + '=[file]'
				sys.exit()
			File = List[1].strip()
			Config[OUTPUT] = open(File, 'w')

		if COLUMN in Command:
			List = Command.split('=')
			if len(List) < 2:
				print "Error in " + COLUMN + " command: ", '-' + COLUMN + '=[number]'
				sys.exit()
			Number = List[1].strip()
			try:
				Config[COLUMN] = int(Number)
			except:
				Config[COLUMN] = 0

		if HEX in Command:
			List = Command.split('=')
			if len(List) < 2:
				print "Error in " + HEX + " command: ", '-' + HEX + '=[0, 1 or 2]'
				sys.exit()
			Number = List[1].strip()
			try:
				Value = int(Number)
				if Value == 1 or Value == 2:
					Config[HEX] = Value
				else:
					Config[HEX] = 0
			except:
				Config[HEX] = 0

def read(File):
	with open(File, "r") as Stream:
		return Stream.read()

def createStringValue(Value):
	if Config[HEX] == 1:
		return "{0:#0{1}x}".format(Value, 4)
	elif Config[HEX] == 2:
		return '0x{0:0{1}X}'.format(Value, 2)
	else:
		if Value > 99: return str(Value)
		if Value > 9: return SPACE + str(Value)
		return SPACE + SPACE + str(Value)

def createArray(String):
	Array = []
	
	for Byte in String:
		Value = ord(Byte)
		StringValue = createStringValue(Value)
		Array.append(StringValue)

	return Array

def write(Array):
	Begin = 'char binary [' + str(len(Array)) + '] = {'
	End = '};'

	String = ''

	String += Begin + LINE + TAB

	Column = 0
	for i, item in enumerate(Array):
		String += item
		if i < len(Array) - 1:
			String += COMMA + SPACE

		if Config[COLUMN] > 0:
			Column += 1
			if Column == Config[COLUMN]:
				Column = 0
				String += LINE
				if i < len(Array) - 1:
					String += TAB

	String += LINE + End + LINE

	Config[OUTPUT].write(String)


def main():
	if len(sys.argv) > 1:
		checkParam()
		configReadParam()
		String = read(sys.argv[1])
		Array = createArray(String)
		write(Array)
		configReset()
	else:
		printUse()

#### Run
if __name__=="__main__":
	main()

'''
Reference
	https://en.wikibooks.org/wiki/Python_Programming/Text
	https://stackoverflow.com/questions/12638408/decorating-hex-function-to-pad-zeros
'''