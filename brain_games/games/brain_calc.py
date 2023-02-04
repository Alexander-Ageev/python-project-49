import brain_games.scripts.brain_games as games
from brain_games.games_logic import calc


def main():
    rule = 'What is the result of the expression?'
    games.main(calc, rule)


if __name__ == '__main__':
    main()
