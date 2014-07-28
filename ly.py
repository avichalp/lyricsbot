import subprocess
import sys
import time

while True:
	if (not subprocess.call(['python','main.py'])) and (not subprocess.call(['python','bot.py'])):
		quit()	
