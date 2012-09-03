from process import Process

class Other(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 6, priority)
		self.timer = int(timer)