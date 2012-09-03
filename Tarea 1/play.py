from process import Process

class Play(Process):
	def __init__(self, priority, name , timer):
		Process.__init__(self, name, 9, priority)
		self.timer = int(timer)