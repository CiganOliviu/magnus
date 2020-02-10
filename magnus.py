import click
import os

# should be global based on moment circumstances
global PATH
PATH = "magnus/sql_data/"

class templates():

    def __init__(self):
        super(templates, self).__init__()

    def database_template(file_object, database_name):

        file_object.write("import sys\n\n")
        file_object.write("sys.path.append('magnus/sql_data/')\n\n")
        file_object.write("from db_operations import db_operations\n\n")
        file_object.write("class " + str(database_name) + "():\n\n")
        file_object.write("\tdef __init__(self):\n")
        file_object.write("\t\tsuper(" + str(database_name) + ", self).__init__()\n\n")
        file_object.write("\tdataset = [\n")
        file_object.write("\t\t{},\n")
        file_object.write("\t\t{},\n")
        file_object.write("\t]\n")

class databaseOperations(templates):

    def __init__(self):
        super(databaseOperations, self).__init__()

    @click.command()
    @click.option('--database_name', default='Database name')
    def create_database(database_name):

        if not(os.path.exists(PATH + str(database_name) + "\\")):
            os.mkdir(PATH + str(database_name) + "\\")

        database = open(PATH + str(database_name) + "\\" + str(database_name) + '.py', "w+")
        templates.database_template(database, database_name)
        database.close()

    @click.command()
    @click.option('--database_name', default='Database name')
    def delete_database(database_name):

        if os.path.exists(PATH + str(database_name) + "\\" + str(database_name) + '.py'):
            os.remove(PATH + str(database_name) + "\\" + str(database_name) + '.py')

class magnus_command_line_interface_system():

    def __init__(self):
        super(magnus_command_line_interface_system, self).__init__()

    @click.group()
    def magnus_command_line_interface():
        pass

    magnus_command_line_interface.add_command(databaseOperations.create_database)
    magnus_command_line_interface.add_command(databaseOperations.delete_database)

if __name__ == '__main__':
    magnus_command_line_interface_system.magnus_command_line_interface()
