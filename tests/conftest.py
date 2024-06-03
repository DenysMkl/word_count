from unittest.mock import patch, mock_open

import pytest


@pytest.fixture()
def mock_open_file():
    mock = mock_open(read_data='hello world hello')
    with patch('builtins.open', mock):
        yield mock


@pytest.fixture()
def mock_error_file():
    mock = mock_open()
    mock.return_value.read.side_effect = IOError("Unable to read file")
    with patch('builtins.open', mock):
        yield mock
