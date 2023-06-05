import unittest
from app import app, count_words


class FlaskAppTests(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Поиск самого частого слова в файле', response.data.decode())

    def test_result(self):
        with open('../text.txt', 'rb') as file:
            response = self.app.post('/', data={'file': file})
            self.assertEqual(response.status_code, 200)
            self.assertIn('<h1>Самое частое слово:</h1>', response.data.decode())

    def test_count_words_empty_file(self):
        file_path = './files/empty.txt'
        expected_word_counts = {}
        actual_word_counts = count_words(file_path)
        self.assertEqual(expected_word_counts, actual_word_counts)

    def test_count_words_single_word(self):
        file_path = './files/single_word.txt'
        expected_word_counts = {'hello': 1}
        actual_word_counts = count_words(file_path)
        self.assertEqual(expected_word_counts, actual_word_counts)

    def test_count_words_multiple_words(self):
        file_path = './files/multiple_words.txt'
        expected_word_counts = {'hello': 2, 'world': 1}
        actual_word_counts = count_words(file_path)
        self.assertEqual(expected_word_counts, actual_word_counts)

    def test_count_words_word_with_punctuation(self):
        file_path = './files/word_with_punctuation.txt'
        expected_word_counts = {'hello': 1, 'world': 1}
        actual_word_counts = count_words(file_path)
        self.assertEqual(expected_word_counts, actual_word_counts)

    def test_count_words_word_with_numbers(self):
        file_path = './files/word_with_numbers.txt'
        expected_word_counts = {'hello': 1, 'world': 1}
        actual_word_counts = count_words(file_path)
        self.assertEqual(expected_word_counts, actual_word_counts)


if __name__ == '__main__':
    unittest.main()
