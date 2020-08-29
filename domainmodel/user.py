from domainmodel.movie import Movie
from domainmodel.review import Review

class User:

    def __init__(self, username: str, password: str):
        if username == "" or type(username) is not str:
            self.__user_name = None
        else:
            self.__user_name = username.strip().lower()
        if password == "" or type(password) is not str:
            self.__password = None
        else:
            self.__password = password
        self.__watched_movies = list()
        self.__reviews = list()
        self.__time_spent_watching_movies_minutes = 0

    @property
    def user_name(self) -> str:
        return self.__user_name

    @property
    def password(self) -> str:
        return self.__password

    @property
    def watched_movies(self) -> list:
        return self.__watched_movies

    @property
    def reviews(self) -> list:
        return self.__reviews

    @property
    def time_spent_watching_movies_minutes(self) -> int:
        return self.__time_spent_watching_movies_minutes

    def __repr__(self):
        return f"<User {self.__user_name}>"

    def __eq__(self, other):
        if not isinstance(other, User):
            return False
        return other.__user_name == self.__user_name

    def __lt__(self, other):
        return (("None" if self.__user_name is None else self.__user_name)
                <
                ("None" if other.__user_name is None else other.__user_name))

    def __hash__(self):
        return hash(self.__user_name)

    def watch_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Only Movies can be added")
        self.__watched_movies.append(movie)
        self.__time_spent_watching_movies_minutes += movie.runtime_minutes

    def add_review(self, review):
        if not isinstance(review, Review):
            raise Exception("Only Reviews can be added")
        self.__reviews.append(review)

