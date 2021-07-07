from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-graphql-accounts',
    version='0.12',
    author='Mahdi Asadzadeh',
    author_email='mahdi.asadzadeh.programing@gmail.com',
    description='A GraphQl API for user signup and authentication using email addresses',
    keywords=[
        'django', 'python', 'graphql', 'GraphQL', 'django-graphone', 'Graphone', 'api',
        'auth', 'authentication', 'email', 'user', 'username', 'python-graphone',
        'registration', 'signup', 'login', 'logout', 'password', 'django-registration',
        'django-email-as-username'
    ],
    url='https://github.com/mahdi-asadzadeh/django-graphql-accounts',
    download_url='https://github.com/mahdi-asadzadeh/django-graphql-accounts',
    packages=['django_graphql_accounts'],
    include_package_data=True,
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'Django>=2.2.8,<=3.1,<=3.2',
        'graphene-django>=2.15' ,
        'celery>=5.1',
        'django-graphql-jwt>=0.3',
        'redis>=3.5'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django :: 2.2',
        'Framework :: Django :: 3.0',
        'Framework :: Django :: 3.1',
        'Framework :: Django :: 3.2',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
