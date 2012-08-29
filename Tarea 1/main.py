import multiprocessing , sys , time
from kernel import Kernel
from kernel_console import KernelConsole

if __name__ == "__main__":

	def runKernel(backend_conn,connQueue):
		kernel = Kernel()
		kernel.run(backend_conn,connQueue)

	def runConsole():
		pass

	#Objetos para comunicar front y back
	backend_conn, frontend_conn = multiprocessing.Pipe()
	connQueue = multiprocessing.Queue()

	kProcess = multiprocessing.Process(target=runKernel, args=(backend_conn,connQueue))
	kProcess.start()

	kernel_console = KernelConsole()
	kernel_console.run(frontend_conn,connQueue)

	#cProcess = multiprocessing.Process(target=runConsole, args=(k,))
	#cProcess.start()