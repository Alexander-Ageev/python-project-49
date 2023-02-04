#!/usr/bin/env python3
import brain_games.cli as cli


ATTEMPS_NUMS = 3


def main(function=None):
    cli.welcome()
    name = cli.username_request()
    cli.hello(name)
    if function is not None:
        for i in range(ATTEMPS_NUMS):
            message, correct_answer = function()
            answer = cli.get_question(message)
            is_correct = cli.check_answer(answer, correct_answer, name)
            if not is_correct:
                return None
        cli.congratuletions(name)


if __name__ == '__main__':
    main()
