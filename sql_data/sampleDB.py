import sys

sys.path.insert(0, 'db_operations/')

from db_operations.db_operations import db_operations

class sampleDB():

	def __init__(self):
		super(sampleDB, self).__init__()

	dataset = [
		{},
		{},
	]
