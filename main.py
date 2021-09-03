import os
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
import shutil
from termcolor import colored

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

            if ph == True:
                print_help()
                ph = False
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
                os.system('PAUSE')

            elif command[0] == 'out':
                output = command[1] + '.pdf'
        
            elif command[0] == 'load':
                filenames = list_of_files(dir)

            elif command[0] == 'quit':
                break

            elif command[0] == 'help':
                ph = True

        except: pass

columns, rows = shutil.get_terminal_size()

lobby()



    
