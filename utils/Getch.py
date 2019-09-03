import sys,tty,termios

class _Getch:       
	def __call__(self):
			fd = sys.stdin.fileno()
			old_settings = termios.tcgetattr(fd)
			try:
				tty.setraw(sys.stdin.fileno())
				ch = sys.stdin.read(1)
			finally:
				termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
			return ch

def getch():
	ValidInputs = ['\r', 'a', 'd', 'p', 'q', 's', 'w', '\033']
	inkey = _Getch()
	while(1):
			k=inkey()
			if k in ValidInputs:
				break
			else:
				print("Invalid Input")
	if k == '\033':
		print("Goodbye!")
		exit(-1)
	return k