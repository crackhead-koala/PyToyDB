from Terminal import *


if __name__ == '__main__':

    terminal = Terminal()

    while True:
        command = input('> ').lower()

        if command == 'create database':
            database_name = input('input name\n> ')
            database_path = input('input path\n> ')
            terminal.create_database(database_name, database_path)

        if command == 'create table':
            database = input('which database?\n> ')
            table_name = input('input table name\n> ')

            terminal.create_table(database, table_name)

        if command == 'exit':
            print('bye.')
            break
