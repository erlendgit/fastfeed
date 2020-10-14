import redis, pickle

from settings import settings


class FastfeedDb:
    """ To clear all keys:
        $ redis-cli flushall
    """

    _instance = None

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls(port=settings.redis_port)
        return cls._instance

    def __init__(self, port):
        self.db = redis.Redis(port=port)

    def load(self, key):
        return pickle.loads(self.db.get(key))

    def store(self, key, value):
        self.db.set(key, pickle.dumps(value))
        self.db.persist(key)

    def expired(self, key):
        return not self.db.exists(key)

    def clear_all(self):
        self.db.flushall()
