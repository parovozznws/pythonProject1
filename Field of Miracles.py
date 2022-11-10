# Игра "Поле чудес". Количество попыток вводится пользователем

import random

f = open('WordsStockRus.txt', 'r', encoding="utf-8")
all_words = f.readlines()
f.close()

def word_generation():
    desicion = input('Сыграем в игру? Y/N')
    if desicion == 'Y' or desicion == 'y':
        current_word = random.choice(all_words)
        print('Я загадал слово из ', len(current_word)-1,' букв')
        return current_word.replace('\n','')
    else:
        print('Спасибо за игру!')
        return ''

def number_of_movies():
    number_movies = input('Введите количество попыток: ')
    if not number_movies.isdigit():
        print('Это не число')
        return 0
    else:
        return int(number_movies)

def transfer_letter(new_string, all_letters):
    i = 0
    k = 0
    my_string =''
    letter = input('Ведите букву: ')
    all_letters += letter
    while i<len(current_word):
        if letter.lower() != current_word[i]:
            if new_string[i] == '-':
                my_string += '-'
            else:
                my_string += new_string[i]
        else:
            my_string += letter.lower()
            k += 1
        i += 1
    if k > 0:
        print('В этом слове ',k,' букв ',letter)
    else:
        print('В этом слове нет буквы ',letter)
    print(my_string)
    return my_string, all_letters


def is_win(new_string, all_letters):
    i = 0
    while i < number_movies:
        new_string, all_letters = transfer_letter(new_string, all_letters)
        if new_string == current_word:
            print('Поздравляю! Вы угадали слово за ', i + 1, ' попыток')
            i = number_movies+1
        else:
            i += 1
            print('Осталось ',number_movies - i,' попыток')
    if i == number_movies:
        fast_word = input('Введите слово\n')
        if fast_word == current_word:
            print('Поздравляю! Вы угадали слово за ', i + 1, ' попыток')
        else:
            print('Вы проиграли! Загаданное слово:',current_word)
    print('Все названные буквы: ', sorted(all_letters))




current_word = word_generation()
new_string = ('-' * len(current_word))
print(new_string)
all_letters = ''
number_movies = number_of_movies()
is_win(new_string, all_letters)









