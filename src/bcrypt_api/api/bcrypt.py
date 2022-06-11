# -*- coding: utf-8 -*-

import bcrypt

def generate_hash(**kwargs):
    password = kwargs.get('body').get('password')
    cost = kwargs.get('body').get('cost')
    #salt = bcrypt.gensalt(rounds=cost, prefix=b'2a')
    return {
        'password': password,
        'hash': bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=cost)).decode()
    }

def check_password(**kwargs):
    password = kwargs.get('body').get('password')
    hashed = kwargs.get('body').get('hash')
    return {
        'result': bcrypt.checkpw(password.encode(), hashed.encode()),
        'password': password,
        'hash': hashed,
    }
