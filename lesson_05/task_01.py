def is_palindrome(word):
    pal = list(reversed(word))
    if pal == list(word):
        print(True)
    else:
        print(False)


is_palindrome('ooo')