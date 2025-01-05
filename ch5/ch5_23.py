import locale
print(locale.getpreferredencoding())

print('UTF-8')
fin2 = open('PoemUTF8.txt', encoding='utf-8')
line = fin2.readline()

while line:
    print(line, end='')
    line = fin2.readline()
