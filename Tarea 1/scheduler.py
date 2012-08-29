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

	def schedule(self, time, process , delay):
		print str(time) +": to new " + str( process.getId() ) + " > " + process.getName()
		heapq.heappush(self.new, (time+delay, process) )

	def run(self,time):
		self.processNew(time)
		self.processRunning(time)
		self.processReady(time)

	def processNew(self,time):
		try:
			flag = True	
			while (flag):
				first = self.new[0]

				if( first[0] == time ):
					process = heapq.heappop(self.new)[1]
					heapq.heappush(self.ready, (process.getPriority() , process) )
					print str(time) +": to ready " + str( process.getId() ) + " > " + process.getName()
				else:
					flag = False

		except IndexError: 
  				pass

	def processRunning(self,time):

		if(self.running != None):
			self.running.runTimer()

			#finish process
			if(self.running.timer == 0):
				self.finish.append(self.running)
				print str(time) +": to finish " + str( self.running.getId() ) + " > " + self.running.getName()
				self.running = None

	def processReady(self,time):
		if(self.running == None):
			try:
				process = heapq.heappop(self.ready)[1]
				self.running = process
				print str(time) +": to running " + str( process.getId() ) + " > " + process.getName()

			except IndexError: 
  				pass
