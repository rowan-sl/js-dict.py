class jsdict:
    """dictionary that can be acsessed by doing foo.bar instead of foo[bar], similarly how dicts/objects work in javascript.\n
    WARNING! if you put a class in this with a key that matches one of the existing functions (eg: 'clear'),\n
    it will be overridden with the realevent builtin function if you acsess it in the special way\n
    (eg: foo.bar) instead of the normal dict way (eg: foo["bar"]\n"""

    def __init__(self, dictionary: dict) -> None:
        self.__dict__: dict = dictionary

    def __repr__(self) -> str:
        return self.__dict__.__repr__()

    def __hash__(self) -> int:
        return self.__dict__.__hash__

    def __lt__(self, other):
        return self.__dict__.__lt__(other)

    def __le__(self, other):
        return self.__dict__.__le__(other)

    def __eq__(self, other):
        return self.__dict__.__eq__(other)

    def __ne__(self, other):
        return self.__dict__.__ne__(other)

    def __gt__(self, other):
        return self.__dict__.__gt__(other)

    def __ge__(self, other):
        return self.__dict__.__ge__(other)

    def __iter__(self):
        return self.__dict__.__iter__()

    def __or__(self, other):
        return self.__dict__.__or__(other)

    def __ror__(self, other):
        return self.__dict__.__ror__(other)

    def __ior__(self, other):
        return self.__dict__.__ior__(other)

    def __len__(self):
        return self.__dict__.__len__()

    def __getitem__(self, key):
        return self.__dict__.__getitem__(key)

    def __setitem__(self, key, value):
        return self.__dict__.__setitem__(key, value)

    def __delitem__(self, key):
        return self.__dict__.__delitem__(key)

    def __contains__(self, item):
        return self.__dict__.__contains__(item)

    def __reversed__(self):
        return self.__dict__.__reversed__()

    def __format__(self, format_spec: str) -> str:
        return self.__dict__.__format__(format_spec)

    def __getattribute__(self, name: str):
        # overrides
        overrides = [
            "get",
            "setdefault",
            "pop",
            "popitem",
            "keys",
            "items",
            "values",
            "update",
            "fromkeys",
            "clear",
            "copy",
        ]
        if name in overrides:
            return self.__dict__.__getattribute__(name)
        return object.__getattribute__(self, name)