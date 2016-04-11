import threading
from time import sleep

NUM_OF_THREADS = 6
TOTAL_ITEMS = 200
BLOCK_SIZE = 10

def blocks(lst, step):
    for block in range(0, len(lst), step):
        yield lst[block:block + step]

class migrationThread(threading.Thread):
    def __init__(self, thread_id, blocks):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.blocks = blocks

    def run(self):
        for block in self.blocks:
            sleep(3)
            print "Thread {} processed: {} - {}".format(self.thread_id, block[0], block[-1])

blocks_groups = blocks(range(TOTAL_ITEMS), BLOCK_SIZE)

for thread in range(1, NUM_OF_THREADS + 1):
    migrationThread(thread, blocks_groups).start()