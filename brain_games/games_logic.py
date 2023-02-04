from random import choice, randint


OPERATIONS = {'+': lambda a, b: a + b,
              '-': lambda a, b: a - b,
              '*': lambda a, b: a * b}
GEN_LIMS = 100


def calc() -> tuple:
    """
    Функция случайным образом генерирует пример вида:
        a [арифметическая операция] b.
    a и b генерируются в диапазоне +-GEN_LIMS,
    допустимые арифметические операции описаны в константе OPERATIONS.
    В результате работы функция возвращает кортеж:
        (строка с примером, правильный ответ).
    """
    a = randint(0, GEN_LIMS)
    b = randint(0, GEN_LIMS)
    operation_type = choice([*OPERATIONS])
    correct_answer = OPERATIONS[operation_type](a, b)
    question = f'Question: {a}{operation_type}{b}'
    return (question, str(correct_answer))


IS_EVEN = {0: 'yes', 1: 'no'}


def check_even():
    """
    Функция генерирует случайное число и возвращает кортеж:
        (вопрос, правильный ответ),
    где правильный ответ "yes", если число четное
    "no" - если нечетное.
    """
    number = randint(1, GEN_LIMS)
    question = f'Question: {number}'
    correct_answer = IS_EVEN[number % 2]
    return (question, correct_answer)


def get_gcd(m: int, k: int) -> int:
    min_number = min(m, k)
    for i in range(min_number, 0, -1):
        if m % i == 0 and k % i == 0:
            break
    return i


def gcd():
    m = randint(1, GEN_LIMS)
    k = randint(1, GEN_LIMS)
    question = f'Question: {m} {k}'
    correct_answer = get_gcd(m, k)
    return (question, str(correct_answer))
