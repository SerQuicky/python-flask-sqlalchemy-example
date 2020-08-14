# Flask-SQLAlchemy-Project 

This repository is an example project for the webframework Flask in combination with the object-relational mapping framework SQLAlchemy. It contains the basic implementation
of a REST-API with a SQL database as its persistant data storage.

## Core-Packages that are used

* ``flask`` *(Webframework for the REST-API)*
* ``flask-sqlalchemy`` *(ORM abstraction layer)*
* ``flask-marshmallow`` and marshmallow-sqlalchemy *(object serialization/deserialization library)*

## Project structure

The project uses a specific structure, the top-level dictionary with the two main scripts *(app.py and tables.py)*. In the entities folder are all the different kinds of 
tables that the project uses. For every table exists one model, route and scheme file. The model-file contains the entity-model, the route-file contains all the API-routes 
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

## Build process

The repository uses ``pipenv`` for the 

