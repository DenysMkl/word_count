import pytest

from src import counter


def test_counter(mock_open_file):
    response = counter.count_words()
    assert response == {'hello': 2, 'world': 1}


def test_error_file(mock_error_file):
    with pytest.raises(IOError):
        assert counter.count_words()
