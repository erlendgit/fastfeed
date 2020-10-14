import redis, pickle

from settings import settings


class FastfeedStore:
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

    def store(self, key, value, ex=None):
        self.db.set(key, pickle.dumps(value), ex=ex)

    def expired(self, key):
        return self.db.ttl(key) < 1