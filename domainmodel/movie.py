from domainmodel.genre import Genre
from domainmodel.actor import Actor
from domainmodel.director import Director

class Movie:

    def __init__(self, title: str, year: int):
        if title == "" or type(title) is not str:
            self.__title = None
        else:
            self.__title = title.strip()
        if year < 1900 or type(year) is not int:
            self.__release_year = None
        else:
            self.__release_year = year
        self.__description = ""
        self.__director = Director("")
        self.__actors = list()
        self.__genres = list()
        self.__runtime_minutes = 0

    @property
    def title(self) -> str:
        return self.__title

    @property
    def release_year(self) -> int:
        return self.__release_year

    @property
    def description(self) -> str:
        return self.__description

    @property
    def director(self) -> Director:
        return self.__director

    @property
    def actors(self) -> list:
        return self.__actors

    @property
    def genres(self) -> list:
        return self.__genres

    @property
    def runtime_minutes(self) -> int:
        return self.__runtime_minutes

    @title.setter
    def title(self, t):
        if t == "" or type(t) is not str:
            self.__title = None
        else:
            self.__title = t.strip()

    @description.setter
    def description(self, d):
        if type(d) is not str:
            self.__title = ""
        else:
            self.__description = d.strip()

    @director.setter
    def director(self, d):
        if not isinstance(d, Director):
            raise Exception("There can only be one Director per Movie")
        self.__director = d

    @actors.setter
    def actors(self, a):
        if not isinstance(a, list):
            raise Exception("It needs to be a list of actor(s)")
        self.__actors = a

    @genres.setter
    def genres(self, g):
        if not isinstance(g, list):
            raise Exception("It needs to be a list of genre(s)")
        self.__genres = g

    @runtime_minutes.setter
    def runtime_minutes(self, rm):
        if rm < 1:
            raise ValueError("Only positive numbers can be assigned to runtime minutes")
        else:
            self.__runtime_minutes = rm

    def __repr__(self):
        return f"<Movie {self.__title}, {self.__release_year}>"

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return (other.__title == self.__title and
                other.__release_year == self.__release_year)

    def __lt__(self, other):
        return (("None" if self.__title is None else self.__title,
                 "None" if self.__release_year is None else self.__release_year)
                <
                ("None" if other.__title is None else other.__title,
                 "None" if other.__release_year is None else other.__release_year))

    def __hash__(self):
        return hash(self.__title + str(self.__release_year))

    def add_actor(self, a):
        if not isinstance(a, Actor):
            raise Exception("Only Actors can be added")
        self.__actors.append(a)

    def remove_actor(self, a):
        if a in self.__actors:
            self.__actors.remove(a)

    def add_genre(self, g):
        if not isinstance(g, Genre):
            raise Exception("Only Genres can be added")
        self.__genres.append(g)

    def remove_genre(self, g):
        if g in self.__genres:
            self.__genres.remove(g)

