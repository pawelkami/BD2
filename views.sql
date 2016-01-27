--Informacje o wszystkich pracownikach wraz z ich danymi kontaktowymi
CREATE VIEW "pracownicy informacje" AS
SELECT P.imie, P.nazwisko, P."PESEL", P."id_PLACOWKA", P."login",
D."miasto", D."ulica", D."numer domu", D."numer lokalu", D."telefon"
FROM "PRACOWNIK" AS P JOIN "DANE KONTAKTOWE" AS D ON D."id" = P."id_DANE KONTAKTOWE"
WHERE P."id_PLACOWKA" = 1;

SELECT * FROM "pracownicy informacje";

DROP VIEW "pracownicy informacje";