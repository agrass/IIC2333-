from process import Process
from historial import Historial
import datetime

class Llamar(Process):
	def __init__(self,name,priority,numero):
		Process.__init__(self,name,1,priority)
		self.numero = numero;
		self.duracion = -1
		self.hist = Historial()
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 1, 'Audifono': 2, 'Microfono': 2, 'GPS': 0, 'Enviar Info': 1, 'Recibir Info': 1}
		if(numero == ""):
			self.printsOnce = True
			self.flag = True
		else:
			self.printsOnce = False
			self.flag = False
	def setNumero(self,numero):
		self.numero = numero;
	def getNumero(self):
		return self.numero;
	def setDuracion(self,value):
		self.duracion=int(value)
	def runTimer(self):
		if(self.numero == ""):
			return False
		else:	
			if(self.timer>=0):
				self.timer -= 1
				if(self.printsOnce):
					print "Llamada a ...", self.numero
					self.printsOnce = False
				return True
	def setFin(self, fin):
		self.fin= fin
	def finish (self,time):
		
		f = open('data/log.txt', 'a')	
		hora = datetime.datetime.now()
		sthora = str(hora)
		f.write("finish : (" + str(self.getId()) + ") "+ self.getName() + " at time: "+ str(time)+' duration: '+str(self.duracion) )

		f.write("\n")		
		f.close() 
		self.hist.Actualizar('llamada saliente',self.numero, sthora,time)
		
		return self.flag

class recibirLlamada(Process):

	def __init__(self,name,priority,numero,duracion):
		Process.__init__(self,name,2,priority)
		self.numero = numero;
		self.hist = Historial()
		self.duracion = int(duracion)
		self.timer = int(duracion)
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 1, 'Audifono': 2, 'Microfono': 2, 'GPS': 0, 'Enviar Info': 1, 'Recibir Info': 1}

	def finish (self,time):
		hora = datetime.datetime.now()
		sthora = str(hora)
		f = open('data/log.txt', 'a')		
		f.write("finish : (" + str(self.getId()) + ") "+ self.getName() + " at time: "+ str(time)+' duration: '+str(self.duracion) )
		f.write("\n")		
		f.close() 

		self.hist.Actualizar('llamada entrante',self.numero,sthora, time)


		
	
			
		
		
		
	
		
		
	