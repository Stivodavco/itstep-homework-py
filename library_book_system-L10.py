class Kniha:
    def __init__(self,nazov,autor,isbn,rok_vydania):
        self.nazov = nazov
        self.autor = autor
        self.isbn = isbn
        self.dostupna = True
        self.rok_vydania = rok_vydania

    def __str__(self):
        dostupnost = ""
        if self.dostupna:
            dostupnost = "Dostupna"
        else:
            dostupnost = "Vypozicana"
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

    def zobrazit_dostupne_knihy(self):
        for kniha in self.zoznam_knih:
            if kniha.dostupna:
                print("{} od {}, ISBN: {}, Rok: {}, Dostupna".format(kniha.nazov,kniha.autor,kniha.isbn,kniha.rok_vydania))

# PRIKLAD #
kniha1 = Kniha("Harry Potter","Rowlingova",123,2010)
kniha2 = Kniha("Pan Prstenov","Tolkien",321,2003)
kniha3 = Kniha("Daka kniha","Patrik",222,2010)

kniznica = Kniznica()
kniznica.pridat_knihu(kniha1)
kniznica.pridat_knihu(kniha2)
kniznica.pridat_knihu(kniha3)
kniznica.vypozicat_knihu(123)
print(kniha1)
print(kniha2)
print("--------")
kniznica.zobrazit_dostupne_knihy()