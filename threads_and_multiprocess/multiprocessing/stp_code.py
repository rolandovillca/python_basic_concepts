import multiprocessing
import time

# Your foo info
def foo(n):
    for i in xrange(10000 * n):
        print 'Tick'
        time.sleep(1)

if __name__ == '__main__':
    #Start fo as a process:
    p = multiprocessing.Process(target=foo, name='Foo', args=(10,))
    p.start()

    #Wait 10 seconds for foo:
    time.sleep(10)

    #Wait a maximum of 10 seconds for too
    #Usage: join([timeout in seconds])
    p.join(10)

    #If thread is active:
    if p.is_alive():
        print 'foo is running... lets kill it...'
        #Terminate foo function if thread is still active
        p.terminate()

        #Cleanup:
        p.join()
