tryb = int(input('1 - komputer\n2 - pvp\n'))
tury = int(input('podaj ilosc tur\n'))
if(tryb == 1):
    gracz1 = input('podaj imie\n')
    gracz2 = 'komputer'
    for i in range(tury):
        input(gracz1 + '\n')
