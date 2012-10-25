from process import Process

class CheckPosition(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 8, priority)
		self.timer = timer
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 1, 'Audifono': 0, 'Microfono': 0, 'GPS': 1, 'Enviar Info': 0, 'Recibir Info': 0}