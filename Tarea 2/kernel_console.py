import multiprocessing , sys , time
from kernel import Kernel 

class KernelConsole:

	def __init__(self,clocktime):
		self.running = True
		self.readingInput = True
		self.writingContact = False
		self.hllamada = False
		self.waitbackend = False
		self.emsje = False
		self.clock = clocktime


	def run(self, frontend_conn,connQueue):

		self.clear()
		self.printMenu()

		while(self.running):
			self.readInput(frontend_conn,connQueue)

		print "\n###########	END  ########### \n"


	def clear(self):
		sys.stdout.write('\033[2J')
		sys.stdout.write('\033[H')
		sys.stdout.flush()

	def printMenu(self):
		print "\n###########	MENU  ########### \n"
		print "menu: Imprimir Menu"
		print "top: Funcion TOP"
		print "read: Cargar Archivo"
		print "1: Llamar"
		print "2: Enviar Mensaje"
		print "3: Ver Agenda de Contactos"
		print "4: Agregar Nuevo Contacto"
		print "5: Ver Historial de Llamadas"
		print "6: Ver Historial de Mensajes"
		print "q: Salir"
		print

	def readInput(self, frontend_conn,connQueue):
		
		contactInput=None
		input = None
		numero = None
		msje = None  
		
		if(self.readingInput):
			input = raw_input("Input: ")
		elif(self.writingContact):
			contactInput = raw_input("Enter Contact (name;number): ")
		elif(self.hllamada):
			numero = raw_input("Ingrese (numero;tiempollamada): ")
		elif(self.emsje):
			msje = raw_input("Ingrese (numero;msje): ")
		elif(self.waitbackend):
			backend_msg = frontend_conn.recv()
			if(backend_msg == "enable_input"):
				print "Finalizado"
				self.waitbackend = False
				self.readingInput = True
		else:
			input = raw_input()
			input = ""
			connQueue.put("terminateTop")
			self.readingInput = True
			self.clear()
			self.printMenu()

		if(input == "menu"):
			self.printMenu()
		elif(input == "read"):
			connQueue.put("read")
		elif(input == "top"):
			self.readingInput = False
			connQueue.put("top")
		elif(input == "3"):
			connQueue.put("contact_list")
		elif(input == "4"):
			connQueue.put("new_contact")
			backend_msg = frontend_conn.recv()
			self.writingContact = True
			self.readingInput = False
		elif(input == "5"):
			connQueue.put("calls_history")
		elif(input == "6"):
			connQueue.put("messages_history")
		elif(input == "q"):
			connQueue.put("quit")
			self.running = False
		elif(input == '1'):
			connQueue.put('hacer_llamada')
			backend_msg = frontend_conn.recv()
			self.hllamada = True
			self.readingInput = False
		elif(input == '2'):
			connQueue.put('enviar_msje')
			backend_msg = frontend_conn.recv()
			self.emsje = True
			self.readingInput = False

		if(numero != None):
			connQueue.put ("hllamada_input;"+numero)
			self.hllamada = False
			self.readingInput = False
			self.waitbackend = True
		if (contactInput != None):
			connQueue.put( "new_contact_input;"+contactInput )
			self.writingContact = False
			self.readingInput = True
		if(msje != None):
			connQueue.put("emsje;"+msje)
			self.emsje = False
			self.readingInput = False
			self.waitbackend=True

		time.sleep(self.clock)