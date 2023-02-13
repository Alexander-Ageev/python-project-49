"""
Логика игры "Проверка на чётность".
"""


from random import randint


IS_EVEN = {0: 'yes', 1: 'no'}
LOWER_BOUND = 1
UPPER_BOUND = 100


def even():
    """
    Функция генерирует случайное число и возвращает кортеж:
        (вопрос, правильный ответ),
    где правильный ответ "yes", если число четное
    "no" - если нечетное.
    """
    number = randint(LOWER_BOUND, UPPER_BOUND)
    question = f'{number}'
    correct_answer = IS_EVEN[number % 2]
    return question, correct_answer
