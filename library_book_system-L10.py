class Kniha:
    def __init__(self,nazov,autor,isbn,dostupna,rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.dostupna = dostupna
        self.rok_vydania = rok_vydania

    def vypozicat(self):
        if self.dostupna:
            self.dostupna = False
        else:
            print("Nie je mozne vypozicat, kniha uz je uz pozicana!")

    def vratit(self):
        if self.dostupna:
            print("Nie je mozne vratit, kniha je uz dostupna.")
        else:
            self.dostupna = True

class Kniznica:
    zoznam_knih = []

    def pridat_knihu(self,kniha):
        self.zoznam_knih.append(kniha)
