# Напишите функцию get_longest_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое длинное слово из этого текста. Для разбиения строки на слова используйте функцию split.

def get_longest_word(set_words: str):
    import re
    if re.fullmatch(r'[a-zA-Z ]*', set_words):
        str_set = set_words.split()
        for i in str_set:
            long_word = ''
            for word in str_set:                # видел что есть решение используя key=len, но я его до конца не понял
                if len(word) > len(long_word):
                    long_word = word
            return long_word
    else:
        print('Write in Latin letters')


print(get_longest_word('the most Longer word in this set'))
print(get_longest_word('это самое длинное слово в Предложении'))

# почему не работает проверка на латинские буквы и пробелы ...