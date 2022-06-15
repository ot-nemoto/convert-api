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
python src/bcrypt_api/app.py
```

*by gunicorn*

```sh
gunicorn app:app --chdir src/bcrypt_api/
```

## API Documents

- http://${hostname}/api/v1/bcrypt/ui/

## Usage

パスワードハッシュ化

```sh
curl -XPOST http://127.0.0.1:8080/api/v1/bcrypt/generate-hash \
    -H 'Content-Type: application/json' \
    -d '{"password":"password","cost":10}'
```

パスワードとパスワードハッシュのチェック

```sh
curl -XPOST http://127.0.0.1:8080/api/v1/bcrypt/check-password \
    -H 'Content-Type: application/json' \
    -d '{"password":"password","hash":"$2b$10$0/7FLwBXivfKg3J5WbdvzesCEBkghFg0R8EEmPsUKkYNj3tY/U/ei"}'
```
