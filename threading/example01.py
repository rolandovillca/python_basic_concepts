import time
from threading import Thread

# Target function:
def sleeper(i):
    print 'thread {} sleeps for 5 seconds'.format(i)
    time.sleep(5)
    print 'thread {} wope up'.format(i)

# Run the threads:
for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()