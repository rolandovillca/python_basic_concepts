import threading
import Queue
import time
import fileinput
import sys

validated_stdin = Queue.Queue()

def my_thread_func(line):
    print 'Running thread for line: {}'.format(line)
    time.sleep(2)
    print 'Completed thread for line: {}'.format(line)

def get_input(stdin):
    for line in iter(stdin.readline, ''):
        validated_stdin.put(line)
    stdin.close()

# How will this loop fit into django?
def queue_validated_line():
    while True:
        if not validated_stdin.empty():
            validated_line = validated_stdin.get()
            processor_thread = threading.Thread(target=my_thread_func, args=(validated_line,))
            processor_thread.start()
            print 'Passing line to thread: {}'.format(validated_line)

# This is a separate thread allowing stdin to go forever.
stdin_thread = threading.Thread(target=get_input, args=(sys.stdin,))
stdin_thread.start()

# Another separated thread.
queue_validated_line_thread = threading.Thread(target=queue_validated_line)
queue_validated_line_thread.start()