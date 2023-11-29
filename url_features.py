import urllib.request
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import math
from collections import Counter
import re
import tldextract
import pandas as pd
import math
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
#url = "https://www.example.com/resource?param1=value1&param2=value2"



'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

"Domain token count: Tokens are taken from the URL String. The Malicious URLs 
use multiple domain tokens. Number of tokens in the domains are calculated"

Example : www.example.com
Considering only example and com as part of the domain
'''

def calculate_domain_token_count(url):
    domain = urllib.parse.urlparse(url).netloc
    #print(domain)
    domain_tokens = domain.split('.')
    #print(domain_tokens)
    #print(domain)
    return len(domain_tokens)-1

'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

Features related to Length: Length of URL gets longer due to addition of
variables or redirected URL. [11,18]. such as, Length of URL (url Len),domain 
(domain Len) and file name (file Name Len), Arguments’ Longest-WordLength3, 
Longest Path Token Length [8], Average length of path token[10]
 (avgpathtokenlen). 

 So here I've taken the path part of the url i.e the part after for eg. in 
 www.example.com/resuources, it is whatever which will appear after com or it's
 equivalent. And then each word separated by '/' in this path is 
 considered as a token. And then the len of each token is added and 
 is divided by total number of tokens

'''
def calculate_avgpathtokenlen(url):
    parsed_url = urlparse(url)
    path = parsed_url.path
    tokens = path.split('/')
    #print(f'{tokens=}')
    # Calculate the average token length
    total_length = sum(len(token) for token in tokens)
    #print(f'{total_length=}')
    
    #To account for the empty token in tokens
    num_tokens = len(tokens)-1
    if num_tokens > 0:
        return total_length / num_tokens
    else:
        return 0 

'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

Some phishing URL use multiple top level domain within a domainname

Considering tld extract is not doing a very good jobs and extracting multiple 
tlds especially in sites like this  - http://black.com.pk/service.paypal.confirm.com.usa.webscrlcmdl.login.submit.dispatch.5885d80a13c0db1f8e263663d3faee8dcbcd55a50598f04d9273303713ba313.980487.98746.874774.8754/paypal.com

I will use regex where we are assuming that tlds will have lowercase letters 
separater by periods. This might not cover all edge cases, but it's working well enough
'''


def calculate_tld(url):
    tlds = re.findall(r'\b[a-z]+\.[a-z]+\b', url)
    #print(tlds)
    tld_count = len(tlds)
    return tld_count

'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

Features related with Length Ratio: The length ratio of the parts of URLis computed to find the abnormal parts [21]. The combination of URL partconsist of argument, path, domain and URL such as argPathRatio (Ratio ofargument and path), argUrlRatio (Ratio of argument and URL), argDomain-Ratio (Argument divided by domain), domainUrlRatio (Domain divided byURL), pathUrlRatio (Path divided by URL), PathDomainRatio (Path dividedby Domain) 

So i have assumed that by argument they mean the query part of the url and divided the len of that with the len of the entire url to get the ratio
'''

def caclulate_arg_url_ratio(url):
    try:
        parsed_url = urlparse(url)
        query = parsed_url.query
        if len(url) == 0:
            return 0 
        #print(f'{query=}')
        #print(f'{len(query)=}')
        #print(f'{len(url)=}')
        argurl_ratio = len(query) / len(url)
        return argurl_ratio
    except Exception as e:
        print(f"Error: {e}")
        return None

def calculate_number_of_dots_in_url(url):
    return url.count('.')

'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

Features related to Length: Length of URL gets longer due to addition ofvariables or redirected URL. [11,18]. such as, Length of URL (url Len),domain (domain Len) and file name (file Name Len), Arguments’ Longest-WordLength3, Longest Path Token Length [8], Average length of path token[10] (avgpathtokenlen) 

From PhishDef: URL Names Say It All
By Anh Le, Athina Markopoulou, Michalis Faloutsos

Features related to the argument part. URLs that serve
pages written in server side scripting languages, such as,
php and asp, often have arguments. The features in this
category include the length of the argument part, the number
of variables, the length of the longest variable value, and the
maximum number of delimiters (‘.’, ‘ ’, and ‘-’) used in a
value. We observe that phishing URLs often include a long
list of arguments, as well as auto-generated argument values,
which are often unusually long. Also, there are instances where
the host name is obfuscated in the values assigned to variables.
The features here are designed to address these instances 

'''
def calculate_arguments_longest_word_length(url):
    words = re.findall(r'\w+', url)
    #print(words)
    #for word in words:
        #print(f'{word=}, {len(word)=}')
    return max(len(word) for word in words) if words else 0
'''
From Malicious URL Detection Based on Associative Classification
by Sandra Kumi 1,ChaeHo Lim 2 andSang-Gon Lee 1 - 
 Attackers use special characters for URL encoded attacks to bypass validation 
 logic. We count the number of special characters (‘;’, ‘+=’, ‘_’, ‘?’, ‘=’, 
 ‘&’, ‘[‘, ‘]’, ‘#’, ‘~’, ‘%’, ‘@’, ‘$’, ‘*’, ‘+’, ‘!’, ‘|’) found in a URL.
'''

'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

URLs use special characters which are suspicious such as // and they have higher risk of redirection 
'''
def calculate_spchar_url(url):
    #parsed_url = urllib.parse.urlparse(url)
    special_characters = {';', '+=', '_', '?', '=', '&', '[', ']', '#', '~', '%', '@', '$', '*', '+', '!', '|', '//'}
    count = 0

    for char in url:
        if char in special_characters:
            #print(char)
            count += 1

    return count
    #print(parsed_url)

    #print(f'{count=}')

    # Count double slashes "//"
    #double_slash_count = url.count("//")

    # Return the total count
    #total_count = count + double_slash_count
    #return total_count
'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

"Symbol Count Domain: A dictionary of delimiters such as ://.:/?=,;()]+ arecalculated from domain. Phishing URLs e.g. have more dots compared to benign ones"

For calculating another feature Symbol Count Domain, they have considered various delimiters
However they haven't commented on the calculation of delimeter path, but considering the same delimeters given above, 
and a few more due to the 'such as', the logic was coded as follows:
Also, put a negative look behind assertion to not consider ://

'''
def calculate_delimeter_path(url):
    path = urllib.parse.urlparse(url).path
    delimiter_pattern =delimiter_pattern = r'[:/?&#=,.;()]+|(?<!:)//'
    #print(url)
    #print(path)
    delimiters = re.findall(delimiter_pattern, path)
    #print(delimiters)
    delimiter_count = len(delimiters)
    return delimiter_count

'''
Same as above, so the same assumptions have been made
'''

def calculate_delimeter_domain(url):
    domain = urllib.parse.urlparse(url).netloc
    #print(domain)
    delimiter_pattern =delimiter_pattern = r'[:/?&#=,.;()[]+|(?<!:)//'
    #print(url)
    delimiters = re.findall(delimiter_pattern, domain)
    #print(delimiters)
    delimiter_count = len(delimiters)
    return delimiter_count

'''
Pretty self explanatory actually

'''
def calculate_number_rate_directory_name(url):
    path = urllib.parse.urlparse(url).path
    digits_in_path = len(re.findall(r'\d', path))
    #print(len(path))
    return digits_in_path / len(path) if len(path) > 0 else 0


'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani
 
Symbol Count Domain: A dictionary of delimiters such as ://.:/?=,;()]+ are
calculated from domain. Phishing URLs e.g. have more dots compared to
benign ones 

However, considering how this would make it exactly the same as  calculate_delimter_domain
I've decideed to instead just coded it so that all possible symbols will be considered
'''

def calculate_symbol_count_domain(url):
    domain = urllib.parse.urlparse(url).netloc
    #print(domain)
    symbols = "!@#$%^&*()_+=-[]{}|;:'\"<>,.?/~`"
    symbol_count = sum(domain.count(symbol) for symbol in symbols)
    return symbol_count

'''
From Detecting Malicious URLs Using Lexical Analysis
By Mohammad Mamun,Muhammad Ahmad Rathore,Arash Habibi Lashkari,Natalia Stakhanova, Ali A. Ghorbani

Malicious URL Detection Based on Associative Classification
by Sandra Kumi ,ChaeHo Lim  and Sang-Gon Lee  
Entropy Domain and Extension: Malicious websites often insert additionalcharacters in the URL to make it look like a legitimate. e.g, CITI can bewritten as CIT1, by replacing last alphabet I with digit 1. English text hasfairly low entropy i.e., it is predictable. By inserting characters the entropychanges than usual. For identifying the randomly generated malicious URLs,alphabet entropy is used."
However, they have not mentioned the formula they have used for entropy. So, using the below paper as reference entropy has been calculated.
Entropy of domain name: Entropy measures the randomness factor or uncertainty in URLs; the higher the entropy, the higher the randomness factor in the URL. Entropy is used to detect randomized domain names. Some malicious URLs use domain generation algorithms (DGA) to change domains frequently, hence blacklisting these URLs is not efficient. DGA is a program that provides malware with new domains on-demand or on the fly [21]. URLs with high entropy are significant indicators of malicious behavior. Entropy can help detect malicious URLs by setting thresholds based on the entropies of legitimate URLs. We calculate the entropy of domain names, using the Shannon entropy formula:
𝐻(𝑥) =−∑𝑖=0𝑛𝑝(𝑥𝑖)log𝑏𝑝(𝑥𝑖)
(1)where H(x) is the Shannon entropy of string x, b is the base of the logarithm used, and p(x) is the probability mass function.
 '''
def calculate_entropy_domain(url):
    #allowed_characters = "abcdefghijklmnopqrstuvwxyz0123456789-"
    domain = urllib.parse.urlparse(url).netloc
    print(domain)
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return 0.0  # Not a valid domain name
    print(domain_parts)
    domain_name = ".".join(domain_parts[1:])
    print(domain_name)
    probabilities = [count / len(domain_name) for count in Counter(domain_name).values()]
    entropy = -sum(p * math.log2(p) for p in probabilities)
    return entropy


def extract_url_feat(url):
    domain_token_count = calculate_domain_token_count(url)
    avgpathtokenlen = calculate_avgpathtokenlen(url)
    tld = calculate_tld(url)
    arg_url_ratio = caclulate_arg_url_ratio(url)
    dots_in_url = calculate_number_of_dots_in_url(url)
    arguments_longest_word_length = calculate_arguments_longest_word_length(url)
    spchar_url = calculate_spchar_url(url)
    delimeter_path = calculate_delimeter_path(url)
    delimeter_domain = calculate_delimeter_domain(url)
    number_rate_directory_name = calculate_number_rate_directory_name(url)
    symbol_count_domain = calculate_symbol_count_domain(url)
    entropy_domain = calculate_entropy_domain(url)
    input_data = [domain_token_count,avgpathtokenlen,tld,arg_url_ratio,dots_in_url,arguments_longest_word_length,spchar_url,delimeter_domain,delimeter_path,number_rate_directory_name,symbol_count_domain,entropy_domain]

    return input_data