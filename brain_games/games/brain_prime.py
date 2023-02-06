#!/usr/bin/env python3
"""
Реализация игры "Простое ли число?".
Игроку показывается случайное число. Он должен ответить yes,
если это число является простым, или no, если число простым не является.
"""


import brain_games.tools.game as game
from brain_games.tools.games_logic import prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game.start(prime, rule)


if __name__ == '__main__':
    main()
