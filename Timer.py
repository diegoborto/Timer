import time
import termcolor
from termcolor import colored
from datetime import datetime
import platform
import os
import winsound

def beep(freq=1000, dur=200):
    system = platform.system()
    for i in range(3):
        if system == "Windows":
            winsound.Beep(freq, dur)
        elif system == "Linux":
            os.system(f"beep -f {freq} -l {dur}")
        elif system == "Darwin":  # macOS
            os.system(f"play -n synth {dur/1000} sine {freq}")
        else:
            print("\a", end="")  # fallback

print(colored('Timer','blue'))
lenght = ''
while lenght == '':
    lenght = input('How many minutes? ')

message = input('Type the message: ')
print('')
# Get the current date and time
now = datetime.now()
current_time = now.time()
formatted_time = now.strftime("%H:%M:%S")
print('Timer started at', formatted_time, 'for ', lenght, ' minutes.')

time.sleep(int(lenght)*60)

now = datetime.now()
current_time = now.time()
formatted_time = now.strftime("%H:%M:%S")
print('Timer done at ', formatted_time)
print(colored('Stopped','red'))
beep()
print(colored('-----------------------------------------------------------------','blue'))
print(colored(message,'blue'))
print(colored('-----------------------------------------------------------------','blue'))
input('Press enter to quit.')




