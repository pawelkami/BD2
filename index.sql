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