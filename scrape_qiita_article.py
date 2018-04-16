import json
import os
import sys
import requests

def abort(message):
    print('Error:{}'.format(message))
    sys.exit(1)

def shaping_text(text):
    # ファイル名に使えない文字を除外
    invalid_chars = u'\\/:*?"<>|'
    for invalid_char in invalid_chars:
        shaping_text = text.replace(invalid_char, u'')
    return shaping_text

def get(url, params, headers):
    get_query = requests.get(url, params=params, proxies=proxies, headers=headers)
    return get_query
    
def print_response(query_data, title=''):
    c = query_data.status_code
    h = query_data.headers
    print('{} Response={}, Detail={}'.format(title,c,h))

# エラーコード出たときの処理
def assert_response(query_data, title=''):
    error_code = query_data.status_code
    h = query_data.headers
    if error_code < 200 or error_code > 299:
        error_message = '{} Response={}, Detail={2}'.format(title,c,h)
        print(error_message)

class Article:
    def __init__(self, response_data):
        self._title      = response_data['title']
        self._html_body  = response_data['rendered_body']
        self._md_body    = response_data['body']
        self._tags       = response_data['tags']
        self._created_at = response_data['created_at'] 
        self._updated_at = response_data['updated_at']
        self._url        = response_data['url']
        user             = response_data['user']
        self._userid     = user['id']
        self._username   = user['name']
        
    def save_as_markdown(self):
        title = shaping_text(self._title)
        body  = self._md_body
        filename = '{}.md'.format(title)
        fullpath = os.path.join(MYDIR, filename)
        with open(fullpath, 'w') as f:
            f.write(body)

MYDIR = os.path.abspath(os.path.dirname(__file__)) + '/QiitaArticles'

headers = {
    'content-type'  : 'application/json',
    'charset'       : 'utf-8',
    'Authorization' : 'Bearer {0}'.format('token')
}

url = 'https://qiita.com/api/v2/authenticated_user/items'
params = {
    'page'     : 1,
    'per_page' : 100,
}

qiita_article_data = get(url, params, headers)
assert_response(qiita_article_data)
print_response(qiita_article_data)

items = qiita_article_data.json()
print('{} entries.'.format(len(items)))
for i, item in enumerate(items):
    print('{} saving...'.format(i+1, len(items)))
    article = Article(item)
    article.save_as_markdown()