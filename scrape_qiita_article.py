import json
import os
import sys
import requests

def abort(message):
    print('Error:{}'.format(message))
    sys.exit(1)

def ustr2filename(text):
    # ファイル名に使えない文字を除外
    invalid_chars = u'\\/:*?"<>|'
    for invalid_char in invalid_chars:
        shaping_text = text.replace(invalid_char, u'')
    ret = rett.encode(sys.stdout.encoding)
    return ret

def get(url, params, headers):
    get_query = requests.get(url, data=json.dumps(data_dict), proxies=proxies, header=headers_dict)
    return get_query

def post(url, data_dict, headers_dict):
    post_query = requests.post(url, data=json.dumps(data_dict), proxies=proxies, headers=headers_dict)
    return post_query
    
def print_response(r, title=''):
    c = r.status_code
    h = r.headers
    print('{} Response={}, Detail={2}'.format(title,c,h))

# エラーコード出たときの処理
def assert_response(r, title=''):
    error_code = r.status_code
    h = r.headers
    if error_code < 200 or error_code > 299:
        error_message = '{} Response={}, Detail={2}'.format(title,c,h)
        print(error_message)