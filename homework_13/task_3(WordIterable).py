class WordIterable:
    def __init__(self, string):
        self.string = string
        self.count = 0

    def __iter__(self):
        self.word = string.split()
        return self

    def __next__(self):
        self.count += 1
        if self.count > len(self.word):
            raise StopIteration()
        return self.word[self.count - 1]


if __name__ == '__main__':
    string = 'один два три четыре пять'
    for i in WordIterable(string):
        print(i)

        assert ['раз', 'два', 'три',] == [i for i in WordIterable('раз два три')]   # не работает :(