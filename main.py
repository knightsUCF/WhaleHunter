#!/usr/bin/python3

import sys
import gui
import feed
import strategy
from multiprocessing import Process



feed = feed.Feed()
strategy = strategy.Strategy()
gui = gui.GUI()



def run():
    
    feed_process = Process(target = feed.run)
    feed_process.start()
    
    strategy_process = Process(target = strategy.run)
    strategy_process.start()

    gui_process = Process(target = gui.run)
    gui_process.start()
    


run()









