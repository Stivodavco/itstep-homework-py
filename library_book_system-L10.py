class Kniha:
    def __init__(self,nazov,autor,isbn,dostupna,rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.dostupna = dostupna
        self.rok_vydania = rok_vydania

    def __str__(self):
        dostupnost = ""
        if kniha.dostupna:
            dostupnost = "Dostupna"
        else:
            dostupnost = "Nedostupna"
        return "{} od {}, ISBN: {}, Rok: {}, {}".format(self.nazov,self.autor,self.isbn,self.rok_vydania,dostupnost)

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

    def vyhladat_knihu(self,nazov):
        for kniha in self.zoznam_knih:
            if kniha.nazov.lower() == nazov.lower():
                return kniha
        print("Kniha s nazvom \'" + nazov + "\' sa nenasla.")
        return None

    def vypozicat_knihu(self,isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                kniha.dostupna = False

    def vratit_knihu(self,isbn):
        for kniha in self.zoznam_knih:
            if kniha.isbn == isbn:
                kniha.dostupna = True

    def zobrazit_zoznam_knih(self):
        for kniha in self.zoznam_knih:
            dostupnost = ""
            if kniha.dostupna:
                dostupnost = "Dostupna"
            else:
                dostupnost = "Nedostupna"
            print("{} od {}, ISBN: {}, Rok: {}, {}".format(kniha.nazov,kniha.autor,kniha.isbn,kniha.rok_vydania,dostupnost))