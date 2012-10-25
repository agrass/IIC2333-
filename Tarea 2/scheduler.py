import heapq
from process import Process
import itertools

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
		#locks para los perifericos 1 locked 0 unlocked
		self.locks = {'Pantalla': 0, 'Audifono': 0, 'Microfono': 0, 'GPS': 0, 'Enviar Info': 0, 'Recibir Info': 0}
		#tiempo para cada ronda
		self.roundRobinTime = 2

		self.counter = itertools.count()

		self.askingForInput = False
		self.waitingForInput = False
		self.writingInput = False

		self.rrtimer = self.roundRobinTime
		
		self.enableInput=False

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

	def getEnableInput(self):
		return self.enableInput

	def setEnableInput(self, value):
		self.enableInput = value	

	def schedule(self, time, process , delay):
		#print str(time) +": to new " + str( process.getId() ) + " > " + process.getName()
		heapq.heappush(self.new, (time+delay, process) )

	def run(self,time):
		self.processNew(time)
		self.processRunning(time)
		self.processReady(time)
		self.processWaiting(time)
		#Envejecimiento
		if (time % 2 == 0):
			self.growOlder()

	def processNew(self,time):
		try:
			flag = True	
			while (flag):
				first = self.new[0]

				if( first[0] == time ):
					process = heapq.heappop(self.new)[1]
					count = next(self.counter)
					heapq.heappush(self.ready, (process.getPriority() ,count, process) )

					#print str(time) +": to ready " + str( process.getId() ) + " > " + process.getName()
				else:
					flag = False

		except IndexError:
			pass

	def processRunning(self,time):

		if(self.running != None):

			self.rrtimer -= 1
			#if false means that needs input
			if ( self.running.runTimer() == False):
				self.rrtimer = self.roundRobinTime
				#print str(time) +": to waiting " + str( self.running.getId() ) + " > " + self.running.getName()
				heapq.heappush(self.waiting, (self.running.getPriority() ,  self.running))
				self.running = None
			#finish process
			elif(self.running.timer == 0):
				self.rrtimer = self.roundRobinTime
				#return True if needs enable input
				if (self.running.finish(time) ):
					self.enableInput = True
				self.releaseLocks(self.running)
				self.finish.append(self.running)
				#print str(time) +": to finish " + str( self.running.getId() ) + " > " + self.running.getName()
				self.running = None
			elif(len(self.ready) != 0):
				# self.ready[0][1].getPriority() < self.running.getPriority()
				# Context change
				if(self.rrtimer <= 0):
					self.rrtimer = self.roundRobinTime
					self.running.resetPriority()
					count = next(self.counter)
					heapq.heappush(	self.ready, (self.running.getPriority(),count, self.running)	)
					self.running = heapq.heappop(self.ready)[2]

	def processWaiting(self,time):
		try:
			first = self.waiting[0]

			if( self.askingForInput == False  and self.writingInput == False ):
				self.askingForInput = True

		except IndexError: 
				pass

	def growOlder(self):
		for item in self.ready :
			item[2].grow()

	def newContactInput(self,time ,contactName,contactNumber):
		try:
			first = self.waiting[0]

			if(first[1].getType()==5):
				first[1].setContactName(contactName)
				first[1].setContactNumber(contactNumber)
				self.askingForInput = False
				self.writingInput = False
				process = heapq.heappop(self.waiting)[1]
				count = next(self.counter)
				heapq.heappush(self.ready, (process.getPriority() ,count, process) )
			else:
				raise IndexError

		except IndexError: 
				print "Error"

	def llamar(self,time,numero,tejec):
		try:
			first = self.waiting[0]

			if(first[1].getType()==1):
				first[1].setNumero(numero)
				first[1].setTimer(tejec)
				self.askingForInput = False
				self.writingInput = False
				process = heapq.heappop(self.waiting)[1]
				count = next(self.counter)
				heapq.heappush(self.ready, (process.getPriority(),count, process))
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
				count = next(self.counter)
				heapq.heappush(self.ready, (process.getPriority(), count, process))
			else:
				raise IndexError
		except IndexError:
			print "Error"

	def processReady(self,time):
		if(self.running == None):
			try:
				process = heapq.heappop(self.ready)[2]
				self.running = process
				self.aquireLocks(self.running)
				#print str(time) +": to running " + str( process.getId() ) + " > " + process.getName()

			except IndexError: 
				pass

	def aquireLocks(self,process):
		externals = process.getExternals()
		for key in externals :
			if(externals[key] == 2) :# Block
				self.locks[key] == 1

	def releaseLocks(self,process):
		externals = process.getExternals()
		for key in externals :
			if(externals[key] == 2) :# Block
				self.locks[key] == 0

	def printProcesses(self, timer):
		output = ""
		output += "Time: "+ str(timer) + "\n"
		output += "\n"
		output += "PID PRI STAT TYPE TIME NAME\n"

		if(self.running != None):
			output += self.running.printProcess("RUN") + "\n"
		for item in self.ready:
			output += item[2].printProcess("RDY") + "\n"
		for item in self.waiting:
			output += item[2].printProcess("WTN") + "\n"

		output += "\nPress enter to stop..."
		return output
