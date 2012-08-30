class Process:

	process_indexer = 0

	def __init__(self,name,type,priority):

		self.id = Process.process_indexer
		self.name = name
		self.type = type
		self.priority = priority
		self.timer = 5

		Process.process_indexer += 1
		
	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def getTimer(self):
		return self.timer

	def setTimer(self,value):
		self.timer = value

	def getPriority(self):
		return self.priority

	def setPriority(self, priority):
		self.priority = priority

	def runTimer(self):
		self.timer -= 1

	# For top function
	def printProcess(self, status):
		line = self.spaceFill(str(self.id), 3) + " " 
		line += self.spaceFill(str(self.priority), 3) + " "
		line += self.spaceFill(status, 4) + " " 
		line += self.spaceFill(str(self.type), 4)
		print line

	def spaceFill(self, word, length):
		lineArray = [" "]*length
		offset = length - len(word)
		for i in range(len(word)):
			if(i < len(word)):
				lineArray[offset + i] = word[i]

		return "".join(lineArray)
		