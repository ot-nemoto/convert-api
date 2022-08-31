# -*- coding: utf-8 -*-

import html

def escape(**kwargs):
    string = kwargs.get('body').get('string')
    return {
        'origin': string,
        'result': html.escape(string),
    }

def unescape(**kwargs):
    string = kwargs.get('body').get('string')
    return {
        'origin': string,
        'result': html.unescape(string),
    }
