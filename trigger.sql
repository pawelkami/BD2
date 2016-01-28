CREATE OR REPLACE FUNCTION set_czas_wypozyczenia() 
RETURNS TRIGGER 
AS $$
BEGIN
  NEW.czas_wypozyczenia := NEW.data_zwrotu - NEW.data_wypozyczenia;
  RETURN NEW;
END $$ LANGUAGE plpgsql;


CREATE TRIGGER set_czas_wypozyczenia_wypozyczenie
BEFORE INSERT OR UPDATE ON "WYPOZYCZENIE"
FOR EACH ROW 
  EXECUTE PROCEDURE set_czas_wypozyczenia();
 

CREATE OR REPLACE FUNCTION reset_czy_wypozyczenie_aktywne()
RETURNS TRIGGER
AS $$
BEGIN
  NEW.czy_wypozyczenie_aktywne := FALSE;
  RETURN NEW;
END $$ LANGUAGE plpgsql;


CREATE TRIGGER reset_czy_wypozyczenie_aktywne_klient_indywidualny
BEFORE INSERT ON "KLIENT INDYWIDUALNY"
FOR EACH ROW
  EXECUTE PROCEDURE reset_czy_wypozyczenie_aktywne();


CREATE OR REPLACE FUNCTION set_czy_wypozyczenie_aktywne()
RETURNS TRIGGER
AS $$
BEGIN
  UPDATE "KLIENT INDYWIDUALNY" SET czy_wypozyczenie_aktywne = TRUE
  WHERE "id" = NEW."id_KLIENT INDYWIDUALNY";
  RETURN NEW;
END $$ LANGUAGE plpgsql;


CREATE OR REPLACE FUNCTION set_czy_wypozyczenie_aktywne()
RETURNS TRIGGER
AS $$
DECLARE
myid boolean;
czas timestamp;
BEGIN
  SELECT "czy_wypozyczenie_aktywne" INTO myid FROM "KLIENT INDYWIDUALNY" WHERE id = NEW."id_KLIENT INDYWIDUALNY";
  IF myid = TRUE THEN
    SELECT "WYPOZYCZENIE"."data_zwrotu" INTO czas FROM "WYPOZYCZENIE" WHERE "WYPOZYCZENIE"."id_KLIENT INDYWIDUALNY" = NEW."id_KLINET INDYWIDUALNY";
	IF now() < czas THEN
      RAISE EXCEPTION 'Klient indywidualny jest juz w posiadaniu samochodu.';
	END IF;
  END IF;
  IF now() < NEW."data_zwrotu" THEN
    UPDATE "KLIENT INDYWIDUALNY" SET czy_wypozyczenie_aktywne = TRUE
	WHERE "id" = NEW."id_KLIENT INDYWIDUALNY";
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;


CREATE TRIGGER set_czy_wypozyczenie_aktywne_klient_indywidualny
BEFORE INSERT ON "WYPOZYCZENIE"
FOR EACH ROW
  EXECUTE PROCEDURE set_czy_wypozyczenie_aktywne();