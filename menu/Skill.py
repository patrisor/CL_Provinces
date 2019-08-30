import Getch
import Screens

def improve(m, player, skill):
	ar = 9
	while True:
		m = Screens.printConfirm(len(m[0]), 10, skill, ar)
		c = Getch.getch()
		if c == 'w' or c == 's':
			ar = Screens.updateConfirm(m, c)
		if c == '\r':
			if ar == 9:
				return
			if ar == 7:
				player.increase(player, skill)
				ar = Screens.updateSkill(m, ar, c, player)
				return

def viewSkills(player, w, h):
	ar = 19 if player.attributes['xp'] < 100 else 7
	while True:
		Box = Screens.initSkills(w, h, ar, player)
		Screens.printSkills(Box)
		c = Getch.getch()
		if c == 'w' or c == 's':
			ar = Screens.updateSkill(Box, ar, c, player)
		if c == '\r':
			if ar == 19:
				return
			if ar == 7:
				improve(Box, player, "Health")
			if ar == 10:
				improve(Box, player, "Mana")
			if ar == 13:
				improve(Box, player, "Strength")
			if ar == 16:
				improve(Box, player, "Defense")
			ar = 19 if player.attributes['xp'] < 100 else 7
