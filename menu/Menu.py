import Getch
import Screens
import Bag
import Skill
import Equip
import Save

def openMenu(p, w, h):
	ar = 5
	Box = Screens.initMenu(w, h, ar)
	while True:
		Screens.printMenu(Box)
		c = (Getch.getch())
		if c == 'p':
			return
		if c == 'w' or c == 's':
			ar = Screens.updateMenu(Box, ar, c)
		if c == '\r':
			if ar == 5:
				Map.viewMap()
			elif ar == 8:
				Bag.viewBag()
			elif ar == 11:
				Skill.viewSkills(p, w, h)
			elif ar == 14:
				Equip.mountItems(p, w * 2, h)
			elif ar == 17:
				Save.confirmExit(p, w, h)
