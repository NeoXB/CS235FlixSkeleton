from datafilereaders.movie_file_csv_reader import MovieFileCSVReader


def test_csv():
    filename = './datafiles/Data1000Movies.csv'
    movie_file_reader = MovieFileCSVReader(filename)
    movie_file_reader.read_csv_file()
    assert (len(movie_file_reader.dataset_of_movies) == 1000) == True
    assert (len(movie_file_reader.dataset_of_actors) == 1985) == True
    assert (len(movie_file_reader.dataset_of_directors) == 644) == True
    assert (len(movie_file_reader.dataset_of_genres) == 20) == True
