
import os, sys, random, platform
try:
    import requests
except:
    os.system('pip2 install requests')

os.system('rm -rf .uid')
for n in range (50000):
	nmbr = random.randint(1111111,9999999)
	sys.stdout = open('.uid', 'a')
	print nmbr
	sys.stdout.flush()

os.system('clear')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from libzomid import subscribe
    subscribe()
elif bit == '32bit':
    from libzomid import subscribe
    subscribe()
