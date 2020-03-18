class Time:
    def __init__(self, hours=0, minutes=0, seconds=0, string_time='', other_class_object=None):
        if hours != 0 and minutes != 0 and seconds != 0:
            self.hours = hours
            self.minutes = minutes
            self.seconds = seconds
        elif string_time != '':
            list_time = string_time.split(':')
            self.hours = list_time[0]
            self.minutes = list_time[1]
            self.seconds = list_time[2]
        else:
            self.hours = other_class_object.hours
            self.minutes = other_class_object.minutes
            self.seconds = other_class_object.seconds

    def __eq__(self, other):
        return (
                self.hours == other.hours and
                self.minutes == other.minutes and
                self.seconds == other.seconds
        )

        def __ne__(self, other):
        return (
                self.hours != other.hours or
                self.minutes != other.minutes or
                self.seconds != other.seconds
        )

    def __lt__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds < other.seconds:
            return True
        else:
            return False

    def __gt__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds > other.seconds:
            return True
        else:
            return False

    def __le__(self, other):
        if self.hours < other.hours:
            return True
        elif self.hours == other.hours and self.minutes < other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds <= other.seconds:
            return True
        else:
            return False

    def __ge__(self, other):
        if self.hours > other.hours:
            return True
        elif self.hours == other.hours and self.minutes > other.minutes:
            return True
        elif self.hours == other.hours and self.minutes == other.minutes and self.seconds >= other.seconds:
            return True
        else:
            return False

    def __sub__(self, other):
        return Time(
            self.hours - other.hours,
            self.minutes - other.minutes,
            self.seconds - other.seconds,
        )

    def __add__(self, other):
        return Time(
            self.hours + other.hours,
            self.minutes + other.minutes,
            self.seconds + other.seconds
        )

    def __mul__(self, value):
        return Time(
            self.hours * value,
            self.minutes * value,
            self.seconds * value
        )

    def __str__(self):
        hours = int(self.hours)
        minutes = int(self.minutes)
        seconds = int(self.seconds)
        while hours > 23 or minutes > 59 or seconds > 59:
            while hours > 23:
                hours = (hours - 24)
            while minutes > 59:
                hours += 1
                minutes = minutes - 60
            while seconds > 59:
                minutes += 1
                seconds = seconds - 60
        if hours < 10:
            hours = f'0{hours}'
        if minutes < 10:
            minutes = f'0{minutes}'
        if seconds < 10:
            seconds = f'0{seconds}'

        return f'{hours}:{minutes}:{seconds}'


first = Time(10, 10, 10)
second = Time(14, 93, 75)
third = Time(10, 10, 10)

print(second)
print(first == second)
print(first == third)
print(second > first)
print(second - first)
print(second + first)
fourth = Time(string_time='47:66:128')  # 00:08:08
print(fourth)
fifth = Time(other_class_object=first)
print(fifth)

print('###############')
test_time1 = Time(10, 10, 10)
test_time2 = Time(10, 10, 10)
print(test_time2 >= test_time1)
