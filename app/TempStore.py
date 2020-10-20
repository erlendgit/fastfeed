import hashlib
import logging

from app.FastfeedDb import FastfeedDb


logger = logging.getLogger('tempstore')


class TempStore:
    def __init__(self, dataKey: str):
        self.key = dataKey

    def __call__(self, f):
        self.key = self.key or '.'.join([f.__globals__['__name__'], f.__qualname__])

        def calling_function(*args, **kwargs):
            key = self.get_data_key(*args[1:], **kwargs)
            db = FastfeedDb.instance()
            if db.expired(key):
                logger.debug("MISS - %s" % key)
                db.store(key, f(*args, **kwargs))
            else:
                logger.debug("HIT - %s" % key)
            return db.load(key)

        return calling_function

    def get_data_key(self, *args, **kwargs):
        if len(args) > 0 or len(kwargs) > 0:
            try:
                return "%s_%s" % (
                    self.key, hashlib.sha256((str(args) + str(kwargs)).encode()).digest().hex()
                )
            except TypeError as e:
                raise e
        return self.key

    @classmethod
    def clear_all(cls):
        FastfeedDb.instance().clear_all()
