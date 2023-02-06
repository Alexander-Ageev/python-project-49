#!/usr/bin/env python3
"""
Реализация игры "Проверка на чётность".
Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число чётное, или no — если нечётное.

"""


import brain_games.tools.game as game
from brain_games.tools.games_logic import even


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    game.start(even, rule)


if __name__ == '__main__':
    main()
