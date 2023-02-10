"""
Логика игры "Арифметическая прогрессия".
"""


from random import randint


MIN_SEQUENCE_LEN = 5
MAX_SEQUENCE_LEN = 15
STEP_UPPER_BOUND = 10
LOWER_BOUND = 0
UPPER_BOUND = 10


def get_progression(start_element: int, step: int, num_elements: int) -> list:
    result = [(start_element + step * i) for i in range(num_elements)]
    return result


def skip_element(progression: list, skip_index: int) -> str:
    progression = [str(i) for i in progression]
    progression[skip_index] = '..'
    progression_str = ' '.join(progression)
    return progression_str


def progression():
    num_elements = randint(MIN_SEQUENCE_LEN, MAX_SEQUENCE_LEN)
    start_element = randint(LOWER_BOUND, UPPER_BOUND)
    step = randint(1, STEP_UPPER_BOUND)
    progression = get_progression(start_element, step, num_elements)
    skip_elemend_id = randint(0, len(progression) - 1)
    correct_answer = progression[skip_elemend_id]
    progression_str = skip_element(progression)
    question = f'{progression_str}'
    return (question, str(correct_answer))
