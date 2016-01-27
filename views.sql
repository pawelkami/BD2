--Informacje o wszystkich pracownikach wraz z ich danymi kontaktowymi
CREATE VIEW "pracownicy informacje" AS
SELECT P.imie, P.nazwisko, P."PESEL", P."id_PLACOWKA", P."login",
D."miasto", D."ulica", D."numer domu", D."numer lokalu", D."telefon"
FROM "PRACOWNIK" AS P JOIN "DANE KONTAKTOWE" AS D ON D."id" = P."id_DANE KONTAKTOWE"
WHERE P."id_PLACOWKA" = 1;

--SELECT * FROM "pracownicy informacje";
--DROP VIEW "pracownicy informacje";

--Wszystkie czesci samochodowe i ekploatacyjne w placowkach

CREATE VIEW "CZESCI SAMOCHODOWE W PLACOWCE" AS
SELECT P."id", RCS."rodzaj", CS."info", CS."ilosc"
FROM "PLACOWKA" AS P LEFT JOIN "SERWIS MAGAZYN" AS SM ON P."id" = SM."id_PLACOWKA" LEFT JOIN "SERWIS_MAGAZYN_CZESC_SAMOCHODOWA" AS SMCS ON SM."id" = SMCS."id_SERWIS MAGAZYN" LEFT JOIN 
 "CZESC SAMOCHODOWA" AS CS ON SMCS."id_CZESC SAMOCHODOWA" = CS."id" LEFT JOIN "RODZAJ CZESCI SAMOCHODOWEJ" AS RCS ON CS."id_RODZAJ CZESCI SAMOCHODOWEJ" = RCS."id";

CREATE VIEW "CZESCI EKSPLOATACYJNE W PLACOWCE" AS
SELECT P."id", RCE."rodzaj", CE."info", CE."ilosc"
FROM "PLACOWKA" AS P LEFT JOIN "SERWIS MAGAZYN" AS SM ON P."id" = SM."id_PLACOWKA" LEFT JOIN "SERWIS_MAGAZYN_CZESC_EKSPLOATACYJNA" AS SMCE ON SM."id" = SMCE."id_SERWIS MAGAZYN" LEFT JOIN 
 "CZESC EKSPLOATACYJNA" AS CE ON SMCE."id_CZESC EKSPLOATACYJNA" = CE."id" LEFT JOIN "RODZAJ CZESCI EKSPLOATACYJNEJ" AS RCE ON CE."id_RODZAJ CZESCI EKSPLOATACYJNEJ" = RCE."id";

--Wszyscy pracownicy placowek
CREATE VIEW "PRACOWNICY PLACOWEK" AS
	SELECT P.imie, P.nazwisko, P."PESEL", P."id_PLACOWKA", P."login",
	D."miasto", D."ulica", D."numer domu", D."numer lokalu", D."telefon"
	FROM "PRACOWNIK" AS P JOIN "DANE KONTAKTOWE" AS D ON D."id" = P."id_DANE KONTAKTOWE";