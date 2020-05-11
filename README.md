# Production
[SimpleNoteAPI!](https://simplenoteapi.herokuapp.com/api/v1/notes/)

# Technology used

    python3
    django3
    django rest framework
    django-environ

# Project setup

    git clone git@github.com:Tushant/drf_sample.git
    cd drf_sample
    mkvirtualenv <virtual_environment_name>
    pip install -r requirements/local.txt
    createdb <database_name> -U <username> --password <password> (e.g createdb drf_sample_dev -U tushant --password tushant)
    export DJANGO_READ_DOT_ENV_FILE=True (this will read all variables from .env)
    python manage.py migrate
    python manage.py createsuperuser (if want to create an admin account)
    python manage.py runserver

# To Run the tests

`python manage.py test notes.tests`

# API Endpoints

    api/v1/notes/ - list all the notes
    api/v1/notes/ - create a note
    api/v1/notes/:noteId/ - retrieve a specific note
    api/v1/notes/:noteId/ - update a specific note
    api/v1/notes/:noteId/ - delete a specific note

### post a note

local - ` curl -X POST -d "title=Deep Dive Django&description=I am loving django&is_published=True" http://127.0.0.1:8000/api/v1/notes/ `

remote - ` curl -X POST -d "title=Deep Dive Django&description=I am loving django&is_published=True" https://simplenoteapi.herokuapp.com/api/v1/notes/ `

### list all the notes

local - ` curl -X GET http://127.0.0.1:8000/api/v1/notes/ `

remote - `curl -X GET https://simplenoteapi.herokuapp.com/api/v1/notes/`


### get particular note

local - ` curl -X GET http://127.0.0.1:8000/api/v1/notes/1/ `

remote - `curl -X GET https://simplenoteapi.herokuapp.com/api/v1/notes/1/`


### update particular note

local - ` curl -X PUT -d "title=Deep Dive Django&description=Django is awesome&is_published=True" http://127.0.0.1:8000/api/v1/notes/1 `

remote - ` curl -X PUT -d "title=Deep Dive Django&description=Django is awesome&is_published=True" https://simplenoteapi.herokuapp.com/api/v1/notes/1/ `

### delete note

local - ` curl -X DELETE http://127.0.0.1:8000/api/v1/notes/1/ `

remote - ` curl -X DELETE https://simplenoteapi.herokuapp.com/api/v1/notes/1/ `
