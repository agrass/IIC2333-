import multiprocessing , sys , time
from kernel import Kernel
from kernel_console import KernelConsole

if __name__ == "__main__":
	def runKernel(backend_conn,connQueue,clocktime):
		kernel = Kernel(clocktime)
		kernel.run(backend_conn,connQueue)

	def runConsole():
		pass

	clocktime = 1.0

	#Clear todo
	with open("data/log.txt", "w") as file:
		file.truncate()
	with open("data/contact_list.txt", "w") as file:
		file.truncate()
	with open("data/received_messages.txt", "w") as file:
		file.truncate()
	with open("data/sent_messages.txt", "w") as file:
		file.truncate()


	#Objetos para comunicar front y back
	backend_conn, frontend_conn = multiprocessing.Pipe()
	connQueue = multiprocessing.Queue()

	kProcess = multiprocessing.Process(target=runKernel, args=(backend_conn,connQueue,clocktime))
	kProcess.start()

	kernel_console = KernelConsole(clocktime)
	kernel_console.run(frontend_conn,connQueue)

	#cProcess = multiprocessing.Process(target=runConsole, args=(k,))
	#cProcess.start()