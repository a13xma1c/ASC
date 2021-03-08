import sys
import threading
import time


class Semaphore(object):

    def __init__(self, initial):
        self.lock = threading.Condition(threading.Lock())
        self.value = initial

    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()

    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class ChopStick(object):

    def __init__(self, number):
        self.number = number           # chop stick ID
        self.user = -1                 # keep track of philosopher using it
        self.lock = threading.Condition(threading.Lock())
        self.taken = False

    def take(self, user):         # used for synchronization
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user = user
            self.taken = True
            print("p[%s] took c[%s]\n" % (user, self.number))
            self.lock.notifyAll()

    def drop(self, user):         # used for synchronization
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user = -1
            self.taken = False
            print("p[%s] dropped c[%s]\n" % (user, self.number))
            self.lock.notifyAll()


class Philosopher (threading.Thread):

    def __init__(self, number, left, right, semaphore):
        threading.Thread.__init__(self)
        self.number = number            # philosopher number
        self.left = left
        self.right = right
        self.semaphore = semaphore

    def run(self):
        for i in range(20):
            self.semaphore.down()           # start service by semaphore
            time.sleep(0.1)                 # think
            self.left.take(self.number)     # pickup left chopstick
            time.sleep(0.1)                 # (yield makes deadlock more likely)
            self.right.take(self.number)    # pickup right chopstick
            time.sleep(0.1)                 # eat
            self.right.drop(self.number)    # drop right chopstick
            self.left.drop(self.number)     # drop left chopstick
            self.semaphore.up()             # end service by semaphore
        sys.stdout.write("p[%s] finished thinking and eating\n" % self.number)


def main():
    # number of philosophers / chop sticks
    n = 5

    # semaphore for deadlock avoidance (n-1 available)
    semaphore = Semaphore(n-1)

    # list of chopsticks
    c = [ChopStick(i) for i in range(n)]

    # list of philosophers
    p = [Philosopher(i, c[i], c[(i+1) % n], semaphore) for i in range(n)]

    for i in range(n):
        p[i].start()


if __name__ == "__main__":
    main()
