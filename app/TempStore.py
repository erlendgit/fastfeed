tempstore = dict()


class TempStore:
    def __init__(self, dataKey: str):
        self.dataKey = dataKey

    def __call__(self, f):
        def calling_function(*args, **kwargs):
            if not tempstore.get(self.dataKey):
                tempstore[self.dataKey] = f(*args, **kwargs)
            return tempstore.get(self.dataKey)

        return calling_function
