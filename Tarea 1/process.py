class Process:

	process_indexer = 0

	def __init__(self,name,type,priority):

		self.id = Process.process_indexer
		self.name = name
		self.type = type
		self.priority = int(priority)
		self.timer = 1

		Process.process_indexer += 1
		
	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def getTimer(self):
		return int(self.timer)

	def setTimer(self,value):
		self.timer = int(value)

	def getPriority(self):
		return self.priority

	def setPriority(self, priority):
		self.priority = priority

	def runTimer(self):
		self.timer -= 1
		return True

	def finish(self,time):
		f = open('data/log.txt', 'a')		
		f.write("finish : (" + str(self.getId()) + ") "+ self.getName() + " at time: "+ str(time) )
		f.write("\n")		
		f.close() 
	# For call function
	def setFin(self,fin):
		self.fin = fin
		
	# For top function
	def printProcess(self, status):
		line = self.spaceFill(str(self.id), 3) + " " 
		line += self.spaceFill(str(self.priority), 3) + " "
		line += self.spaceFill(status, 4) + " " 
		line += self.spaceFill(str(self.type), 4) + " "
		line += self.spaceFill(str(self.timer), 4) + " "
		line += str(self.name)
		return line

	def spaceFill(self, word, length):
		lineArray = [" "]*length
		offset = length - len(word)
		for i in range(len(word)):
			if(i < len(word)):
				lineArray[offset + i] = word[i]

		return "".join(lineArray)
		