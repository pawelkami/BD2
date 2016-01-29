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



-- Procedur� wypiszNieprzypisaneZamowieniaZew()  mo�na sprawdzi� potem kt�re zamowienia zewnetrzne trzeba przypisa� dostawcom zewn
CREATE TRIGGER set_czy_wypozyczenie_aktywne_klient_indywidualny
BEFORE INSERT ON "WYPOZYCZENIE"
FOR EACH ROW
  EXECUTE PROCEDURE set_czy_wypozyczenie_aktywne();

CREATE OR REPLACE FUNCTION add_ZAMOWIENIE_ZEWNETRZNE_CS()
RETURNS TRIGGER
AS $$
DECLARE
idserwis int;
idzamowienie int;
BEGIN
  IF NEW."ilosc" = 0 THEN
  SELECT S.id INTO idserwis FROM "SERWIS MAGAZYN" AS S LEFT JOIN "SERWIS_MAGAZYN_CZESC_SAMOCHODOWA" AS SMCS ON S."id" = SMCS."id_SERWIS MAGAZYN" LEFT JOIN "CZESC SAMOCHODOWA" AS CS ON SMCS."id_CZESC SAMOCHODOWA" = CS."id" WHERE CS."id" = NEW.id;
  INSERT INTO "ZAMOWIENIE ZEWNETRZNE"("id_SERWIS MAGAZYN") VALUES (idserwis);
  SELECT id INTO idzamowienie FROM "ZAMOWIENIE ZEWNETRZNE" ORDER BY id DESC LIMIT 1;
  INSERT INTO "ZAMOWIENIE_ZEWNETRZNE_CZESC_SAMOCHODOWA"("id_ZAMOWIENIE ZEWNETRZNE", "id_CZESC SAMOCHODOWA", ilosc) VALUES (idzamowienie, NEW.id, 10);
  NEW."ilosc" = 10;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;


CREATE TRIGGER brak_czesci_samochodowych
BEFORE UPDATE ON "CZESC SAMOCHODOWA"
FOR EACH ROW
  EXECUTE PROCEDURE add_ZAMOWIENIE_ZEWNETRZNE_CS();


CREATE OR REPLACE FUNCTION add_ZAMOWIENIE_ZEWNETRZNE_CE()
RETURNS TRIGGER
AS $$
DECLARE
idserwis int;
idzamowienie int;
BEGIN
  IF NEW."ilosc" = 0 THEN
  SELECT S.id INTO idserwis FROM "SERWIS MAGAZYN" AS S LEFT JOIN "SERWIS_MAGAZYN_CZESC_EKSPLOATACYJNA" AS SMCE ON S."id" = SMCE."id_SERWIS MAGAZYN" LEFT JOIN "CZESC EKSPLOATACYJNA" AS CE ON SMCE."id_CZESC EKSPLOATACYJNA" = CE."id" WHERE CE."id" = NEW.id;
  INSERT INTO "ZAMOWIENIE ZEWNETRZNE"("id_SERWIS MAGAZYN") VALUES (idserwis);
  SELECT id INTO idzamowienie FROM "ZAMOWIENIE ZEWNETRZNE" ORDER BY id DESC LIMIT 1;
  INSERT INTO "ZAMOWIENIE_ZEWNETRZNE_CZESC_EKSPLOATACYJNA"("id_ZAMOWIENIE ZEWNETRZNE", "id_CZESC EKSPLOATACYJNA", ilosc) VALUES (idzamowienie, NEW.id, 10);
  NEW."ilosc" = 10;
  END IF;
  RETURN NEW;
END $$ LANGUAGE plpgsql;


CREATE TRIGGER brak_czesci_eksploatacyjnych
BEFORE UPDATE ON "CZESC EKSPLOATACYJNA"
FOR EACH ROW
  EXECUTE PROCEDURE add_ZAMOWIENIE_ZEWNETRZNE_CE();