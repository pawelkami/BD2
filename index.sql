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