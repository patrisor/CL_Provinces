# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Map.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 00:06:24 by patrisor          #+#    #+#              #
#    Updated: 2019/08/27 01:04:34 by patrisor         ###   ########.fr        #
#    Updated: 2019/08/21 02:04:05 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import random

class TestMap:

    def __init__(self, w, h, p, i, enemies):
        ret = [([1] * w)] + ([([1] + ([0] * (w - 2)) + [1]) for _ in range(h - 2)]) + [([1] * w)]
        # Places character
        ret[p.coords[0]][p.coords[1]] = 2
        # Randomizes Coin drops
        for r in range(25): ret[random.randint(1, w - 2)][random.randint(1, h - 2)] = i.COINS
        # PLACE WEAPONS
        while True:
            r = random.randint(1, w - 2)
            c = random.randint(1, h - 2)
            if ret[r][c] != 0: continue
            ret[r][c] = i.KNIFE
            break
        # Place Enemies
        for e in enemies:
            ret[e.coords[0]][e.coords[1]] = e.id
        self.map = ret

    def controls(self):
        return "WALK: W, A, S, and D\nPAUSE: P\n\n"

    # TODO: update
    def printMap(self, p, i):
        #FOR TESTING
        '''
        print('\n')
        for r in range(len(self.map)):
            print(str(r) + ' ' + ' '.join(str(e) for e in self.map[r])) 
        '''
        out = ""
        for r in range(len(self.map)):
            for c in range(len(self.map[r])):
                if r == 0:
                    if c == 0: out += "┌"
                    elif c == len(self.map[r]) - 1: out += "┐"
                    else: out += "──"
                if r > 0 and r < len(self.map) - 1:
                    if self.map[r][c] == 1: out += "│"
                    if self.map[r][c] == p.id: out += "🕺"
                    if self.map[r][c] == i.COINS: out += "💰"
                    if self.map[r][c] == i.KNIFE: out += "🔪"
                    if self.map[r][c] == 20: out += "🦍" 
                    if self.map[r][c] == 0: out += "  "
                if r == len(self.map) - 1:
                    if c == 0: out += "└"
                    elif c == len(self.map[r]) - 1: out += "┘"
                    else: out += "──"
            out += "\n"
        print(out + "CONTROLS:\n" + self.controls() + "SKILLS:\n" + p.skillTreeToString() + "\n\n\n")

    # Function SAVES the old address of the player position, then updates it with player / ENEMY pos
    def updateMap(self, i, p, enemies, t):
        p.move(self.map, i)
        if ((t % 3) == 2):
            for e in enemies:
                e.move(self.map, p)
        return 0
