import time , sys, os
from scheduler import Scheduler
from process import Process
from store_contact import StoreContact

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
			
			if(self.scheduler.getAskingForInput() ):
				self.scheduler.setWaitingForInput(True)

			if(self.scheduler.getWaitingForInput()):
				backend_conn.send("readyForInput")
				self.scheduler.setWaitingForInput(False)
				self.scheduler.setAskingForInput(False)
				self.scheduler.setWritingInput(True)

			self.checkInput(self.i,connQueue)
			self.i += 1

			if(self.topActive == True):
				self.top()
			
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
				self.topActive = True
			elif(input == "terminateTop"):
				self.topActive = False
			elif(input == "contact_list"):
				self.readContactList(time)
			elif(input == "new_contact"):
				self.newContact(time)
			elif( input.startswith("new_contact_input") ):
				split = input.split(";")
				contactName =  split[1]
				contactNumber = split[2]
				self.scheduler.newContactInput(time,contactName,contactNumber)
			elif(input == "quit" ):
				self.running = False

	def newContact(self,time):
		print "Wating to run new contact ..."
		
		# 5 default priority
		process = StoreContact ( 5 , "nuevo_contacto" , "" , "" )
		# 0 delay
		self.scheduler.schedule(time,process,1)

	def top(self):
		os.system('cls' if os.name=='nt' else 'clear')
		char_matrix = []
		print "Time: "+ str(self.i)
		print
		print "PID PRI STAT TYPE NAME"
		self.scheduler.printProcesses()
		print "\nPress enter to stop..."
		
	def readContactList(self,time):
		os.system('cls' if os.name=='nt' else 'clear')
		print "CONTACTS"
		print
		with open('data/contact_list.txt', 'r') as file:
			for line in file:
				print line

	def readFile(self,time):
		with open('test.txt', 'r') as file:
			for line in file:

				split = line.split(";")

				process = None

				process_type =  split[2]
				delay = int(split[1])

				if   process_type == "1":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "2":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "3":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "4":
					process = Process( split[0], split[2], split[3] )
				elif process_type == "5":
					process = StoreContact ( split[3] , split[0] , split[4] , split[5] )
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
				
				if(process != None):
					self.scheduler.schedule(time,process,delay)


			print "> Read file test.txt"

