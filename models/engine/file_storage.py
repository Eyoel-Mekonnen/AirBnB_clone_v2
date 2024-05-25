#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        list_of_classes = ["Amenity", "State",
                           "User", "Place", "Review", "City"]
        dict_of_objects = {}
        print("I was here")
        if cls is None:
            for key, value in FileStorage.__objects.items():
                dict_of_objects[key] = value
        else:
            if isinstance(cls, str) and cls in list_of_classes:
                print("I am here")
                cls = globals().get(cls)
            else:
                pass
            if cls:
                for key, value in FileStorage.__objects.items():
                    if isinstance(value, cls):
                        dict_of_objects[key] = value
        return dict_of_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        object_id = obj.__class__.__name__ + "." + getattr(obj, "id")
        FileStorage.__objects[object_id] = obj

    def save(self):
        """Saves storage dictionary to file"""
        json_dict = {}
        for key, value in FileStorage.__objects.items():
            json_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(json_dict))

    def delete(self, obj=None):
        """Deletes an object from __objects."""
        if obj is None:
            return
        object_id = obj.__class__.__name__ + "." + getattr(obj, "id")
        if object_id in FileStorage.__objects:
            del FileStorage.__objects[object_id]
            self.save()

    def reload(self):
        """Loads storage dictionary from file"""

        json_file = {}
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                json_file = json.loads(f.read())
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}, initializing empty storage.")
        try:
            for key, value in json_file.items():
                cls_name = key.split(".")[0]
                cls_object = globals().get(cls_name)
                value.pop('__class__', None)
                obj_creation = cls_object(**value)
                self.new(obj_creation)
        except FileNotFoundError:
            pass

    def close(self):
        """Calls reload method to desrialize objects"""
        self.reload()
