import pytest as pytest
from unittest.mock import MagicMock
from dao.genre import GenreDAO
from dao.model.genre import Genre
from service.genre import GenreService


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(None)

    horror = Genre(id=1, name='horror')
    comedy = Genre(id=2, name='comedy')
    drama = Genre(id=3, name='drama')

    genre_dao.get_one = MagicMock(return_value=horror)
    genre_dao.get_all = MagicMock(return_value=[horror, comedy, drama])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.delete = MagicMock()
    genre_dao.update = MagicMock(return_value=horror)

    return genre_dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genre_service(self, genre_dao):
        self.genre_service = GenreService(dao=genre_dao)

    def test_get_one(self):
        genre = self.genre_service.get_one(1)
        assert genre is not None
        assert genre.id is not None

    def test_get_all(self):
        genres = self.genre_service.get_all()
        assert len(genres) > 0

    def test_create(self):
        new_genre = {
            "id": 1,
            "name": "Fighting",
        }
        genre = self.genre_service.create(new_genre)
        assert genre.id is not None

    def test_delete(self):
        self.genre_service.delete(1)

    def test_update(self):
        new_genre = {
            "id": 1,
            "name": "Fighting",
        }
        genre = self.genre_service.update(new_genre)
        assert genre is not None
        assert genre.id is not None
