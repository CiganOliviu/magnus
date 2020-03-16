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

    def __get_size(self, dict_db_object) -> str:

        to_count_data = ""

        for value in dict_db_object:
            to_count_data += str(dict_db_object[value])
            to_count_data += "---"

        return to_count_data

    def draw_data_border(self, list_arg):

        compressed_data = self.__get_size(list_arg)

        for i in range(len(list(compressed_data))):
            print("-", end="")

    def draw_file_data_border(self, file_object, list_arg):

        compressed_data = self.__get_size(list_arg)

        for i in range(len(list(compressed_data))):
            file_object.write("-")


class db_operations():

    def __init__(self):
        super(db_operations, self).__init__()

    def select_from_table(self, db_object):

        for value in db_object.dataset:
            print(value)

    def select_specific_data(self, db_object, selected_attribute, value_of_selected_attribute):

        for value in db_object.dataset:
            if value[selected_attribute] == value_of_selected_attribute:
                print(value)

    def insert_in_table(self, db_object, value):

        db_object.dataset.append(value)

    def insert_data_in_file(self, file_name, db_object):

        output_file = open(file_name, "w+")

        for value in db_object.dataset:
            output_file.write(str(value) + "\n")

    def insert_table_in_file(self, file_name, db_object):
        output_file = open(file_name, "w+")

        for value in db_object.dataset:
            db_template = templates()

            db_template.draw_file_data_border(output_file, value)
            output_file.write('\n')
            output_file.write("|")
            for key in value:
                output_file.write(" ")
                output_file.write(str(value[key]) + " ")
                output_file.write("|")
            output_file.write('\n')
            db_template.draw_file_data_border(output_file, value)
            output_file.write('\n')

    def update_in_table(self, db_object, selection_attribute, old_data, insertion_attribute, new_data):

        for value in db_object.dataset:
            if value[selection_attribute] == old_data:
                value[insertion_attribute] = new_data

    def delete_from_table(self, db_object, selection_attribute, old_data, to_remove_data):

        for value in db_object.dataset:
            if value[selection_attribute] == old_data:
                del(db_object.dataset[to_remove_data - 1])

    def describe(self, db_object):

        for value in db_object.dataset:
            db_template = templates()

            db_template.draw_data_border(value)
            print()
            print("|", end="")
            for key in value:
                print(end=" ")
                print(value[key], end=" ")
                print("|", end="")
            print()
            db_template.draw_data_border(value)
            print()

    def save_activity(self, db_name, db_table):

        db_template = templates()

        datetime_list_template = []
        templates.datetime_template(datetime_list_template)

        filelog = open(PATH + db_name + "/" + db_table + "_logfile.txt", "a")
        filelog.write(str(datetime_list_template) + '\n')
        filelog.close()
