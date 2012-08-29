import multiprocessing , sys , time
from kernel import Kernel 

class KernelConsole:

	def __init__(self):
		self.running = True
		self.readingInput = True

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
		print "top: Funcion TOP"
		print "read: Cargar Archivo"
		print "1: Llamar"
		print "2: Recibir Llamada"
		print "3: Enviar Mensaje"
		print "4: Recibir Mensaje"
		print "q: Salir"
		print

	def readInput(self, frontend_conn,connQueue):
		if(self.readingInput):
			input = raw_input("Input :")

		if(input == "read"):
			connQueue.put("read")
		elif(input == "q"):
			connQueue.put("quit")
			self.running = False

		time.sleep(1)