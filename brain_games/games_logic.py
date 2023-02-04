from random import choice, randint


OPERATIONS = ['+', '-', '*']
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
    a = randint(-GEN_LIMS, GEN_LIMS)
    b = randint(-GEN_LIMS, GEN_LIMS)
    operation_type = choice(OPERATIONS)
    if operation_type == '+':
        correct_answer = a + b
    elif operation_type == '-':
        correct_answer = a - b
    elif operation_type == '*':
        correct_answer = a * b
    else:
        question = 'wrong arithmetic operation'
    question = f'Question: {a} {operation_type} {b}'
    return (question, str(correct_answer))


IS_EVEN = {0: 'yes', 1: 'no'}


def check_even():
    number = randint(1, 100)
    question = f'Question: {number}'
    correct_answer = IS_EVEN[number % 2]
    return (question, correct_answer)
