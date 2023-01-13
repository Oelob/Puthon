# Напишите программу, удаляющую из текста все слова, содержащие "абв"

original_text = 'програабвмма удаления всеабвх лишабвних элементов абвгдейка посланец прогабвдла'

temp = 'абв'
list_text = original_text.split()
result = ''
print(list_text)
for word in list_text:
    if temp in word:
        continue
    else:
        result = result + ' ' + word
    
print(result)