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
