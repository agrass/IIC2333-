import heapq
from process import Process

class Scheduler:
	
	def __init__(self):
		#Cola new con pares (tiempo , proceso)
		self.new = []
		#Cola ready con pares (prioridad , proceso)
		self.ready = []
		#Cola waiting con pares (prioridad , proceso)
		self.waiting = []
		#proceso corriendo
		self.running = None
		#lista de procesos terminados
		self.finish = []

		self.askingForInput = False
		self.waitingForInput = False
		self.writingInput = False

	def setAskingForInput(self, value):
		self.askingForInput = value

	def getAskingForInput(self):
		return self.askingForInput

	def getWaitingForInput(self):
		return self.waitingForInput

	def setWaitingForInput(self, value):
		self.waitingForInput = value

	def getWritingInput(self):
		return self.writingInput

	def setWritingInput(self, value):
		self.writingInput = value	

	def schedule(self, time, process , delay):

		# print str(time) +": to new " + str( process.getId() ) + " > " + process.getName()
		heapq.heappush(self.new, (time+delay, process) )

	def run(self,time):
		self.processNew(time)
		self.processRunning(time)
		self.processReady(time)
		self.processWaiting(time)
	def processNew(self,time):
		try:
			flag = True	
			while (flag):
				first = self.new[0]

				if( first[0] == time ):
					process = heapq.heappop(self.new)[1]
					heapq.heappush(self.ready, (process.getPriority() , process) )
					# print str(time) +": to ready " + str( process.getId() ) + " > " + process.getName()
				else:
					flag = False

		except IndexError:
			pass

	def processRunning(self,time):

		if(self.running != None):
			#if false means that needs input
			if ( self.running.runTimer() == False):
				heapq.heappush(self.waiting, (self.running.getPriority() ,  self.running))
				self.running = None
			#finish process
			elif(self.running.timer == 0):
				self.running.finish(time)
				self.finish.append(self.running)
				# print str(time) +": to finish " + str( self.running.getId() ) + " > " + self.running.getName()
				self.running = None

	def processWaiting(self,time):
		try:
			first = self.waiting[0]

			if( self.askingForInput == False  and self.writingInput == False ):
				self.askingForInput = True

		except IndexError: 
				pass

	def newContactInput(self,time ,contactName,contactNumber):
		try:
			first = self.waiting[0]

			if(first[1].getType()==5):
				first[1].setContactName(contactName)
				first[1].setContactNumber(contactNumber)
				self.askingForInput = False
				self.writingInput = False
				process = heapq.heappop(self.waiting)[1]
				heapq.heappush(self.ready, (process.getPriority() , process) )
			else:
				raise IndexError

		except IndexError: 
				print "Super Error"
	def llamar(self,time,numero,tejec):
		try:
			first = self.waiting[0]
			if(first[1].getType()==1):
				first[1].setNumero(numero)
				first[1].setTimer(tejec)
				self.askingForInput = False
				self.writingInput = False
				process = heapq.heappop(self.waiting)[1]
				heapq.heappush(self.ready, (process.getPriority(), process))
			else:
				raise IndexError
		except IndexError:
			print "Error"
	def mensaje(self,time,numero,mensaje):
		try:
			first = self.waiting[0]
			if(first [1].getType() == 3):
				first[1].setNumero(numero)
				first[1].setMsge(mensaje)
				self.askingForInput = False
				self.writingInput = False
				process = heapq.heappop(self.waiting)[1]
				heapq.heappush(self.ready, (process.getPriority(), process))
			else:
				raise IndexError
		except IndexError:
			print "Error"
	def processReady(self,time):
		if(self.running == None):
			try:
				process = heapq.heappop(self.ready)[1]
				self.running = process
				#print str(time) +": to running " + str( process.getId() ) + " > " + process.getName()

			except IndexError: 
				pass


	def printProcesses(self, timer):
		output = ""
		output += "Time: "+ str(timer) + "\n"
		output += "\n"
		output += "PID PRI STAT TYPE TIME NAME\n"
		if(self.running != None):
			output += self.running.printProcess("RUN") + "\n"
		for item in self.ready:
			output += item[1].printProcess("RDY") + "\n"
		for item in self.waiting:
			output += item[1].printProcess("WTN") + "\n"

		output += "\nPress enter to stop..."
		return output
