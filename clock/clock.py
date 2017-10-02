class Clock:

    def __init__(self, hours, minutes):
        self.h = 0
        self.m = 0
        self.add(hours*60 + minutes)

    def __str__(self):
        return str("%02d" % (self.h % 24) + ":" + "%02d" % (self.m))

    def __eq__(self, other):
        return str(self) == str(other)

    def add(self, m):
        all_minutes = self.m + m
        self.h += all_minutes // 60
        self.m = all_minutes % 60
        return self
