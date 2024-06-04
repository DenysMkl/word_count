from unittest.mock import patch, mock_open

import pytest


@pytest.fixture()
def mock_open_file_with_data():
    mock = mock_open(read_data='hello\n\n\n world hello')
    with patch('builtins.open', mock):
        yield mock


@pytest.fixture()
def mock_open_empty_file():
    mock = mock_open(read_data='')
    with patch('builtins.open', mock):
        yield mock