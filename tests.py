from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гарри Поттер')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.books_genre.keys()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_set_book_genre_set_genre(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        collector.add_new_book('Гарри Поттер')
        collector.set_book_genre('Гарри Поттер', 'Фантастика')
        actual_genre = collector.get_book_genre('Гарри Поттер')

        assert actual_genre == 'Фантастика'


    def test_get_book_genre_get_genre(self):
       collector = BooksCollector()

       collector.add_new_book('Синий трактор')
       collector.set_book_genre('Синий трактор','Мультфильмы')
       actual_genre = collector.get_book_genre('Синий трактор')

       assert actual_genre == 'Мультфильмы'



    def test_get_books_with_specific_genre_with_right_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Синий трактор')
        collector.add_new_book('Бриллиантовая рука')
        collector.add_new_book('Моана')
        collector.set_book_genre('Синий трактор','Мультфильмы')
        collector.set_book_genre('Бриллиантовая рука','Комедии')
        collector.set_book_genre('Моана', 'Мультфильмы')
        actual_books =collector.get_books_with_specific_genre("Мультфильмы")

        assert actual_books == ['Синий трактор','Моана']

    def test_get_books_genre_received_all(self):
         collector = BooksCollector()

         collector.add_new_book('Моана')
         collector.add_new_book('Бриллиантовая рука')
         collector.set_book_genre('Моана','Мультфильмы')
         collector.set_book_genre('Бриллиантовая рука', 'Комедии')

         expected_genre = collector.get_books_genre()

         assert expected_genre == {'Моана':'Мультфильмы' ,'Бриллиантовая рука': 'Комедии'}

    def test_get_books_for_children_with_right_books(self):
        collector = BooksCollector()

        collector.add_new_book('Моана')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Моана', 'Мультфильмы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        expected_books = collector.get_books_for_children()

        assert expected_books == ['Моана']

    def test_add_book_in_favorites_get_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Три кота')
        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Три кота', 'Мультфильмы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        collector.add_book_in_favorites('Шерлок Холмс')

        expected_favourite_books=collector.get_list_of_favorites_books()

        assert expected_favourite_books == ['Шерлок Холмс']

    def test_delete_book_from_favorites_decrease_number_of_favorites(self):
        collector=BooksCollector()

        collector.add_new_book('Анна Каренина')
        collector.add_new_book('Шантарам')
        collector.add_book_in_favorites('Анна Каренина')
        collector.add_book_in_favorites('Шантарам')
        collector.delete_book_from_favorites('Шантарам')

        expected_favourite_books=collector.get_list_of_favorites_books()

        assert expected_favourite_books == ['Анна Каренина']
