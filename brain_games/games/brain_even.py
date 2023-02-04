import brain_games.scripts.brain_games as game
from brain_games.games_logic import check_even


def main():
    rule = 'Answer "yes" if the number is even, otherwise answer "no".'
    game.main(check_even, rule)


if __name__ == '__main__':
    main()
