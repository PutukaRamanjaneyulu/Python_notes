# 1. MultiProcessing
''' Processor are runtime at time in 2 Functions and more Functions are the at time'''
import multiprocessing.process
import time
import multiprocessing
import os

starting_time=time.time()
def india():
    print(f'CPU1 processes id: {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')
def uk():
    print(f'CPU2 processes id: {os.getpid()}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'uk : {i}')

if __name__ == "__main__":
    print(f'Main Processor id : {(os.getpid())}')
    cpu1 = multiprocessing.Process(target=india,args=())
    cpu2 = multiprocessing.Process(target=uk,args=())


    cpu1.start()
    cpu2.start()

    cpu1.join()
    cpu2.join()


    
    print(f'Total Time :{(time.time()-starting_time)}')
    print(f'main Function Exits')