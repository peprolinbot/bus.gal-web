# bus.gal-web

<img src="buses/static/buses/logo.svg" alt="bus.gal-telegram" width=200/>

[![status-badge](https://woodpecker.peprolinbot.com/api/badges/peprolinbot/bus.gal-web/status.svg)](https://woodpecker.peprolinbot.com/peprolinbot/bus.gal-web)

An unofficial clone of [bus.gal](https://www.bus.gal/) made with [Django](https://www.djangoproject.com/) that serves you info about the buses from the Galician Public Transport Network. 

You can find an instance hosted by myself on [galibus.peprolinbot.com](https://galibus.peprolinbot.com).

Data is obtained through  [bus.gal-api](https://github.com/peprolinbot/bus.gal-api).

## 🔧 How to Install

### 🐳 Docker (Recommended)

If you want to host your own instance of the web, it is as easy as a docker container.

So the command is:
 
```bash
docker run -d --name bus.gal-web \
    -e DJANGO_ALLOWED_HOSTS="example.com" \
    -e DJANGO_SECRET_KEY="changemetosomethingsecureplease" \
    -p 8080:80 \
    quay.io/peprolinbot/bus.gal-web:latest
```

Or you can also use the `docker-compose.yml` file at the root of this repo. You know: `docker-compose up -d`.

#### Environment Variables

| Name                     | Description |
|--------------------------|-------------|
| `DJANGO_DEBUG` (bool)    | Whether to enable Django's debug mode. Leave it false in production. _(Default: False)_
| `DJANGO_ALLOWED_HOSTS` | Space-separated list of host/domain names that Django can serve. Not needed in debug mode. _(Default: "")_
| `DJANGO_SECRET_KEY`  |  The key to securing signed data. Must be randomly generated and kept secure. _(Default: "django-insecure-(krka)#p79n81tjf-)dy9f1!k^4*j&+qf5_eurt7)o%8%mr1ce")_

_**Note🗒️:**_ DJANGO_DEBUG is true only when the variable's value is the string "true" (not case sensitive)

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