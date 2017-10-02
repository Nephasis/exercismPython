class Clock:

    def __init__(self, h, m):
        self.h = h
        self.m = 0
        self.add(m)

    def __str__(self):
        return str("%02d" % (self.h % 24) + ":" + "%02d" % (self.m))

    def __eq__(self, other):
        return str(self) == str(other)

    def add(self, m):
        self.m += m
        self.h += self.m % 60



print Clock(8, 0)

