# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    main.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: rpapagna <rpapagna@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2019/08/19 20:04:28 by patrisor          #+#    #+#              #
#    Updated: 2019/08/27 01:04:31 by patrisor         ###   ########.fr        #
#    Updated: 2019/08/22 04:08:26 by rpapagna         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys
sys.path.append('utils')
sys.path.append('menu')
sys.path.append('src')
import Screens,Menu,Maps,Objects

# TODO: Play with this library
import Processing

def main():
    MAP_WIDTH = 25
    MAP_HEIGHT = 25
    PLAYER = Objects.Player(int(MAP_WIDTH / 2), int(MAP_HEIGHT / 2))
    ITEMS = Objects.Items()
    ENEMIES = Objects.spawnEnemies(5, MAP_WIDTH, MAP_HEIGHT)
    MAP = Maps.TestMap(MAP_WIDTH, MAP_HEIGHT, PLAYER, ITEMS, ENEMIES)
    timer = 0
    while True:
        # Print Updated Map
        MAP.printMap(PLAYER, ITEMS)
        # Input from User
        inp = Processing.processInput(PLAYER, MAP, ITEMS, ENEMIES)
        # TODO: Update Map, based on input and player position
        MAP.updateMap(inp, PLAYER, ENEMIES, timer)
        timer += 1
    return(0)

if __name__ == "__main__":
    main()
