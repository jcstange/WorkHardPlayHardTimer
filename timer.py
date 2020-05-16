# timer.py

import time
import sys
import os

class Timer:

    def __init__(self):
        self._start_time = None

    def updateDisplay(self, startPoint):
        print('\r ###',time.strftime('%H:%M:%S', time.gmtime(startPoint)), end=" ###")
    
    def startTimer(self, minutes):
        currentTime = time.perf_counter()
        startPoint = minutes*60
        while startPoint > 0:
            if time.perf_counter() - currentTime  > 1:
                currentTime = time.perf_counter()
                startPoint = startPoint - 1
                self.updateDisplay(startPoint)

    def timer(self, minutes):
        print('Starting Timer')
        self._start_time = time.perf_counter()
        self.startTimer(minutes)
        os.system('say "Beer time."')

    def pomodore(self, minutes, rest):
        print('Starting Pomodore')
        while True:
            for x in range(3): 
                print('\n### Work hard ###')
                os.system('say "Work Hard."')
                self.startTimer(minutes)
                print('\n### Play Easy ###')
                os.system('say "Play Easy."')
                self.startTimer(rest)
            
            print('\n### Play Hard ###')
            os.system('say "Play Hard."')
            self.startTimer(minutes)

    def stop(self):
        elapsed_time = time.perf_counter() - self._start_time
        self._start_time = None
        print(f"Elapsed time: {self.elapsed_time:0.4f} seconds")
