import os,time,platform

os.system('clear')

#print('[>] Checking Updates')

os.system('git pull')
bit = platform.architecture()[0]
if bit=='64bit':
 import code64
elif bit=='32bit':
 import code32
else:
 print('\33[1;31m[×] unknown Device 32')
