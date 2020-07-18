<!-- markdownlint-disable MD033 MD041 MD013 -->
<table align="center"><tr><td align="center" width="9999">

<img width="300" src="frontend/static/images/logo.png">

# Django-vue-spa-template

Used for SPA (single-page application) applications

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE.md)
[![Code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg)](https://github.com/prettier/prettier)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

</td></tr></table>

- [:snake: Quickstart](#snake-quickstart)
- [:file_cabinet: Backend](#file_cabinet-backend)
- [:computer: Frontend](#computer-frontend)

## :scroll: TODO List

- [ ] Kubernatus file
- [ ] Jenkinsfile
- [ ] Gitlab ci file
- [ ] Документация
- [ ] Cache string setting
- [ ] Cache django setting
- [ ] Add vagrant file
- [ ] Add docker dev files
- [ ] Move docker file in .config folder
- [ ] Move Jenkinsfile in .config folder
- [ ] Django logging

<!-- - [ ] Integration Celery if need
- [ ] Integration kombu if need
- [ ] Integration Yosun if need -->

## :snake: Quickstart

- [:twisted_rightwards_arrows: Dependency](#twisted_rightwards_arrows-dependency)
- [:hammer_and_wrench: Development](#hammer_and_wrench-development)
- [:shield: Production](#shield-production)
- [:file_folder: Project structure](#file_folder-project-structure)
- [:arrow_forward: Make commands](#arrow_forward-make-commands)

### :twisted_rightwards_arrows: Dependency

- python - 3.7 or higher
- nodejs - 12.15 or higher
- vue cli - 4.1.1 or higher ([install](https://cli.vuejs.org/ru/guide/installation.html))
- poetry - 1.0 or higher ([install](https://python-poetry.org/docs/#installation))
- yarn ([install](https://classic.yarnpkg.com/en/docs/install/))
- make

### :hammer_and_wrench: Development

1. `make install` - install all packages, init .env file if not exist and migrate database (for debug)
2. `make run` - run dev servers

### :shield: Production

...

### :file_folder: Project structure

📦 project  
┣ 📂 .config  
┃ ┣ 📂 docker  
┃ ┃ ┗ 📜 nginx.conf  
┃ ┣ 📜 gunicorn.service  
┃ ┣ 📜 gunicorn.socket  
┃ ┣ 📜 nginx.conf  
┃ ┗ 📜 robots.txt  
┣ 📂 backend  
┣ 📂 frontend  
┣ 📂 public  
┃ ┣ 📂 keys  
┃ ┣ 📂 logs  
┃ ┣ 📂 media  
┃ ┗ 📂 static  
┣ 📜 .dockerignore  
┣ 📜 .editorconfig  
┣ 📜 .env.example  
┣ 📜 .eslintrc.js  
┣ 📜 .gitignore  
┣ 📜 .prettierrc  
┣ 📜 .pylintrc  
┣ 📜 babel.config.js  
┣ 📜 docker-compose.yml  
┣ 📜 Dockerfile  
┣ 📜 Jenkinsfile  
┣ 📜 LICENSE.md  
┣ 📜 Makefile  
┣ 📜 package.json  
┣ 📜 poetry.toml  
┣ 📜 postcss.config.js  
┣ 📜 pyproject.toml  
┣ 📜 README.md  
┣ 📜 setup.cfg  
┗ 📜 vue.config.js

- `.config` - configuration folder for project
  - `docker` - configuration folder for docker
    - `nginx.conf` - configuration file nginx for docker
  - `robots.txt` - file that contains site indexing options for search engine robots
- `backend` - backend folder ([see more](#backend))
- `frontend` - frontend folder ([see more](#frontend))
- `public`
  - `keys` - folder for ssl keys file (jwt keys, https certificate)
  - `logs` - folder for log application and log nginx
  - `media` - folder for project media files
  - `static` - folder for project static files (command collectstatic copy files here)
- `.dockerignore` - file allows you to exclude files from the context Docker
- `.editorconfig` - file helps maintain consistent coding styles for multiple developers working on the same project across various editors and IDEs
- `.env.example` - file that contains environment variables (**NOT REMOVE PARAMETERS**)
- `.eslintrc.js` - configuration file for ESLint
- `.gitignore` - file allows you to exclude files from the context git
- `.prettierrc` - configuration file for Prettier
- `.pylintrc` - configuration file for PyLint
- `babel.config.js` - configuration file for Babel
- `docker-compose.yml` - file for deploy in docker compose
- `Dockerfile` - file for build docker image
- `Jenkinsfile` - configuration file for Jenkins
- `LICENSE.md` - file license for project
- `Makefile` - file for make utility
- `package.json` - **package list file for frontend**
- `poetry.toml` - configuration file for Poetry
- `postcss.config.js` - configuration file for PostCSS
- `pyproject.toml` - **package list file for backend**
- `README.md` - file readme for project
- `setup.cfg` - configuration file for flake8
- `vue.config.js` - configuration file for webpack(vue cli)

### :arrow_forward: Make commands

- `make migrate` - synchronizes the database state with the current set of models and migrations
- `make clear` - clear `public/static` folder and remove `static/dist` folder
- `make run-django-server` - run django dev server
- `make run-webpack-server` - run webpack dev server
- `make open-localhost` - open localhost:8000 in default webbrowser
- `make install` - install all packages, init .env file if not exist and migrate database (for debug)

```bash
poetry install --no-root
yarn
poetry run task initconfig --debug
@make migrate
```

- `make install-prod` - install all packages, init .env file if not exist (for production)

```bash
poetry install --no-root
yarn
poetry run task initconfig
```

- `make run` - run dev servers and open localhost:8000 in default webbrowser

```bash
@make -j 3 run-django-server run-webpack-server open-localhost
```

- `make build` - build js/sass, copy to `public/static` and migrate database

```bash
yarn build
poetry run task collectstatic
@make migrate
```

- `make deploy` - build js/sass, copy to `public/static`, migrate database, restart gunicorn and restart nginx

```bash
@make build
systemctl restart gunicorn
systemctl restart nginx
```

- `make docker-run` - create docker volumes and up docker containers

```bash
poetry run task dockervolumes
docker-compose up
```

## :file_cabinet: Backend

- [:file_folder: Backend structure](#file_folder-backend-structure)
- [:battery: Backend packages](#battery-backend-packages)
- [:iphone: Default apps](#iphone-default-apps)
- [:gear: Settings](#gear-settings)
- [:arrow_forward: Commands](#arrow_forward-commands)

### :file_folder: Backend structure

📦 backend  
 ┣ 📂 apps  
 ┃ ┣ 📂 api  
 ┃ ┃ ┗ 📂 auth  
 ┃ ┣ 📂 core  
 ┃ ┃ ┣ 📂 api  
 ┃ ┃ ┣ 📂 main  
 ┃ ┃ ┗ 📂 utils  
 ┣ 📂 config  
 ┃ ┣ 📂 settings  
 ┃ ┃ ┣ 📂 base  
 ┃ ┃ ┃ ┣ 📜 apps.py  
 ┃ ┃ ┃ ┣ 📜 environment.py  
 ┃ ┃ ┃ ┗ 📜 middlewares.py  
 ┃ ┃ ┣ 📂 components  
 ┃ ┃ ┃ ┣ 📜 auth.py  
 ┃ ┃ ┃ ┣ 📜 constance.py  
 ┃ ┃ ┃ ┣ 📜 email.py  
 ┃ ┃ ┃ ┣ 📜 explorer.py  
 ┃ ┃ ┃ ┣ 📜 internationalization.py  
 ┃ ┃ ┃ ┣ 📜 logging.py  
 ┃ ┃ ┃ ┣ 📜 paths.py  
 ┃ ┃ ┃ ┣ 📜 rest_framework.py  
 ┃ ┃ ┃ ┗ 📜 static.py  
 ┃ ┃ ┣ 📂 environments  
 ┃ ┃ ┃ ┣ 📜 common.py  
 ┃ ┃ ┃ ┣ 📜 development.py  
 ┃ ┃ ┃ ┗ 📜 production.py  
 ┃ ┃ ┗ 📜 custom.py  
 ┃ ┣ 📜 urls.py  
 ┃ ┗ 📜 wsgi.py  
 ┣ 📂 fixtures  
 ┗ 📜 manage.py

...

### :battery: Backend packages

**Packages**:

- [django-cleanup](https://github.com/un1t/django-cleanup) - Automatically deletes files for FileField, ImageField and subclasses
- [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks) - Tweak the form field rendering in templates, not in python-level form definitions
- [django-settings-export](https://github.com/jakubroztocil/django-settings-export) - Often it is needed to make some of your Django project's settings accessible from within templates. This app provides a simple mechanism for doing just that.
- [django-webpack-loader](https://github.com/owais/django-webpack-loader) - Use webpack to generate your static bundles without django's staticfiles or opaque wrappers.
- [djangorestframework](https://www.django-rest-framework.org/) - Django REST framework is a powerful and flexible toolkit for building Web APIs.
- [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses. This allows in-browser requests to your Django application from other origins.
- [drf-yasg](https://github.com/axnsan12/drf-yasg) - Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.
- [arrow](https://arrow.readthedocs.io/en/latest/) - Arrow is a Python library that offers a sensible and human-friendly approach to creating, manipulating, formatting and converting dates, times and timestamps.
- [django-import-export](https://github.com/django-import-export/django-import-export) - Django application and library for importing and exporting data with included admin integration.
- [django-constance](https://github.com/jazzband/django-constance) - A Django app for storing dynamic settings in pluggable backends (Redis and Django model backend built in) with an integration with the Django admin app.
- [django-environ](https://github.com/joke2k/django-environ) - Allows you to use Twelve-factor methodology to configure your Django application with environment variables.
- [gunicorn](https://github.com/benoitc/gunicorn) - Python WSGI HTTP Server for UNIX
- [mysqlclient](https://github.com/PyMySQL/mysqlclient-python) - MySQL database adapter for the Python programming language
- [psycopg2](https://github.com/psycopg/psycopg2) - PostgreSQL database adapter for the Python programming language
- [djangorestframework-simplejwt](https://github.com/davesque/django-rest-framework-simplejwt) - JSON Web Token authentication plugin for the Django REST Framework.
- [pillow](https://python-pillow.org/) - PIL is the Python Imaging Library.
- [django-sql-explorer](https://github.com/groveco/django-sql-explorer) - Quickly write and share SQL queries in a simple, usable SQL editor, preview the results in the browser, share links, download CSV, JSON, or Excel files (and even expose queries as API endpoints, if desired), and keep the information flowing.
- [django-storages](https://github.com/jschneier/django-storages) - Collection of custom storage backends for Django.
- [django-etc](https://github.com/idlesign/django-etc) - Tiny stuff for Django that won't fit into separate apps.
- [django-rest-multiple-models](https://github.com/MattBroach/DjangoRestMultipleModels) - View (and mixin) for serializing multiple models or querysets in Django Rest Framework

**Dev packages**:

- [pylint](https://github.com/PyCQA/pylint) - Python static code analysis tool which looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.
- [django-debug-toolbar](https://github.com/jazzband/django-debug-toolbar) - The Django Debug Toolbar is a configurable set of panels that display various debug information about the current request/response and when clicked, display more details about the panel's content.
- [autopep8](https://github.com/hhatto/autopep8) - A tool that automatically formats Python code to conform to the PEP 8 style guide.
- [django-extensions](https://github.com/django-extensions/django-extensions) - Django Extensions is a collection of custom extensions for the Django Framework.
- [pylint-django](https://github.com/PyCQA/pylint-django) - Pylint plugin for improving code analysis for when using Django

### :iphone: Default apps

...

### :gear: Settings

...

### :arrow_forward: Commands

- `poetry run task manage` - wrapper `python manage.py` command ([see more](https://docs.djangoproject.com/en/3.0/ref/django-admin/))
- `poetry run task clear` - clear `public/static` folder and remove `static/dist` folder
- `poetry run task dumpdata` -
- `poetry run task migrate` - synchronizes the database state with the current set of models and migrations ([see more](https://docs.djangoproject.com/en/3.0/ref/django-admin/#migrate))
- `poetry run task server` - run django dev server ([see more](https://docs.djangoproject.com/en/3.0/ref/django-admin/#runserver))
- `poetry run task loaddata` -
- `poetry run task startapp` -
- `poetry run task initconfig` - generate .env file
  - `--debug` - option generate file for development
- `poetry run task dockervolumes` - create dockervolumes dirs
- `poetry run task makemigrations` - creates new migrations based on the changes detected to your models ([see more](https://docs.djangoproject.com/en/3.0/ref/django-admin/#makemigrations))
- `poetry run task createsuperuser` - create superuser django ([see more](https://docs.djangoproject.com/en/3.0/ref/django-admin/#createsuperuser))
- `poetry run task collectstatic` - copy static to `public/static` ([see more](https://docs.djangoproject.com/en/3.0/ref/django-admin/#collectstatic))
- `poetry run task gunicorn` - run gunicorn server

## :computer: Frontend

- [:file_folder: Frontend structure](#file_folder-frontend-structure)
- [:card_file_box: Js structure description](#card_file_box-js-structure-description)
- [:paintbrush: Sass structure description](#paintbrush-sass-structure-description)
- [:battery: Frontend packages](#battery-frontend-packages)

### :file_folder: Frontend structure

📦 frontend  
 ┣ 📂 js  
 ┃ ┣ 📂 components  
 ┃ ┃ ┣ 📜 App.vue  
 ┃ ┃ ┣ 📜 Child.vue  
 ┃ ┃ ┣ 📜 Example.vue  
 ┃ ┃ ┗ 📜 index.js  
 ┃ ┣ 📂 lang  
 ┃ ┃ ┣ 📜 en.json  
 ┃ ┃ ┗ 📜 ru.json  
 ┃ ┣ 📂 layouts  
 ┃ ┃ ┗ 📜 default.vue  
 ┃ ┣ 📂 middleware  
 ┃ ┃ ┣ 📜 admin.js  
 ┃ ┃ ┣ 📜 auth.js  
 ┃ ┃ ┣ 📜 locale.js  
 ┃ ┃ ┗ 📜 staff.js  
 ┃ ┣ 📂 pages  
 ┃ ┃ ┣ 📂 auth  
 ┃ ┃ ┃ ┗ 📜 login.vue  
 ┃ ┃ ┣ 📂 errors  
 ┃ ┃ ┃ ┗ 📜 404.vue  
 ┃ ┃ ┗ 📜 home.vue  
 ┃ ┣ 📂 plugins  
 ┃ ┃ ┣ 📜 axios.js  
 ┃ ┃ ┣ 📜 i18n.js  
 ┃ ┃ ┗ 📜 index.js  
 ┃ ┣ 📂 router  
 ┃ ┃ ┣ 📜 index.js  
 ┃ ┃ ┗ 📜 routes.js  
 ┃ ┣ 📂 store  
 ┃ ┃ ┣ 📂 modules  
 ┃ ┃ ┃ ┣ 📜 auth.js  
 ┃ ┃ ┃ ┗ 📜 lang.js  
 ┃ ┃ ┣ 📜 index.js  
 ┃ ┃ ┗ 📜 mutation-types.js  
 ┃ ┣ 📂 utils  
 ┃ ┃ ┗ 📜 include.js  
 ┃ ┗ 📜 app.js  
 ┣ 📂 sass  
 ┃ ┣ 📂 abstracts  
 ┃ ┃ ┣ 📜 \_functions.sass  
 ┃ ┃ ┣ 📜 \_index.sass  
 ┃ ┃ ┣ 📜 \_mixins.sass  
 ┃ ┃ ┗ 📜 \_variables.sass  
 ┃ ┣ 📂 base  
 ┃ ┃ ┣ 📜 \_base.sass  
 ┃ ┃ ┣ 📜 \_fonts.sass  
 ┃ ┃ ┗ 📜 \_index.sass  
 ┃ ┣ 📂 components  
 ┃ ┃ ┗ 📜 \_index.sass  
 ┃ ┣ 📂 layout  
 ┃ ┃ ┣ 📜 \_footer.sass  
 ┃ ┃ ┣ 📜 \_header.sass  
 ┃ ┃ ┗ 📜 \_index.sass  
 ┃ ┣ 📂 pages  
 ┃ ┃ ┣ 📜 \_home.sass  
 ┃ ┃ ┗ 📜 \_index.sass  
 ┃ ┣ 📂 themes  
 ┃ ┃ ┣ 📜 \_default.sass  
 ┃ ┃ ┗ 📜 \_index.sass  
 ┃ ┣ 📂 vendors  
 ┃ ┃ ┗ 📜 \_index.sass  
 ┃ ┗ 📜 app.sass  
 ┣ 📂 static  
 ┃ ┣ 📂 dist  
 ┃ ┣ 📂 documents  
 ┃ ┣ 📂 fonts  
 ┃ ┗ 📂 images  
 ┗ 📂 templates  
 ┃ ┣ 📂 admin  
 ┃ ┃ ┗ 📜 base_site.html  
 ┃ ┣ 📂 components  
 ┃ ┃ ┗ 📜 noscript.html  
 ┃ ┣ 📜 app.html  
 ┃ ┗ 📜 base.html

### :card_file_box: Js structure description

...

### :paintbrush: Sass structure description

...

### :battery: Frontend packages

...

## :copyright: License

MIT. See [LICENSE](LICENSE.md) for more details.
