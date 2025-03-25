import pytest
class ValidatorRodnehoCisla:
    def __init__(self,rodne_cislo):
        self.rodne_cislo = rodne_cislo

    def je_celocislo(self):
        try:
            int(self.rodne_cislo)
        except:
            return False
        else:
            return True

    def skontroluj_dlzku(self):
        return len(str(self.rodne_cislo)) == 9 or len(str(self.rodne_cislo)) == 10

    # druhy par dvojcisel
    def skontroluj_mesiac(self):
        mesiac = int(str(self.rodne_cislo)[2:4])
        return mesiac <= 62 and mesiac > 0

    # treti par dvojcisel
    def skontroluj_den(self):
        den = int(str(self.rodne_cislo)[4:6])
        mesiac = int(str(self.rodne_cislo)[2:4])
        print(den)
        print(mesiac)
        max_dni = {
            # MESIAC : MAXIMALNY POCET DNI
            1 : 31,
            2: 29,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }
        return den > 0 and (den <= max_dni[mesiac] or den <= max_dni[mesiac-50])

    def skontroluj_delitelnost(self):
        return self.rodne_cislo % 11 == 0

    def skontroluj_validitu(self):
        if self.je_celocislo() and self.skontroluj_dlzku():
            return self.skontroluj_mesiac() and self.skontroluj_den() and self.skontroluj_delitelnost()
        else:
            return False

@pytest.mark.parametrize("rodne_cislo,ocakavana_validita", [
    (2501015154, True),
    (2502301234, False),
    (25023012345, False),
    (2501011234, False),
    (2551012475, True),
    ("pes", False)
])
def rodne_cisla_test(rodne_cislo, ocakavana_validita):
    v = ValidatorRodnehoCisla(rodne_cislo)
    assert v.skontroluj_validitu() == ocakavana_validita