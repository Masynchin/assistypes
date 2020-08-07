# LISTS

class StructuredList(list):
	def __init__(self, lst):
		super().__init__(lst)

	@property
	def size(self):
		return self._get_size(self)

	def _get_size(self, seq):
		if isinstance(seq[0], list):
			return (len(seq), ) + self._get_size(seq[0])
		else:
			return (len(seq), )

	def resize(self, size):
		if not self.is_linear():
			self[:] = self.get_linear()
		temp = []
		for num in size[:0:-1]:
			for i in range(0, len(self), num):
				temp.append(self[i:i+num])
			self[:] = temp[:]
			temp[:] = []

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


# RANGES

class FloatRange:
	def __init__(self, *args):
		if (ln := len(args)) > 3 or ln == 0:
			raise ValueError('need at least one argument')
		elif ln == 1:
			self.start = 0
			self.stop = args[0]
			self.step = 1
		elif ln == 2:
			self.start = args[0]
			self.stop = args[1]
			self.step = 1
		elif ln == 3:
			self.start, self.stop, self.step = args
		
		if self.step == 0:
			raise ValueError("step can't be equal 0")
		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')

		self.start = float(self.start)
		self.i = self.start
		self.step = float(self.step)

	def __iter__(self):
		return self.range()
	
	def range(self):
		if self.start < self.stop:
			while self.i < self.stop:
				yield self.i
				self.i += self.step
		else:
			while self.i > self.stop:
				yield self.i
				self.i += self.step

	def __repr__(self):
		return f'FloatRange(start={self.start}, stop={self.stop}, step={self.step})'


class RoundedRange(FloatRange):
	def __init__(self, *args):
		super().__init__(*args)
		self.float_len = len(str(self.step).split('.')[-1])

	def __iter__(self):
		return self.range()

	def range(self):
		if self.start < self.stop:
			while self.i < self.stop:
				yield self.i
				self.i += self.step
				self.i = round(self.i, self.float_len)
		else:
			while self.i > self.stop:
				yield self.i
				self.i += self.step
				self.i = round(self.i, self.float_len)

	def __repr__(self):
		return (f'RoundRange(start={self.start}, stop={self.stop}, '
				f'step={self.step}, rounded={self.float_len})')
