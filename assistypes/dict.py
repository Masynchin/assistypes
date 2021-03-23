class AttributedDict(dict):
    def __getattr__(self, attr):
        if isinstance(value := self[attr], dict):
            return AttributedDict(value)
        return value

    def __setattr__(self, attr, value):
        super().__setitem__(attr, value)

    def __delattr__(self, attr):
        super().__delitem__(attr)

    def __repr__(self):
        return "%s(%s)" % (self.__class__.__name__, super().__repr__())
