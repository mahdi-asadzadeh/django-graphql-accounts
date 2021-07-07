django-graphql-accounts
=====================


`django-graphql-accounts` is a Django/Python application that provides a GraphQL interface for user signup and authentication.  Email addresses are used for authentication, rather than usernames.  Because the authentication user model is based on Django's `AbstractBaseUser` and is itself abstract, the model can be extended without the need for additional database tables.  JWT authentication allows the API to be accessed from a variety of front ends, including Django, React and AngularJS clients, and iOS and Android mobile apps.


Features
--------

- API endpoints for signup, signup email verification, login, logout, password reset, password reset verification, password change, email change, and user detail.
- Extensible abstract user model.
- Perform password confirmation and other client-side validation on the front end for a better user experience.
- JWT authentication.
- Useing celery for send registrations email (optional).
- Useing redis for save registrations token (optional).


Installation
------------

`django-graphql-accounts` is available on the Python Package Index (PyPI) at https://pypi.org/project/django-graphql-accounts/.

Install `django-graphql-accounts` using one of the following techniques.

- Use pip.  Note that particular versions of Django and the Django graphone may be installed.

```
pip install django-graphql-accounts
```

- Download the .tar.gz file from PyPI and install it yourself.
- Download the [source from Github](http://github.com/mahdi-asadzadeh/django-graphql-accounts) and install it yourself.

If you install it yourself, also install [Django](https://www.djangoproject.com/), the [Django Graphone](https://docs.graphene-python.org/projects/django/en/latest/), and [Django Graphql JWT](https://django-graphql-jwt.domake.io/en/latest/index.html), and [Redis Python](https://pypi.org/project/redis/)

Usage
-----

Create a Django project, if you haven't already. For example,

```python
django-admin startproject mysite
```

In the `settings.py` file of your project, include `django_graphql_accounts` and `` in `INSTALLED_APPS`. Set the authentication scheme for the Django Graphql JWT.

```python
mysite/settings.py
----

INSTALLED_APPS = [
	...
	'django_graphql_accounts',
	...
]

GRAPHENE = {
	"SCHEMA": "config.schema.schema",
	'MIDDLEWARE': [
		'graphql_jwt.middleware.JSONWebTokenMiddleware',
	],
}

AUTHENTICATION_BACKENDS = [
	'graphql_jwt.backends.JSONWebTokenBackend',
	'django.contrib.auth.backends.ModelBackend',
]
```
<!-- 
Optionally, you may add an `AUTH_EMAIL_VERIFICATION` setting to specify whether to enable email verification for new users on account registration/signup. Setting this to `False` will automatically verify newly created users. -->
In the `schemas.py` file of your project, Add queries and mutations to the class of your schemas. For example,
```python
mysite/schemas.py
----

import graphene
from graphql_jwt import mutations
from django_graphql_accounts.mutations import AccountsMutation
from django_graphql_accounts.queries import AccountsQuery


class Query(AccountsQuery, ... , graphene.ObjectType):
    pass


class Mutation(AccountsMutation, ... , graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)

```



Create a Django application for your user data.  For example,

```python
python manage.py startapp accounts
```

In the `models.py` file of your application, extend `EmailAbstractUser`, add custom fields, and assign `objects` to `EmailUserManager()`.  For example,

```python
accounts/models.py
----

from django.db import models
from django_graphql_accounts.models import EmailUserManager, EmailAbstractUser

class MyUser(EmailAbstractUser):
	# Custom fields
	date_of_birth = models.DateField('Date of birth', null=True, blank=True)

	# ........, etc

	# Required
	objects = EmailUserManager()
```

In the `settings.py` file of your project, Set `AUTH_USER_MODEL` to the class of your user model.  For example,

```python
mysite/settings.py
----

INSTALLED_APPS = [
	...
	'django_graphql_accounts',
	'accounts',
	...
]

AUTH_USER_MODEL = 'accounts.MyUser'

```

In the `admin.py` file of your project, extend `EmailUserAdmin` to add your custom fields.  For example,

```python
accounts/admin.py
----

from django.contrib import admin
from django.contrib.auth import get_user_model


User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

```


Create the database tables with Django's `makemigrations`, `migrate`, and create a superuser with `createsuperuser`.

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```


Check your setup by starting a Web server on your local machine:

```python
python manage.py runserver
```

When users signup or reset their password, they will be sent an email with a link and verification code.  Include email settings as environment variables or in your project's `settings.py` file.  For example,

```python
mysite/settings.py
----

# Email settings
# https://docs.djangoproject.com/en/3.1/topics/email/
# https://docs.djangoproject.com/en/3.1/ref/settings/#email-host

import os

EMAIL_BACKEND = config('EMAIL_BACKEND')
MAILER_EMAIL_BACKEND = config('MAILER_EMAIL_BACKEND')
EMAIL_HOST = config('EMAIL_HOST')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_PORT = config('EMAIL_PORT')
EMAIL_USE_SSL = config('EMAIL_USE_SSL')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL')

EMAIL_FROM = os.environ.get('AUTHEMAIL_DEFAULT_EMAIL_FROM') or '<YOUR DEFAULT_EMAIL_FROM HERE>'
EMAIL_BCC = os.environ.get('AUTHEMAIL_DEFAULT_EMAIL_BCC') or '<YOUR DEFAULT_EMAIL_BCC HERE>'

EMAIL_HOST = os.environ.get('AUTHEMAIL_EMAIL_HOST') or 'smtp.gmail.com'
EMAIL_PORT = os.environ.get('AUTHEMAIL_EMAIL_PORT') or 587
EMAIL_HOST_USER = os.environ.get('AUTHEMAIL_EMAIL_HOST_USER') or '<YOUR EMAIL_HOST_USER HERE>'
EMAIL_HOST_PASSWORD = os.environ.get('AUTHEMAIL_EMAIL_HOST_PASSWORD') or '<YOUR EMAIL_HOST_PASSWORD HERE>'
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False
```
