from main import BooksCollector
import pytest

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


    def test_get_books_with_specific_genre_with_right_genre(self):
        collector = BooksCollector()
        book_genres = {'Синий трактор':'Мультфильмы','Бриллиантовая рука':'Комедии','Моана':"Мультфильмы"}
        book_names = list(book_genres.keys())
        sinii_traktor = book_names[0]
        brilliantovaya_ruka = book_names[1]
        moana = book_names[2]

        collector.add_new_book(sinii_traktor)
        collector.add_new_book(brilliantovaya_ruka)
        collector.add_new_book(moana)
        collector.set_book_genre(sinii_traktor,book_genres[sinii_traktor])
        collector.set_book_genre(brilliantovaya_ruka,book_genres[brilliantovaya_ruka])
        collector.set_book_genre(moana, book_genres[moana])
        actual_books =collector.get_books_with_specific_genre("Мультфильмы")

        assert actual_books == ['Синий трактор','Моана']

    @pytest.mark.parametrize('book', ['Отцы и дети', 'Фауст'])
    def test_add_new_book_with_good_name(self, book):

        collector = BooksCollector()
        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 1

    @pytest.mark.parametrize('book', ['', 'Бриллиантовая рука Бриллиантовая рука Бриллиантовая рука'])
    def test_add_new_book_with_not_good_name(self, book):
        collector = BooksCollector()
        collector.add_new_book(book)

        assert len(collector.get_books_genre()) == 0



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
        book_genres = {'Моана': 'Мультфильмы', 'Шерлок Холмс': 'Детективы', 'Дракула': "Ужасы"}
        book_names = list(book_genres.keys())
        moana = book_names[0]
        sherlok_holms = book_names[1]
        drakula = book_names[2]

        collector.add_new_book(moana)
        collector.add_new_book(sherlok_holms)
        collector.add_new_book(drakula)
        collector.set_book_genre(moana, book_genres[moana])
        collector.set_book_genre(sherlok_holms, book_genres[sherlok_holms])
        collector.set_book_genre(drakula,book_genres[drakula])

        expected_books = collector.get_books_for_children()

        assert expected_books == ['Моана']

    def test_add_book_in_favorites_get_favourites(self):
        collector = BooksCollector()

        collector.add_new_book('Шерлок Холмс')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')

        collector.add_book_in_favorites('Шерлок Холмс')

        expected_favourite_books=collector.get_list_of_favorites_books()

        assert expected_favourite_books == ['Шерлок Холмс']

    def test_delete_book_from_favorites_decrease_number_of_favorites(self):
        collector=BooksCollector()

        collector.add_new_book('Шантарам')
        collector.add_book_in_favorites('Шантарам')
        collector.delete_book_from_favorites('Шантарам')

        expected_favourite_books=collector.get_list_of_favorites_books()

        assert expected_favourite_books == []

    def test_get_list_of_favorites_books_received_all(self):
        collector=BooksCollector()

        collector.add_new_book('Война и мир')
        collector.add_new_book('Маленький принц')

        collector.add_book_in_favorites('Война и мир')
        collector.add_book_in_favorites('Маленький принц')

        expected_favourite_books = collector.get_list_of_favorites_books()

        assert expected_favourite_books == ['Война и мир','Маленький принц']
