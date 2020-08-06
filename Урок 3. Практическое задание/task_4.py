from hashlib import sha512

URL_CASH_LIST = []


def url_hashing(url):
    url_hash = sha512(bytes(url * 7, 'utf-8')).hexdigest()
    if url_hash not in URL_CASH_LIST:
        URL_CASH_LIST.append(url_hash)
        print(URL_CASH_LIST)
        url_hashing(input('Введите URL: '))
    else:
        print('Такой адрес уже есть в кэше!')
        print(URL_CASH_LIST)
        url_hashing(input('Введите URL: '))


url_hashing(input('Введите URL: '))
