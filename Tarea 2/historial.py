class Historial:

	def Actualizar (self,tipo,numero,hora, tiempo):
		hist = open('data/historial.txt','a+')
	
		hist.write('\r\n'+str(hora)+","+str(numero)+','+str(tiempo)+','+str(tipo))
		hist.close()
	def verHistorial(self):
		hist = open('data/historial.txt','r')
		linea = hist.readline()
		while linea != "":
			print linea
			linea = hist.readline()
		hist.close();
	def verHistorialMsge(self):
		hist = open('data/sent_messages.txt','r')
		linea = hist.readline()
		while linea != "":
			print linea
			linea = hist.readline()
		hist.close();
	def verHistorialMsgeRec(self):
		hist = open('data/received_messages.txt','r')
		linea = hist.readline()
		while linea !="":
			print linea
			linea = hist.readline()
		hist.close();