from process import Process

class CheckPosition(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 8, priority)
		self.timer = timer