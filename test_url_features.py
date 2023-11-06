from url_features import calculate_spchar_url
import pytest

@pytest.mark.parametrize("test_input,expected", [("www.google.com", 0)])
def test_calculate_spchar_url(test_input, expected):
    assert calculate_spchar_url(test_input) == expected

