from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker, scoped_session
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import Base



class DBStorage:
    """doc"""

    __engine = None
    __session = None
    def __init__(self):
        """doc"""
        db_user = getenv("HBNB_MYSQL_USER")
        db_passwd = getenv("HBNB_MYSQL_PWD")
        db_host = getenv("HBNB_MYSQL_HOST")
        db_name = getenv("HBNB_MYSQL_DB")
        test = False if getenv("HBNB_ENV") == "test" else True

        EStr = f"mysql+mysqldb://{db_user}:{db_passwd}@{db_host}/{db_name}"
        self.__engine = create_engine(EStr, pool_pre_ping=True)
        if test is True:
            Base.metadata.drop_all(self.__engine)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(
                sessionmaker(bind=self.__engine, expire_on_commit=False)
                )
        self.__session = Session


    def all(self, cls=None):
        """doc"""
        available_cls = [User, Place, State, City, Amenity, Review]
        content ={}
        if cls:
            for obj in self.__session.query(cls).all():
                name = obj.__class__.__name__
                key = "{}.{}".formart(name, obj.id)
                content[key] = obj
        else:
            for cls in available_cls:
                for obj in self.__session.query(cls).all():
                    name = obj.__class__.__name__
                    key = "{}.{}".formart(name, obj.id)
                    content[key] = obj
        return content
    
    def new(self, obj=None):
        """doc"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """doc"""
        self.__session.commit()


    def delete(self, obj=None):
        """doc"""
        if obj:
            self.__session.delete(obj)

    def close(self):
        """doc"""
        self.__session.remove()


