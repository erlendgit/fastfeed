from app.FastfeedDb import FastfeedDb


class TempStore:
    def __init__(self, dataKey: str):
        self.dataKey = dataKey

    def __call__(self, f):
        def calling_function(*args, **kwargs):
            db = FastfeedDb.instance()
            if db.expired(self.dataKey):
                db.store(self.dataKey, f(*args, **kwargs))
            return db.load(self.dataKey)

        return calling_function

    @classmethod
    def clear_all(cls):
        FastfeedDb.instance().clear_all()
