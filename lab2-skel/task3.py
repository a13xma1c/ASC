"""
Coffee Factory: A multiple producer - multiple consumer approach

Generate a base class Coffee which knows only the coffee name
Create the Espresso, Americano and Cappuccino classes which inherit the base class knowing that
each coffee type has a predetermined size.
Each of these classes have a get message method

Create 3 additional classes as following:
    * Distributor - A shared space where the producers puts coffees and the consumers takes them
    * CoffeeFactory - An infinite loop, which always sends coffees to the distributor
    * User - Another infinite loop, which always takes coffees from the distributor

The scope of this exercise is to correctly use threads, classes and synchronization objects.
The size of the coffee (ex. small, medium, large) is chosen randomly everytime.
The coffee type is chosen randomly everytime.

Example of output:

Consumer 65 consumed espresso
Factory 7 produced a nice small espresso
Consumer 87 consumed cappuccino
Factory 9 produced an italian medium cappuccino
Consumer 90 consumed americano
Consumer 84 consumed espresso
Factory 8 produced a strong medium americano
Consumer 135 consumed cappuccino
Consumer 94 consumed americano
"""
from threading import Thread
from queue import Queue
import sys
import random
import time


size_list = ["small", "medium", "large"]
random.seed()


class Coffee:
    """ Base class """
    def __init__(self):
        pass

    def get_name(self):
        """ Returns the coffee name """
        raise NotImplementedError

    def get_size(self):
        """ Returns the coffee size """
        raise NotImplementedError

    def get_message(self):
        raise NotImplementedError


class ExampleCoffee:
    """ Espresso implementation """
    def __init__(self, size):
        pass

    def get_message(self):
        """ Output message """
        raise NotImplementedError


class Espresso(Coffee):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def get_name(self):
        return "espresso"

    def set_size(self, size):
        self.size = size
        return self

    def get_size(self):
        return self.size

    def get_message(self):
        return "%s %s" % (self.size, self.get_name())


class Americano(Coffee):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def get_name(self):
        return "Americano"

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size
        return self

    def get_message(self):
        return "%s %s" % (self.size, self.get_name())


class Cappuccino(Coffee):
    def __init__(self, size):
        super().__init__()
        self.size = size

    def get_name(self):
        return "Cappuccino"

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size
        return self

    def get_message(self):
        return "%s %s" % (self.size, self.get_name())


coffee_list = [Espresso("small"), Americano("small"), Cappuccino("small")]


class Distributor(Queue):
    def __init__(self, size):
        super().__init__(size)


class CoffeeFactory(Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.full():
                new_coffee = coffee_list[random.randint(0, 2)].set_size(size_list[random.randint(0, 2)])
                self.queue.put(new_coffee)
                print("Making a %s\n" % new_coffee.get_message())
                time.sleep(random.random())


class User(Thread):
    def __init__(self, name, queue):
        super().__init__()
        self.name = name
        self.queue = queue

    def run(self):
        while True:
            if not self.queue.empty():
                item = self.queue.get()
                print("%s is drinking a %s\n" % (self.name, item.get_message()))
                time.sleep(random.random())


if __name__ == '__main__':
    dist = Distributor(int(sys.argv[1]))

    nr_prod = int(input("Number of baristas:"))
    nr_dev = int(input("Number of developers:"))

    baristas = []
    devs = []
    for i in range(0, nr_prod):
        bar = CoffeeFactory(dist)
        baristas.append(bar)

    for i in range(0, nr_dev):
        dev = User("Alex %s-lescu" % i, dist)
        devs.append(dev)

    for b in baristas:
        b.start()

    time.sleep(2)

    for d in devs:
        d.start()

