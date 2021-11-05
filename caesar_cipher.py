def language(english=False, russian=False):
    if english:
        lst = [i for i in "abcdefghijklmnopqrstuvwxyz"]
    if russian:
        lst = [i for i in "абвгдежзийклмнопрстуфхцчшщъыьэюя"]
    return lst


def main_program(language_lst, coder=False, decoder=False):
    finish_text = ""
    start_text1 = ""
    start_text_lst = []
    index = 0

    if choice == "1":
        step = int(input("Введите шаг сдвига. Значение должно быть больше нуля: "))
        start_text = input("Введите текст для трансформации: ")
        for i in range(len(start_text)):
            if start_text[i].isalpha():
                length_range = language_lst.index(start_text[i].lower())
                if coder:
                    if length_range + step > 0:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range + step - len(language_lst)].upper()
                        else:
                            finish_text += language_lst[length_range + step - len(language_lst)]
                    else:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range + step].upper()
                        else:
                            finish_text += language_lst[length_range + step]
                if decoder:
                    if length_range - step < 0:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range - step + len(language_lst)].upper()
                        else:
                            finish_text += language_lst[length_range - step + len(language_lst)]
                    else:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range - step].upper()
                        else:
                            finish_text += language_lst[length_range - step]
            elif start_text[i] == " ":
                finish_text += start_text[i]
            else:
                finish_text += start_text[i]

    if choice == "2":
        start_text = input("Введите текст для трансформации: ")
        for i in range(len(start_text)):
            if start_text[i].isalpha():
                start_text1 += start_text[i]
            elif start_text[i] == " ":
                start_text_lst.append(start_text1)
                start_text1 = ""
        start_text_lst.append(start_text1)

        for i in range(len(start_text)):
            if start_text[i].isalpha():
                length_range = language_lst.index(start_text[i].lower())
                step = len(start_text_lst[index])
                if coder:
                    if length_range + step > 0:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range + step - len(language_lst)].upper()
                        else:
                            finish_text += language_lst[length_range + step - len(language_lst)]
                    else:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range + step].upper()
                        else:
                            finish_text += language_lst[length_range + step]
                if decoder:
                    if length_range - step < 0:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range - step + len(language_lst)].upper()
                        else:
                            finish_text += language_lst[length_range - step + len(language_lst)]
                    else:
                        if start_text[i] == start_text[i].upper():
                            finish_text += language_lst[length_range - step].upper()
                        else:
                            finish_text += language_lst[length_range - step]
            elif start_text[i] == " ":
                finish_text += start_text[i]
                index += 1
            else:
                finish_text += start_text[i]
    print(finish_text)


while True:
    coder1 = input("Для шифрования текста введите - 1, для дешифрования введите - 2: ")
    if coder1 == "1":
        coder1 = True
        decoder1 = False
        break
    elif coder1 == "2":
        coder1 = False
        decoder1 = True
        break
    else:
        print("Ошибка ввода! Введите значение 1 или 2")

while True:
    english1 = input("Выберите язык текста, английский - 1, русский - 2: ")
    if english1 == "1":
        english1 = True
        russian1 = False
        break
    elif english1 == "2":
        english1 = False
        russian1 = True
        break
    else:
        print("Ошибка ввода! Введите значение 1 или 2")

while True:
    choice = input("Выберите сдвиг шифрования. Постоянный - 1, переменный - 2: ")
    if choice == "1" or choice == "2":
        break
    else:
        print("Ошибка ввода! Введите правильное значение 1 или 2")


language_lst1 = language(english1, russian1)
main_program(language_lst1, coder1, decoder1)
