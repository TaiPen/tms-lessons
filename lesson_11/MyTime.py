class MyTime:
    def __init__(self, seconds):
        self.seconds = float(seconds)

    @property
    def hours(self):
        return int(self.seconds) // 3600

    @property
    def minutes(self):
        return int(self.seconds) % 3600 // 60

    def __mul__(self, num):
        return MyTime(self.seconds * num)

    def __truediv__(self, num):
        return MyTime(self.seconds / num)

    def __floordiv__(self, num):
        return MyTime(self.seconds // num)

    def __eq__(self, other: 'MyTime') -> bool:
        return self.seconds == other.seconds

    def __add__(self, other):
        return MyTime(self.seconds + other.seconds)

    def __sub__(self, other):
        return MyTime(self.seconds - other.seconds)

    def get_formatted_str(self):
        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds % 60:04.1f}'

    def __str__(self):
        return f'{self.seconds}s'


if __name__ == '__main__':
    time = MyTime(3724.5) # 3600 + 120 + 4.5
    assert time.hours == 1
    assert time.minutes == 2
    assert MyTime(5) * 2 == MyTime(10)
    assert MyTime(5) / 2 == MyTime(2.5)
    assert MyTime(5) // 2 == MyTime(2)
    assert MyTime(5) + MyTime(2) == MyTime(7)
    assert MyTime(5) - MyTime(2) == MyTime(3)
    assert str(MyTime(10)) == '10.5s'

    # print(MyTime(10))
    # print(time.get_formatted_str())

