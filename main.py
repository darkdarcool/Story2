import os,random
import time, sys
player_damage1 = 20
xp = 0
if xp <= 400:
	player_damage1 + 5

#colors

black = "\033[0;30m"
red = "\033[0;31m"
green = "\033[0;32m"
yellow = "\033[0;33m"
blue = "\033[0;34m"
magenta = "\033[0;35m"
cyan = "\033[0;36m"
white = "\033[0;37m"
bblack = "\033[0;90m"
bred = "\033[0;91m"
bgreen = "\033[0;92m"
byellow = "\033[0;93m"
bblue = "\033[0;94m"
bmagenta = "\033[0;95m"
bcyan = "\033[0;96m"
bwhite = "\033[0;97m"
bold = '\033[1m'
end = '\033[0m'

def typewriter(message):
	for i in message:
		sys.stdout.write(i)
		sys.stdout.flush()
		if ((i != "\n") and (i != ":")):
			time.sleep(0.08)
		else:
			time.sleep(0.2)
			
typewriter('Hello replers! I have decided that I want to make another GlitchInTheSystem story! I hope you enjoy the project, have a great day!\n - DarkDarcool')
time.sleep(2)
os.system('clear')
typewriter('When you came back up for bed, you see the game, laying on your bed, ' + bold + 'NOT' + end + ' where you left it. That weirded you out, but you thought it was just your younger brother playing with it and he left it on your bed\n
')
