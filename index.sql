CREATE INDEX idxkolor
  ON public."SAMOCHOD"
  USING hash
  (kolor COLLATE pg_catalog."default");

CREATE INDEX idxmoc
  ON public."SAMOCHOD"
  USING hash
  (moc);

CREATE INDEX idxrocznik
  ON public."SAMOCHOD"
  USING hash
  (rocznik);

CREATE INDEX idxrodzaj
  ON public."SAMOCHOD"
  USING hash
  (rodzaj);

CREATE INDEX idxskrzynia
  ON public."SAMOCHOD"
  USING btree
  (automatyczna_skrzynia);

CREATE INDEX idxpojemnosc
  ON public."SAMOCHOD"
  USING btree
  (pojemnosc_silnika COLLATE pg_catalog."default");

CREATE INDEX idxmarka
  ON public."SAMOCHOD"
  USING hash
  (marka COLLATE pg_catalog."default");

CREATE INDEX idxmodel
  ON public."SAMOCHOD"
  USING hash
  (model COLLATE pg_catalog."default");

CREATE INDEX idxprzeglad
  ON public."SAMOCHOD"
  USING hash
  (data_przegladu);

CREATE INDEX idxcena
  ON public."SAMOCHOD"
  USING hash
  (cena_za_dzien);

CREATE INDEX idxczy_wypozyczony
  ON public."SAMOCHOD"
  USING hash
  (czy_wypozyczony);

CREATE INDEX idxwartosc
  ON public."SAMOCHOD"
  USING hash
  (wartosc);

-- Index: public."idxHaslo"

-- DROP INDEX public."idxHaslo";

CREATE INDEX "idxHaslo"
  ON public."PRACOWNIK SZEREGOWY"
  USING hash
  (nazwisko COLLATE pg_catalog."default");

-- Index: public."idxLogin"

-- DROP INDEX public."idxLogin";

CREATE INDEX "idxLogin"
  ON public."PRACOWNIK SZEREGOWY"
  USING hash
  (login COLLATE pg_catalog."default");


-- Index: public."PRACOWNIK_haslo_idx"

-- DROP INDEX public."PRACOWNIK_haslo_idx";

CREATE INDEX "PRACOWNIK_haslo_idx"
  ON public."PRACOWNIK"
  USING hash
  (haslo COLLATE pg_catalog."default");

-- Index: public."PRACOWNIK_login_haslo_idx"

-- DROP INDEX public."PRACOWNIK_login_haslo_idx";

CREATE INDEX "PRACOWNIK_login_haslo_idx"
  ON public."PRACOWNIK"
  USING btree
  (login COLLATE pg_catalog."default", haslo COLLATE pg_catalog."default");

-- Index: public."PRACOWNIK_login_idx"

-- DROP INDEX public."PRACOWNIK_login_idx";

CREATE INDEX "PRACOWNIK_login_idx"
  ON public."PRACOWNIK"
  USING hash
  (login COLLATE pg_catalog."default");



-- DROP INDEX public."idxHasloKier";

CREATE INDEX "idxHasloKier"
  ON public."KIEROWNIK"
  USING hash
  (haslo COLLATE pg_catalog."default");

-- Index: public."idxLoginKier"

-- DROP INDEX public."idxLoginKier";

CREATE INDEX "idxLoginKier"
  ON public."KIEROWNIK"
  USING hash
  (login COLLATE pg_catalog."default");


-- Index: public."idxHasloDyr"

-- DROP INDEX public."idxHasloDyr";

CREATE INDEX "idxHasloDyr"
  ON public."DYREKTOR"
  USING hash
  (haslo COLLATE pg_catalog."default");

-- Index: public."idxLoginDyr"

-- DROP INDEX public."idxLoginDyr";

CREATE INDEX "idxLoginDyr"
  ON public."DYREKTOR"
  USING hash
  (login COLLATE pg_catalog."default");


-- Index: public."idxTelefon"

-- DROP INDEX public."idxTelefon";

CREATE INDEX "idxTelefon"
  ON public."DANE KONTAKTOWE"
  USING hash
  (telefon COLLATE pg_catalog."default");
