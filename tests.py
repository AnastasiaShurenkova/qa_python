from main import BooksCollector

class TestBooksCollector:
    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.books_genre = {}
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2


    def test_add_new_book_len_name_more_than_forty(self):
         collector = BooksCollector()
         collector.books_genre = {}
         collector.add_new_book('Гордость и предубеждение и зомби и вампиры')

         assert len(collector.books_genre) == 0

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение') == 'Фантастика'

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')

        assert collector.get_book_genre('Незнайка') == 'Мультфильмы'


    def test_get_books_for_children_genre_cartoon(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Незнайка']

    def test_get_books_for_children_genre_horror(self):
        collector = BooksCollector()
        collector.add_new_book('Фредди Крюгер')
        collector.set_book_genre('Фредди Крюгер', 'Ужасы')

        assert collector.get_books_for_children() == []

    def test_get_books_with_specific_genre_fantasy(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Гордость и предубеждение']

    def test_get_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')

        assert collector.get_book_genre('Гордость и предубеждение') == 'Фантастика'

    def test_add_book_in_favorites_in_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.add_book_in_favorites('Незнайка')

        assert collector.get_list_of_favorites_books() == ['Незнайка']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Незнайка')
        collector.set_book_genre('Незнайка', 'Мультфильмы')
        collector.add_new_book('Гордость и предубеждение')
        collector.set_book_genre('Гордость и предубеждение', 'Фантастика')
        collector.add_book_in_favorites('Незнайка')
        collector.add_book_in_favorites('Гордость и предубеждение')
        collector.delete_book_from_favorites('Незнайка')

        assert collector.get_list_of_favorites_books() == ['Гордость и предубеждение']

    def test_get_list_of_favorites_books_without_books_in_list(self):
        collector = BooksCollector()

        assert collector.get_list_of_favorites_books() == []

