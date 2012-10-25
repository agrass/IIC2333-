from process import Process

class SendPosition(Process):
	def __init__(self, priority, name):
		Process.__init__(self, name, 7, priority)
		self.timer = 2
		# 0 no usa , 1 usa , 2 bloquea
		self.external = {'Pantalla': 0, 'Audifono': 0, 'Microfono': 0, 'GPS': 1, 'Enviar Info': 1, 'Recibir Info': 0}