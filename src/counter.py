class ContextManager:
    def __init__(self, filename, method='r'):
        self.filename = filename
        self.method = method

    def __enter__(self):
        self.file = open(self.filename, self.method)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()

    def read_file(self):
        data = self.file.read()
        return data


def count_words(filename):
    with ContextManager(filename) as file:
        text_of_words = file.read_file()
        list_of_words = text_of_words.split()
        dict_word_count = dict()
        for word in set(list_of_words):
            count_of_word = list_of_words.count(word)
            dict_word_count.update({word: count_of_word})

    return dict_word_count
