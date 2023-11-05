import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import math
from collections import Counter
import re
'''
def extract_url_feat(url):
    try:
        #here i'll put the code to get the features
        return features
    except Exception as e:
        print("Error: ", e)
        return None
  '''
#url =   "https://www.github.com/lolidrk/Breaking_monoliths/blob/main/microservices/23/addition/app.py"
url = "https://www.example.com/resource?param1=value1&param2=value2"
def calculate_domain_token_count(url):
    domain = urllib.parse.urlparse(url).netloc
    #print(domain)
    domain_tokens = domain.split('.')
    #print(domain_tokens)
    return len(domain_tokens)

def calculate_avgpathtokenlen(url):
    path = urllib.parse.urlparse(url).path
    #print(f'{path=}')
    path_tokens = re.split(r'[/\-_]', path)
    #print(f'{path_tokens=}')
    #print(len(path_tokens))
    total_len = sum(len(token) for token in path_tokens)
    #print(f'{total_len=}')
    return total_len / len(path_tokens) if len(path_tokens) > 0 else 0

def calculate_tld(url):
    
    domain = urllib.parse.urlparse(url).netloc
    domain_tokens = domain.split('.')
    
    if len(domain_tokens) > 1:
        num_tld_tokens = len(domain_tokens) - 1  
        if num_tld_tokens >= 4:
            return 4
        elif num_tld_tokens == 3:
            return 3
        elif num_tld_tokens == 2:
            return 2
    else:
        return 4

def caclulate_arg_url_ratio(url):
    try:
        parsed_url = urlparse(url)
        query = parsed_url.query
        if len(url) == 0:
            return 0  
        argurl_ratio = len(query) / len(url)
        return argurl_ratio
    except Exception as e:
        print(f"Error: {e}")
        return None

def calculate_number_of_dots_in_url(url):
    return url.count('.')

def calculate_arguments_longest_word_length(url):
    query = urllib.parse.urlparse(url).query
    words = re.findall(r'\w+', query)
    #print(words)
    return max(len(word) for word in words) if words else 0

def caclulate_spchar_url(url):
    #parsed_url = urllib.parse.urlparse(url)
    special_characters = "?-_=%"
    count = 0
    #print(parsed_url)
    for char in url:
        if char in special_characters:
            #print(char)
            count += 1
    #print(f'{count=}')

    # Count double slashes "//"
    double_slash_count = url.count("//")

    # Return the total count
    total_count = count + double_slash_count
    return total_count

def calculate_delimeter_path(url):
    path = urllib.parse.urlparse(url).path
    delimiter_pattern = r'[:/?,=,;()]+'
    #print(url)
    #print(path)
    # Use re.findall to find all delimiters in the path
    delimiters = re.findall(delimiter_pattern, path)
    #print(delimiters)
    # Count the number of delimiters found
    delimiter_count = len(delimiters)
    
    return delimiter_count

def calculate_delimeter_domain(url):
    domain = urllib.parse.urlparse(url).netloc
    #print(domain)
    return domain.count('/')

#might need to check if this is getting calculated propoerly
def calculate_number_rate_directory_name(url):
    path = urllib.parse.urlparse(url).path
    digits_in_path = len(re.findall(r'\d', path))
    return digits_in_path / len(path) if len(path) > 0 else 0

#assuming they're not counting the dot after www
def calculate_symbol_count_domain(url):
    domain = urllib.parse.urlparse(url).netloc
    #print(domain)
    delimiters = re.findall(r'[://.:/?=,;()]+', domain)
    #print(delimiters)
    return len(delimiters)-1

#apply less weight to this 
def calculate_entropy_domain(url):
    #allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789-"
    domain = urllib.parse.urlparse(url).netloc
    print(domain)
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return 0.0  # Not a valid domain name
    print(domain_parts)
    domain_name = domain_parts[-2] + "." + domain_parts[-1]
    print(domain_name)
    pmf = [float(domain_name.count(c)) / len(domain_name) for c in set(domain_name)]
    min_scale = 0.6836405664
    max_scale = 1.0
    entropy = -sum(p * math.log(p, 2) for p in pmf)
    scaled_entropy = (max_scale - min_scale) * (entropy - 0) + min_scale
    scaled_entropy = min(scaled_entropy, 1.0)

    return scaled_entropy
domain_token_count = calculate_domain_token_count(url)
avgpathtokenlen = calculate_avgpathtokenlen(url)
tld = calculate_tld(url)
arg_url_ratio = caclulate_arg_url_ratio(url)
dots_in_url = calculate_number_of_dots_in_url(url)
arguments_longest_word_length = calculate_arguments_longest_word_length(url)
spchar_url = caclulate_spchar_url(url)
delimeter_path = calculate_delimeter_path(url)
delimeter_domain = calculate_delimeter_domain(url)
number_rate_directory_name = calculate_number_rate_directory_name(url)
symbol_count_domain = calculate_symbol_count_domain(url)
entropy_domain = calculate_entropy_domain(url)
