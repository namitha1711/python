import sys

class Time:
    def __init__(self, hour=0, minute=0, second=0, *, seconds=None):
        if seconds is not None:
            self.seconds = seconds
        else:
            self.seconds = second + 60 * (minute + 60 * hour)

    def __str__(self):
        minutes, sec = divmod(self.seconds, 60)
        hour, minute = divmod(minutes, 60)
        return f"{hour:02d}:{minute:02d}:{sec:02d}"

    def print_time(self):
        print(self.__str__())

    def time_to_int(self):
        return self.seconds

    def is_after(self, other):
        return self.seconds > other.seconds

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)

    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        assert self.is_valid() and other.is_valid()
        return Time(seconds=self.seconds + other.seconds)

    def increment(self, seconds):
        return Time(seconds=self.seconds + seconds)

    def is_valid(self):
        return self.seconds >= 0

def int_to_time(seconds):
    return Time(seconds=seconds)

def main():
    start = Time(9, 45, 0)
    start.print_time()

    end = start.increment(1337)
    end.print_time()

    print("Is end after start?")
    print(end.is_after(start))

    print("Using __str__")
    print(start, end)

    start = Time(9, 45)
    duration = Time(1, 35)
    print(start + duration)
    print(start + 1337)
    print(1337 + start)

    print("Example of polymorphism")
    t1 = Time(7, 43)
    t2 = Time(7, 41)
    t3 = Time(7, 37)
    total = sum([t1, t2, t3], Time(seconds=0))
    print(total)

if __name__ == '__main__':
    main()
