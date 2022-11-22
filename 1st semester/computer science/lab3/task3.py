#var1
import re
test_text = ('Классное слово – обороноспособность, которое должно идти после слов: трава и молоко.',
    'Король провёл публичную казнь на глазах у всех.',
    'Ворон сидел в траве и клевал кукурузу.',
    'Работа не волк, волк это ходить, работа это ворк.',
    'Крысы любят сыр, но не любят котов.')

for test_string in test_text:
        test_string = re.findall(r'\w+', test_string)
        test_string = " ".join(test_string).lower() #обьединяем все элементы в одну строку с разделением " ", преобразуя символы верхнего регистяяяяяяяяяяра в нижний,
        words = test_string.split()
        matching_words = []

        for word in words:
                vowels = set(re.findall(r'[аяуеыоэюи]+', word))

        if len(vowels) == 1:
                matching_words.append(word)

        for i in sorted(matching_words, key= lambda x:len(x)):
                print(i)
 
