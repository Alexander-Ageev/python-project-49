import brain_games.tools.game as game
from brain_games.tools.games_logic import prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game.start(prime, rule)


if __name__ == '__main__':
    main()
