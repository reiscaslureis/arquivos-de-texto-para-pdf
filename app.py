import os
import shutil
import time
from termcolor import colored

from modules import *

def print_filenames_list(filenames):
    for i in range(len(filenames)):
        if filenames[i][1] == False:
            color = 'cyan'
        else: color = 'green'

        if i < 10:
            print(colored(f' [0{i}] {filenames[i][0]}', color))
        else: print(colored(f' [{i}] {filenames[i][0]}', color))

    print(columns * '-')

def set_special_file(filenames, x):
    if filenames[x][1] == True:
        filenames[x][1] = False
    else: filenames[x][1] = True

def insert(filenames, x, y):
    aux = filenames[x]
    filenames.pop(x)
    filenames.insert(y, aux)


def print_help():
    with open('help.txt', 'r') as h:
        print(h.read())

    print(columns * '-')

def lobby():
    output = 'output'
    while True:
        global columns
        columns, rows = shutil.get_terminal_size()
        os.system('cls')
        print(columns * '-')
        try:
            print_filenames_list(filenames)
            print_help()
        except: print_help()

        command = input(' > ').split()

        try:
            if command[0] == 'd':
                dir = ''
                for l in range(len(command)):
                    if l == 0:
                        pass
                    else:
                        if l == 1:
                            dir += f'{command[l]}';
                        else: dir += f' {command[l]}';

                filenames = list_of_files(dir)

            elif command[0] == 's':
                set_special_file(filenames, int(command[1]))

            elif command[0] == 'i':
                insert(filenames, int(command[1]), int(command[2]))

            elif command[0] == 'r':
                create_pdfs(filenames, dir)
                merge_pdfs(filenames, output, dir)
                delete_files(filenames, dir)

        except: pass

lobby()







    
