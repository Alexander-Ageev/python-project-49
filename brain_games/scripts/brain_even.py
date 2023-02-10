#!/usr/bin/env python3
"""
Реализация игры "Проверка на чётность".
Суть игры в следующем: пользователю показывается случайное число.
И ему нужно ответить yes, если число чётное, или no — если нечётное.

"""


import brain_games.engine.engine as game
from brain_games.games.brain_even import even


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    game.play_game(even, rule)


if __name__ == '__main__':
    main()
