class SquaresIterable:
    def __int__(self, count):
        self.count = count
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.num += 1
        if self.num > self.count
            raise StopIteration()
        return self.num ** 2


for i in SquaresIterable(10):
    print(i)
#
# def generate_squares(count):
#     for i in range(1, count + 1):
#         yield i ** 2
#
# if __name__ == '__main__':
#     for i in generate_squares(10):
#         print(i)