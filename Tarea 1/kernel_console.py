import multiprocessing , sys , time
from kernel import Kernel 

class KernelConsole:

	def __init__(self):
		self.running = True
		self.readingInput = True
		self.writingContact = False
		self.hllamada = False

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
		print "2: Recibir Llamada"
		print "3: Enviar Mensaje"
		print "4: Recibir Mensaje"
		print "5: Ver Agenda de Contactos"
		print "6: Agregar Nuevo Contacto"
		print "7: Ver Historial de Llamadas"
		print "8: Ver Historial de Mensajes"
		print "q: Salir"
		print

	def readInput(self, frontend_conn,connQueue):
		
		contactInput=None
		input = None
		numero = None
		if(self.readingInput):
			input = raw_input("Input: ")
		elif(self.writingContact):
			contactInput = raw_input("Enter Contact (name;number): ")
		elif(self.hllamada):
			numero = raw_input("Ingrese numero: ")
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
		elif(input == "5"):
			connQueue.put("contact_list")
		elif(input == "6"):
			connQueue.put("new_contact")
			backend_msg = frontend_conn.recv()
			self.writingContact = True
			self.readingInput = False
		elif(input == "7"):
			connQueue.put("calls_history")
		elif(input == "8"):
			connQueue.put("messages_history")
		elif(input == "q"):
			connQueue.put("quit")
			self.running = False
		elif(input == '1'):
			connQueue.put('hacer_llamada')
			backend_msg = frontend_conn.recv()
			self.hllamada = True
			self.readingInput = False
			
		if(numero != None):
			connQueue.put ("hllamada_input"+numero)
			self.hllamada = False
			self.readingInput = True

		if (contactInput != None):
			connQueue.put( "new_contact_input;"+contactInput )
			self.writingContact = False
			self.readingInput = True

		time.sleep(1)