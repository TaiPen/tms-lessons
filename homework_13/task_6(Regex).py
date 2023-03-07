import re

def generate_words(string: str):
    list_str = re.findall(r'[а-яА-Яa-zA-z]+', string)
    for i in list_str:
        yield i


if __name__ == '__main__':
    string = 'один два три четыре пять'
    for i in generate_words(string):
        print(i)

    assert ['раз', 'два', 'три', ] == [i for i in generate_words('раз. два! +три*')]   # не работает :(