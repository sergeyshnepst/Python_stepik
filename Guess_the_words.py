import random

ru_alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
word_list = [
    "стот",
    "стут",
    "кровоть",
    "кресле",
    "шкак",
    "полка",
    "тумба",
    "автомобиль",
]

guessed = False  # сигнальная метка
guessed_letters = []  # список уже названных букв
guessed_words = []  # список уже названных слов
tries = 6  # количество попыток


def get_word():
    return random.choice(word_list)


# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return print(stages[tries])


def play(tries):
    print("Давайте играть в угадайку слов!\n")
    print("Для выхода введите 'q'")
    display_hangman(tries)
    print("Вам дается 6 попыток необходимо побуквенно отгадать загаданное слово")
    print(f"Загаданное слово содержит {len(word)} букв")
    # строка, содержащая символы _ на каждую букву задуманного слова
    word_completion = "_" * len(word)
    print(word_completion)


def guess_letter():
    global word
    global tries
    word_completion = "_" * len(word)
    while word_completion != word and tries != 0:
        letter = input("\nВведите букву или слово целиком:\n")
        # Ветка, если введено слово целиком
        if len(letter) > 1:
            if letter in guessed_words:
                print("Вы уже вводили это слово")
            elif letter != word:
                tries -= 1
                print("Это не то слово")
                display_hangman(tries)
            else:
                word_completion = letter
            guessed_words.append(letter)
        # Ветка, если введена только одна буква
        else:
            if letter.lower() == "q":
                print("Вы вышли из игры")
                break
            elif letter.lower() in ru_alphabet:
                if letter.lower() in word:
                    for i in range(len(word)):
                        if word[i] == letter.lower():
                            word_completion = (
                                word_completion[:i] + word[i] + word_completion[i + 1 :]
                            )
                    print("Такая буква есть в этом слове")
                elif letter.lower() in guessed_letters:
                    print("Вы уже называли такую букву")
                else:
                    tries -= 1
                    print("Такой буквы нет в этом слове")
                guessed_letters.append(letter)
                display_hangman(tries)
            else:
                print("\nМожно ввесть только русскую букву")
            print(word_completion)
    if word_completion == word:
        print("Поздравляю, Вы выиграли!")
        display_hangman(tries)
    else:
        print("Вы проиграли, попробуйте в следующий раз")


tries = 6
word = get_word()
play(tries)
guess_letter()
