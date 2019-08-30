import Getch
import Screens

def mountItems(player, w, h):
    ar = 8
    Box = Screens.initEquip(player, w, h, ar)
    while True:
        Screens.printMenu(Box)
        c = Getch.getch()
        if c == '\r':
            return