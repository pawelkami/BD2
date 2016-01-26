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
SELECT S."wartosc", S."rodzaj", S."moc", S."kolor", S."rocznik", S."automatyczna_skrzynia", S."pojemnosc_silnika", S."marka", S."model",
	D."ulica", D."numer domu", D."numer lokalu", D."telefon"
FROM "SAMOCHOD" AS S, "WYPOZYCZALNIA", "PLACOWKA", "DANE KONTAKTOWE" AS D
WHERE S."id_WYPOZYCZALNIA" = "WYPOZYCZALNIA".id AND "WYPOZYCZALNIA"."id_PLACOWKA" = "PLACOWKA"."id"
	AND "PLACOWKA"."id_DANE KONTAKTOWE" = D.id
	AND S."rocznik" < Extract(year from CURRENT_DATE)-2;