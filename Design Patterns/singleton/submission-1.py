class Singleton:

    instance = None
    # In python consider this method as the 'getInstance'
    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(Singleton)
        return cls.instance

    def getValue(self) -> str:
        return instance.val

    def setValue(self, value: str):
        instance.val = value