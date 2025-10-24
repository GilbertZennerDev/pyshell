'''
a shell in python

supported commands:

cd
pwd
./a.out runs program
'''

import os
import subprocess as sp

def error(e):
	print(e)

def pwd():
	os.getcwd()
def cd(newdir):
	try: os.chdir(os.path.expanduser(newdir))
	except Exception as e: error(e)
def runprog(*args):
	try: sp.run(*args)
	except Exception as e: error(e)
def run():
	while 1:
		txt = input("pyshell: ").split(' ')
		if txt[0] == 'pwd': pwd()
		if txt[0] == 'cd':
			if txt[1]: cd(txt[1])
		else: runprog(txt)
run()
