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
	def __init__(self):
		self.ram = []
		self.clear = ""
		if platform.system() == "Windows":
			self.clear = "cls"
		else:
			self.clear = "clear"
	def update(self):
		os.system(self.clear)
		for i in self.ram:
			print(i,end = "") 
	def print(self,msg,end = "\n",color = ""):
	
		self.ram.append(color + msg + end)
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




