# Напишите функцию get_most_frequent_word, которая на вход принимает текст (только английские слова и пробелы),
# и возвращает самое часто встречающееся слово. Если таких слов несколько - верните любое.

def get_most_frequent_word (set_words: str):
    str_set = set_words.split()
    duble = {x for x in str_set if str_set.count(x) > 1}
    return duble


print(get_most_frequent_word('and me and you and him about me to me'))


# решение нагуглил :)