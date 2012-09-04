from process import Process

class StoreContact(Process):
	def __init__(self, priority, name, contactName, contactNumber):
		Process.__init__(self, name, 5, priority)
		self.contactName = contactName
		self.contactNumber = contactNumber

	def runTimer(self):
		#means no number
		if(self.contactName == "" and self.contactNumber == ""):
			return False
		else:
			self.timer -= 1
			return True

	def getContactName(self):
		return self.contactName

	def getContactNumber(self):
		return self.contactNumber

	def setContactName(self,contactName):
		self.contactName = contactName

	def setContactNumber(self,contactNumber):
		self.contactNumber = contactNumber

	def finish(self,time):		
		self.writeLog("El contacto fue agregado con exito", time)
		f = open('data/contact_list.txt', 'a')		
		f.write( self.getContactName() + ":"+self.getContactNumber() )
		f.write("\n")		
		f.close() 

		return False
	