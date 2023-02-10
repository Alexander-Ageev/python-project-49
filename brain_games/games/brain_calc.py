"""
Логика игры "Калькулятор".
"""


from random import choice, randint


OPERATIONS = {'+': lambda a, b: a + b,
              '-': lambda a, b: a - b,
              '*': lambda a, b: a * b}
LOWER_BOUND = 0
UPPER_BOUND = 100


def calc() -> tuple:
    """
    Функция случайным образом генерирует пример вида:
        a [арифметическая операция] b.
    a и b генерируются в диапазоне +-GEN_LIMS,
    допустимые арифметические операции описаны в константе OPERATIONS.
    В результате работы функция возвращает кортеж:
        (строка с примером, правильный ответ).
    """
    a = randint(LOWER_BOUND, UPPER_BOUND)
    b = randint(LOWER_BOUND, UPPER_BOUND)
    operation_type = choice([*OPERATIONS])
    correct_answer = OPERATIONS[operation_type](a, b)
    question = f'{a} {operation_type} {b}'
    return (question, str(correct_answer))
