from domainmodel.genre import Genre


def test_genre_name():
    genre1 = Genre("Comedy")
    assert repr(genre1) == "<Genre Comedy>"
    genre2 = Genre("")
    assert repr(genre2) == "<Genre None>"
    genre3 = Genre(0)
    assert genre3.genre_name is None
