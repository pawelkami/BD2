--Informacje o wszystkich pracownikach wraz z ich danymi kontaktowymi
SELECT P.imie, P.nazwisko, P."PESEL", P."id_PLACOWKA", P."login",
D."miasto", D."ulica", D."numer domu", D."numer lokalu", D."telefon"
FROM "PRACOWNIK" AS P JOIN "DANE KONTAKTOWE" AS D ON D."id" = P."id_DANE KONTAKTOWE"
WHERE P."id_PLACOWKA" = 1;

--Informacje o wszystkich pracownikach z konkretnej placowki
SELECT * FROM wypiszPracownikowPlacowki(5);

--Srednie ceny samochodow ze wszystkich kategorii
SELECT "rodzaj", AVG("wartosc")
FROM "SAMOCHOD"
GROUP BY "rodzaj"
ORDER BY "rodzaj";

--Wsyzstkie samochody, ktore mozna sprzedac
SELECT S."marka", S."model", S."wartosc", S."rodzaj", S."moc", S."kolor", S."rocznik", S."automatyczna_skrzynia", S."pojemnosc_silnika", 
	D."ulica", D."numer domu", D."numer lokalu", D."telefon"
FROM "SAMOCHOD" AS S LEFT JOIN "WYPOZYCZALNIA" ON S."id_WYPOZYCZALNIA" = "WYPOZYCZALNIA".id LEFT JOIN "PLACOWKA" ON "WYPOZYCZALNIA"."id_PLACOWKA" = "PLACOWKA"."id" 
	LEFT JOIN  "DANE KONTAKTOWE" AS D ON "PLACOWKA"."id_DANE KONTAKTOWE" = D.id
WHERE  S."rocznik" < Extract(year from CURRENT_DATE)-2;

--Wszystkie rezerwacje na najblizsze kilka dni
SELECT * FROM "REZERWACJA" 
LEFT JOIN "SAMOCHOD" ON "REZERWACJA"."id_SAMOCHOD" = "SAMOCHOD"."id" 
LEFT JOIN "KLIENT INDYWIDUALNY" ON "REZERWACJA"."id_KLIENT INDYWIDUALNY" = "KLIENT INDYWIDUALNY"."id"
LEFT JOIN "KLIENT INSTYTUCJONALNY" ON "REZERWACJA"."id_KLIENT INSTYTUCJONALNY" = "KLIENT INSTYTUCJONALNY"."id"
WHERE DATE_PART('day', "REZERWACJA"."data_wynajmu" - now()) >= 0 and DATE_PART('day', "REZERWACJA"."data_wynajmu" - now()) <= 20;

--Ilosc pracownikow w poszczegolnych miastach
SELECT "DANE KONTAKTOWE"."miasto", COUNT(*) AS "ilosc" FROM "PRACOWNIK" 
LEFT JOIN "PLACOWKA" ON "PLACOWKA"."id" = "PRACOWNIK"."id_PLACOWKA"
LEFT JOIN "DANE KONTAKTOWE" ON "PLACOWKA"."id" = "DANE KONTAKTOWE"."id"
GROUP BY "DANE KONTAKTOWE"."miasto";

-- do indexow
SELECT *
 FROM "SAMOCHOD"
 WHERE "rocznik" > 2012 AND "moc" < 300 AND "moc" > 200 AND "kolor" = 'rozowy';