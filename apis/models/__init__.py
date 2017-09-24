from mongoengine import connect

from apis.settings import Config


# Establish a connection to the database.
print(Config.MONGO_MASTER_URL)
connect(Config.MONGO_DATABASE)


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
