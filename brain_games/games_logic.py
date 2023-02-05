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


MIN_SEQUENCE_LEN = 5
MAX_SEQUENCE_LEN = 15
GEN_STEP_LIM = 10


def get_progression(start_element: int, step: int, num_elements: int) -> list:
    result = [str(start_element + step * i) for i in range(num_elements)]
    return result


def progression():
    num_elements = randint(MIN_SEQUENCE_LEN, MAX_SEQUENCE_LEN)
    start_element = randint(0, GEN_LIMS)
    step = randint(1, GEN_STEP_LIM)
    progression_list = get_progression(start_element, step, num_elements)
    skip_elemend_id = randint(0, len(progression_list) - 1)
    correct_answer = progression_list[skip_elemend_id]
    progression_list[skip_elemend_id] = '..'
    progression_str = ' '.join(progression_list)
    question = f'Question: {progression_str}'
    return (question, str(correct_answer))


def is_prime(number: int) -> str:
    for i in range(2, number):
        if number % i == 0 and number != i:
            return 'no'
    return 'yes'


def prime():
    number = randint(2, GEN_LIMS)
    correct_answer = is_prime(number)
    question = f'Question: {number}'
    return (question, correct_answer)
