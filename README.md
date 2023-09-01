# bus.gal-web

<img src="buses/static/buses/img/logo.svg" alt="bus.gal-web" width=200/>

[![Docker Repository on Quay](https://quay.io/repository/peprolinbot/bus.gal-web/status "Docker Repository on Quay")](https://quay.io/repository/peprolinbot/bus.gal-web)

An unofficial clone of [bus.gal](https://www.bus.gal/) made with [Django](https://www.djangoproject.com/) that serves you info about the buses from the Galician Public Transport Network, and as a bonus substitutes the, now deprecated, [XeNovaPing](https://github.com/peprolinbot/xenovaping), and sends you an email when you can get the payback of your trips done with the Xente Nova card (actually any Galician Public Transport card which supports refunds. 

You can find an instance hosted by myself on [galibus.peprolinbot.com](https://galibus.peprolinbot.com).

Data is obtained through  [bus.gal-api](https://github.com/peprolinbot/bus.gal-api).

## 🔧 How to Install

### 🐳 Docker (Recommended)

If you want to host your own instance of the web, it is as easy as a docker container. Check the environment variables below to configure important things, as this example below supposes things like the mail server doesn't use authentication, which isn't realistic.

So the command is:
 
```bash
docker run -d --name bus.gal-web \
    -e DJANGO_ALLOWED_HOSTS="example.com" \
    -e DJANGO_SECRET_KEY="changemetosomethingsecureplease" \
    -e TPGAL_USER="john@example.com" \
    -e TPGAL_PASSWORD="rockyou" \
    -e EMAIL_HOST="127.0.0.1" \
    -e DEFAULT_FROM_EMAIL="xenovaping@example.com" \
    -e EMAIL_BASE_URL="http://example.com" \
    -p 8080:80 \
    -v /data/busgalweb-cfg/db.sqlite3:/app/db.sqlite3
    quay.io/peprolinbot/bus.gal-web:latest
```

Or you can also use the `docker-compose.yml` file at the root of this repo. You know: `docker-compose up -d`.

#### Environment Variables

| Name                     | Description |
|--------------------------|-------------|
| `DJANGO_DEBUG` (bool)    | Whether to enable Django's debug mode. Leave it false in production. _(Default: False)_
| `DJANGO_ALLOWED_HOSTS` | Space-separated list of host/domain names that Django can serve. Not needed in debug mode. _(Default: "")_
| `DJANGO_SECRET_KEY`  |  The key to securing signed data. Must be randomly generated and kept secure. _(Default: "django-insecure-(krka)#p79n81tjf-)dy9f1!k^4*j&+qf5_eurt7)o%8%mr1ce")_
| `STOPS_CACHE_DIR`  |  The place to store the stops cache. This is a [whoosh](https://whoosh.readthedocs.io/) index _(Default: "/tmp/bgw-stops-cache")_
| `GUNICORN_WORKERS`  |  Gunicorn's `--workers` argument _(Default: 3)_
| `GUNICORN_TIMEOUT`  |  Gunicorn's `--timeout` argument _(Default: 30)_
| `TPGAL_USER`  |  User to login to the TPGal API _(Required)_
| `TPGAL_PASSWORD`  |  Password to login to the TPGal API _(Required)_
| `EMAIL_HOST`  |  Smtp server host  _(Default: "localhost")_
| `EMAIL_USE_TLS`  |  _(Default: False)_
| `EMAIL_USE_SSL`  |  _(Default: False)_
| `EMAIL_PORT`  |  _(Default: 25)_
| `EMAIL_HOST_USER`  |   _(Default: "")_
| `EMAIL_HOST_PASSWORD`  |   _(Default: "")_
| `DEFAULT_FROM_EMAIL`  |  Email address used when sending  _(Default: "webmaster@localhost")_
| `EMAIL_BASE_URL`  |  Used for the images and urls in the emails  _(Default: "http://127.0.0.1:8000")_

_**Note🗒️:**_ Booleans are only true when their value is the string "true" (not case sensitive)

_**Note🗒️:**_ EMAIL_USE_TLS/EMAIL_USE_SSL are mutually exclusive, so only set one of those settings to True.

_**Tip💡:**_ You can generate a secret key with `openssl rand -hex 32`

#### Building the image

```bash
git clone https://codeberg.org/peprolinbot/bus.gal-web.git
cd bus.gal-web
docker build -t bus.gal-web .
```

### 💪🏻 Without Docker (for development)

Only use this for development unless you know what you're doing.

```bash
git clone https://codeberg.org/peprolinbot/bus.gal-web.git
cd bus.gal-web
export DJANGO_DEBUG=true
python3 manage.py runserver
```

Please check [Django's documentation](https://docs.djangoproject.com/en/4.1/).

## ⚠️ Disclaimer

This project is not endorsed by, directly affiliated with, maintained by, sponsored by or in any way officially related with la Xunta de Galicia, the bus operators or any of the companies involved in the [bus.gal](https://www.bus.gal/) website and/or the [app](https://play.google.com/store/apps/details?id=gal.xunta.transportepublico).

## ❤️ Credits

- Logo: https://pixabay.com/images/id-2027077/