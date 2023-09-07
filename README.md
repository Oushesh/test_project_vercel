## The Backend is written in Django and serves to retrieve all
   queries from different social media profiles on several platforms

## Backend goal: convert the ipynb to make different endpoints
   that serve the frontend on Nextjs

##  How to get started: 
    django use 4.0
    * django-admin startproject courtneyryan [courtneyryan is projectname]
    * python manage.py runserver 
    * python manage.py runserver port (8000)
    * python manage.py makemigrations
    * cd courtneyryan --> python manage.py startapp "appname"
    * python manage.py startapp
    * Write your first views to get the views.py convert function to
      html response
    * I usually use supabase and postgresql as database
    * Here 
        -- courtneyOracle: is the django app:
        -- courtneyryan: is the django project.

    * install pip install django-ninja django-ninja to get started.

## Directory Structure:
   * docs -- images for readme.md

## Data is currently under Data folder but will be moved to Supabase
   or PostGreSQL afterwards or s3 afterwards. (next step)

## Currently data sits  on the local server
   
## How to run on Docker? 
   * docker compose up

## Deployment Setup in Heroku:
   * brew tap heroku/brew && brew install heroku
   * heroku login
   * heroku login -i 

## Deployments done on heroku
   Check here: https://devcenter.heroku.com/articles/git
   Currently main branch is ueded for deployments:
   --> git push heroku main

## Tips for Deployment: 
   * python manage.py collectstatic
   * allowed all hosts * in settings.py
   * python manage.py generate_secret_key
   * python manage.py createsuperuser
   * python manage.py changepassword username
   * after defining the models in Data, views for rendering the request: 
     * python manage.py makemigrations && python manage.py migrate
   * 2 settings created:
        -- dev.py and base.py, prod.py for deyploment in different environments.
   * all static files saved in aws s3

## Bugs: No S3 right now: debugging soon. (my account problem)
    --> on aws S3 we will have all the static files saved.

## Posgresql database: 
    *  heroku addons:create heroku-postgresql:hobby-dev or mini which is a bit paid

## setup AWS S3:https://simpleisbetterthancomplex.com/tutorial/2017/08/01/how-to-setup-amazon-s3-in-a-django-project.html
   --> aws to save the collect static files.

## how did I setup this Backend code:   https://www.youtube.com/watch?v=ftpepZo9GSI&t=546s

## Data: now local will be saved on supabase soon
## with all the precomputed embeddings:
## Successful deployment on Heroku

## App
