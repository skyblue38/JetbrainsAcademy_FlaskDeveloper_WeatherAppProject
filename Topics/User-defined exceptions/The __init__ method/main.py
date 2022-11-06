def check_word(word):
    if "0" in list(word):
        raise NotWordError(word)
    return word

def error_handling(word):
    try:
        print(check_word(word))
    except NotWordError:
        print(NotWordError(word).message)

