from commands import intCommandsFull, intCommandsShort, nonValueCommands, arduinoCode
import sourceCode

class turtleCommandsClass():

	def __init__(self, turtleCode=''):
		self.turtleCode=turtleCode.lower() #Converting the entire code to lowercase
		self.__formatCommands()		#Converting the commands to work better


	def __formatCommands(self):
		l=self.turtleCode.split() #Getting individual words
		self.turtleCommandsLst=[] #Creating a list to save commands
		for x in enumerate(l):

			turtleCommandsClass.__checkTurtleSyntax(x[1]) #Checking each items format and raising errors when they're incorrect

			#Checking where each item belongs and how to run it
			
			#Checking if the item belongs to int commands list (if it was one above or below)
			if turtleCommandsClass.__isIntTurtleCommand(x[1]):
				self.turtleCommandsLst.append('{0} {1}'.format(x[1], l[x[0]+1]))

			#Same thing here
			if turtleCommandsClass.__isNonValueCommand(x[1]):
				self.turtleCommandsLst.append(x[1])

			#continuing if the item is an interger
			if x[1].isdigit() or x[1].isdecimal():
				continue


	@staticmethod
	def __isNonValueCommand(cmd):
		return cmd in nonValueCommands

	@staticmethod
	def __isIntTurtleCommand(cmd):
		 
		ch1 = turtleCommandsClass.__isShortLengthIntTurtleCommand(cmd) 
		ch2 = turtleCommandsClass.__isFullLengthIntTurtleCommand(cmd)
		return ch1 or ch2

	@staticmethod
	def __isFullLengthIntTurtleCommand(cmd):
		return cmd in intCommandsFull

	@staticmethod
	def __isShortLengthIntTurtleCommand(cmd):
		return cmd in intCommandsShort

	@staticmethod
	def __checkTurtleSyntax(cmd):
		#Checking if command belongs in intCommandsShort
		ch1 = turtleCommandsClass.__isIntTurtleCommand(cmd) #cmd in intCommandsShort

		# #Checking if command belongs in intCommandsFull
		# ch2 = turtleCommandsClass.__is #cmd in intCommandsFull

		#Checking if command belongs in nonValueCommands
		ch3 = turtleCommandsClass.__isNonValueCommand(cmd) #cmd in nonValueCommands

		#Checking if the command is actually an integer
		ch4 = cmd.isdigit() or cmd.isdecimal()

		#If any of these conditions are true, and raises if none of them work
		if (ch1 or ch3 or ch4):
			return None
		else:
			raise SyntaxError('Invalid Command: {0} not understood'.format(cmd))


	#Method for converting mainloop code to C++ arduino Code
	def getArduinoLoopCode(self):
		code=''
		for x in self.turtleCommandsLst:

			#Assigning Boolean Values to check how they work
			isIn_intCommandsFull=x.split()[0] in intCommandsFull
			isIn_intCommandsShort=x.split()[0] in intCommandsShort
			isIn_nonValueCommands=x.split()[0] in nonValueCommands

			if isIn_intCommandsFull or isIn_intCommandsShort:
				code += arduinoCode[x.split()[0]] + '({0});\n\t'.format(x.split()[1])

			if isIn_nonValueCommands:
				code += arduinoCode[x.split()[0]]+'();\n\t'

		return code[:-2]


	def getArduinoCode(self):
		arduinoSourceCode = sourceCode.getArduinoSourceCode
		arduinoLoopCode = self.getArduinoLoopCode()
		arduinoSourceCode = arduinoSourceCode.replace("//1650--TENNIS", arduinoLoopCode)
		return arduinoSourceCode


	def saveArduinoCode(self, fileName='Output Arduino Code.ino'):
		open(fileName,'w').write(self.getArduinoCode())


def main():
	s='fd 5 rt 9'				#input('Enter the Turtle Command')
	t=turtleCommandsClass(turtleCode=s).saveArduinoCode()

if __name__ == '__main__':
	main()