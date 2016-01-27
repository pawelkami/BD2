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
		SELECT * FROM "PRACOWNICY PLACOWEK"
		WHERE "PRACOWNICY PLACOWEK"."id_PLACOWKA" = x;
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


create type czesc_type as (id integer, rodzaj character varying(32), info character varying(50), ilosc integer);

CREATE OR REPLACE FUNCTION  stanMagazynowy(placowka int) 
RETURNS SETOF czesc_type AS
$func$
declare
r czesc_type%rowtype;
BEGIN
	FOR r IN 	
		SELECT *
		FROM "CZESCI SAMOCHODOWE W PLACOWCE" 
		WHERE "CZESCI SAMOCHODOWE W PLACOWCE"."id" = placowka
	LOOP
		RETURN NEXT r;
	END LOOP;
	FOR r IN 	
		SELECT *
		FROM "CZESCI EKSPLOATACYJNE W PLACOWCE" 
		WHERE "CZESCI EKSPLOATACYJNE W PLACOWCE"."id" = placowka
	LOOP
		RETURN NEXT r;
	END LOOP;

END
$func$
LANGUAGE plpgsql;