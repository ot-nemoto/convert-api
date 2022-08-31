# -*- coding: utf-8 -*-

from urllib.parse import quote, unquote

def encode(**kwargs):
    string = kwargs.get('body').get('string')
    return {
        'origin': string,
        'result': quote(string),
    }

def decode(**kwargs):
    string = kwargs.get('body').get('string')
    return {
        'origin': string,
        'result': unquote(string),
    }
