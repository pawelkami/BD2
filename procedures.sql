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

