# Django books API.
It is a books [API](https://still-mountain-79365.herokuapp.com/).
Also you can view [REST-API](https://still-mountain-79365.herokuapp.com/api/)

Available online:

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/Sicret89/google_books_api/graphs/commit-activity)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Sicret89/google_books_api/issues)

# Running the app

There are two ways to run this app - locally or using docker-compose.
First, clone this repo to a directory of your choice. The directory containing this README will be the work directory for all of the CLI commands afterwards.

## Docker

### Requirements

Install Docker for the OS of your choice.

**Make sure to put every variable and its value in a separate line!**

Make sure Docker backend is running, then:
```sh
$ docker-compose build
$ docker-compose up -d
```

If those commands successfully complete, try out your composed instance at

http://localhost:8000/

or Django REST:

http://localhost:8000/api

If you can see the BrowsableAPI interface, congrats! You have a running instance of Django Book Catalogue API.

## Locally

### Configuration
Before running the Django app, you have to rename .env_dev to .env

### Requirements
1. Clone this project then cd to the folder.
2. Please virtual environment en for this project and activate like so:

```sh
$ python -m venv <venv-name>
$ source <venv-name>/bin/activate
```

3. Install the requirements to the virutal or global Python environment:

```sh
$ pip install -r requirements.txt
```

4. Then, go back to the project directory, and perform migrations on the database:

```sh
$ python manage.py migrate
```
### Running the server

If this command runs without errors, great! Now, try to run the server. You can either use the built-in webserver:

```sh
$ python manage.py runserver
```

If those commands successfully complete, try out your composed instance at

http://localhost:8000/
or for REST
http://localhost:8000/api

If you can see the BrowsableAPI interface, congrats! You have a running instance of Django Book Catalogue API.

# Running tests

To run the tests, use:

```sh
$ python manage.py test
```

To run tests in Docker environment, connect to the shell of running instance and run that same command.

 # Chosen technologies

 ## Database
 SQLite3 - for development

 PostgreSQL - Pairs well with Django, also it's the db I'm most familiar with

 ## Additional packages
 Requests - Standard choice to perform HTTP requests for external API's

 Django-filter - Easy to use class-based filtering and ordering for viewsets

 Gunicorn - Popular choice for production WSGI servers

 WhiteNoise - Pairs well with Django, allows to serve static files easier in WSGI apps

 Bootstrap - Library that focuses on simplifying the development and make web pages resposive easier.

