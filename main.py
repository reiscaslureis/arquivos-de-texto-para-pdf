import os
import shutil
import time

from PyPDF2.generic import NullObject

from modules import *

def lobby():
    output = 'resultado.pdf'
    ph = False
    specials = []
    while True:
        try:
            os.system('cls')
            print(columns * '-')
            try:
                print(specials)
                print(f' diretorio > {dir}')
                print(f' resultado > {output}')
                print(columns * '-')
                print('> Ordem das Paginas do PDF <'.center(columns))
                print_list_of_files(filenames, specials)
            except: 
                print(f' diretorio >')
                print(f' resultado > {output}')

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
                
                specials.remove(int(command[1]))
                specials.append(int(command[2]))

            elif command[0] == 'r':
                create_pdfs(filenames, dir, specials)
                merge_pdfs(filenames, output, dir)
                delete_files(filenames, dir)
                time.sleep(1)

            elif command[0] == 'o':
                output = command[1] + '.pdf'
        
            elif command[0] == 'l':
                filenames = list_of_files(dir)

            elif command[0] == 'q':
                break

            elif command[0] == 't':
                if int(command[1]) in specials:
                    specials.remove(int(command[1]))
                else: specials.append(int(command[1]))
    
        except: pass

columns, rows = shutil.get_terminal_size()

lobby()



    
