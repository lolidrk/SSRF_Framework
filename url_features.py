import urllib.request
from bs4 import BeautifulSoup
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
url =   "https://github.com/lolidrk/Breaking_monoliths/blob/main/microservices/23/addition/app.py"

domain_tokens = url.split('/')
domain_token_count = len(domain_tokens)

avgpathtokenlen = len(url) / domain_token_count

