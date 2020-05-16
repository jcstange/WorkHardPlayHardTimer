from timer import Timer
from sys import argv

timer = Timer()
try:
    timer.pomodore(int(argv[1]), int(argv[2]))
except:    
    timer.timer(int(argv[1]))
