from domainmodel.actor import Actor
from domainmodel.director import Director
from domainmodel.movie import Movie
import pytest

@pytest.fixture()
def test_lt():
    m1 = Movie("",0)
    m2 = Movie("",0)
    assert (m1 < m2) == False

def test_eq():
    m1 = Movie("wow", 0)
    m2 = Movie("wow", 1899)
    assert (m1 == m2) == True

def test_set_title():
    m1 = Movie("wow", 0)
    m1.title = "WOW"
    assert (m1.title == "WOW") == True

def test_add_actors():
    m1 = Movie("wow", 0)
    m1.actors = [Actor("a"),Actor("b"),Actor("c")]
    assert (m1.actors == [Actor("a"),Actor("b"),Actor("c")]) == True

def test_one_director():
    m1 = Movie("wow", 0)
    with pytest.raises(Exception):
        m1.director = [Director("a"),Director("b")]

def test_description():
    m1 = Movie("wow", 0)
    m1.description = ""
    assert (m1.description == "") == True

def test_hash():
    m1 = Movie("wow", 2000)
    hash1 = hash("wow" + str(2000))
    assert(hash(m1) == hash1) == True

def test_repr():
    m1 = Movie("wow", 0)
    assert(repr(m1) == "<Movie wow, None>") == True