import time , sys, os
from scheduler import Scheduler
from process import Process
from llamar import Llamar
from llamar import recibirLlamada
from store_contact import StoreContact
from other import Other
from send_position import SendPosition
from check_position import CheckPosition
from play import Play
from music import Music
from historial import Historial
from message import sendMessage
from message import receiveMessage

class Kernel:

	def __init__(self,clocktime):
		self.scheduler = Scheduler()
		self.running = True
		self.topActive = False
		self.clock = clocktime

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

			if ( self.scheduler.getEnableInput() ):
				backend_conn.send("enable_input")
				self.scheduler.setEnableInput(False)


			self.checkInput(self.i,connQueue)
			self.i += 1

			if(self.topActive == True):
				self.top()
			
			time.sleep(self.clock)

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
			elif(input == "hacer_llamada"):
				self.hacerLlamada(time)
			elif( input.startswith("new_contact_input") ):
				split = input.split(";")
				contactName =  split[1].rstrip('\r\n')
				contactNumber = split[2].rstrip('\r\n')
				self.scheduler.newContactInput(time,contactName,contactNumber)
			elif(input == "calls_history"):
				self.callsHistory()
			elif(input == "messages_history"):
				self.messagesHistory()
			elif(input.startswith('hllamada_input')):
				split = input.split(';')
				numero = split[1]
				tejec = int(split[2])
				self.scheduler.llamar(time,numero,tejec)
			elif(input.startswith('emsje')):
				split = input.split(';')
				numero = split [1]
				mensaje = split [2]
				self.scheduler.mensaje(time,numero,mensaje)
			elif(input == "quit" ):
				self.running = False
			elif(input == "enviar_msje"):
				self.enviarMsje(time)
	def enviarMsje(self,time):
		print "Waiting to run send msg..."
		process = sendMessage("enviar_msje",0,"","")
		self.scheduler.schedule(time,process,1)

				
	def hacerLlamada(self,time):
		print "Waiting to run make call..."
		processl = Llamar('hacer_llamada',0,"")
		self.scheduler.schedule(time, processl,1)

	def newContact(self,time):
		print "Wating to run new contact ..."
		
		# 1 default priority
		process = StoreContact ( 1 , "nuevo_contacto" , "" , "" )
		# 0 delay
		self.scheduler.schedule(time,process,1)

	def top(self):
		os.system('cls' if os.name=='nt' else 'clear')
		print self.scheduler.printProcesses(self.i)

	def callsHistory(self):
		os.system('cls' if os.name=='nt' else 'clear')
		print "Historial de Llamadas\n"
		hist = Historial()
		hist.verHistorial()
		print  "\r\n \r\n ##### FIN HISTORIAL LLAMADAS ##### \r\n \r\n"
		

	def messagesHistory(self):
		os.system('cls' if os.name=='nt' else 'clear')
		output = "Historial de Mensajes\n\n"
		output += "Mensajes Recibidos:\n\n"
		hist = Historial()
		print 'Historial de Mensajes Recibidos\n'
		hist.verHistorialMsgeRec()

		print "\r\n Historial de Mensajes Enviados\r\n"
		
		hist.verHistorialMsge()
		print  "\r\n \r\n ##### FIN HISTORIAL MENSAJES ##### \r\n \r\n"
		
	def readContactList(self,time):
		os.system('cls' if os.name=='nt' else 'clear')
		print "CONTACTS"
		print
		with open('data/contact_list.txt', 'r') as file:
			for line in file:
				sys.stdout.write(line)
		print

	def readFile(self,time):
		with open('test.txt', 'r') as file:
			for line in file:

				split = line.split(";")

				process = None

				process_type =  split[2]
				delay = int(split[1])

				if process_type == "1":
					process = Llamar( split[0], split[3] , split[4])
					process.setTimer( split[5] )
					process.setDuracion( split[5] )
				elif process_type == "2":
					process = recibirLlamada( split[0], split[3], split[4], split[5] )
				elif process_type == "3":
					process = sendMessage( split[0], split[3], split[5], split[4] )
				elif process_type == "4":
					process = receiveMessage( split[0],split[3],split[5],split[4] )
				elif process_type == "5":
					process = StoreContact ( split[3] , split[0] , split[4].rstrip('\r\n') , split[5].rstrip('\r\n') )
				elif process_type == "6":
					process = Other( split[3] , split[0] , split[4])
				elif process_type == "7":
					process = SendPosition( split[3] , split[0])
				elif process_type == "8":
					process = CheckPosition( split[3] , split[0] , split[4])
				elif process_type == "9":
					process = Play( split[3] , split[0] , split[4])
				elif process_type == "10":
					process = Music( split[3] , split[0] , split[4])
				
				if(process != None):
					self.scheduler.schedule(time,process,delay)


			print "> Read file test.txt"

