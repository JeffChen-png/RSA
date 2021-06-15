from functions import *
from pollard import *

print("Введите требуемую длинну ключа:")
length = int(input())

p = prime_numbers_generator(int(length // 2))
q = prime_numbers_generator(int(length // 2))
print('p {} and q {}'.format(p, q))
fi = euler_method(int(p), int(q))
n = n_generation(int(p), int(q))
e = e_generation(int(fi), int(n))
print('open key:', e, n)
d = d_generation(int(e), int(fi))
print('secret key:', d, n)
open_key_generation(e, n)
secret_key_generation(d, n)

with open('text.txt') as file:
    input_text = file.read()

text = ''.join('{0:08b}'.format(ord(x), 'b') for x in input_text)
# text = ''.join([format(int.from_bytes(i.encode(), 'big'), '08b') for i in input_text])
print('input text  bits:', text)
print('len:', len(text))

encrypt = encrypt(text, length, e, n)

with open('encrypt.txt', mode='w') as file:
    file.write(encrypt)
print('len encrypt:', len(encrypt))

decrypt = decrypt(encrypt, length, d, n)

with open('decrypt.txt', mode='w') as file:
    file.write(decrypt)
print('len decrypt:', len(decrypt))

