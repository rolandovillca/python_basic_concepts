import time
import multiprocessing

square_result = []

def calc_square(numbers):
    for n in numbers:
        square_result.append(n*n)
    print 'Result within process: ', square_result

if __name__ == '__main__':
    arr = [1, 2, 3]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()

    print 'Result out of process: ', square_result
    print 'Done...'
