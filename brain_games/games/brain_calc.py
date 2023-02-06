#!/usr/bin/env python3
"""
Реализация игры "Калькулятор".
Суть игры в следующем: пользователю показывается
случайное математическое выражение,
например 35 + 16, которое нужно вычислить и записать правильный ответ.
"""


import brain_games.tools.game as game
from brain_games.tools.games_logic import calc


def main():
    rule = 'What is the result of the expression?'
    game.start(calc, rule)


if __name__ == '__main__':
    main()
