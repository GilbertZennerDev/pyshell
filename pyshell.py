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
	print(os.getcwd())
def cd(newdir):
	try: os.chdir(os.path.expanduser(newdir))
	except Exception as e: error(e)
def runprog(*args):
	try: sp.run(*args)
	except Exception as e: error(e)
def run():
	cmds = ['pwd', 'cd', 'export', 'echo']
	while 1:
		txt = input("pyshell: ").split(' ')
		if txt[0] == 'pwd': pwd()
		if txt[0] == 'cd' and txt[1]: cd(txt[1])
		if '$' in txt[0]: print(os.getenv(txt[0]))
		#if txt[0] == 'export': runprog(['bash', '-c', " ".join(txt)]); print(" ".join(txt))
		if txt[0] == 'echo':
			if txt[1][0] == '$': txt[1] = txt[1][1:]; print(os.getenv(txt[1]))
		if txt[0] not in cmds: runprog(txt)
run()
