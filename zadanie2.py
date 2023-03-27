import random
miasta = ['Warszawa', 'Krakow', 'Wroclaw', 'Szczecin', 'Gdansk', 'Gdynia', 'Koszalin', 'Lodz', 'Siedlce', 'Poznan', 'Bydgoszcz']
wycieczka = []
for i in range(10):
    tmp = random.randrange(0,len(miasta))
    wycieczka.append(miasta[tmp])
    miasta.remove(miasta[tmp])
print(wycieczka)