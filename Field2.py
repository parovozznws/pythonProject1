class field_of_miracles:

    def word_generation():
        desicion = input('Сыграем в игру? Y/N')
        if desicion == 'Y' or desicion == 'y':
            current_word = random.choice(all_words)
            print('Я загадал слово из ', len(current_word)-1,' букв')
            return current_word.replace('\n','')
        else:
            print('Спасибо за игру!')
        return ''