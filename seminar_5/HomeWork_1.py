# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
from random import sample
import random

f=lambda count,word:' '.join([''.join(random.sample(word, len(word))) for x in range(count)])
k=f(8,'abw')
print(k)

w=k.split()

d=lambda txt,word:' '.join([txt[x] for x in range(len(txt)-1) if word!=txt[x]])
print(d(w,'abw'))

