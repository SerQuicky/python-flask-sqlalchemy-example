# Flask-SQLAlchemy-Project 

This repository is an example project for the webframework ``Flask`` in combination with the object-relational mapping framework ``SQLAlchemy``. It contains the basic implementation of a REST-API with a SQL database as its persistant data storage.

## Core-Packages that are used

* ``flask`` *(Webframework for the REST-API)*
* ``flask-sqlalchemy`` *(ORM abstraction layer)*
* ``flask-marshmallow and marshmallow-sqlalchemy`` *(object serialization/deserialization library)*

## Project structure

The project uses a specific structure, the top-level dictionary has the two main scripts *(app.py and tables.py)*. In the entities folder are all the different kinds of 
tables that the project uses. For each table exists a model-, route- and scheme-file. The model-file contains the entity-model, the route-file contains all the API-routes 
and the database/ORM-Requests, so its basically a Data-Access-Object (DAO) and the scheme is for the serialization/deserialization of the objects. Therefore the project uses
the following structure:

```
├── entities
│   ├── first_entity
│     ├── model.py
│     ├── routes.py
│     ├── scheme.py
│   ├── second_entity
│     ├── model.py
│     ├── routes.py
│     ├── scheme.py
│   └── ...
├── app.py
└── tables.py
```

The advantage of this structure is that all entities are decoupled and compliant with the single-responsibility principle.

## Build process

The repository uses ``pipenv`` for the package management, after the repository checkout ``pipenv install`` should be executed so all the needed packages can be installed.
After this the pipenv-enviorment can be started with ``pipenv shell``.

It is important to set the ``SQLALCHEMY_DATABASE_URI`` before any of the main scripts are used, it is basically the database connector, if it is not set the programm will run
into an error. You can use any SQL based database for this, just set the right connection-settings.

As mentioned, the project contains two main scripts, normally you would start the ``app.py`` for the REST-Service, but firstly all tables should be created, therefore ``python tables.py`` has to be executed. After this execute ``python app.py``, if the console does not show any errors you are good to go!

