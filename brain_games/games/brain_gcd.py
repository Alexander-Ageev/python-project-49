import brain_games.scripts.brain_games as game
from brain_games.games_logic import gcd


def main():
    rule = 'Find the greatest common divisor of given numbers.'
    game.main(gcd, rule)


if __name__ == '__main__':
    main()
