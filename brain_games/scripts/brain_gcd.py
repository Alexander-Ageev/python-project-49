#!/usr/bin/env python3
"""
Реализация игры "наибольший общий делитель (НОД)".
Суть игры в следующем: пользователю показывается два случайных числа,
например, 25 50. Пользователь должен вычислить
и ввести наибольший общий делитель этих чисел.
"""


import brain_games.engine.engine as game
from brain_games.games.brain_gcd import gcd


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    game.play_game(gcd, rule)


if __name__ == '__main__':
    main()
