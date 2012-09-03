from process import Process
from historial import Historial
import datetime

class Llamar(Process):
	def __init__(self,name,type,priority,numero):
		Process.__init__(self,name,type,priority)
		self.numero = numero;
		self.hist = Historial()
	def getNumero(self):
		return self.numero;
	def setTejec(self, duracion):
		self.duracion = duracion
	def runTimer(self):
		self.tini = datetime.datetime.now()
		print "Llamando a ...", self.numero
		self.fin = raw_input("Para finalizar presione 1: ")
		if(self.fin=='1'):
			self.tfin=datetime.datetime.now()
			self.duracion = self.tfin-self.tini
			print "Llamada finalizada.  Duracion: ", self.duracion
			self.hist.Actualizar('llamada',self.numero, self.tini)

			
		
		
		
	
		
		
	