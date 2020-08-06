from hashlib import sha256

my_string = input('Введите строку!: ')
my_list = []
my_hash_set = set()


def under_strings(my_string_of_letters, my_l, number_of_letters):
    if number_of_letters == len(my_string_of_letters):
        return my_l
    else:
        for i in range(0, len(my_string_of_letters) + 1 - number_of_letters):
            my_l.append(my_string_of_letters[i:(i + number_of_letters)])
        return under_strings(my_string_of_letters, my_l, number_of_letters + 1)


def make_hash():
    for word in under_strings(my_string, my_list, 1):
        my_hash_set.add(sha256(bytes(word, 'utf-8')).hexdigest())
    print(my_hash_set)
    print(set(my_list))
    print(len(my_hash_set))


make_hash()
