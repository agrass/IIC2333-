from process import Process

class Music(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 10, priority)
		self.timer = int(timer)