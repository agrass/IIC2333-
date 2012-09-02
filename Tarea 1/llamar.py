from process import Process
class Llamar(Process):
	def __init__(self,name,type,priority,numero,tejec):
		Process.init(self,name,type,priority)
		self.numero = numero;
		self.tejec = tejec;
	def getNumero(self):
		return self.numero;
	def getTEjec(self):
		return self.tejec;
	def historial():
		archivo = open("historial.txt","w");
		
		
	