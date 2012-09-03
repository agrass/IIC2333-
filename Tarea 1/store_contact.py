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
		f = open('data/log.txt', 'a')		
		f.write("finish : (" + str(self.getId()) + ") "+ self.getName() + " at time: "+ str(time) )
		f.write("\n")		
		f.close() 

		f = open('data/contact_list.txt', 'a')		
		f.write( self.getContactName() + " "+self.getContactNumber() )
		f.write("\n")		
		f.close() 
	