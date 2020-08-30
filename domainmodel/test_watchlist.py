from domainmodel.genre import Genre
from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.watchlist import WatchList
import pytest

@pytest.fixture()
def w():
    return WatchList(User('ABC','123'),"")

def test_default_name(w):
    assert w.watchlist_name == "New Watchlist"

def test_iter_and_next(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    iterable = iter(w)
    assert next(iterable) == Movie("Moana", 2016)

def test_add_and_remove_movie(w):
    w.add_movie(Movie("Moana", 2016))
    w.remove_movie(Movie("Moana", 2016))
    assert w.watchlist == []

def test_select_movie(w):
    w.add_movie(Movie("Moana", 2016))
    assert w.select_movie_to_watch(0) == Movie("Moana", 2016)

def test_size(w):
    w.add_movie(Movie("Moana", 2016))
    assert w.size() == 1

def test_first_movie_in_watchlist(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    assert w.first_movie_in_watchlist() == Movie("Moana", 2016)

def test_clear_watchlist(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    w.clear_watchlist()
    assert w.watchlist == []

def test_share_watchlist(w):
    w.add_movie(Movie("Moana", 2016))
    w.add_movie(Movie("Ice Age", 2002))
    w.add_movie(Movie("Guardians of the Galaxy", 2012))
    user1 = User("DEF","wow")
    w1 = w.share_watchlist(user1)
    assert w1.watchlist_owner == user1
    assert w1.watchlist == w.watchlist

def test_sort_by_title(w):
    m1 = Movie("Moana", 2016)
    m2 = Movie("Ice Age", 2002)
    m3 = Movie("Guardians of the Galaxy", 2012)
    w.add_movie(m1)
    w.add_movie(m2)
    w.add_movie(m3)
    watchlist = w.sort_watchlist_by_title()
    assert watchlist == [m3,m2,m1]

def test_sort_by_year(w):
    m1 = Movie("Moana", 2016)
    m2 = Movie("Ice Age", 2002)
    m3 = Movie("Guardians of the Galaxy", 2012)
    w.add_movie(m1)
    w.add_movie(m2)
    w.add_movie(m3)
    watchlist = w.sort_watchlist_by_year()
    assert watchlist == [m2,m3,m1]

def test_sort_by_runtime(w):
    m1 = Movie("Moana", 2016)
    m2 = Movie("Ice Age", 2002)
    m3 = Movie("Guardians of the Galaxy", 2012)
    m1.runtime_minutes = 1
    m2.runtime_minutes = 100
    m3.runtime_minutes = 10
    w.add_movie(m1)
    w.add_movie(m2)
    w.add_movie(m3)
    watchlist = w.sort_watchlist_by_runtime()
    assert watchlist == [m1,m3,m2]

def test_change_watchlist_name(w):
    w.change_watchlist_name("WOW")
    assert w.watchlist_name == "WOW"

def test_get_recommendations(w):
    m1 = Movie("Action",2000)
    m1.genres = [Genre("Crime"),Genre("Drama"),Genre("Horror")]
    w.add_movie(m1)
    w1 = w.get_recommendations("Data1000Movies.csv")
    movies = [Movie("Hounds of Love", 2016), Movie("Funny Games", 2007), Movie("The Girl Next Door", 2007)]
    assert w1.watchlist == movies
