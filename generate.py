#!/usr/bin/python
#-*- coding: utf-8 -*-

import random
import string
import psycopg2

cities = []
streets = []
logins = []
firstnames = []
lastnames = []
cars = []
boolean_array = ["TRUE", "FALSE"]
rodzaj_dzialu = ["SERWIS", "SERWIS MAGAZYN", "WYPOZYCZALNIA"]
rodzaj_samochodu = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K']
historia_naprawy = ["wymiana lozysk", "wymiana akumulatora", "wymiana silnika", "wymiana paska rozrzadu", "wymiana alternatora", "lakierowanie",
                    "wymiana reflektorow", "wymiana klockow hamulcowych", "wymiana tarcz hamulcowych"]
czesc_samochodowa = {'AMORTYZATOR':["gazowy", "olejowy"], 'SILNIK':["diesel", "benzyna", "LPG", "hybrydowy", "elektryczny"],
                     'SKRZYNIA BIEGOW':["automatyczna", "manualna"], 'REFLEKTOR': ["przedni", "tylny"], "OPONA": ["zimowa", "letnia"]}

czesc_eksploatacyjna = {"OLEJ SILNIKOWY": ["hydrauliczny", "mineralny", "syntetyczny", "polsyntetyczny"], "PLYN HAMULCOWY": ["K2", "Bosch"],
                        "FILTR POWIETRZA":['Bosch', 'Filtron', 'Fiaam'], "FILTR PALIWA" : ['Bosch', 'Filtron', 'Fiaam'],
                        "FILTR OLEJU": ['Bosch', 'Filtron', 'Fiaam']}

kolor = ["czerwony", "niebieski", "zielony", "fioletowy", "czarny", "bialy", "bordowy", "zolty", "rozowy", "blekitny"]
model = ["One", "Two", "Three"]

with open('cities.txt', 'r') as f:
    cities = f.read().splitlines()

with open('streets.txt', 'r') as f:
    streets = f.read().splitlines()

with open('firstnames.txt', 'r') as f:
    firstnames = f.read().splitlines()

with open('lastnames.txt', 'r') as f:
    lastnames = f.read().splitlines()

with open('VehicleManufacturers.txt', 'r') as f:
    cars = f.read().splitlines()

def save_data(filename, string):
    with open(filename, 'w') as f:
        f.write(string)

DANE_KONTAKTOWE_count = 0
KLIENT_INDYWIDUALNY_count = 0
PLACOWKA_count = 0
WYPOZYCZALNIA_count = 0
SERWIS_count = 0
SERWIS_MAGAZYN_count = 0
ZGLOSZENIE_count = 0
KIEROWNIK_count = 0
PRACOWNIK_SZEREGOWY_count = 0
KLIENT_INSTYTUCJONALNY_count = 0
ZGLOSZENIE_ZEWNETRZNE_count = 0
BADANIE_OKRESOWE_count = 0
NAPRAWA_count = 0
PRZYGOTOWANIE_DO_SEZONU_count = 0
ZAMOWIENIE_WEWNETRZNE_count = 0
ZAMOWIENIE_ZEWNETRZNE_count = 0
SAMOCHOD_count = 0
REZERWACJA_count = 0
SKIEROWANIE_NA_BADANIE_count = 0
WYPOZYCZENIE_count = 0
ZEWNETRZNY_DOWSTAWCA_count = 0
CZESC_SAMOCHODOWA_count = 0

def addZeroChar(var):
    if var < 10:
        ret = '0' + str(var)
    else:
        ret = str(var)

    return ret


def generatePESEL():
    yy = str(random.randint(30,99))
    miesiac = random.randint(1,12)

    mm = addZeroChar(miesiac)

    dzien = random.randint(1,28)
    dd = addZeroChar(dzien)

    rest = str(random.randint(10000, 99999))

    return yy + mm + dd + rest

def generateTimestamp():
    yyyy = str(random.randint(2000, 2016))
    month = random.randint(1,12)
    mm = addZeroChar(month)

    day = random.randint(1,28)
    dd = addZeroChar(day)

    hour = random.randint(0,23)
    hh = addZeroChar(hour)

    minutes = random.randint(0,59)
    m = addZeroChar(minutes)

    seconds = random.randint(0,59)
    ss = addZeroChar(seconds)

    timestamp = "%s-%s-%s %s:%s:%s" % (yyyy, mm, dd, hh, m, ss)

    return timestamp

# timestamp, do którego można dodać określoną liczbę dni/miesięcy/lat
def addToTimestamp(timestamp, days, months=0, years=0):
    newTimestamp = str(timestamp)

    year = int(timestamp[:4])
    month = int(timestamp[5:7])
    day = int(timestamp[8:10])
    time = timestamp[11:]

    year += years
    month += months

    day += days
    while day > 28:
        day -= 28
        month += 1

    while month > 12:
        month -= 12
        year += 1

    return "%s-%s-%s %s" % (str(year), addZeroChar(month), addZeroChar(day), time)


def generateDANE_KONTAKTOWE(data, count):
  for i in xrange(1, count+1):
      ulica = streets[random.randint(0, len(streets)-1)]
      miasto = cities[random.randint(0, len(cities)-1)]
      numer_domu = str(random.randint(0, 1000))
      numer_lokalu = str(random.randint(0, 200))
      telefon = str( random.randint(100000000, 999999999) )
      query = "INSERT INTO \"public\".\"DANE KONTAKTOWE\" (\"ulica\", \"numer domu\", \"numer lokalu\", \"telefon\", \"miasto\") " \
              "VALUES('%s', %s, %s, '%s', '%s' );\n" \
              % (ulica, numer_domu, numer_lokalu, telefon, miasto)
      data += query

  global DANE_KONTAKTOWE_count
  DANE_KONTAKTOWE_count = count
  return data


def generateKLIENT_INDYWIDUALNY(data, count):
    for i in xrange(1, count+1):
        haslo = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for j in range(10))
        firstname = firstnames[random.randint(0, len(firstnames)-1)]
        lastname = lastnames[random.randint(0, len(lastnames)-1)]
        login = firstname + str(random.randint(1, 99999))
        query = "INSERT INTO \"public\".\"KLIENT INDYWIDUALNY\" (\"login\", \"haslo\", \"id_DANE KONTAKTOWE\", \"imie\", \"nazwisko\") " \
                "VALUES('%s', '%s', %s, '%s', '%s' );\n" \
                % (login, haslo, str(i), firstname, lastname)
        data += query

    global KLIENT_INDYWIDUALNY_count
    KLIENT_INDYWIDUALNY_count = count
    return data


def generatePLACOWKA(data, count):
    for i in xrange(1, count+1):
        query = "INSERT INTO \"public\".\"PLACOWKA\"(\"id_DANE KONTAKTOWE\") " \
                "VALUES (%s);\n" \
                % (str(i))
        data += query

        data += generateDYREKTOR(i)

        query = "INSERT INTO \"public\".\"WYPOZYCZALNIA\"(\"id_PLACOWKA\") " \
                "VALUES (%s);\n" \
                % (str(i))

        data += query

        query = "INSERT INTO \"public\".\"SERWIS\"(\"id_PLACOWKA\") " \
                "VALUES (%s);\n" \
                % (str(i))

        data += query

        query = "INSERT INTO \"public\".\"SERWIS MAGAZYN\"(\"id_PLACOWKA\") " \
                "VALUES (%s);\n" \
                % (str(i))

        data += query

    global PLACOWKA_count, WYPOZYCZALNIA_count, SERWIS_count, SERWIS_MAGAZYN_count
    PLACOWKA_count = count
    WYPOZYCZALNIA_count = count
    SERWIS_count = count
    SERWIS_MAGAZYN_count = count
    return data

def generateDYREKTOR(id):
    firstname = firstnames[random.randint(0, len(firstnames)-1)]
    lastname = lastnames[random.randint(0, len(lastnames)-1)]
    pesel = generatePESEL()
    dane_kontaktowe = str(random.randint(1, DANE_KONTAKTOWE_count))
    login = firstname + str(random.randint(1, 99999))
    haslo = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for j in range(10))
    data_zmiany_hasla = generateTimestamp()
    query = "INSERT INTO \"public\".\"DYREKTOR\"(imie, nazwisko, \"PESEL\", \"id_DANE KONTAKTOWE\", \"id_PLACOWKA\", login, haslo, data_zmiany_hasla) " \
            "VALUES ('%s', '%s', '%s', %s, %s, '%s', '%s', '%s');\n" \
            % (firstname, lastname, pesel, dane_kontaktowe, str(id), login, haslo, data_zmiany_hasla)

    return query


def generateZGLOSZENIE(data, count):
    for i in xrange(1, count+1):
        query = "INSERT INTO \"public\".\"ZGLOSZENIE\"(\"id_SERWIS\", priorytet) " \
                "VALUES (%s, %s);\n" \
                % (str(random.randint(1, SERWIS_count)), str(random.randint(0,2)))

        data += query

        if i % 4 == 0: # BADANIE OKRESOWE
            global BADANIE_OKRESOWE_count
            BADANIE_OKRESOWE_count += 1

            query = "INSERT INTO \"public\".\"BADANIE OKRESOWE\"(\"id_ZGLOSZENIE\", myjnia, jazda_probna) " \
                    "VALUES (%s, %s, %s); \n" \
                    % (str(i), boolean_array[random.randint(0,1)], boolean_array[random.randint(0,1)])

        elif i % 4 == 1: # NAPRAWA
            global NAPRAWA_count
            NAPRAWA_count += 1

            query = "INSERT INTO \"public\".\"NAPRAWA\"(\"id_ZGLOSZENIE\", myjnia, jazda_probna) " \
                    "VALUES (%s, %s, %s);\n" \
                    % (str(i), boolean_array[random.randint(0,1)], boolean_array[random.randint(0,1)])


        elif i % 4 == 2: # PRZYGOTOWANIE DO SEZONU
            global PRZYGOTOWANIE_DO_SEZONU_count
            PRZYGOTOWANIE_DO_SEZONU_count += 1

            query = "INSERT INTO \"public\".\"PRZYGOTOWANIE DO SEZONU\"(\"id_ZGLOSZENIE\") " \
                    "VALUES (%s);\n" \
                    % (str(i))

        elif i % 4 == 3:
            global ZAMOWIENIE_WEWNETRZNE_count
            ZAMOWIENIE_WEWNETRZNE_count += 1
            query = "INSERT INTO \"public\".\"ZAMOWIENIE WEWNETRZNE\"(\"id_ZGLOSZENIE\", \"id_SERWIS MAGAZYN\", \"id_PRACOWNIK SZEREGOWY\")" \
                    "VALUES (%s, %s, %s);\n" \
                    % (str(i), str(random.randint(1, SERWIS_MAGAZYN_count)),
                       str(random.randint(1, PRACOWNIK_SZEREGOWY_count)))

        data += query

        if i % 4 != 3:
            query = "INSERT INTO \"public\".\"RAPORT\"(\"id_ZGLOSZENIE\", \"id_PRACOWNIK SZEREGOWY\", data) " \
                    "VALUES (%s, %s, '%s');\n" \
                    % (str(i), str(random.randint(1, PRACOWNIK_SZEREGOWY_count)), generateTimestamp())
            data += query

    global ZGLOSZENIE_count
    ZGLOSZENIE_count = count
    return data

def generateKIEROWNIK(data, count):
    for i in xrange(1, count+1):
        firstname = firstnames[random.randint(0, len(firstnames)-1)]
        lastname = lastnames[random.randint(0, len(lastnames)-1)]
        pesel = generatePESEL()
        dane_kontaktowe = str(random.randint(1, DANE_KONTAKTOWE_count))
        login = firstname + str(random.randint(1, 99999))
        haslo = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for j in range(10))
        data_zmiany_hasla = generateTimestamp()
        placowka = str(random.randint(1,PLACOWKA_count))
        dzial = rodzaj_dzialu[random.randint(0, len(rodzaj_dzialu) - 1)]
        query = "INSERT INTO \"public\".\"KIEROWNIK\"(imie, nazwisko, \"PESEL\", \"id_DANE KONTAKTOWE\", " \
                "\"id_PLACOWKA\", login, haslo, data_zmiany_hasla, \"id_DYREKTOR\", dzial) " \
                "VALUES ('%s', '%s', '%s', %s, %s, '%s', '%s', '%s', %s, '%s');\n" \
                % (firstname, lastname, pesel, dane_kontaktowe,
                   placowka, login, haslo, data_zmiany_hasla, placowka, dzial )
        data += query

        #generowanie pracownikow podleglych kierownikowi
        for j in xrange(1, random.randint(1, 10)):
            global PRACOWNIK_SZEREGOWY_count
            PRACOWNIK_SZEREGOWY_count = PRACOWNIK_SZEREGOWY_count + 1
            firstname = firstnames[random.randint(0, len(firstnames)-1)]
            lastname = lastnames[random.randint(0, len(lastnames)-1)]
            pesel = generatePESEL()
            dane_kontaktowe = str(random.randint(1, DANE_KONTAKTOWE_count))
            login = firstname + str(random.randint(1, 99999))
            haslo = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for j in range(10))
            data_zmiany_hasla = generateTimestamp()
            pracownik_query = "INSERT INTO \"public\".\"PRACOWNIK SZEREGOWY\"(imie, nazwisko, \"PESEL\", " \
                              "\"id_DANE KONTAKTOWE\", \"id_PLACOWKA\", login, haslo, data_zmiany_hasla, dzial, \"id_KIEROWNIK\")" \
                              " VALUES ('%s', '%s', '%s', %s, %s, '%s', '%s', '%s', '%s', %s);\n" \
                              % (firstname, lastname,
                                 pesel, dane_kontaktowe, placowka, login, haslo, data_zmiany_hasla, dzial, str(i) )
            data += pracownik_query

    global KIEROWNIK_count
    KIEROWNIK_count = count
    return data

def generateKLIENT_INSTYTUCJONALNY(data, count):
    for i in xrange(1, count+1):
        firstname = firstnames[random.randint(0, len(firstnames)-1)]
        lastname = lastnames[random.randint(0, len(lastnames)-1)]
        dane_kontaktowe = str(random.randint(1, DANE_KONTAKTOWE_count))
        login = firstname + str(random.randint(1, 99999))
        haslo = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for j in range(10))
        data_zmiany_hasla = generateTimestamp()
        regon = random.randint(10000000000000, 99999999999999)
        nip = random.randint(1000000000, 9999999999)
        pracownik_szeregowy = random.randint(1, PRACOWNIK_SZEREGOWY_count)
        query = "INSERT INTO \"public\".\"KLIENT INSTYTUCJONALNY\"(login, haslo, \"id_DANE KONTAKTOWE\", " \
                "\"NIP\", \"REGON\", \"id_PRACOWNIK SZEREGOWY\")" \
                "VALUES ('%s', '%s', %s, '%s', '%s', %s);\n" \
                % (login, haslo, dane_kontaktowe, str(nip), str(regon), str(pracownik_szeregowy) )
        data += query

    global KLIENT_INSTYTUCJONALNY_count
    KLIENT_INSTYTUCJONALNY_count = count
    return data

def generateZGLOSZENIE_ZEWNETRZNE(data):
    for i in xrange(1, (ZGLOSZENIE_count+1)/2):
        klient_instytucjonalny = ""
        klient_indywidualny = ""
        if i % 2:
            klient_instytucjonalny = str(random.randint(1, KLIENT_INSTYTUCJONALNY_count))
            klient_indywidualny = "NULL"
        else:
            klient_indywidualny = str(random.randint(1, KLIENT_INDYWIDUALNY_count))
            klient_instytucjonalny = "NULL"

        query = "INSERT INTO \"public\".\"ZGLOSZENIE ZEWNETRZNE\"(\"id_ZGLOSZENIE\", \"id_KLIENT INSTYTUCJONALNY\"," \
                "\"id_KLIENT INDYWIDUALNY\") " \
                "VALUES (%s, %s, %s);\n" \
                % (str(i), klient_instytucjonalny, klient_indywidualny)

        data += query
    global ZGLOSZENIE_ZEWNETRZNE_count
    ZGLOSZENIE_ZEWNETRZNE_count = ZGLOSZENIE_count / 2

    return data

def generateZEWNETRZNY_DOSTAWCA(data):
    for i in xrange(0, len(cars)-1):
        query = "INSERT INTO \"public\".\"ZEWNETRZNY DOSTAWCA\"(nazwa) " \
                "VALUES ('%s');\n" \
                % (cars[i])

        data += query
    global ZEWNETRZNY_DOWSTAWCA_count
    ZEWNETRZNY_DOWSTAWCA_count = len(cars)-1
    return data


def generateZAMOWIENIE_ZEWNETRZNE(data, count):
    for i in xrange(1, count + 1):
        query = "INSERT INTO \"public\".\"ZAMOWIENIE ZEWNETRZNE\"(\"id_SERWIS MAGAZYN\") " \
                "VALUES (%s);\n" \
                % (str(random.randint(1, SERWIS_MAGAZYN_count)))

        data += query

        zamowienie_czesc = "INSERT INTO \"ZAMOWIENIE_ZEWNETRZNE_ZEWNETRZNY_DOSTAWCA\"" \
                           "(\"id_ZAMOWIENIE ZEWNETRZNE\", \"id_ZEWNETRZNY DOSTAWCA\") " \
                           "VALUES (%s, %s);\n" \
                           % (str(i), random.randint(1, ZEWNETRZNY_DOWSTAWCA_count))
        data += zamowienie_czesc

    global ZAMOWIENIE_ZEWNETRZNE_count
    ZAMOWIENIE_ZEWNETRZNE_count = count
    return data

def generateCZESCI_SAMOCHODOWE(data, count):
    i = 1
    for key in czesc_samochodowa:
        query = "INSERT INTO \"public\".\"RODZAJ CZESCI SAMOCHODOWEJ\"(rodzaj) " \
                "VALUES ('%s');\n" \
                % (key)

        data += query

        for j in xrange(1, count):
            list = czesc_samochodowa[key]
            description = list[random.randint(0, len(list)-1)]
            czesc_query = "INSERT INTO \"public\".\"CZESC SAMOCHODOWA\"(\"id_RODZAJ CZESCI SAMOCHODOWEJ\", info, " \
                          "ilosc, \"id_ZAMOWIENIE WEWNETRZNE\") " \
                          "VALUES (%s, '%s', %s, %s);\n" \
                          % (str(i), description, str(random.randint(1,999)), str(random.randint(1, ZAMOWIENIE_WEWNETRZNE_count)))
            data += czesc_query

            serwismagazyn_czesc = "INSERT INTO \"SERWIS_MAGAZYN_CZESC_SAMOCHODOWA\"" \
                                  "(\"id_SERWIS MAGAZYN\", \"id_CZESC SAMOCHODOWA\") " \
                                  "VALUES (%s, %s);\n" \
                                  % (random.randint(1, SERWIS_MAGAZYN_count), str(j))

            data += serwismagazyn_czesc
            if random.randint(0,1):
                zamowienie_zewnetrzne_czesc = "INSERT INTO \"ZAMOWIENIE_ZEWNETRZNE_CZESC_SAMOCHODOWA\"" \
                                              "(\"id_ZAMOWIENIE ZEWNETRZNE\", \"id_CZESC SAMOCHODOWA\", ilosc) " \
                                              "VALUES (%s, %s, %s)\n;" \
                                              % (random.randint(1,ZAMOWIENIE_ZEWNETRZNE_count), str(j), random.randint(1,10))
                data += zamowienie_zewnetrzne_czesc

        i += 1
    global CZESC_SAMOCHODOWA_count
    CZESC_SAMOCHODOWA_count = count
    return data


def generateCZESCI_EKSPLOATACYJNE(data, count):
    i = 1
    for key in czesc_eksploatacyjna:
        query = "INSERT INTO \"public\".\"RODZAJ CZESCI EKSPLOATACYJNEJ\"(rodzaj) " \
                "VALUES ('%s');\n" \
                % (key)

        data += query

        for j in xrange(1, count):
            list = czesc_eksploatacyjna[key]
            description = list[random.randint(0, len(list)-1)]
            czesc_query = "INSERT INTO \"public\".\"CZESC EKSPLOATACYJNA\"(\"id_RODZAJ CZESCI EKSPLOATACYJNEJ\", info, " \
                          "ilosc, \"id_ZAMOWIENIE WEWNETRZNE\") " \
                          "VALUES (%s, '%s', %s, %s);\n" \
                          % (str(i), description, str(random.randint(1,999)), str(random.randint(1, ZAMOWIENIE_WEWNETRZNE_count)))
            data += czesc_query

            serwismagazyn_czesc = "INSERT INTO \"SERWIS_MAGAZYN_CZESC_EKSPLOATACYJNA\"" \
                                  "(\"id_SERWIS MAGAZYN\", \"id_CZESC EKSPLOATACYJNA\") " \
                                  "VALUES (%s, %s);\n" \
                                  % (random.randint(1, SERWIS_MAGAZYN_count), str(j))
            data += serwismagazyn_czesc

            if random.randint(0,1):
                zamowienie_zewnetrzne_czesc = "INSERT INTO \"ZAMOWIENIE_ZEWNETRZNE_CZESC_EKSPLOATACYJNA\"" \
                                              "(\"id_ZAMOWIENIE ZEWNETRZNE\", \"id_CZESC EKSPLOATACYJNA\", ilosc) " \
                                              "VALUES (%s, %s, %s)\n;" \
                                              % (random.randint(1,ZAMOWIENIE_ZEWNETRZNE_count), str(j), random.randint(1,20))
                data += zamowienie_zewnetrzne_czesc
        i += 1
    return data

def generateSAMOCHOD(data, count):
    for i in xrange(1, count+1):
        rodzaj = rodzaj_samochodu[random.randint(0, len(rodzaj_samochodu)-1)]
        moc = random.randint(70, 350)
        color = kolor[random.randint(0, len(kolor)-1)]
        rocznik = str(random.randint(2012, 2016))
        automat = boolean_array[random.randint(0,len(boolean_array)-1)]
        pojemnosc = str(round(random.uniform(1.0, 5.0), 3))
        marka = cars[random.randint(0, len(cars)-1)]
        model_samochodu = model[random.randint(0, len(model)-1)]
        wypozyczalnia = str(random.randint(1, WYPOZYCZALNIA_count))
        cena = str(random.randint(50, 3000))
        wartosc = str(random.randint(5000, 250000))
        czy_wypozyczony = boolean_array[random.randint(0,len(boolean_array)-1)]
        query = "INSERT INTO \"public\".\"SAMOCHOD\"(rodzaj, moc, kolor, rocznik, automatyczna_skrzynia, pojemnosc_silnika, " \
                "marka, model, data_przegladu, \"id_WYPOZYCZALNIA\", cena_za_dzien, czy_wypozyczony, wartosc) " \
                "VALUES ('%s', %s, '%s', %s, %s, %s, '%s', '%s', '%s', %s, %s, %s, %s);\n" \
                % (rodzaj, moc, color, rocznik, automat, pojemnosc, marka, model_samochodu, generateTimestamp(),
                   wypozyczalnia, cena, czy_wypozyczony, wartosc)

        data += query

    global SAMOCHOD_count
    SAMOCHOD_count = count
    return data

def generateREZERWACJA(data, count):
    for i in xrange(1, count+1):
        czy_internetowo = boolean_array[random.randint(0,len(boolean_array)-1)]
        czy_potwierdzono = boolean_array[random.randint(0,len(boolean_array)-1)]
        wypozyczalnia = str(random.randint(1, WYPOZYCZALNIA_count))
        samochod = str(i)
        rabat = str(random.randint(0,20))
        klient_indywidualny = "NULL"
        klient_instytucjonalny = "NULL"

        if i % 2:
            klient_indywidualny = str(i)
        else:
            klient_instytucjonalny = str(random.randint(1, KLIENT_INSTYTUCJONALNY_count))

        query = "INSERT INTO \"public\".\"REZERWACJA\"(id, czy_internetowo, data_wynajmu, \"id_WYPOZYCZALNIA\", " \
                "rodzaj_samochodu, rabat, \"id_KLIENT INDYWIDUALNY\", \"id_KLIENT INSTYTUCJONALNY\", " \
                "\"id_SAMOCHOD\", czy_potwierdzono)" \
                "SELECT %s, %s, '%s', \"SAMOCHOD\".\"id_WYPOZYCZALNIA\" id, \"SAMOCHOD\".rodzaj, %s, %s, %s, \"SAMOCHOD\".id, %s FROM \"SAMOCHOD\" " \
                "WHERE \"SAMOCHOD\".id=%s;\n" \
                % (str(i), czy_internetowo, generateTimestamp(), rabat, klient_indywidualny, klient_instytucjonalny,
                   czy_potwierdzono, samochod)

        data += query

    global REZERWACJA_count
    REZERWACJA_count = count
    return data

def generateHISTORIA_NAPRAWY(data):
    for i in xrange(1, NAPRAWA_count+1):
        opis = historia_naprawy[random.randint(0, len(historia_naprawy)-1)]
        query = "INSERT INTO \"public\".\"HISTORIA NAPRAWY\"(\"id_SAMOCHOD\", opis, data, \"id_NAPRAWA\") " \
                "VALUES (%s, '%s', '%s', %s);\n" \
                % (random.randint(1, SAMOCHOD_count), opis, generateTimestamp(), str(i))

        data += query
    return data

def generateSKIEROWANIE_NA_BADANIE(data, count):
    for i in xrange(1, count+1):
        pracownik = str(random.randint(1, PRACOWNIK_SZEREGOWY_count))
        samochod = str(random.randint(1, SAMOCHOD_count))
        czy_zaakceptowano = boolean_array[random.randint(0,1)]
        query = "INSERT INTO \"public\".\"SKIEROWANIE NA BADANIE\"(czy_zaakceptowano, \"id_KIEROWNIK\", " \
                "\"id_PRACOWNIK SZEREGOWY\", \"id_SERWIS\", \"id_SAMOCHOD\")" \
                "SELECT %s, \"PRACOWNIK SZEREGOWY\".\"id_KIEROWNIK\", id, \"PRACOWNIK SZEREGOWY\".\"id_PLACOWKA\", %s " \
                "FROM \"PRACOWNIK SZEREGOWY\" WHERE id=%s;\n"\
                % (czy_zaakceptowano, samochod, pracownik)

        data += query
    global SKIEROWANIE_NA_BADANIE_count
    SKIEROWANIE_NA_BADANIE_count = count
    return data

def generateWYPOZYCZENIE(data, count):
    for i in xrange(1, count+1):
        data_wypozyczenia = generateTimestamp()
        data_zwrotu = addToTimestamp(data_wypozyczenia, random.randint(1,28), random.randint(1, 3), 0)

        if i >= SAMOCHOD_count:
            count = i
            break

        samochod = str(i)

        klient_instytucjonalny = "NULL"
        klient_indywidualny = "NULL"

        if random.randint(0,1):
            klient_indywidualny = str(i)
        else:
            klient_instytucjonalny = str(random.randint(1, KLIENT_INSTYTUCJONALNY_count))

        query = "INSERT INTO \"public\".\"WYPOZYCZENIE\"(data_wypozyczenia, data_zwrotu, \"id_SAMOCHOD\", " \
                "\"id_KLIENT INDYWIDUALNY\", \"id_KLIENT INSTYTUCJONALNY\")" \
                "VALUES ('%s', '%s', %s, %s, %s);\n" \
                % (data_wypozyczenia, data_zwrotu, samochod, klient_indywidualny, klient_instytucjonalny )

        data += query

    global WYPOZYCZENIE_count
    WYPOZYCZENIE_count = count
    return data

def generateUserAdmin(username, password, dbname):
    query = "DROP USER IF EXISTS %s; CREATE USER %s WITH PASSWORD '%s'; GRANT ALL PRIVILEGES ON DATABASE \"%s\" to %s;\n" % (username, username, password, dbname, username)
    return query

def generateUser(username, password):
    query = "DROP USER IF EXISTS %s; CREATE USER %s WITH PASSWORD '%s'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO %s;\n" \
            % (username, username, password, username)
    return query

def openFile(filename):
    with open(filename) as f:
        data = f.read()
        return data

if __name__ == "__main__":
    insertsFilename = "inserts.sql"

    databaseScript = openFile("database.sql")
    procedures = openFile("procedures.sql")
    views = openFile("views.sql")
    trigger = openFile("trigger.sql")
	
    print("Podaj dane do zalogowania się na serwerze. W nawiasach są proponowane wartości.")
    dbname = raw_input("Nazwa nowej bazy danych[wypozyczalniaDB]: ").lower()
    user = raw_input("Login[postgres]: ")
    host = raw_input("Adres[localhost]: ")
    port = raw_input("Port[5432 lub 5433]: ")
    password = raw_input("Hasło: ")

    dbname.lower()
    dropCommand = "DROP DATABASE IF EXISTS %s ;" % (dbname)
    createCommand = "CREATE DATABASE %s ;" % (dbname)
                    #"WITH OWNER = postgres ENCODING = \'UTF8\' TABLESPACE = pg_default " \
                    #"LC_COLLATE = \'pl_PL.utf8\' LC_CTYPE = \'pl_PL.utf8\' CONNECTION LIMIT = 0;\n" \


    userAdmin = generateUserAdmin("testerAdmin", "test", dbname)
    userGenerated = generateUser("tester", "test")
    dbUsers = userAdmin + userGenerated
    print("Creating database...")

    # logujemy się do głównej bazy, żeby stworzyć nową bazę
    try:
        conn = psycopg2.connect(dbname='postgres', user=user, host=host, password=password, port=port)
    except:
        print("Problem with connecting database. Shutting down program.")
        exit()

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(dropCommand)
    cur.execute(createCommand)
    cur.close()
    conn.close()

    # działamy na nowej bazie
    try:
        conn = psycopg2.connect(dbname=dbname, user=user, host=host, password=password, port=port)
    except:
        print("Problem with connecting to new database. Shutting down program.")
        exit()

    conn.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()

    print("Adding users...")
    cur.execute(dbUsers)
    print("Creating tables in database...")
    cur.execute(databaseScript)
    print("Adding views...")
    cur.execute(views)
    print("Adding triggers...")
    cur.execute(trigger)

    print("Adding procedures...")
    cur.execute(procedures)


    data = ""
    print("Generating inserts...")
    data = generateDANE_KONTAKTOWE(data, 10000)
    data = generateKLIENT_INDYWIDUALNY(data, 10000)
    data = generatePLACOWKA(data, 200)
    data = generateKIEROWNIK(data, 600)
    data = generateZGLOSZENIE(data, 20000)
    data = generateKLIENT_INSTYTUCJONALNY(data, 10000)
    data = generateZEWNETRZNY_DOSTAWCA(data)
    data = generateZGLOSZENIE_ZEWNETRZNE(data)
    data = generateZAMOWIENIE_ZEWNETRZNE(data, 5000)
    data = generateCZESCI_SAMOCHODOWE(data, 100)
    data = generateCZESCI_EKSPLOATACYJNE(data, 100)
    data = generateSAMOCHOD(data, 15000)
    data = generateREZERWACJA(data, 3000)
    data = generateHISTORIA_NAPRAWY(data)
    data = generateSKIEROWANIE_NA_BADANIE(data, 1000)
    data = generateWYPOZYCZENIE(data, 10000)
    data = data.decode('latin-1').encode("utf-8")
    save_data(insertsFilename, data)


    print("Inserting...")
    cur.execute(data)
    cur.close()
    conn.close()
