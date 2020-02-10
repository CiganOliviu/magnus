import os

class db_operations():

    def __init__(self):
        super(db_operations, self).__init__()

    def select(self, db_object):

        for value in db_object.dataset:
            print(value)

    def insert(self, db_object, value):

        db_object.dataset.append(value)
    
    def update(self, db_object, attribute_for_editing):
        
        pass
