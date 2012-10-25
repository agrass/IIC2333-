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
		#locks para los perifericos Process = locked None = unlocked
		self.locks = {'Pantalla': None, 'Audifono': None, 'Microfono': None, 'GPS': None, 'Enviar Info': None, 'Recibir Info': None}
		#tiempo para cada ronda
		self.roundRobinTime = 2

		self.counter = itertools.count()

		self.askingForInput = False
		self.waitingForInput = False
		self.writingInput = False

		self.rrtimer = self.roundRobinTime
		
		self.enableInput=False

		self.processWaitingForInput = None

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
		if (time % 5 == 0):
			self.growOlder()

	def processNew(self,time):
		try:
			flag = True	
			while (flag):
				first = self.new[0]

				if( first[0] == time ):
					process = heapq.heappop(self.new)[1]
					count = next(self.counter)
					heapq.heappush(self.ready, [process.getPriority() ,count, process] )

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
				entry = [self.running.getPriority() ,  self.running]
				heapq.heappush(self.waiting, entry )
				self.processWaitingForInput = entry
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
					heapq.heappush(	self.ready, [self.running.getPriority(),count, self.running]	)
					self.running = None

	def processWaiting(self,time):

		for item in self.waiting :

			if(item[1].getBlockedFlag()):

				externals = item[1].getExternals()
				isBlocked = False

				for key in externals :
					if( (externals[key] == 2 or externals[key] == 1) and (self.locks[key] != None) ): # Blocked
						isBlocked=True

				if(	not isBlocked ):
					item[1].setBlockedFlag(False)
					count = next(self.counter)
					heapq.heappush(	self.ready, [item[1].getPriority(), count, item[1]]	)
					self.waiting.remove(item)

		if( self.processWaitingForInput != None and self.askingForInput == False  and self.writingInput == False ):
			self.askingForInput = True


	def growOlder(self):
		for item in self.ready :
			item[2].grow()
			item[0] = item[2].getPriority()

	def newContactInput(self,time ,contactName,contactNumber):
		try:
			first = self.processWaitingForInput[1]

			if(first.getType()==5):
				first.setContactName(contactName)
				first.setContactNumber(contactNumber)
				self.askingForInput = False
				self.writingInput = False
				self.waiting.remove(self.processWaitingForInput)
				count = next(self.counter)
				heapq.heappush(self.ready, [first.getPriority() ,count, first] )
				self.processWaitingForInput= None
			else:
				raise IndexError

		except IndexError: 
				print "Error"

	def llamar(self,time,numero,tejec):
		try:
			first = self.processWaitingForInput[1]

			if(first.getType()==1):
				first.setNumero(numero)
				first.setTimer(tejec)
				first.setDuracion(tejec)
				self.askingForInput = False
				self.writingInput = False
				self.waiting.remove(self.processWaitingForInput)
				count = next(self.counter)
				heapq.heappush(self.ready, [first.getPriority(),count, first])
				self.processWaitingForInput= None
			else:
				raise IndexError
		except IndexError:
			print "Error"

	def mensaje(self,time,numero,mensaje):
		try:
			first = self.processWaitingForInput[1]
			if(first.getType() == 3):
				first.setNumero(numero)
				first.setMsge(mensaje)
				self.askingForInput = False
				self.writingInput = False
				self.waiting.remove(self.processWaitingForInput)
				count = next(self.counter)
				heapq.heappush(self.ready, [first.getPriority(), count, first])
				self.processWaitingForInput= None
			else:
				raise IndexError
		except IndexError:
			print "Error"

	def processReady(self,time):
		if(self.running == None):
			try:
				process = heapq.heappop(self.ready)[2]
				
				externals = process.getExternals()
				isBlocked = False
				for key in externals :
						if( (externals[key] == 2 or externals[key] == 1) and (self.locks[key] != None) ): # Blocked
							if( not (self.locks[key] == process) ):
								isBlocked=True
				if(isBlocked):
					#print "["+str(time)+"] "+str(process.getId()) + " is Blocked"
					process.resetPriority()
					process.setBlockedFlag(True)
					entry = [process.getPriority() ,  process]
					heapq.heappush(self.waiting, entry )
					self.processReady(time)
				else:
					#print "["+str(time)+"] "+str(process.getId()) + " is not Blocked"
					self.running = process
					self.aquireLocks(self.running)
					#print str(time) +": to running " + str( process.getId() ) + " > " + process.getName()

			except IndexError: 
				pass
				#print "["+str(time)+"] None in ready"

	def aquireLocks(self,process):
		externals = process.getExternals()
		for key in externals :

			if(externals[key] == 2) :# Block
				self.locks[key] = process

	def releaseLocks(self,process):
		externals = process.getExternals()
		for key in externals :
			if(externals[key] == 2 and self.locks[key] == process) :# Block
				self.locks[key] = None

	def printProcesses(self, timer):
		output = ""
		output += "Time: "+ str(timer) + "\n"
		output += "\n"
		output += "PID PRI STAT TYPE TIME NAME\n"

		if(self.running != None):
			output += self.running.printProcess("RUN") + "\n"
		for item in self.ready:
			output += item[2].printProcess("RDY")+"\n"
		for item in self.waiting:
			output += item[1].printProcess("WTN") + "\n"
		output += "\n [ "
		for key in self.locks :
			if(self.locks[key]):
				output += key + ": "+str(self.locks[key].getId())+" "
			else:
				output += key + ": None "
		output += "] \n"
		output += "\nPress enter to stop..."
		return output
