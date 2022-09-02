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

## Swagger

*master*

- https://ot-nemoto-convert-api.onrender.com/api/v1/ui/

*develop*

- https://ot-nemoto-convert-api.fly.dev/api/v1/ui/
