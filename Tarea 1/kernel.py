import time
from scheduler import Scheduler
from process import Process

class Kernel:

	def __init__(self):
		self.scheduler = Scheduler()
		self.running = True

	def run(self):
		i=1
		while self.running:
			print i
			i += 1
			time.sleep(1)

	def readFile(self):
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
				print str( p.getId() )+": "+p.getName()

kernel = Kernel()
kernel.readFile()
