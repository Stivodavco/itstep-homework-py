from validator_rodneho_cisla import ValidatorRodnehoCisla
import pytest

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