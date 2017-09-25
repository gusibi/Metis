import random

from bson.objectid import ObjectId
from mongoengine import connect
from weixin.helper import safe_char, smart_bytes

from apis.settings import Config

# Establish a connection to the database.
connect(Config.MONGO_DATABASE)


def generation_objectid():
    random_str = ''.join(random.sample(safe_char[:-4], 12))
    # return random_str
    return ObjectId(smart_bytes(random_str))


class ObjectModel(object):

    def __init__(self, *args, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    @classmethod
    def object_from_dictionary(cls, entry):
        # make dict keys all strings
        if entry is None:
            return ""
        entry_str_dict = dict([(str(key), value) for key, value in entry.items()])
        return cls(**entry_str_dict)

    def __repr__(self):
        return str(self)

    def __str__(self):
        return self.__unicode__()
