import pytest
from logics.barbarian import Barbarian
from logics.mage import Mage

def test_barbarian():
    barb_char = Barbarian("Conan")
    assert barb_char.name == "Conan"

def test_mage():
    mage_char = Mage("Merlin")
    assert mage_char.name == "Merlin"
