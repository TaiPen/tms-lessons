import MyTime


class MyTimeInterval:
    def __init__(self,start, finish):
        self.start = MyTime(start)
        self.finish = MyTime(finish)

    def is_inside(self, time):
        return self.start < time <self.finish

    def intersects(self,time_other):
        return
