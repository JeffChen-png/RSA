import random

fermat_number = [3, 17, 257, 65537]


def is_prime(n, k):  # miller-rabin
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
        if n % p == 0:
            return n == p
    s, d = 0, n - 1
    while d % 2 == 0:
        s, d = s + 1, d // 2
    for i in range(k):
        x = pow(random.randint(2, n - 1), d, n)
        if x == 1 or x == n - 1:
            continue
        for r in range(1, s):
            x = (x * x) % n
            if x == 1:
                return False
            if x == n - 1:
                break
        else:
            return False
    return True


# def is_prime(T):
#     for k in range(10):
#         if pow(random.randint(0, T - 1), T - 1) % T == 1:
#             print(k)
#             return True
#         else:
#             print(k)
#             return False


def prime_numbers_generator(length):
    num = bin(0)
    num += (bin(random.getrandbits(length - 1))[2:])
    # while not is_prime(int(num, 2), 10):
    #     num = bin(1)
    #     num += (bin(random.getrandbits(length - 1))[2:])
    return int(num, 2)


def euler_method(p, q):
    fi = (p - 1) * (q - 1)

    return fi


def euclidean_method(a, b):
    while b:
        a, b = b, a % b

    return a


def extended_euclidean_method(a, b):
    x, xx, y, yy = 1, 0, 0, 1
    while b:
        q = a // b
        a, b = b, a % b
        x, xx = xx, x - xx * q
        y, yy = yy, y - yy * q

    return x


def n_generation(p, q):
    n = p * q

    return n


def e_generation(fi, n):
    e = fermat_number[random.randint(0, len(fermat_number) - 1)]

    while not (euclidean_method(fi, e) == 1) & (e < n):
        e = e_generation(fi, n)

    return e


def d_generation(e, fi):
    d = extended_euclidean_method(e, fi)

    if d < 0:
        d += fi

    return d


def open_key_generation(e, n):
    open_key = ' '.join(map(str, [bin(e)[2:], bin(n)[2:]]))

    with open('open_key.txt', mode='w') as file:
        file.write(open_key)

    # key = key.split(" ")
    # print('readed key', '{0:08b}'.format(ord(key[0])), 'b', int(key[1], 2))


def secret_key_generation(d, n):
    secret_key = ' '.join(map(str, [bin(d)[2:], bin(n)[2:]]))

    with open('secret_key.txt', mode='w') as file:
        file.write(secret_key)


def exponentiation(x, d, n):  # возведение в степень
    y = 1

    while d > 0:
        if d % 2 != 0:
            y = (y * x) % n
        d = d // 2
        x = (x * x) % n

    return y


def encrypt(text, length, key_part, n):
    out_text = []

    for i in range(0, len(text), length // 4):
        out_text.append(bin(exponentiation(int((text[i: i + length // 4]), 2), key_part, n))[2:])
        # out_text.append((exponentiation(int((text[i: i + length // 4]), 2), key_part, n)))

    encrypted = ' '.join(map(str, out_text))

    return encrypted


def decrypt(text, length, key_part, n):
    text = text.split(' ')
    out_text = []

    for el in text:
        out_text.append(bin(exponentiation(int(el, 2), key_part, n))[2:].zfill(length // 4))

    decrypted = ''.join(map(str, out_text))
    print('output text bits:', decrypted)
    dec_text = int(decrypted, 2)

    decrypted = dec_text.to_bytes((dec_text.bit_length()) + 7 // 8, 'big').decode()
    print('output text text:', decrypted)

    return decrypted
