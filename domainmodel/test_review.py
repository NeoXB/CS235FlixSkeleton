from domainmodel.review import Review


def test_eq():
    r1 = Review("", "", 0)
    r2 = Review("", "", 0)
    assert (r1 == r2) == True