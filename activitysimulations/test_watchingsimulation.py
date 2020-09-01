from activitysimulations.watchingsimulation import MovieWatchingSimulation
from domainmodel.movie import Movie
from domainmodel.review import Review
from domainmodel.user import User
import pytest

@pytest.fixture()
def simulation():
    return MovieWatchingSimulation(User('ABC','123'), Movie("WOW",2020))

def test_add_user(simulation):
    simulation.add_user(User('X','123456'))
    simulation.add_user(User('Y','00000'))
    simulation.add_user(User('Z','abcd'))
    assert simulation.watch_group == [User('ABC','123'),User('X','123456'),User('Y','00000'),User('Z','abcd')]

def test_remove_user(simulation):
    simulation.add_user(User('X', '123456'))
    simulation.add_user(User('Y', '00000'))
    simulation.add_user(User('Z', 'abcd'))
    simulation.remove_user(User('X','123456'))
    simulation.remove_user(User('Y','00000'))
    simulation.remove_user(User('Z','abcd'))
    simulation.remove_user(User('ABC','123'))
    assert simulation.watch_group == [simulation.administrator]

def test_change_movie(simulation):
    simulation.change_movie(Movie("NEW",2021))
    assert simulation.movie_to_watch == Movie("NEW",2021)

def test_write_review_for_everyone(simulation):
    u1 = User('X', '123456')
    simulation.add_user(u1)
    r1 = Review(Movie('WOW',2020),"A very good movie",10)
    simulation.write_review_for_everyone(r1)
    assert len(simulation.administrator.reviews) == 1
    assert u1.reviews[0].movie == Movie('WOW',2020)

def test_update_user_information(simulation):
    u1 = User('X', '123456')
    u2 = User('Y','00000')
    simulation.add_user(u1)
    simulation.add_user(u2)
    m1 = Movie("NEW",2021)
    m1.runtime_minutes = 100
    simulation.change_movie(m1)
    simulation.update_user_information()
    assert len(simulation.administrator.watched_movies) == 1
    assert u1.watched_movies[0] == m1
    assert u2.time_spent_watching_movies_minutes == 100
