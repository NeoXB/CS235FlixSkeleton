from domainmodel.movie import Movie
from domainmodel.user import User
from domainmodel.review import Review

class MovieWatchingSimulation:

    def __init__(self, admin: User, movie: Movie):
        if type(admin) is not User:
            raise Exception("Sorry, that is an invalid User")
        else:
            self.__administrator = admin
        if type(movie) is not Movie:
            raise Exception("Sorry, that is an invalid Movie")
        else:
            self.__movie_to_watch = movie
        self.__watch_group = list()
        self.__watch_group.append(self.__administrator)

    @property
    def administrator(self):
        return self.__administrator

    @property
    def movie_to_watch(self):
        return self.__movie_to_watch

    @property
    def watch_group(self):
        return self.__watch_group

    def add_user(self, user):
        if not isinstance(user, User):
            raise Exception("Please add a valid User")
        elif user not in self.__watch_group:
            self.__watch_group.append(user)

    def remove_user(self, user):
        if not isinstance(user, User):
            raise Exception("Please remove a valid User")
        elif user in self.__watch_group and user != self.__administrator:
            self.__watch_group.remove(user)

    def change_movie(self, movie):
        if not isinstance(movie, Movie):
            raise Exception("Please add a valid Movie")
        elif movie == self.__movie_to_watch:
            raise Exception("That movie is already in queue")
        else:
            self.__movie_to_watch = movie

    def write_review_for_everyone(self, review):
        if not isinstance(review, Review):
            raise Exception("Please write a valid Review")
        elif review.movie != self.__movie_to_watch:
            raise Exception("Please write a Review for the Movie in queue")
        else:
            for user in self.__watch_group:
                if review not in user.reviews:
                    user.add_review(review)

    def update_user_information(self):
        for user in self.__watch_group:
            if self.__movie_to_watch not in user.watched_movies:
                user.watch_movie(self.__movie_to_watch)
