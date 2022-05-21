from colorama import init, Fore, Back, Style
import os
import platform
init(autoreset = True)
class FColor:
	BLACK = Fore.BLACK
	RED = Fore.RED
	GREEN = Fore.GREEN
	YELLOW = Fore.YELLOW
	BLUE = Fore.BLUE
	MAGENTA = Fore.MAGENTA
	CYAN = Fore.CYAN
	WHITE = Fore.WHITE
	RESET = Fore.RESET

class BColor:
	BLACK = Back.BLACK
	RED = Back.RED
	GREEN = Back.GREEN
	YELLOW = Back.YELLOW
	BLUE = Back.BLUE
	MAGENTA = Back.MAGENTA
	CYAN = Back.CYAN
	WHITE = Back.WHITE
	RESET = Back.RESET
class Style:
	BRIGHT = Style.BRIGHT
	DIM = Style.DIM
	NORMAL = Style.NORMAL
	RESET_ALL = Style.RESET_ALL
class console:
	def __init__(self,margin=""):
		self.ram = []
		self.clear = ""
		self.margin = margin
		self.onprogress = False
		if platform.system() == "Windows":
			self.clear = "cls"
		else:
			self.clear = "clear"
	def update(self):
		os.system(self.clear)
		for i in self.ram:
			print(i,end = "")
	def print(self,color = "",msg="",end = "\n",__cancelonprogress__=False):
		if self.onprogress and __cancelonprogress__ == False:
			self.ram.insert(-1,color + self.margin + msg + end)
		else:
			self.ram.append(color + self.margin + msg + end)
		self.update()
	def erase_line(self,line):
		try:
			self.ram.pop(line)
			self.update()
		except Exception as e:
			raise e
	def erase_screen(self):
		self.ram = []
		self.update()
	def progress_bar(self,iteration, total, decimals = 1, length = 100, printEnd = "\r"):
		if self.onprogress:
			self.erase_line(-1)
		prefix = 'Progress:'
		suffix = 'Complete'
		fill = '█'
		percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
		filledLength = int(length * iteration // total)
		bar = fill * filledLength + '-' * (length - filledLength)
		self.print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd,__cancelonprogress__ = True)
		self.onprogress = True
		if iteration == total:
			self.onprogress = False
			print()
