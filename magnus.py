import click
import os

# should be global based on moment circumstances
global PATH
PATH = "magnus/sql_data/"

class databaseOperations():

    def __init__(self):
        super(databaseOperations, self).__init__()

    @click.command()
    @click.option('--database_name', default='Database name')
    def create_database(database_name):

        create_database = open(PATH + str(database_name) + '.py', "w+")

        create_database.close()

    @click.command()
    @click.option('--database_name', default='Database name')
    def delete_database(database_name):

        if (os.path.exists(PATH + str(database_name) + '.py')):
            os.remove(PATH + str(database_name) + '.py')

class magnus_command_line_interface_system(object):

    def __init__(self):
        super(magnus_command_line_interface_system, self).__init__()

    @click.group()
    def magnus_command_line_interface():
        pass

    magnus_command_line_interface.add_command(databaseOperations.create_database)
    magnus_command_line_interface.add_command(databaseOperations.delete_database)

if __name__ == '__main__':
    magnus_command_line_interface_system.magnus_command_line_interface()
