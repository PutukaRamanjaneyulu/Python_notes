''' How Application handle with the Customers. when Customers are using the application 
'''

# Drawback of normal level of Code
import time

starting_time=time.time()
def india():
    for i in range(1,11):
        time.sleep(0.5)
        print(f'india : {i}')
def uk():
    for i in range(1,11):
        time.sleep(0.5)
        print(f'uk : {i}')
india()
uk()
print(f'Total Time :{(time.time()-starting_time)}')