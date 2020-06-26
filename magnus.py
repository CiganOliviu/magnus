import click
import datetime
import os

# should be global based on moment circumstances
global PATH
PATH = "\magnus\sql_data\\"

class templates():

    def __init__(self):
        super(templates, self).__init__()

    def database_template(file_object, database_name):

        file_object.write("class " + str(database_name) + "():\n\n")
        file_object.write("\tdef __init__(self):\n")
        file_object.write("\t\tsuper(" + str(database_name) + ", self).__init__()\n\n")
        file_object.write("\tdataset = [\n")
        file_object.write("\t\t{},\n")
        file_object.write("\t\t{},\n")
        file_object.write("\t]\n")

    def datetime_template(datetime_list_template):

        created_date = datetime.date.today()
        datetime_list_template.append("Database created at " + str(created_date))

class databaseOperations(templates):

    def __init__(self):
        super(databaseOperations, self).__init__()

    @click.command()
    @click.option('--database_name', default='Database name')
    def create_database(database_name):

        if not(os.path.exists(PATH + str(database_name) + "//")):
            os.mkdir(PATH + str(database_name) + "//")

        database = open(PATH + str(database_name) + "//" + str(database_name) + '.py', "w+")
        templates.database_template(database, database_name)
        database.close()

        datetime_list_template = []
        templates.datetime_template(datetime_list_template)

        datetime_log_file = open(PATH + str(database_name) + "//" + str(database_name) + '_logfile.txt', "w+")
        datetime_log_file.write(str(datetime_list_template) + '\n')
        datetime_log_file.close()

    @click.command()
    @click.option('--database_name', default='Database name')
    def delete_database(database_name):

        if os.path.exists(PATH + str(database_name) + "//" + str(database_name) + '.py'):
            os.remove(PATH + str(database_name) + "//" + str(database_name) + '.py')

    @click.command()
    @click.option('--database_name', default='Database name')
    @click.option('--script_name', default='Script name')
    def create_script(database_name, script_name):

        if os.path.exists(PATH + str(database_name) + "//"):

            database = open(PATH + str(database_name) + "//" + str(script_name) + '.py', "w+")
            templates.database_template(database, script_name)
            database.close()

class magnus_command_line_interface_system():

    def __init__(self):
        super(magnus_command_line_interface_system, self).__init__()

    @click.group()
    def magnus_command_line_interface():
        pass

    magnus_command_line_interface.add_command(databaseOperations.create_database)
    magnus_command_line_interface.add_command(databaseOperations.delete_database)
    magnus_command_line_interface.add_command(databaseOperations.create_script)

if __name__ == '__main__':
    magnus_command_line_interface_system.magnus_command_line_interface()
