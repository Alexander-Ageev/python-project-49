import brain_games.scripts.brain_games as game
from brain_games.games_logic import prime


def main():
    rule = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    game.main(prime, rule)


if __name__ == '__main__':
    main()
