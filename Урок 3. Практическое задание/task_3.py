from hashlib import sha256

MY_STRING = input('Введите строку!: ')
MY_LIST = []
MY_HASH_SET = set()


def under_strings(my_string_of_letters, my_l, number_of_letters):
    if number_of_letters == len(my_string_of_letters):
        return my_l
    else:
        for i in range(0, len(my_string_of_letters) + 1 - number_of_letters):
            my_l.append(my_string_of_letters[i:(i + number_of_letters)])
        return under_strings(my_string_of_letters, my_l, number_of_letters + 1)


def make_hash():
    for word in under_strings(MY_STRING, MY_LIST, 1):
        MY_HASH_SET.add(sha256(bytes(word, 'utf-8')).hexdigest())
    print(MY_HASH_SET)
    print(set(MY_LIST))
    print(len(MY_HASH_SET))


make_hash()
