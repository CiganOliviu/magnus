import os

class db_operations():

    def __init__(self):
        super(db_operations, self).__init__()

    def select(self, db_object):

        for value in db_object.dataset:
            print(value)

    def insert(self, db_object, value):

        db_object.dataset.append(value)

    def update(self, db_object, selection_attribute, old_data, insertion_attribute, new_data):

        for value in db_object.dataset:
            if value[selection_attribute] == old_data:
                value[insertion_attribute] = new_data

    def delete(self, db_object, selection_attribute, old_data, to_remove_data):

        for value in db_object.dataset:
            if value[selection_attribute] == old_data:
                del(db_object.dataset[to_remove_data - 1])
