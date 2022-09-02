# -*- coding: utf-8 -*-

import base64

def encode(**kwargs):
    string = kwargs.get('body').get('string')
    return {
        'origin': string,
        'result': base64.encodebytes(string.encode()).decode(),
    }

def decode(**kwargs):
    string = kwargs.get('body').get('string')
    return {
        'origin': string,
        'result': base64.decodebytes(string.encode()).decode(),
    }
