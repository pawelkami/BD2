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