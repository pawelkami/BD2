CREATE OR REPLACE FUNCTION  wypiszPracownikowPlacowki(x int) 
RETURNS TABLE
(
   imie character varying(20),
   nazwisko character varying(30),
   pesel character varying(11),
   idplacowka integer,
   login character varying(20),
   miasto character varying(30),
   ulica character varying(80),
   nrdomu integer,
   nrlokalu integer,
   telefon character varying(15)
) AS
$func$
BEGIN
		RETURN QUERY
		SELECT P.imie, P.nazwisko, P."PESEL", P."id_PLACOWKA", P."login",
		D."miasto", D."ulica", D."numer domu", D."numer lokalu", D."telefon"
		FROM "PRACOWNIK" AS P JOIN "DANE KONTAKTOWE" AS D ON D."id" = P."id_DANE KONTAKTOWE"
		WHERE P."id_PLACOWKA" = x;
END
$func$
LANGUAGE plpgsql;



CREATE OR REPLACE FUNCTION  sredniaIloscWypozyczen(mm int, fromYear int, toYear int) 
RETURNS int AS
$func$
declare
srednia int;
BEGIN
	SELECT COUNT(*) into srednia 
	FROM "WYPOZYCZENIE"
	WHERE mm = Extract(month from "data_wypozyczenia")
		AND fromYear <= Extract(year from "data_wypozyczenia")
		AND toYear >= Extract(year from "data_wypozyczenia");
	RETURN srednia;
END
$func$
LANGUAGE plpgsql;


create type czesc_type as (rodzaj character varying(32), info character varying(50), ilosc integer);

CREATE OR REPLACE FUNCTION  stanMagazynowy(placowka int) 
RETURNS SETOF czesc_type AS
$func$
declare
r czesc_type%rowtype;
BEGIN
	FOR r IN 	
		SELECT RCE."rodzaj", CE."info", CE."ilosc"
		FROM "PLACOWKA" AS P, "SERWIS MAGAZYN" AS SM, "SERWIS_MAGAZYN_CZESC_EKSPLOATACYJNA" AS SMCE,
		 "CZESC EKSPLOATACYJNA" AS CE,"RODZAJ CZESCI EKSPLOATACYJNEJ" AS RCE
		WHERE P."id" = placowka AND SM."id_PLACOWKA" = P."id" AND SM."id" = SMCE."id_SERWIS MAGAZYN" AND SMCE."id_CZESC EKSPLOATACYJNA" = CE."id"
		 AND CE."id_RODZAJ CZESCI EKSPLOATACYJNEJ" = RCE."id"
	LOOP
		RETURN NEXT r;
	END LOOP;
END
$func$
LANGUAGE plpgsql;

