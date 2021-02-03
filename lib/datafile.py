# ---------------------------------------------------------------------------
# IMPORT
import os, sys, csv, json, re
from pathlib2 import Path
from datetime import datetime, date

class TextFile(object):
	'''data file getter and setter'''

	def __repr__( self ):
		return '<%s>' % (
			self.__class__.__name__
		)

	def __init__( self, key, path, file ):
		self.key = key
		self.path = path
		self.name = file
		self.ext = file.split('.')[-1]
		self.src = '%s/%s' % (path, file)
		self.data = []
		self.savecount = 0
		# if folder does not exist already
		if os.path.exists(path) == False:
			os.makedirs(path)
		# create files and folders
		Path(self.src).touch(exist_ok=True)

	def save( self, text='' ):
		# append text to text file
		with open( self.src, 'a' ) as textfile:
			textfile.write("\r\n%s" % text)
		# increase the number of words saved
		self.savecount = self.savecount + 1
		return True
