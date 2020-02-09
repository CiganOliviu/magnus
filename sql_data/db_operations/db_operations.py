import os

class db_operations():

    def __init__(self):
        super(db_operations, self).__init__()

    def select(self, db_object):

        for value in db_object.dataset:
            print(value)
