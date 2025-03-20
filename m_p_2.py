import time
import os
import multiprocessing
starting_time = time.time()
# Processing work the simultaneously 
# Threading work the Concurrent(line by line)
import threading


def india():
    print(f'Cpu1 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'India : {i}')
def uk():
    print(f'Cpu1 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'uk : {i}')
def parish():
    print(f'Cpu2 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'paridh : {i}')
def Canada():
    print(f'Cpu2 Processor id: {(os.getpid())}')
    for i in range(1,11):
        time.sleep(0.5)
        print(f'canada : {i}')
def Comman_1():
    t1=threading.Thread(target=india,args=())
    t2=threading.Thread(target=uk,args=())
    t1.start()
    t2.start()
def Comman_2():
    t3=threading.Thread(target=parish,args=())
    t4=threading.Thread(target=Canada,args=())
    t3.start()
    t4.start()


if __name__ == "__main__":
    print(f'Main Processor id: {(os.getpid())}')
    cpu1=threading.Thread(target=Comman_1,args=())
    cpu2=threading.Thread(target=Comman_2,args=())

    cpu1.start()
    cpu2.start()


    print(f'Total Time : {(time.time()-starting_time)}')
    print(f'Main Processor Exit')
