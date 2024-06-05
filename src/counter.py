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
    """Retrieves data from the selected file and counts
        the number of times each word is mentioned in that file.

    Returns dictionary that stores the calculation results.
    The keys in the dictionary are the words themselves,
    and the values are the number of times each word appears in the file.
    """
    with ContextManager(filename) as file:
        text_of_words = file.read_file()

    list_of_words = text_of_words.split()
    list_of_words = list(map(lambda x: x.rstrip(',. '), list_of_words))
    dict_word_count = dict()

    for word in set(list_of_words):
        count_of_word = list_of_words.count(word)
        dict_word_count.update({word: count_of_word})

    return dict_word_count


if __name__ == '__main__':
    print(count_words('text.txt'))
