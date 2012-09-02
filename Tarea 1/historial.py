class Historial:

	def Actualizar (self,tipo,numero,hora):
		hist = open('historial.txt','a+')
	
		hist.write('\r\n'+str(hora)+","+str(numero)+','+str(tipo))
		hist.close()
	def verHistorial(self):
		hist = open('historial.txt','r')
		linea = hist.readline()
		while linea != "":
			print linea
			linea = hist.readline()
		hist.close();