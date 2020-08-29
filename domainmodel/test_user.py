from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User


def test_username():
    user1 = User('Martin', 'pw12345')
    user2 = User('IAN', 'pw67890')
    user3 = User('daniel', 'pw87465')
    user4 = User('', '')
    assert (repr(user1) == "<User martin>") == True
    assert (repr(user2) == "<User ian>") == True
    assert (repr(user3) == "<User daniel>") == True
    assert (repr(user4) == "<User None>") == True

def test_eq():
    user1 = User('a', 'pw12345')
    user2 = User('b', 'pw67890')
    assert (user1 == user2) == False

def test_lt():
    user1 = User('a', 'pw12345')
    user2 = User('b', 'pw67890')
    assert (user2 < user1) == False

def test_hash():
    user1 = User('a', 'pw12345')
    user2 = User('a', 'pw67890')
    assert (hash(user1) == hash(user2)) == True

def test_watch_movie():
    user1 = User('Martin', 'pw12345')
    m1 = Movie("a",2000)
    m2 = Movie("b",2000)
    m1.runtime_minutes = 10
    m2.runtime_minutes = 20
    user1.watch_movie(m1)
    user1.watch_movie(m2)
    assert (user1.time_spent_watching_movies_minutes == 30) == True
    assert (user1.watched_movies == [m1,m2]) == True

def test_add_review():
    user1 = User('Martin', 'pw12345')
    m1 = Movie('a',2000)
    r1 = Review(m1,'wow',10)
    user1.add_review(r1)
    assert(user1.reviews == [r1]) == True