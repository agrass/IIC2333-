from process import Process

class Other(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 6, priority)
		self.timer = int(timer)
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 1, 'Audifono': 1, 'Microfono': 1, 'GPS': 1, 'Enviar Info': 1, 'Recibir Info': 1}