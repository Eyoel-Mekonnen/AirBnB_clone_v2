#!/usr/bin/python3
"""New Engine DataBase Storage."""
from sqlalchemy import create_engine
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity
from sqlalchemy.orm import sessionmaker, scoped_session, relationship
from sqlalchemy.orm.session import object_session


class DBStorage:
    """Class DB storage Created."""
    __engine = None
    __session = None

    def __init__(self):
        """Instance Creation."""
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}/{}"
                                      .format(getenv("HBNB_MYSQL_USER"),
                                              getenv("HBNB_MYSQL_PWD"),
                                              getenv("HBNB_MYSQL_HOST"),
                                              getenv("HBNB_MYSQL_DB")),
                                      pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Fetche Data from the tables."""
        class_map = {
                     'State': State,
                     'City': City,
                     'User': User,
                     'Place': Place,
                     'Review': Review,
                     'Amenity': Amenity
        }
        dic_of_tables = {}
        if cls is None:
            for cls_name, cls_obj in class_map.items():
                table_instances = self.__session.query(cls_obj).all()
                for instance in table_instances:
                    key = cls_name + "." + str(instance.id)
                    dic_of_tables[key] = instance
        else:
            if isinstance(cls, str):
                cls = class_map.get(cls)
            if cls:
                table_instances = self.__session.query(cls).all()
                for instance in table_instances:
                    key = cls.__name__ + "." + str(instance.id)
                    dic_of_tables[key] = instance
        return dic_of_tables

    def new(self, obj):
        """Add the object to current database session."""
        if object_session(obj) and object_session(obj) != self.__session:
            self.__session.add(obj)
        self.__session.add(obj)

    def save(self):
        """Commit all change to database."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete from current database session"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ Create Tables in the database create database session."""
        Base.metadata.create_all(self.__engine)
        session_fact = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fact)
        self.__session = Session()
