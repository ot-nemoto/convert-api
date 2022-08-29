# convert-api

変換API

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

### bcrypt

*Generate Hash*

```sh
curl -XPOST https://ot-nemoto-convert-api.onrender.com/api/v1/bcrypt/generate-hash \
    -H 'Content-Type: application/json' \
    -d '{"password":"Passw0rd","cost":10,"version":"2a"}'
```

*Check Password*

```sh
curl -XPOST https://ot-nemoto-convert-api.onrender.com/api/v1/bcrypt/check-password \
    -H 'Content-Type: application/json' \
    -d '{"password":"Passw0rd","hash":"$2a$10$UrC0NWxz.FHzGLrIp5PMcesTzs9YD6qSPw8yy4ZupM3YeoEswt4sq"}'
```

## Swagger

- https://ot-nemoto-convert-api.onrender.com/api/v1/ui/
