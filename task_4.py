# 4. Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
#            Первый — возведение в степень с помощью оператора **.
#            Второй — более сложная реализация без оператора **,
#            предусматривающая использование цикла.

def power_1 (num_1, num_2):
    return int(num_1)**int(num_2)
print(power_1(input('Enter base: '), input('Enter negative exponent: ')))

def power_2(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    if n >= 0:
        return res
    else:
        return 1 / res
print(power_2(int(input('Enter base: ')), int(input('Enter negative exponent: '))))