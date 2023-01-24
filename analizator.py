def analiz(file_alalize, serarch_word):
    with open(file_alalize, 'r', encoding='utf-8') as f:
        text = f.readlines()
        count_words = 0
        for i in text:
            if serarch_word.lower() in i.lower():
                count_words +=1
        print(f"Нужное слово было найдено {count_words} раз.")

analiz('Отчет.txt', 'Высшее образование')