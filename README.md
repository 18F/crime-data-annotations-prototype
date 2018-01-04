# Crime data annotations CMS prototype

## Purpose

To test an idea/data model for UCR annotations and a system that would enable the folks at CJIS to maintain the dataset. The data model is inspired/lifted from [18f/crime-data-api#567](https://github.com/18F/crime-data-api/issues/567).

## Running the project

This project relies on `docker-compose`, so make sure that is installed. After cloning down the repo and moving to the project root directory, run the following:

1. `docker-compose run web python manage.py migrate` (this should handle setting up the environment)
1. `docker-compose run web python manage.py loadinitialdata`
1. `docker-compose up`
1. In another shell to keep ^^ running, `docker-compose run web python manage.py createsuperuser` and follow the prompts
1. View the admin interface at [http://0.0.0.0:8000/admin](http://0.0.0.0:8000/admin)
