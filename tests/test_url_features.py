import url_features
import pytest

@pytest.mark.parametrize("test_input,expected", [("www.google.com", 0)])
def test_calculate_spchar_url(test_input, expected):
    result = url_features.calculate_spchar_url(test_input)
    assert result == expected

