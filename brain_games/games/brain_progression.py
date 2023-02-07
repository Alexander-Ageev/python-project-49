"""
Логика игры "Арифметическая прогрессия".
"""


from random import randint


MIN_SEQUENCE_LEN = 5
MAX_SEQUENCE_LEN = 15
GEN_STEP_LIM = 10
PROGRESSION_GEN_LIMS = 10


def get_progression(start_element: int, step: int, num_elements: int) -> list:
    result = [(start_element + step * i) for i in range(num_elements)]
    return result


def skip_random_element(progression: list) -> str:
    progression = [str(i) for i in progression]
    skip_elemend_id = randint(0, len(progression) - 1)
    skip_index = progression[skip_elemend_id]
    progression[skip_elemend_id] = '..'
    progression_str = ' '.join(progression)
    return (progression_str, skip_index)


def progression():
    num_elements = randint(MIN_SEQUENCE_LEN, MAX_SEQUENCE_LEN)
    start_element = randint(0, PROGRESSION_GEN_LIMS)
    step = randint(1, GEN_STEP_LIM)
    progression = get_progression(start_element, step, num_elements)
    progression_str, correct_answer = skip_random_element(progression)
    question = f'{progression_str}'
    return (question, str(correct_answer))
