"""
Логика игры "Простое ли число?".
"""


from random import randint
# число 1 формально не является простым,
# лучше избежать разночтений и не генерировать его.
LOWER_BOUND = 2
UPPER_BOUND = 100


def is_prime(number: int) -> str:
    for i in range(2, number):
        if number % i == 0 and number != i:
            return False
    return True


def prime():
    number = randint(LOWER_BOUND, UPPER_BOUND)
    correct_answer = 'yes' if is_prime(number) else 'no'
    question = f'{number}'
    return question, correct_answer
