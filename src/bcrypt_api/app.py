# -*- coding: utf-8 -*-

import connexion

options = {"swagger_ui": True}
app = connexion.FlaskApp(__name__, specification_dir='openapi/', options=options)
app.add_api('bcrypt_api.yaml')

if __name__ == "__main__":
    app.run(port=8080)
