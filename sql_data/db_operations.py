import datetime
import os

# should be global based on moment circumstances
global PATH
PATH = "magnus/sql_data/"

class templates():

    def __init__(self):
        super(templates, self).__init__()

    def datetime_template(datetime_list_template):

        created_date = datetime.date.today()
        datetime_list_template.append("Database updated at " + str(created_date))

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

    def save_activity(self, db_name):

        db_template = templates()

        datetime_list_template = []
        templates.datetime_template(datetime_list_template)

        filelog = open(PATH + db_name + "/" + db_name + "_logfile.txt", "a")
        filelog.write(str(datetime_list_template) + '\n')
        filelog.close()
