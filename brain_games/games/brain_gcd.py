"""
Логика игры "Наибольший общий делитель".
"""

from random import randint


GCD_GEN_LIMS = 100


def get_gcd(m: int, k: int) -> int:
    min_number = min(m, k)
    for i in range(min_number, 0, -1):
        if m % i == 0 and k % i == 0:
            break
    return i


def gcd():
    m = randint(1, GCD_GEN_LIMS)
    k = randint(1, GCD_GEN_LIMS)
    question = f'{m} {k}'
    correct_answer = get_gcd(m, k)
    return (question, str(correct_answer))
