import csv

from domainmodel.movie import Movie
from domainmodel.actor import Actor
from domainmodel.genre import Genre
from domainmodel.director import Director

class MovieFileCSVReader:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_movies = list()
        self.__dataset_of_actors = set()
        self.__dataset_of_directors = set()
        self.__dataset_of_genres = set()

    @property
    def dataset_of_movies(self) -> list:
        return self.__dataset_of_movies

    @property
    def dataset_of_actors(self) -> set:
        return self.__dataset_of_actors

    @property
    def dataset_of_directors(self) -> set:
        return self.__dataset_of_directors

    @property
    def dataset_of_genres(self) -> set:
        return self.__dataset_of_genres

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)
            i = 0
            for row in movie_file_reader:
                # reading from csv
                title = row['Title']
                genres = row['Genre'].split(",")
                movie_description = row['Description'].strip()
                director = row['Director'].strip()
                actors = row['Actors'].split(",")
                year = int(row['Year'].strip())
                runtime = int(row['Runtime (Minutes)'].strip())

                # assigning to respective objects
                movie_director = Director(director)
                movie_genres = list()
                for g in genres:
                    genre = g.strip()
                    movie_genres.append(Genre(genre))
                movie_actors = list()
                for a in actors:
                    actor = a.strip()
                    movie_actors.append(Actor(actor))

                # assigning to respective datasets
                self.__dataset_of_movies.append(Movie(title, year))
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].genres = movie_genres
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].description = movie_description
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].director = movie_director
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].actors = movie_actors
                self.__dataset_of_movies[len(self.__dataset_of_movies)-1].runtime_minutes = runtime
                for a in movie_actors:
                    self.__dataset_of_actors.add(a)
                self.__dataset_of_directors.add(movie_director)
                for g in movie_genres:
                    self.__dataset_of_genres.add(g)
                i += 1