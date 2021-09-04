import os
import shutil
import time

from PyPDF2.generic import NullObject

from modules import *

def lobby():
    output = 'resultado.pdf'
    ph = False
    while True:
        try:
            os.system('cls')
            print(columns * '-')
            try:
                print(f' diretorio > {dir}')
                print(f' resultado > {output}')
                print(columns * '-')
                print('> Ordem das Paginas do PDF <'.center(columns))
                print_list_of_files(filenames)
            except: 
                print(f' diretorio >')
                print(f' resultado >')

            print(columns * '-')

            print_help()
            print(columns * '-')

            command = input(' > ').split()

            if command[0] == 'd':
                dir = command[1]
                filenames = list_of_files(command[1])

            elif command[0] == 's':
                aux = filenames[int(command[1])]
                filenames[int(command[1])] = filenames[int(command[2])]
                filenames[int(command[2])] = aux

            elif command[0] == 'i':
                aux = filenames[int(command[1])]
                filenames.remove(aux)
                filenames.insert(int(command[2]), aux)

            elif command[0] == 'r':
                create_pdfs(filenames, dir)
                merge_pdfs(filenames, output, dir)
                delete_files(filenames, dir)
                time.sleep(1)

            elif command[0] == 'o':
                output = command[1] + '.pdf'
        
            elif command[0] == 'l':
                filenames = list_of_files(dir)

            elif command[0] == 'q':
                break
    
        except: pass

columns, rows = shutil.get_terminal_size()

lobby()



    
