import sys
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
	def __init__(self, priority, message= ""):
		Process.__init__(self, "Send Message", 3, priority)
		if len(message) == 0:
			message = raw_input("Escribe mensaje: ")		
		self.message = message
		self.timer = 20*len(message)
		self.saveMessage()
    #guardar output message    
	def saveMessage(self):		
		f = open('data/sent_messages.txt', 'a')		
		f.write(self.message)
		f.write("\n")		
		f.close()    

if __name__ == "__main__":
	receiveMessage(3, "Mensaje prueba 1")	
	receiveMessage( 3, "Mensaje Prueba 2")
	receiveMessage(3)
	sendMessage(1)

	getReceivedMessages()

	