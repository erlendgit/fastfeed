from app.FastfeedDb import FastfeedDb


class TempStore:
    def __init__(self, dataKey: str, expire):
        self.dataKey = dataKey
        self.expire = expire

    def __call__(self, f):
        def calling_function(*args, **kwargs):
            db = FastfeedDb.instance()
            if db.expired(self.dataKey):
                db.store(self.dataKey, f(*args, **kwargs), ex=self.expire)
            return db.load(self.dataKey)

        return calling_function
