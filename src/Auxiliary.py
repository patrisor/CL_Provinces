# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    auxiliary.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: patrisor <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/20 04:08:54 by patrisor          #+#    #+#              #
#    Updated: 2019/08/26 22:32:27 by patrisor         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

''' COLLISION DETECTION
m[p.x + 1][p.y]: Checks for wall under you; if there is boundary, return 's'
m[p.x - 1][p.y]: Checks for wall above you; if there is boundary, return 'w'
m[p.x][p.y + 1]: Checks for wall to the right; if there is boundary, return 'd'
m[p.x][p.y - 1]: Checks for wall to the left; if there is boundary, return 'a'
RETURN List of anticipated moves that can't be made'''
# NOTE: p can be substituted for enemy class
def check_collision(p, m, i):
    ret = []
    if m[p.coords[0]][p.coords[1] + 1] == i or m[p.coords[0]][p.coords[1] - 1] == i:
        ret.append(('d' if m[p.coords[0]][p.coords[1] + 1] == i else 'a'))
    if m[p.coords[0] + 1][p.coords[1]] == i or m[p.coords[0] - 1][p.coords[1]] == i:
        ret.append(('s' if m[p.coords[0] + 1][p.coords[1]] == i else 'w'))
    return ret

def isCollided(keys, i, inp, hit = 0):
    if(len(keys[i]) > 0): 
        for x in range(len(keys[i])): 
            if keys[i][x] == inp: hit += 1
    return(True if hit > 0 else False)

# Return List of possible collisions between objects
# If you want the ability to add more items, then add another function call to this list, and
# update the third parameter to the item you are looking for
def getCollisions(PLAYER, MAP, ITEMS):
    return [check_collision(PLAYER, MAP.map, 1), check_collision(PLAYER, MAP.map, ITEMS.COINS),
            check_collision(PLAYER, MAP.map, ITEMS.KNIFE), check_collision(PLAYER, MAP.map, 20)]
