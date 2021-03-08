"""
    Basic thread handling exercise:

    Use the Thread class to create and run more than 10 threads which print their name and a random
    number they receive as argument. The number of threads must be received from the command line.

    e.g. Hello, I'm Thread-96 and I received the number 42

"""

from threading import Thread
import sys
import random


def thread_function(thread_id, nr):
    print("Hello, I'm Thread-%s and I received the number %s" % (thread_id, nr))


MAX_NUM = 100000
random.seed()
nr_threads = int(sys.argv[1])
thread_list = []

for i in range(0, nr_threads):
    t = Thread(target=thread_function, args=(i, random.randint(0, MAX_NUM)))
    thread_list.append(t)

for t in thread_list:
    t.start()

for t in thread_list:
    t.join()
