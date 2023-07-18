# Сделать программу в виде функций в которой нужно будет угадывать число.

from random import randint

DELIMITER = "." * 120

def intro() -> None:
    print(DELIMITER)
    print("Привіт, вгадай число від 1 до 10 включно за 3 спроби")
    print(DELIMITER)


def generate_data() -> (int, int):
    max_attempts = 3
    return randint(1, 10), max_attempts


def game_process(number: int, max_attempts: int) -> None:
    print("Починаємо")

    user_attempts = 0
    while True:
        print(DELIMITER)

        if max_attempts == user_attempts + 1:
            print("Остання спроба")
        else:
            print(f"залишилось спроб: {max_attempts - user_attempts}")

        if user_attempts >= max_attempts:
            print(f"спроби закінчились, моє число: {number}")
            break

        user_attempts += 1
        user_num = input("Твоє число? ")
        if not user_num.isdigit():
            print("Не вгадано.")
            continue

        user_num = int(user_num)
        if user_num < number:
            print("Я загадала більше  число!")
        elif user_num > number:
            print("Я загадала менше число!")
        else:
            print(f"Молодець, ти вгадав за {user_attempts} "
                  f"спроб {'у'if user_attempts == 1 else'и'}")
            break
    print(DELIMITER)


def get_exit() -> bool:
    res = False
    user_answer = input("Хочеш вийти? (y/т) ")
    if user_answer.lower() in ('y', 'д'):
        print("Що ж, па-па!")
        print(DELIMITER)
        res = True
    return res


def main():
    while True:
        intro()
        number, max_attempts = generate_data()
        game_process(number, max_attempts)
        if get_exit():
            break


main()