import random
from getpass import getpass

tryb = int(input('1 - komputer\n2 - pvp\n'))
tury = int(input('podaj ilosc tur\n'))
ruchy = "papier", "kamien", "nozyce"
w1 = 0
w2 = 0
his1 = []
his2 = []
if tryb == 1:
    gracz1 = input('podaj imie\n')
    gracz2 = 'komputer'
    for i in range(tury):
        g1 = int(input("1 - papier\n2 - kamien\n3 - nozyce\n"))
        g2 = random.randrange(0, len(ruchy))
        his1.append(ruchy[g1-1])
        his2.append(ruchy[g2-1])
        print(gracz1 + ": " + ruchy[g1 - 1])
        print("komputer: " + ruchy[g2 - 1])
        if g1 == g2:
            print("remis")
        elif (g1 == 1 and g2 == 2) or (g1 == 2 and g2 == 3) or (g1 == 3 and g2 == 1):
            print(gracz1 + " wygrywa")
            w1 += 1
        else:
            print(gracz2 + " wygrywa")
            w2 += 1

elif tryb == 2:
    gracz1 = input('podaj imie\n')
    gracz2 = input('podaj imie\n')
    for i in range(tury):
        g1 = int(getpass(gracz1 + ":\n1 - papier\n2 - kamien\n3 - nozyce\n"))
        g2 = int(getpass(gracz2 + ":\n1 - papier\n2 - kamien\n3 - nozyce\n"))
        his1.append(ruchy[g1 - 1])
        his2.append(ruchy[g2 - 1])
        print(gracz1 + ": " + ruchy[g1 - 1])
        print(gracz2 + ": " + ruchy[g2 - 1])
        if g1 == g2:
            print("remis")
        elif (g1 == 1 and g2 == 2) or (g1 == 2 and g2 == 3) or (g1 == 3 and g2 == 1):
            print(gracz1 + " wygrywa")
            w1 += 1
        else:
            print(gracz2 + " wygrywa")
            w2 += 1
else:
    print("?????????")
print(gracz1 + ": " + str(w1))
print(his1)
print(gracz2 + ": " + str(w2))
print(his2)
if w1 > w2:
    print(gracz1 + " wygrywa gre")
elif w2 > w1:
    print(gracz2 + " wygrywa gre")
else:
    print("gra zakonczona remisem")
