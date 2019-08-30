import Getch
import Screens

def confirmExit(player, w, h):
	ar = 9
	while True:
		m = Screens.printConfirm(w, 10, "exit ", ar)
		c = Getch.getch()
		if c == 'w' or c == 's':
			ar = Screens.updateConfirm(m, c)
		if c == '\r':
			if ar == 7:
				print("save and quit successful")
				exit(-1)
			if ar == 9:
				return