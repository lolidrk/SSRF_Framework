import pytest
from url_features import calculate_domain_token_count
from url_features import calculate_spchar_url
from url_features import calculate_avgpathtokenlen
from url_features import calculate_tld
from url_features import caclulate_arg_url_ratio
from url_features import calculate_number_of_dots_in_url
from url_features import calculate_arguments_longest_word_length
from url_features import calculate_delimeter_path
from url_features import calculate_delimeter_domain
from url_features import calculate_number_rate_directory_name
from url_features import calculate_symbol_count_domain
from url_features import calculate_entropy_domain

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 4)])
def test_calculate_spchar_url(test_input, expected):
    assert calculate_spchar_url(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 2)])
def test_calculate_domain_token_count(test_input, expected):
    assert calculate_domain_token_count(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 8)])
def test_calculate_avgpathtokenlen(test_input, expected):
    assert calculate_avgpathtokenlen(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 1)])
def test_calculate_tld(test_input, expected):
    assert calculate_tld(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 0.45)])
def test_caclulate_arg_url_ratio(test_input, expected):
    assert caclulate_arg_url_ratio(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 2)])
def test_calculate_number_of_dots_in_url(test_input, expected):
    assert calculate_number_of_dots_in_url(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 8)])
def test_calculate_arguments_longest_word_length(test_input, expected):
    assert calculate_arguments_longest_word_length(test_input) == expected

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource//lmao.?param1=value1&param2=value2", 3)])
def test_calculate_delimeter_path(test_input, expected):
    assert calculate_delimeter_path(test_input) == expected 

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource//lmao.?param1=value1&param2=value2", 2)])
def test_calculate_delimeter_domain(test_input, expected):
    assert calculate_delimeter_domain(test_input) == expected       

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource99//lmao.?param1=value1&param2=value2",  0.1111111111111111)])
def test_calculate_number_rate_directory_name(test_input, expected):
    assert calculate_number_rate_directory_name(test_input) == expected   

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2", 2)])
def test_calculate_symbol_count_domain(test_input, expected):
    assert calculate_symbol_count_domain(test_input) == expected   

@pytest.mark.parametrize("test_input,expected", [("https://www.example.com/resource?param1=value1&param2=value2",   3.0957952550009344)])
def test_calculate_entropy_domain(test_input, expected):
    assert calculate_entropy_domain(test_input) == expected   
