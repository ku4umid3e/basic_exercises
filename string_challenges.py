# Вывести последнюю букву в слове
word = 'Архангельск'
print(word[-1])

# Вывести количество букв "а" в слове
word = 'Архангельск'
all_a = word.lower().count('а')
print(all_a)

# Вывести количество гласных букв в слове
word = 'Архангельск'
print(all_a+word.count('е'))


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
print(len(sentence.split(' ')))


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
#print(*[i[0] + '\n' for i in sentence.split(' ')])
for word in sentence.split(' '):
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
len_word = []
for word in sentence.split(' '):
    len_word.append(len(word.strip()))
print(int(sum(len_word) / len(len_word)))
