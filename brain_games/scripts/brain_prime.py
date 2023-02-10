#!/usr/bin/env python3
"""
Реализация игры "Простое ли число?".
Игроку показывается случайное число. Он должен ответить yes,
если это число является простым, или no, если число простым не является.
"""


import brain_games.engine.engine as game
from brain_games.games.brain_prime import prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game.play_game(prime, rule)


if __name__ == '__main__':
    main()
