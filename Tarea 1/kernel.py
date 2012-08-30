import time , sys
from scheduler import Scheduler
from process import Process

class Kernel:

	def __init__(self):
		self.scheduler = Scheduler()
		self.running = True
		self.topActive = False

	def run(self,backend_conn,connQueue):
		self.i=0
		while self.running:
			#print str(self.i)
			self.scheduler.run(self.i)
			self.checkInput(self.i,connQueue)
			self.i += 1
			time.sleep(1)

	def checkInput(self,time, connQueue):
		try:
			input = connQueue.get_nowait()
		except Exception:
			return

		if(input != None):
			if(input == "read"):
				self.readFile(time)
			elif(input == "top"):
				self.top()
			elif(input == "quit" ):
				self.running = False

	def top(self):
		self.topActive = True
		char_matrix = []
		print "PID PRI STAT TYPE"
		self.scheduler.printProcesses()

	def readFile(self,time):
		with open('test.txt', 'r') as file:
			process_list = []
			for line in file:

				split = line.split(";")
				process_type =  split[2]

				if   process_type == "1":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "2":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "3":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "4":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "5":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "6":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "7":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "8":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "9":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "10":
					process = Process( split[0], split[2], split[3] )

				process_list.append(process)

			for p in process_list:
				self.scheduler.schedule(time,p,1)

