"""
Реализация игры "Арифметическая прогрессия".
Показываем игроку ряд чисел, образующий арифметическую прогрессию,
заменив любое из чисел двумя точками. Игрок должен определить это число.

Рекомендуемая длина прогрессии – 10 чисел. Длина может генерироваться
случайным образом, но должна содержать не менее 5-ти чисел!
Позиция спрятанного элемента каждый раз изменяется.
"""


import brain_games.tools.game as game
from brain_games.tools.games_logic import progression


def main():
    rule = 'What number is missing in the progression?'
    game.start(progression, rule)


if __name__ == '__main__':
    main()
