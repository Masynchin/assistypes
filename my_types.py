# LISTS

class StructuredList(list):
	def __init__(self, lst):
		super().__init__(lst)

	def resize(self, size: tuple):
		new_lst = self._create_empty_list(size)

		for i, elem in enumerate(self.get_linear()):
			indexes = self._get_position(i, size)
			row = new_lst[indexes[0]]
			
			for index in indexes[1:-1]:
				row = row[index]
			row[indexes[-1]] = elem

		self[:] = new_lst

	def _create_empty_list(self, size):
		if len(size) == 1:
			return [None for i in range(size[0])]
		if len(size) == 2:
			return [[None] * size[1] for i in range(size[0])]
		elif len(size) > 2:
			return [self._create_empty_list(size[1:]) for i in range(size[0])]

	def _get_position(self, number, size):
		size = self._get_size(size)

		position = []
		for n in size:
			i = number // n
			position.append(i)
			number -= n * i
		position.append(number)

		return tuple(position)

	def _get_size(self, size):
		position = []

		new_size = []
		for i in range(1, len(size)):
			new_size.append(mul(size[i:]))
		return tuple(new_size)

	def get_linear(self):
		return self._get_linear(self)

	def _get_linear(self, elem):
		if isinstance(elem, list):
			if len(elem) > 1:
				return self._get_linear(elem[0]) + self._get_linear(elem[1:])
			else:
				return self._get_linear(elem[0])
		return [elem]


# RANGES

class MutableRange:
	def __init__(self, *args):
		if (ln := len(args)) > 3 or ln == 0:
			raise ValueError('the class requires one, two or three arguments')
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

		self.i = self.start

	def __iter__(self):
		return self.range()
	
	def range(self):
		while self.i < self.stop:
			yield self.i
			self.i += self.step

	def __repr__(self):
		return f'{self.__class__.__name__}(start={self.start}, stop={self.stop}, step={self.step})'

	def change_start(self, new_start):
		self.start = new_start

		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')

	def change_step(self, new_step):
		self.step = new_step

		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')

	def change_stop(self, new_stop):
		self.stop = new_stop

		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')

	def add_to_start(self, diff):
		self.start += diff

		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')

	def add_to_step(self, diff):
		self.step += diff

		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')

	def add_to_stop(self, diff):
		self.stop += diff

		if (self.stop - self.start) / self.step < 0:
			raise ValueError('infinite range')


class FloatRange(MutableRange):
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

		self.i = self.start
		self.step = float(self.step)

	# метод __iter__ определён в родительском классе
	# метод __repr__ определён в родительском классе


class RoundRange(FloatRange):
	def __init__(self, *args):
		super().__init__(*args)
		self.float_len = len(str(self.step).split('.')[1])

	def range(self):
		while self.i < self.stop:
			yield self.i
			self.i += self.step
			self.i = round(self.i, self.float_len)

	# метод __iter__ определён в родительском классе
	# метод __repr__ определён в родительском классе


# OTHER FUNCTIONS

def mul(seq):
	result = 1
	for n in seq:
		result *= n
	return result