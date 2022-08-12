import time
import datetime
# global timer 
# timer = False
def start_clock(timer):
    while timer == False:
        start = input("press enter to start time")
        if start =="":
            start_time= time.time()
            timer =True
            print("TIME HAS STARTED")
            return start_time
        else:
            start_clock(timer)
def stop_clock( start_time):
    timer = True 
    while timer ==True:
        stop = input("press enter to stop the clock")
        if stop =="":
            end_time = time.time()
        else:
            stop_clock(start_time)
        timer = False 
    total_time = end_time - start_time 
    total_time = total_time /60
    total_time = "{:.2f}".format(total_time)
    print(total_time)
    return total_time



