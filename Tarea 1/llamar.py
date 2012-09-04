from process import Process
from historial import Historial
import datetime

class Llamar(Process):
	def __init__(self,name,priority,numero):
		Process.__init__(self,name,1,priority)
		self.numero = numero;
		self.hist = Historial()
		self.printsOnce = True
	def setNumero(self,numero):
		self.numero = numero;
	def getNumero(self):
		return self.numero;
	def runTimer(self):
		if(self.numero == ""):
			return False
		else:	
			if(self.timer>=0):
				self.timer -= 1
				if(self.printsOnce):
					print "Llamando a ...", self.numero
					self.printsOnce = False
				return True
	def setFin(self, fin):
		self.fin= fin
	def finish (self,time):		
		self.writeLog("LLamada finalizada", time)
		print "Llamada finalizada."
		self.hist.Actualizar('llamada',self.numero, time)
		
		return True

		
	
			
		
		
		
	
		
		
	