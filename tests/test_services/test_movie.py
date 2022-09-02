import pytest as pytest
from unittest.mock import MagicMock
from dao.movie import MovieDAO
from dao.model.movie import Movie
from service.movie import MovieService


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(None)

    aladdin = Movie(id=1, title='aladdin', description='desc',
                    trailer='trailer', year=2021, rating=5.0)
    harry_potter = Movie(id=2, title='harry_potter', description='desc',
                         trailer='trailer', year=2008, rating=4.5)
    friends = Movie(id=3, title='friends', description='desc',
                    trailer='trailer', year=2000, rating=3.9)

    movie_dao.get_one = MagicMock(return_value=aladdin)
    movie_dao.get_all = MagicMock(return_value=[aladdin, harry_potter, friends])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.delete = MagicMock()
    movie_dao.update = MagicMock(return_value=aladdin)

    return movie_dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert movie.id is not None

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        new_movie = {
            'id': 1,
            'tittle': 'new_title',
            'description': 'new_desc',
            'trailer': 'new_trailer',
            'year': 2022,
            'rating': 5.0,
        }
        movie = self.movie_service.create(new_movie)
        assert movie.id is not None

    def test_delete(self):
        self.movie_service.delete(1)

    def test_update(self):
        new_movie = {
            'id': 100,
            'tittle': 'new_title',
            'description': 'new_desc',
            'trailer': 'new_trailer',
            'year': 2022,
            'rating': 2.5,
        }
        movie = self.movie_service.update(new_movie)
        assert movie is not None
        assert movie.id is not None
