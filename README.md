# AirBnB_clone

AirBnB clone is an ALX project to build an application similar tothe popular Airbnb. This application will be completed in milestones (steps) and each step will link to a concept:

## Files and Directories
- [models](./models):
This directory contains all classes used for the entire project. A class, called "model" in a OOP project is the representation of an object/instance.

- [tests](./tests):
This directory contains all unit tests.

- [console.py](./console.py):
console.py file is the entry point of our command interpreter

- [models/base_model.py](./models/base_model.py):
This file is the base class of all our models. It contains common elements:
	- attributes: id, created_at and updated_at
	- methods: save() and to_json()

- [models/engine](./models/engine):
This directory contains all storage classes (using the same prototype). For the moment, it contains onlt the [file_storage.py](./models/engine/file_storage.py) file.

## Storage
Persistency is really important for a web application. It means: every time your program is executed, it starts with all objects previously created from another execution. Without persistency, all the work done in a previous execution won’t be saved and will be gone.

In this project, you will manipulate 2 types of storage: file and database. For the moment, you will focus on file.

Why separate “storage management” from “model”? It’s to make your models modular and independent. With this architecture, you can easily replace your storage system without re-coding everything everywhere.

You will always use class attributes for any object. Why not instance attributes? For 3 reasons:
	- Provide easy class description: everybody will be able to see quickly what a model should contain (which attributes, etc…)
	- Provide default value of any attribute
	- In the future, provide the same model behavior for file storage or database storage

## How can I store my instances?


## The console:
1. create your data model
2. manage (create, update, destroy, etc) objects via a console / command interpreter
3. store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
![server-side(storage engine)]()
