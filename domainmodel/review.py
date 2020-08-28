from datetime import datetime

from domainmodel.movie import Movie

class Review:

    def __init__(self, movie: Movie, txt: str, rating: int):
        if type(movie) is not Movie:
            self.__movie = Movie("", 0)
        else:
            self.__movie = movie
        if type(txt) is not str:
            self.__review_text = None
        else:
            self.__review_text = txt.strip()
        if rating < 1 or rating > 10 or type(rating) is not int:
            self.__rating = None
        else:
            self.__rating = rating
        self.__timestamp = datetime.now()

    @property
    def movie(self) -> Movie:
        return self.__movie

    @property
    def review_text(self) -> str:
        return self.__review_text

    @property
    def rating(self) -> int:
        return self.__rating

    @property
    def timestamp(self) -> datetime:
        return self.__timestamp

    def __repr__(self):
        return f"<Review {self.__movie}, {self.__review_text}, {self.__rating}, {self.__timestamp}>"

    def __eq__(self, other):
        if not isinstance(other, Review):
            return False
        return (other.__movie == self.__movie and
                other.__review_text == self.__review_text and
                other.__rating == self.__rating and
                other.__timestamp == self.__timestamp)
