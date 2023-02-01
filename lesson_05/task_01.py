def is_palindrome(word):
    pal = str(reversed(word))
    if pal == word:
        print(True)
    else:
        print(False)


is_palindrome('olo')