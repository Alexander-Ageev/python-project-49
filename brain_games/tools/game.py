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


import brain_games.tools.cli as cli


ATTEMPS_NUMS = 3


def start(function=None, rule=None):
    cli.welcome()
    name = cli.username_request()
    cli.hello(name)
    cli.get_rule(rule)
    if function is not None:
        for i in range(ATTEMPS_NUMS):
            message, correct_answer = function()
            answer = cli.get_question(message)
            is_correct = cli.check_answer(answer, correct_answer, name)
            if not is_correct:
                return None
        cli.congratulations(name)
