import os
import shutil
import time

from PyPDF2.generic import NullObject

from modules import *

def lobby():
    output = 'result.pdf'
    ph = False
    while True:
        try:
            os.system('cls')
            print(columns * '-')
            try:
                print(f'directory > {dir}')
                print(f'output > {output}')
                print(columns * '-')
                print('> PDF PAGES ORDER <'.center(columns))
                print_list_of_files(filenames)
            except: 
                print(f'directory >')
                print(f'output >')

            print(columns * '-')

            print_help()
            print(columns * '-')

            command = input(' > ').split()

            if command[0] == 'dir':
                dir = command[1]
                filenames = list_of_files(command[1])

            elif command[0] == 'swap':
                aux = filenames[int(command[1])]
                filenames[int(command[1])] = filenames[int(command[2])]
                filenames[int(command[2])] = aux

            elif command[0] == 'run':
                create_pdfs(filenames, dir)
                merge_pdfs(filenames, output)
                delete_files(filenames)
                time.sleep(1)

            elif command[0] == 'out':
                output = command[1] + '.pdf'
        
            elif command[0] == 'load':
                filenames = list_of_files(dir)

            elif command[0] == 'quit':
                break
    
        except: pass

columns, rows = shutil.get_terminal_size()

lobby()



    
