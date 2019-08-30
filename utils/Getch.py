import sys,tty,termios

class _Getch:       
    def __call__(self):
        # Take in a file descriptor for standard input; 0
        fd = sys.stdin.fileno()
        # Return a list containing the tty attributes for file descriptor 0
        # List is as follows: [iflag, oflag, cflag, lflag, ispeed, ospeed, cc];
        # where cc is a list of the tty special characters
        old_settings = termios.tcgetattr(fd)
        try:
            # Change the mode of the file descriptor fd to raw. If when is omitted, 
            # it defaults to termios.TCSAFLUSH, and is passed to termios.tcsetattr()
            tty.setraw(sys.stdin.fileno())
            # Reads input 
            ch = sys.stdin.read(1)
        finally:
            # In case there is an exemption, it will default everything back 
            # Set the tty attributes for file descriptor, 0, from the attributes
            # TCSADRAIN to change after transmitting all queued output
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def getch():
    ValidInputs = ['\r', 'a', 'd', 'p', 'q', 's', 'w', '\033']
    inkey = _Getch()
    while(1):
        k=inkey()
        if k in ValidInputs: break
        else: print("Invalid Input")
    if k == '\033':
        print("Goodbye!")
        exit(-1)
    return k
