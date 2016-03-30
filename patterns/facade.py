#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

SLEEP = 0.5

# First Object:
class Test1:
    def run(self):
        print '----- Into test 1 -----'
        time.sleep(SLEEP)
        print 'Setting up'
        time.sleep(SLEEP)
        print 'Running tests'
        time.sleep(SLEEP)
        print 'Tearing down'
        time.sleep(SLEEP)
        print 'Test finished\n'

# Second Object:
class Test2:
    def run(self):
        print '----- Into test 2 -----'
        time.sleep(SLEEP)
        print 'Setting up'
        time.sleep(SLEEP)
        print 'Running tests'
        time.sleep(SLEEP)
        print 'Tearing down'
        time.sleep(SLEEP)
        print 'Test finished\n'

# Third Object:
class Test3:
    def run(self):
        print '----- Into test 3 -----'
        time.sleep(SLEEP)
        print 'Setting up'
        time.sleep(SLEEP)
        print 'Running tests'
        time.sleep(SLEEP)
        print 'Tearing down'
        time.sleep(SLEEP)
        print 'Test finished\n'

# Facade:
class TestRunner:
    def __init__(self):
        self.test1 = Test1()
        self.test2 = Test2()
        self.test3 = Test3()
        self.tests = [i for i in (self.test1, self.test2, self.test3)]

    def run_all(self):
        [test.run() for test in self.tests]

# Main root to start program:
if __name__ == '__main__':
    test_runner = TestRunner()
    test_runner.run_all()
