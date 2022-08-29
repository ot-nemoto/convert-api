# -*- coding: utf-8 -*-

import bcrypt

def generate_hash(**kwargs):
    password = kwargs.get('body').get('password')
    cost = kwargs.get('body').get('cost', 10)
    version = kwargs.get('body').get('version', '2a')
    salt = bcrypt.gensalt(rounds=cost, prefix=version.encode())
    return {
        'password': password,
        'hash': bcrypt.hashpw(password.encode(), salt).decode(),
    }

def check_password(**kwargs):
    password = kwargs.get('body').get('password')
    hashed = kwargs.get('body').get('hash')
    return {
        'result': bcrypt.checkpw(password.encode(), hashed.encode()),
        'password': password,
        'hash': hashed,
    }
