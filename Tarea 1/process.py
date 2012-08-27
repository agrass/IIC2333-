class Process:

	process_indexer = 0

	def __init__(self,name,type,priority):

		self.id = Process.process_indexer
		self.name = name
		self.type = type
		self.priority = priority

		Process.process_indexer += 1
		
	def getId(self):
		return self.id

	def getName(self):
		return self.name

	def getType(self):
		return self.type

	def setPriority(self, prioridad):
		self.priority = priority

	def getPriority(self):
		return self.priority
