"""
Модуль реализует алгоритм проведения игры:
1. Приветствие
2. Знакомство с пользователем
3. Описание правил игры
4. Проведение игры
Пользователю задается по очереди три вопроса.
Если в течение трех вопросов пользователь ошибается - игра заканчивается,
а пользователю предлагается попробовать начать сначала.
Если пользователь правильно ответил на три вопроса - игра заканчивается,
а пользователь поздравляется с успешным прохождением игры.
"""


import prompt


ATTEMPS_NUMS = 3


def start(function=None, rule=None):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n>>> ')
    print(f'Hello, {name}!')
    if rule is not None:
        print(rule)
    if function is not None:
        for i in range(ATTEMPS_NUMS):
            question, correct_answer = function()
            print(f'Question: {question}')
            answer = prompt.string('Your answer:\n>>> ').lower()
            if answer == correct_answer:
                print('Correct!')
            else:
                print(f"'{answer}' is wrong answer ;(.")
                print(f"Correct answer was '{correct_answer}'.")
                print(f"Let's try again, {name}!")
                return None
        print(f'Congratulations, {name}!')
