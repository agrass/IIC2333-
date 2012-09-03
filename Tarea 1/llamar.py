from process import Process
from historial import Historial
import datetime

class Llamar(Process):
	def __init__(self,name,type,priority,numero):
		Process.__init__(self,name,type,priority)
		self.numero = numero;
		self.hist = Historial()
	def setNumero(self,numero):
		self.numero = numero;
	def getNumero(self):
		return self.numero;
	def setTejec(self, duracion):
		self.duracion = duracion
	def runTimer(self):
		self.tini = datetime.datetime.now()
		self.timer -= 1
		if(self.numero == ""):
			return False
		else:	
			if(self.timer>0):
				print "Llamando a ...", self.numero
				return True
			else:
				return False
	def setFin(self, fin):
		self.fin= fin
	def finalizar (self,time):
		self.tfin=datetime.datetime.now()
		self.duracion = self.tfin-self.tini
		print "Llamada finalizada.  Duracion: ", self.duracion
		self.hist.Actualizar('llamada',self.numero, self.tini)

		
	
			
		
		
		
	
		
		
	