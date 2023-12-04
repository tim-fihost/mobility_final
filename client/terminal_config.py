import subprocess
import time
from client import get_data
def terminal_input(command):
    result = subprocess.run(command,shell=True,capture_output=True,text=True)
    print('Command:')
    print(result.stdout)
    print(f"Return code: {result.returncode}")
while True:
    dataout = get_data()
    if dataout == 'forward':
        terminal_input('w')
    if dataout == 'stop':
        terminal_input('s')
    if dataout == 'back':
        terminal_input('x')
    if dataout == 'left':
        terminal_input('a')
    if dataout == 'right':
        terminal_input('d')