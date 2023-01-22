from random import randint
import prompt


ATTEMPS_NUMS = 3
IS_EVEN = {0: 'yes', 1: 'no'}


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name?\n>>> ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for i in range(ATTEMPS_NUMS):
        number = randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer:\n>>> ').lower()
        correct_answer = IS_EVEN[number % 2]
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(.")
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return None
    print(f'Congratulations, {name}!')
    return None


if __name__ == '__main__':
    main()
