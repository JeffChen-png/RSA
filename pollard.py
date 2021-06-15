# import time
# from functions import *
# import matplotlib.pyplot as plt
#
#
# def rho_pollard(n):
#     x = random.randint(0, n - 2)
#     y = 1
#     i = 1
#     stage = 2
#     while euclidean_method(n, abs(x - y)) == 1:
#         if stage == i:
#             y = x
#             stage = 2 * stage
#         x = (x * x + 1) % n
#         i += 1
#
#     return euclidean_method(n, abs(x - y))
#
#
# t_array = []
# l_array = []
#
# for i in range(30, 100, 2):
#     p = prime_numbers_generator(int(i // 2))
#     q = prime_numbers_generator(int(i // 2))
#     print('p {} and q {}'.format(p, q))
#     n = int(p) * int(q)
#     start_time = time.time()
#     pp = rho_pollard(n)
#     t = time.time() - start_time
#     print('RHO p {} and q {}'.format(pp, int(n/pp)))
#     t_array.append(t)
#     l_array.append(i)
#     print('t =', t)
#     print('length:', i)
#     print('_________________________________________')
#
# plt.title("Зависимости времени разложения t от l")  # заголовок
# plt.xlabel("Длинна ключа")  # ось абсцисс
# plt.ylabel("Время вычисления")  # ось ординат
# plt.grid()  # включение отображение сетки
# plt.plot(l_array, t_array)  # построение графика
# plt.show()
#
# r = 0.25
# t_array = []
# r_array = []
# while r <= 0.75:
#     p = prime_numbers_generator(int(r*70))
#     q = prime_numbers_generator(int((1-r)*70))
#     print('p {} and q {}'.format(p, q))
#     n = int(p) * int(q)
#     start_time = time.time()
#     pp = rho_pollard(n)
#     t = time.time() - start_time
#     print('RHO p {} and q {}'.format(pp, int(n/pp)))
#     t_array.append(t)
#     r_array.append(r)
#     print('t =', t)
#     print('r:', r)
#     print('_________________________________________')
#     r += 0.05
#
# plt.title("График зависимости времени разложения t от r")  # заголовок
# plt.xlabel("r")  # ось абсцисс
# plt.ylabel("Время вычисления")  # ось ординат
# plt.grid()  # включение отображение сетки
# plt.plot(r_array, t_array)  # построение графика
# plt.show()
