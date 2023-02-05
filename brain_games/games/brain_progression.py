import brain_games.scripts.brain_games as games
from brain_games.games_logic import progression


def main():
    rule = 'What number is missing in the progression?'
    games.main(progression, rule)


if __name__ == '__main__':
    main()
