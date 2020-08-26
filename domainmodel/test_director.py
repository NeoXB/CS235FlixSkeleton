from domainmodel.director import Director

def test_director_full_name():
    director1 = Director("Taika Waititi")
    assert repr(director1) == "<Director Taika Waititi>"
    director2 = Director("")
    assert director2.director_full_name is None
    director3 = Director(42)
    assert director3.director_full_name is None
    director4 = Director("")
    assert repr(director4) == "<Director None>"

def test_director_equal():
    director1 = Director("b")
    director2 = Director("B")
    assert (director1 == director2) == False

def test_director_lt():
    director1 = Director("Cameron Diaz")
    director2 = Director("Brad Pitt")
    assert (director1 > director2) == True

def test_director_hash():
    director1 = Director("Taika Waititi")
    assert hash(director1)
