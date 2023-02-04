import prompt


def welcome():
    print('Welcome to the Brain Games!')


def username_request() -> str:
    name = prompt.string('May I have your name?\n>>> ')
    return name


def hello(name: str) -> str:
    print(f'Hello, {name}!')


def get_rule(rule: str):
    if rule is not None:
        print(rule)


def calc_rule():
    print('What is the result of the expression?')


def get_question(question: str) -> tuple:
    print(question)
    answer = prompt.string('Your answer:\n>>> ').lower()
    return answer


def check_answer(answer: str, correct_answer: str, name: str) -> bool:
    if answer == correct_answer:
        print('Correct!')
        result = True
    else:
        print(f"'{answer}' is wrong answer ;(.")
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        result = False
    return result


def congratuletions(name: str) -> None:
    print(f'Congratulations, {name}!')
