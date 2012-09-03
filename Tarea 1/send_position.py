from process import Process

class SendPosition(Process):
	def __init__(self, priority, name):
		Process.__init__(self, name, 7, priority)
		self.timer = 2