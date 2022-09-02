## Описание
Задание на применение моков и тестов. Тестируем сервисный слой приложения, мокируем DAO.

### Требования к ПО
- Python 3.10

### Установка и запуск
1. Создать и активировать виртуальное окружение
```bash
python -m venv venv

source venv/bin/activate
```

2. Установить зависимости
```bash
pip install -r requirements.txt
```

3. Запускаем тесты

 - Объявляем переменные окружения
```bash
export PROJECT_DIR=/path_to_project/skypro_hw_20
export PYTHONPATH=$PROJECT_DIR
```
- Запускаем тесты
```bash
pytest -v -s
```
4. Результаты
```bash
========== test session starts ==========
collected 15 items                                                                                                                                                                                                                     

tests/test_services/test_director.py::TestDirectorService::test_get_one PASSED
tests/test_services/test_director.py::TestDirectorService::test_get_all PASSED
tests/test_services/test_director.py::TestDirectorService::test_create PASSED
tests/test_services/test_director.py::TestDirectorService::test_delete PASSED
tests/test_services/test_director.py::TestDirectorService::test_update PASSED
tests/test_services/test_genre.py::TestGenreService::test_get_one PASSED
tests/test_services/test_genre.py::TestGenreService::test_get_all PASSED
tests/test_services/test_genre.py::TestGenreService::test_create PASSED
tests/test_services/test_genre.py::TestGenreService::test_delete PASSED
tests/test_services/test_genre.py::TestGenreService::test_update PASSED
tests/test_services/test_movie.py::TestMovieService::test_get_one PASSED
tests/test_services/test_movie.py::TestMovieService::test_get_all PASSED
tests/test_services/test_movie.py::TestMovieService::test_create PASSED
tests/test_services/test_movie.py::TestMovieService::test_delete PASSED
tests/test_services/test_movie.py::TestMovieService::test_update PASSED
```

## Задание

**Шаг 1.** Клонируем [репозиторий](https://github.com/skypro-008/lesson18/tree/main/demostration_solution). Оттуда забираем папку demonstration_solution.

**Шаг 2.** Создаем файловую структуру для тестов.

**Шаг 3.** Создаем фикстуру с моком для DirectorDAO.

**Шаг 4.** Пишем класс с тестами для DirectorService.

**Шаг 5.** Создаем фикстуру с моком для GenreDAO.

**Шаг 6.** Пишем класс с тестами для GenreService.

**Шаг 7.** Создаем фикстуру с моком для MovieDAO.

**Шаг 8.** Пишем класс с тестами для MovieService.


**Критерии приема работы:**

1. Тесты запускаются по команде pytest.
2. Написаны тесты на класс DirectorService.
3. Написаны тесты на класс GenreService.
4. Написаны тесты на класс MovieService.

---
[SkyPro](https://sky.pro) - [Python Developer](https://sky.pro/courses/programming/python-web-course)