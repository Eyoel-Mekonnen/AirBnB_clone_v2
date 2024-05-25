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
        #print("I am here first")
        list_of_classes = ["Amenity", "State", "User", "Place", "Review", "City"]
        dict_of_objects = {}
        if cls is None:
            #print("I am none")
            for key, value in FileStorage.__objects.items():
                dict_of_objects[key] = value
        else: 
            if isinstance(cls, str) and cls in list_of_classes:
                #print("Cls name here")
                #print("I am not none")
                cls = globals().get(cls)
            else:
                #print("I am not an object")
                pass
            #print("{} I was here".format(cls))
                if cls:
                    for key, value in FileStorage.__objects.items():
                        if isinstance(value, cls):
                            dict_of_objects[key] = value
        #print("dict_of_objects:", dict_of_objects)
        #print(dict_of_objects)
        return dict_of_objects

    def new(self, obj):
        """Adds new object to storage dictionary"""
        object_id = obj.__class__.__name__ + "." + getattr(obj, "id")
        FileStorage.__objects[object_id] = obj
        #print(obj)

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
            #print("Loaded data:", json_file)
        except FileNotFoundError:
            pass
        except json.JSONDecodeError as e:
            print(f"JSON decode error: {e}, initializing empty storage.")
        try:
            for key, value in json_file.items():
                #print("Am here")
                cls_name = key.split(".")[0]
                #print(cls_name)
                #print("trying to print class name")
                cls_object = globals().get(cls_name)
                value.pop('__class__', None)
                #if cls_object:
                #print(cls_object)
                obj_creation = cls_object(**value)
                #print("I am a New Object Created")
                self.new(obj_creation)
                #print("I am reloaded")
                #print("Obj_creation {}".format(obj_creation))
        except:
            pass

    def close(self):
        """Calls reload method to desrialize objects"""
        self.reload()
