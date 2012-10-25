from process import Process

class Music(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 10, priority)
		self.timer = int(timer)
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 1, 'Audifono': 1, 'Microfono': 0, 'GPS': 0, 'Enviar Info': 0, 'Recibir Info': 0}