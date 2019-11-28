'''
Created by  linzero 2019/11/28 17:01
'''

def is_isbn_or_key(word):
    """
    :param word:
    :return:
    """
    isbn_or_key = 'key'
    if len(word) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = word.replace('-', '')
    if '-' in word and len(short_q) == 10 and word.replace('-', '').isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key