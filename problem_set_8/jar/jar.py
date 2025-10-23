class Jar:

    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError
        self._capacity = capacity
        self._ncookie = 0

    def __str__(self):
        n = self.size
        return n * "🍪"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError
        else:
            self._ncookie = self.size + n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError
        else:
            self._ncookie = self.size - n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity

    @property
    def size(self):
        return self._ncookie
