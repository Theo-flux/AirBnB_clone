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

## The console:
1. create your data model
2. manage (create, update, destroy, etc) objects via a console / command interpreter
3. store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine
![server-side(storage engine)]()
