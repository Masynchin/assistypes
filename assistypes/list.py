class StructuredList(list):
    @property
    def size(self):
        return self._get_size(self)

    def _get_size(self, seq):
        if isinstance(seq[0], list):
            return (len(seq),) + self._get_size(seq[0])
        return (len(seq),)

    def resize(self, size):
        if not self.is_linear():
            self[:] = self.get_linear()

        temp = []
        for num in size[:0:-1]:
            for i in range(0, len(self), num):
                temp.append(self[i:i+num])
            self[:] = temp[:]
            temp.clear()

    def is_linear(self):
        for elem in self:
            if isinstance(elem, list):
                return False
        return True

    def get_linear(self):
        while isinstance(self[0], list):
            temp = []
            for elem in self:
                temp.extend(elem)
            self[:] = temp
        return self
