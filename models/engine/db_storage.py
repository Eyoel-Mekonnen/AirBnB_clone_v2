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
        tables = [State, City, User, Place, Review, Amenity]
        table_instances = []
        dic_of_tables = {}
        if cls is None:
            for table in tables:
                table_instances.extend(self.__session.query(table).all())
            for table in table_instances:
                key = table.__class__.__name__ + "." + str(table.id)
                dic_of_tables[key] = table
        else:
            if isinstance(cls, str):
                cls = globals()[cls]
            table_instance = self.__session.query(cls).all()
            for table in table_instance:
                key = table.__class__.__name__ + "." + str(table.id)
                dic_of_tables[key] = table
            if '_sa_instance_state' in dic_of_tables:
                del dic_of_tables['_sa_instance']
        return dic_of_tables

    def new(self, obj):
        """Add the object to current database session."""
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
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
