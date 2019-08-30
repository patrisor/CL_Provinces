#main menu
def initMenu(w, h, ar):
	m = [[" "] * (w) for i in range(h)]
	m[0][0] = '┌'
	m[0][w - 1] = '┐'
	m[h - 1][0] = '└'
	m[h - 1][w - 1] = '┘'
	for i in range(1, w - 1):
		m[0][i] = '─'
		m[h- 1][i] = '─'
	for i in range(1, h - 1):
		m[i][0] = '│'
		m[i][w - 1] = '│'
	title = "Main Menu"
	for c in range(len(title)):
		j = (int)((w - len(title)) / 2) + c
		m[1][j] = title[c]
		m[2][j] = '─'
		m[2][j + 2] = '─'
		m[2][j - 2] = '─'
	menuitems = ["View Map",
				 "Backpack",
				 "Skill",
				 "Equip",
				 "Exit Game"]
	z = 0
	m[ar][5] = '>'
	for i in range (5, h - 4, (int)((h - 7) / len(menuitems))):
		for c in range (len(menuitems[z])):
			itemw = (int)((w - len(menuitems[z])) / 2) + c
			m[i][itemw] = menuitems[z][c]
			m[i + 1][itemw] = '─'
			m[i + 1][itemw + 1] = '─'
			m[i + 1][itemw - 1] = '─'
		z += 1
	return m

def printMenu(m):
	for i in range(len(m)):
		line = ''.join(m[i])
		if "Main" in line:
			print(line[0 : 6] + "\033[1m\033[36m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Map" in line:
			print(line[0 : 6] + "\033[1m\033[36m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Back" in line:
			print(line[0 : 6] + "\033[1m\033[33m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Skill" in line:
			print(line[0 : 6] + "\033[1m\033[32m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Weapon" in line:
			print(line[0 : 6] + "\033[31m" + line [6 : 36] + "\033[36m" + line[36 : -1] + "\033[0m" + line[-0])
		elif "Equip" in line:
			print(line[0 : 6] + "\033[1m\033[35m" + line[6 : -1] + "\033[0m" + line[-0])
		elif "Exit" in line:
			print(line[0 : 6] + "\033[1m\033[31m" + line[6 : -1] + "\033[0m" + line[-0])
		else:
			print(line)

def updateMenu(m, ar, c):
	for i in range(len(m)):
		if '>' in m[i]:
			if (i == 5 and c == 'w') or (i == 17 and c == 's'):
				return ar
			else:
				m[i][5] = ' '
				i = i - 3 if c == 'w' else i + 3
				m[i][5] = '>'
				return i

#skills menu
def initSkills(w, h, ar, p):
	m = [[" "] * (w) for i in range(h)]
	m[0][0] = '┌'
	m[0][w - 1] = '┐'
	m[h - 1][0] = '└'
	m[h - 1][w - 1] = '┘'
	for i in range(1, w - 1):
		m[0][i] = '─'
		m[h- 1][i] = '─'
	for i in range(1, h - 1):
		m[i][0] = '│'
		m[i][w - 1] = '│'
	title = "Skills"
	for c in range(len(title)):
		j = (int)((w - len(title)) / 2) + c
		m[1][j] = title[c]
		m[2][j] = '─'
		m[2][j + 2] = '─'
		m[2][j - 2] = '─'
	xp = "EXP        level  " + str(p.attributes['level'])
	for c in range(len(xp)):
		j = (int)((w - len(xp)) / 2) + c
		m[3][j] = xp[c]
	for c in range(5, 24):
		if c == 5:
			m[4][c] = '['
		elif c == 23:
			m[4][c] = ']'
		else:
			i = int(((c - 5) / 17) * 100)
			if p.attributes['xp'] >= 100:
				m[4][c] = '▓'
			elif i <= p.attributes['xp']:
				m[4][c] = '░'
			else:
				m[4][c] = ' '
		if p.attributes['xp'] >= 100:
			upgrade = "upgrades available : " + str(int(p.attributes['xp'] / 100))
			for i in range(len(upgrade)):
				m[5][i + 4] = upgrade[i]
	menuitems = ["",
				"Health   : " + str(p.attributes['Health']).rjust(4),
				"Mana     : " + str(p.attributes['Mana']).rjust(4),
				"Strength : " + str(p.attributes['Strength']).rjust(4),
                "Defense  : " + str(p.attributes['Defense']).rjust(4),
				"Exit Menu"]
	z = 0
	m[ar][5] = '>'
	for i in range (4, h - 1, 3):
		for c in range(len(menuitems[z])):
			itemw = c + 8
			m[i][itemw] = menuitems[z][c]
		z += 1
	return m

def printSkills(m):
	box = "\r"
	for i in range(len(m)):
		line = ''.join(m[i])
		if "Skill" in line:
			box = box + (line[0 : 6] + "\033[1m\033[32m" + line[6 : -1] + "\033[0m" + line[-0] + '\n')
		else:
			box = box + line + '\n'
	print (box, end = '')

def updateSkill(m, ar, c, p):
	for i in range(len(m)):
		if '>' in m[i]:
			if (i == 7 and c == 'w') or (i == 19 and c == 's') or (p.attributes['xp'] < 100):
				return ar
			else:
				m[i][5] = ' '
				i = i - 3 if c == 'w' else i + 3
				m[i][5] = '>'
				return i

#equip menu
def initEquip(p, w, h, ar):
	m = [[" "] * (w) for i in range(h + 1)]
	m[0][0] = '┌'
	m[0][w - 1] = '┐'
	m[h - 1][0] = '└'
	m[h - 1][w - 1] = '┘'
	for i in range(1, w - 1):
		m[0][i] = '─'
		m[h- 1][i] = '─'
	for i in range(1, h - 1):
		m[i][0] = '│'
		m[i][w - 1] = '│'
	title = "Equip"
	for c in range(len(title)):
		j = int((w - len(title)) / 2) + c
		m[1][j] = title[c]
		m[2][j] = '─'
		m[2][j + 2] = '─'
		m[2][j - 2] = '─'
	equip = ["Weapon",
			"Armor"]
	for i in range(len(equip)):
		for c in range(len(equip[i])):
			j = int(((w / 2) - len(equip[i])) / 2) + c
			m[3][j + 30 if i / 1 == 1 else j] = equip[i][c]
	if len(p.weapon[0]) > int(w / 2) - 1:
		for i in range(len(p.weapon[0])):
			if i > int(w / 2) - 5:
				j = int(((w / 2) - (len(p.weapon[0]) / 2)) / 2) + (i - 26)
				m[5][j - 5] = p.weapon[0][i]
			else:
				j = int(((w / 2) - (len(p.weapon[0]) / 2)) / 2) + i
				m[4][j - 5] = p.weapon[0][i]
	else:
		for i in range(len(p.weapon[0])):
			j = int(((w / 2) - len(p.weapon[0])) / 2) + i
			m[4][j] = p.weapon[0][i]
	if len(p.armor[0]) > int(w / 2) - 1:
		for i in range(len(p.armor[0])):
			if i > int(w / 2) - 5:
				j = int(((w / 2) - (len(p.armor[0]) / 2)) / 2) + (i - 26) + int(w / 2)
				m[5][j - 6] = p.armor[0][i]
			else:
				j = int(((w / 2) - (len(p.armor[0]) / 2)) / 2) + i + int(w / 2)
				m[4][j - 6] = p.armor[0][i]
	else:
		for i in range(len(p.armor[0])):
			j = int(((w / 2) - len(p.armor[0])) / 2) + i  + int(w / 2)
			m[4][j] = p.armor[0][i]
	m[6][9] = '+'
	m[6][int(w / 2) + 9] = '+'
	bonusStr = str(p.weapon[1]) + " Strength"
	bonusDef = str(p.armor[1]) + " Defense"
	for i in range(len(bonusStr)):
    		m[6][11 + i] = bonusStr[i]
	for i in range(len(bonusDef)):
		m[6][int(w / 2) + 11 + i] = bonusDef[i]
	return m

#confirm window
def printConfirm(w, h, opt, ar):
	text = "confirm ?"
	m = [[" "] * (w) for i in range(h + 1)]
	s = int((w/2) - (w/4))
	f = w - int(w/4)
	m[0][s - 1] = '┌'
	m[0][f] = '┐'
	m[h][s - 1] = '└'
	m[h][f] = '┘'
	for i in range(1, h):
		m[i][s - 1] = '│'
		m[i][f] = '│'
	for i in range(s, f):
		m[0][i] = '─'
		m[2][i] = '─'
		m[h][i] = '─'
	for i in range(len(opt)):
		m[1][int((w - len(opt)) / 2) + i] = opt[i]
	for i in range(len(text)):
		m[4][int((w - len(text)) / 2) + i] = text[i]
		m[5][int((w - len(text)) / 2) + i] = '─'
	m[7][s + s] = 'Y'
	m[9][s + s] = 'N'
	m[ar][s + s - 4] = '>'
	for i in range(len(m)):
		line = ''.join(m[i])
		print(line)
	return m

def updateConfirm(m, c):
	for i in range(len(m)):
		if '>' in m[i]:
			if (i == 7 and c == 'w') or (i == 9 and c == 's'):
				return i
			else:
				m[i][int(len(m[0]) / 3)] = ' '
				i = i - 2 if c == 'w' else i + 2
				m[i][int(len(m[0]) / 3)] = '>'
				return i
