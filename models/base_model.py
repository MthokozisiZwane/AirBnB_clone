#!/usr/bin/python3


import uuid
from datetime import datetime
from .engine.file_storage import storage

"""
 a class that defines all common attributes/methods for other classes
"""


class BaseModel:
    """
    defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        initializing the BaseModel class
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        if not isinstance(value, datetime):
                            value = datetime.strptime(value,
                                                      '%Y-%m-%dT%H:%M:%S.%f')

                    setattr(self, key, value)
            storage.new(self)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns
        -------
        returns a dictionary containing all keys/values
        of __dict__ of the instance

        """
        return {
            'id': self.id,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            '__class__': self.__class__.__name__,
            **self.__dict__
            }
