import sys
import datetime
# Add the main folder path to the sys.path list
sys.path.append('../')
# Now you can import your module
from process import Process

#leer todos los mensajes guardados
def getReceivedMessages():		
	f = open('data/received_messages.txt', 'r')		
	for line in f:
		print line
	f.close() 
def getSentMessages():		
	f = open('data/received_messages.txt', 'r')		
	for line in f:
		print line
	f.close() 

#proceso recivir mensajes
class receiveMessage(Process):
	def __init__(self, name , priority, message, numero):
		Process.__init__(self, name, 4, priority)
		self.message = message
		self.numero = numero
		self.timer = int(0.02* len(message))+1	
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 0, 'Audifono': 1, 'Microfono': 0, 'GPS': 0, 'Enviar Info': 1, 'Recibir Info': 1}

    #guardar output message    
	def saveMessage(self,tiempo):		
		f = open('data/received_messages.txt', 'a')		
		f.write(str(tiempo)+' from: '+str(self.numero)+' =>'+str(self.message))
		f.write("\n")		
		f.close() 

	def finish (self, time):
		f = open('data/log.txt', 'a')		
		f.write("finish : (" + str(self.getId()) + ") "+ self.getName() + " at time: "+ str(time) )
		f.write("\n")		
		f.close() 
		tiempo = datetime.datetime.now()
		self.saveMessage(tiempo)
		return False

#proceso mandar mensaje, tengo la duda con respecto a escribir mensaje en consola
class sendMessage(Process):
	def __init__(self,name, priority, message, numero):
		Process.__init__(self, name, 3, priority)		
		self.message = message
		self.numero = numero
		self.timer = int(0.02*len(message)) + 1
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 0, 'Audifono': 1, 'Microfono': 0, 'GPS': 0, 'Enviar Info': 1, 'Recibir Info': 1}
		if (numero == ""):
			self.printOnce=True
			self.flag = True
		else:
			self.printOnce=False
			self.flag = False
		
	def setNumero(self,numero):
		self.numero = numero
	def getNumero(self):
		return self.numero
	def setMsge(self,message):
		self.message = message
		self.timer = int(0.02*len(message)) + 1
	def runTimer(self):
		if(self.numero == ""):
			return False
		else:
			if(self.timer>=0):
				if(self.printOnce):
					print "Enviando mensaje ..."
					self.printOnce = False
				self.timer -=1
				return True
			else:
				return False
    #guardar output message  
	def finish (self, time):
		f = open('data/log.txt', 'a')		
		f.write("finish : (" + str(self.getId()) + ") "+ self.getName() + " at time: "+ str(time) )
		f.write("\n")		
		f.close() 

		tiempo = datetime.datetime.now()
		self.saveMessage(tiempo)
		return self.flag
	def saveMessage(self,tiempo):		
		f = open('data/sent_messages.txt', 'a+')		
		f.write(str(tiempo)+' to: '+str(self.numero)+' => '+str(self.message))
		f.write("\r\n")		
		f.close()    

	