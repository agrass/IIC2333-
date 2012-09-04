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
	def __init__(self, priority, message= ""):
		Process.__init__(self, 'Recive Message', 4, priority)
		self.message = message
		self.timer = 20 * len(message)
		self.saveMessage()
    #guardar output message    
	def saveMessage(self):		
		f = open('data/received_messages.txt', 'a')		
		f.write(self.message)
		f.write("\n")		
		f.close() 


#proceso mandar mensaje, tengo la duda con respecto a escribir mensaje en consola
class sendMessage(Process):
	def __init__(self, priority, message, numero):
		Process.__init__(self, "Send Message", 3, priority)		
		self.message = message
		self.numero = numero
		self.timer = int(0.02*len(message)) + 1
		self.printOnce=True
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
		self.writeLog("Mensaje enviado", time)
		print "Mensaje enviado!"
		tiempo = datetime.datetime.now()
		self.saveMessage(tiempo)
		return True
	def saveMessage(self,tiempo):		
		f = open('data/sent_messages.txt', 'a+')		
		f.write(str(tiempo)+' '+str(self.numero)+' '+str(self.message))
		f.write("\r\n")		
		f.close()    

	