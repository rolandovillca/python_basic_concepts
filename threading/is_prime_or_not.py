'''
Thi example shows a thread, which determines, if a number is prime or not.
The Thread is defined with the threading module, using the locks:
'''

import threading

class PrimeNumber(threading.Thread):
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self): 
        counter = 2
        res = True

        while counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
                res = False 
            counter += 1 
        
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 

threads = []

while True: 
    input = long(raw_input("number: ")) 
    if input < 1: 
        break 
 
    thread = PrimeNumber(input) 
    threads += [thread] 
    thread.start() 
 
'''
The join() method makes sure that the main program waits until all threads have terminated.
'''
for t in threads: 
    t.join()