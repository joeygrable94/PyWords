import os
try:
	from .__init__ import PyDictionary #Python 3
	from .datafile import TextFile
except:
	from __init__ import PyDictionary
	from datafile import TextFile

class Words(PyDictionary):

	HERE = os.path.dirname(os.path.realpath(__file__))

	def __repr__(self):
		return '<%s count="%d" current="%s" definitions="%d">' % (
			__class__.__name__,
			self.count,
			self.current,
			self._countDefinitions()
		)

	def __init__(self):
		self.file = 'words.txt'
		self.src = '%s/%s' % (self.HERE, self.file)
		self.data = self._load()
		self.count = self._getCount()
		self.current = ''
		self.definitions = {}
		self.synonyms = {}
		self.antonyms = {}
		self.mods = 0

	def update(self):
		self.data = self._load()
		self.count = self._getCount()
		print(self)

	def define(self, word):
		defs = None
		try:
			if self._exists(word):
				self.current = word
				self.definitions = self.meaning(word)
				self.synonyms = self.synonym(word)
				self.antonyms = self.antonym(word)
			else:
				raise Exception( 'DoesNotExist', word )
		except Exception:
			if self._add(word):
				return self.define(word)
		finally:
			return self.definitions

	def _add(self, word):
		'''
		check word not already in data
		add word to data src then update
		'''
		if not self._exists(word) and self._save(word):
			return self.update()

	def _exists(self, word):
		# if word is data list
		return True if word in self.data else False

	def _getCount(self):
		# count word list
		return len(self.data)

	def _load(self):
		valid_words = []
		with open(self.src) as word_file:
			valid_words = sorted(set( word_file.read().split() ))
		return valid_words

	def _save(self, text):
		# append text to text file
		with open( self.src, 'a' ) as textfile:
			textfile.write("\r\n%s" % text)
		# increase the number of words saved
		self.mods = self.mods + 1
		return True

	def _countDefinitions(self):
		total = 0
		for lkey in self.definitions.keys():
			total = total + len(self.definitions[lkey])
		return total


