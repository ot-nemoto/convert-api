# bcrypt-api

bcryptでパスワードハッシュ化、パスワードとパスワードハッシュのチェックを行うAPI

## Environment

```sh
python --version
  # Python 3.8.13
```

## Run locally

*Install libraries*

```sh
pip install -r requirements.txt
```

```sh
python src/convert_api/app.py
```

*by gunicorn*

```sh
gunicorn app:app --chdir src/convert_api/
```

## Usage

### パスワードハッシュ化

```sh
curl -XPOST https://ot-nemoto-convert-api.onrender.com/api/v1/bcrypt/generate-hash \
    -H 'Content-Type: application/json' \
    -d '{"password":"Passw0rd","cost":10,"version":"2a"}'
```

### パスワードとパスワードハッシュのチェック

```sh
curl -XPOST https://ot-nemoto-convert-api.onrender.com/api/v1/bcrypt/check-password \
    -H 'Content-Type: application/json' \
    -d '{"password":"Passw0rd","hash":"$2a$10$UrC0NWxz.FHzGLrIp5PMcesTzs9YD6qSPw8yy4ZupM3YeoEswt4sq"}'
```

### Swagger

- https://ot-nemoto-convert-api.onrender.com/api/v1/ui/
