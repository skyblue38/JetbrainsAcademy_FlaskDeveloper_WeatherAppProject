name = input()

def normalize(a_name):
    mapping = {'é': 'e', 'ë': 'e', 'á': 'a', 'å': 'aa', 'œ': 'oe', 'æ': 'ae'}
    new_name = ''
    for char in a_name:
        new_name = new_name + mapping.get(char, char)
    return new_name

print(normalize(name))
