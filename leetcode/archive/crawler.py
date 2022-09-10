from bs4 import BeautifulSoup
from html.parser import HTMLParser
import requests
import re, time, os
import urllib2, random, yaml
import sys

PARSER = 'html.parser'
htmlparser = HTMLParser()

def get_article_name(url, extension='html', prefix=""):
    if url.endswith('/'): url = url[:-1]
    arr = url.split('/')
    filename = arr[-2] if arr[-1] == 'description' else arr[-1]
    return "%s/%s%s.%s" % ('/tmp/page', prefix, filename, extension)

def load_from_local(url):
    article = get_article_name(url)
    if os.path.isfile(article):
        return file(article).read()
    return None

def load_from_url(url):
    user_agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46'
    req = urllib2.Request(str(url), data=None, headers={'User-Agent': user_agent})
    con = urllib2.urlopen( req )
    html = con.read()
    time.sleep(random.randint(10,20))
    return html

def load_page(url, save=False):
    page = load_from_local(url)
    if page:
        return BeautifulSoup(page, PARSER)
    
    page = load_from_url(url)
    soup = BeautifulSoup(page, PARSER)
    if save:
        article = get_article_name(url)
        with open(article, 'w') as f:
            f.write(page)
    return soup

# def extract_page_links(url):
#     links = []
#     soup = load_page(url)
#     for link in soup.find_all('a', {'sasource': "analysis__"}):
#         url = link.get('href')
#         links.append('https://seekingalpha.com/' + url)
#     return links


def extract_content(soup):
    for meta in soup.find_all('meta', {'name': "description"}):
        return htmlparser.unescape(meta['content']).encode('utf-8')

if __name__ == '__main__':
    items = []
    with open('/Users/zezhen/Dropbox/leetcode/all.csv') as fin:
        for line in fin:
            url,difficulty,number,acceptance,solution = line.strip().split(',')
            if url == 'url': continue

            soup = load_page(url, True)
            content = extract_content(soup)
            prefix = "%s%s_" % (difficulty[0].lower(),number)
            article = get_article_name(url, 'py', prefix)
            with open(article, 'w') as f:
                f.write("'''\n")
                f.write(url + "\n")
                if solution != "undefined":
                    f.write(solution + "\n")
                # f.write(acceptance + "\n\n")
                f.write(content)
                f.write("'''\n")