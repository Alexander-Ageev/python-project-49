"""
Логика игры "Наибольший общий делитель".
"""

from random import randint

LOWER_BOUND = 1
UPPER_BOUND = 100


def get_gcd(m: int, k: int) -> int:
    min_number = min(m, k)
    for i in range(min_number, 0, -1):
        if m % i == 0 and k % i == 0:
            break
    return i


def get_gcd_evkl(m: int, k: int) -> int:
    min_number = min(m, k)
    max_number = max(m, k)
    while max_number % min_number != 0:
        remainder = max_number % min_number
        # Сначала вычисляем максимальный элемент,
        # иначе минимальный элемент поменяется и рассчеты будут некорректными
        max_number = max(min_number, remainder)
        min_number = min(min_number, remainder)
    return min_number


def gcd():
    m = randint(LOWER_BOUND, UPPER_BOUND)
    k = randint(LOWER_BOUND, UPPER_BOUND)
    question = f'{m} {k}'
    correct_answer = get_gcd(m, k)
    return (question, str(correct_answer))
