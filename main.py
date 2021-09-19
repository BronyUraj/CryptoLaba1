import string
alphabetrus = ''.join([chr(i) for i in range(ord('а'), ord('а') + 6)] + [chr(ord('а') + 33)] + [chr(i) for i in
                                                                                                range(ord('а') + 6,
                                                                                                      ord('а') + 32)])

alphabeteng = string.ascii_lowercase
task6_crypt = "Pbatenghyngvbaf! Vg'f n Pnrfne pvcure!".lower()

def task1encr(opentext, key):
    result_encr = [''] * len(opentext)
    cur = 0
    index = 0
    for i in range(0, len(opentext)):
        result_encr[i] = opentext[index]
        index += key
        if index >= len(opentext):
            cur += 1
            index = cur

    return ''.join(result_encr)


def task1decr(crypttext, key):
    result_encr = [''] * len(crypttext)
    cur = 0
    index = 0
    for i in range(0, len(crypttext)):
        result_encr[index] = crypttext[i]
        index += key
        if index >= len(crypttext):
            cur += 1
            index = cur

    return ''.join(result_encr)


def task2encr(opentext, key1, key2):
    result_encr = ""
    for i in range(0, len(opentext)):
        if i % 2 != 0:
            result_encr += alphabetrus[(alphabetrus.index(opentext[i]) - key1) % 33]
        else:
            result_encr += alphabetrus[(alphabetrus.index(opentext[i]) + key2) % 33]
    return result_encr


def task2decr(crypttext, key1, key2):
    result_decr = ""
    for i in range(0, len(crypttext)):
        if i % 2 != 0:
            result_decr += alphabetrus[(alphabetrus.index(crypttext[i]) + key1) % 33]
        else:
            result_decr += alphabetrus[(alphabetrus.index(crypttext[i]) - key2) % 33]
    return result_decr


def task6Decr(crypttext):
    result_decr = ""
    for k in range(1, 33):
        for i in range(0, len(crypttext)):
            if crypttext[i] in alphabeteng:
                result_decr += alphabeteng[(alphabeteng.index(crypttext[i]) + k) % 26]
            else:
                result_decr += crypttext[i]
        print(result_decr, "key = ", k)
        result_decr = ""

def task7encr(opentext):
    result_encr = ""
    for i in range(0, len(opentext)):
        if opentext[i] in alphabetrus:
            result_encr += alphabetrus[(alphabetrus.index(opentext[i]) + 13) % 33]
        else:
            result_encr += opentext[i]
    return result_encr

def task7decr(crypttext):
    result_decr = ""
    for i in range(0, len(crypttext)):
        if crypttext[i] in alphabetrus:
            result_decr += alphabetrus[(alphabetrus.index(crypttext[i]) - 13) % 33]
        else:
            result_decr += crypttext[i]
    return result_decr

if __name__ == '__main__':
    # print(task2encr("привет", 5, 8))
    # print(task2decr("члрэмн", 5, 8))
    # print(task1encr("Приколист", 4))
    # print(task1decr("Потрлиикс", 4))
    #task6Decr(task6_crypt)
    print(task7encr("Проверка Шифра Цезаря".lower()))
    print(task7encr("ьэыосэчм ехбэм гсфмэл"))

