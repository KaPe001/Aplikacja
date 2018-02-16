import csv

def csvDoSlownik(nazwa, separator):
    slownik = {}
    sciezka = open('./csv/'+nazwa, 'r', encoding='UTF-8')
    for linia in sciezka:
        if len(linia) > 1:
            linia = linia.strip()
            wiersz = linia.split(separator)
            if wiersz[0] != '':
                slownik[int(wiersz[0])] = wiersz[1:len(wiersz)]
    return slownik

def prettyDictionary(data):
    data = print("\n".join("{}\t{}".format(k, v) for k, v in data.items()))
    return data


def znajdzBakterie(pozywka, cecha):
    kodyBakterii = []
    nazwaBakterii = []


    file = csv.reader(open('./csv/calosc.csv', 'r'))
    for data in file:
        if data[1] == str(pozywka) and data[2] == str(cecha):
            kodyBakterii.append(data[0])

    nazwy = csv.reader(open('./csv/gatunki.csv', 'r'))

    for data in nazwy:
        for bacteria in kodyBakterii:
            if data[0] == bacteria:
                nazwaBakterii.append(data[1])

    return nazwaBakterii





pozywki = csvDoSlownik('pozywki.csv', ',')
cechy = csvDoSlownik('cechy.csv', ',')

prettyDictionary(pozywki)

wyborPozywki = 0
while (wyborPozywki < 1) or (wyborPozywki > len(pozywki)):
    wyborPozywki = int(input('Podaj numer pozywki: '))


prettyDictionary(cechy)

wyborCechy = 0
while (wyborCechy < 1) or (wyborCechy > len(cechy)):
    wyborCechy = int(input('Podaj nummer cechy: '))


print('Wybrałeś:')
print(' - Pożywkę: ')
print(pozywki[wyborPozywki])

print(' - Cechę: ')
print(cechy[wyborCechy])

print('Twoja bakteria to: ' +
      str(znajdzBakterie(wyborPozywki,wyborCechy))
)