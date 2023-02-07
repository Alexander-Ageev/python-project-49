"""
Логика игры "Простое ли число?".
"""


from random import randint


PRIME_GEN_LIMS = 100


def is_prime(number: int) -> str:
    for i in range(2, number):
        if number % i == 0 and number != i:
            return False
    return True


def prime():
    number = randint(2, PRIME_GEN_LIMS)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = f'{number}'
    return (question, correct_answer)
