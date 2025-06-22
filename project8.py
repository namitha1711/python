class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

def time_to_seconds(t):
    return t.hours * 3600 + t.minutes * 60 + t.seconds

def seconds_to_time(seconds):
    hours, remainder = divmod(int(seconds), 3600)
    minutes, sec = divmod(remainder, 60)
    return Time(hours, minutes, sec)

def mul_time(t, factor):
    total_sec = time_to_seconds(t) * factor
    return seconds_to_time(total_sec)

def average_pace(finish_time, distance):
    return mul_time(finish_time, 1 / distance)
