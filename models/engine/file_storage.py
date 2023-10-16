#!/usr/bin/python3

import json
from datetime import datetime
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

"""
A class to store objects
"""


class FileStorage:
    """
    A class  that serializes instances to a JSON file
    and deserializes a JSON file to instances
    """
    __file_path = "file.json"
    __objects = {"BaseModel": BaseModel, "State": State, "City": City,
                 "Amenity": Amenity, "Place": Place, "Review": Review}

    def all(self):
        """
        a method that returns the dictionary __objects

        Returns
        -------
       dictionary __objects

        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)

        Returns
        -------
        None.

        """
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = self.serialize_object(obj)

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file, default=self.serialize_object)

    def serialize_object(self, obj):

        """
        Serialize an object to a dictionary,
        converting datetime objects.

        Parameters
        ----------
        obj : object
            The object to be serialized.

        Returns
        -------
        dict
            The serialized object as a dictionary.
        """
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, FileStorage):
            return obj.to_dict()
        else:

            return obj.__dict__

    def reload(self):
        """
        deserializes the JSON file to __objects (only if
        the JSON file (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)

        Returns
        -------
        None.

        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = file.read()
                if data:
                    data = json.loads(data)
                for key, obj_dict in data.items():
                    class_name, obj_id = key.split('.')
                    obj = BaseModel(**obj_dict)
                    FileStorage.__objects[key] = obj

        except (FileNotFoundError, json.JSONDecodeError):
            pass
