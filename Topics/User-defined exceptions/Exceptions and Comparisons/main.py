class WordError(Exception):
    pass


def check_w_letter(word):
    if "w" in list(word):
        raise WordError
    return word
