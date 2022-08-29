# -*- coding: utf-8 -*-

import connexion

options = { 'swagger_ui': True }
app = connexion.FlaskApp(__name__, specification_dir='.', options=options)
app.add_api('openapi.yaml')

if __name__ == "__main__":
    app.run(port=8080)
