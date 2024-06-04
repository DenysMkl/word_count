import pytest

from src import counter


def test_counter_file(mock_open_file_with_data):
    result = counter.count_words('text.txt')
    assert result == {'hello': 2, 'world': 1}


def test_empty_file(mock_open_empty_file):
    result = counter.count_words('text.txt')
    assert result == {}


def test_not_specify_file():
    with pytest.raises(TypeError):
        assert counter.count_words()


def test_not_existed_file():
    with pytest.raises(FileNotFoundError):
        assert counter.count_words('text.txt')
