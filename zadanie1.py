liczby = input()
liczby = liczby.split(',')
min = int(liczby[0])
max = int(liczby[0])
for i in liczby:
    i = int(i)
    if i < min:
        min = i
    if i > max:
        max = i
print('min = ' + str(min))
print('max = ' + str(max))