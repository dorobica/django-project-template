# Django project template

## export settings

before using manage.py export correct settings module:

    export DJANGO_SETTINGS_MODULE=project.settings.[env]

    ./manage.py

## config

config file example:

    [database]
    name: dbname
    user: dbuser
    password: dbpassword

    [secrets]
    secret_key: somelongsecretrandomkey

export config file path:

    export PROJECT_CONFIG_PATH=/path/to/config/file
