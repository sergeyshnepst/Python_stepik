import random

left, right = 1, 100


def random_number(fromm, to):
    num = random.randint(fromm, to)
    count = 1
    while True:
        user_num = int(input())
        count += 1
        if user_num > num:
            print("Слишком много, попробуйте еще раз")
            continue
        elif user_num < num:
            print("Слишком мало, попробуйте еще раз")
            continue
        else:
            return f"Вы угадали, поздравляем! \nКоличетсво попыток: {count}"


# пока не предумал как встроить через функцию
# количество попыток для угадывания == 7
def number_of_attempts():
    middle = (left + right) // 2
    count = 1
    while middle != num:
        if middle < num:
            print("мало")
            left = middle + 1
            middle = (left + right) // 2
        elif middle > num:
            print("много")
            right = middle - 1
            middle = (left + right) // 2
        num = int(input())
        count += 1
    print("Угадали", num)
    print(count)


print(random_number(left, right))
