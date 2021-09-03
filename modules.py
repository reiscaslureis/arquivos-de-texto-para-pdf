import os
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
import shutil
from termcolor import colored

def list_of_files(dir):
    for (dirpath, dirnames, filenames) in os.walk(dir):
        break

    return filenames

def print_list_of_files(filenames):
    for i in range(len(filenames)):
        if i < 10:
            print(colored(f'[0{i}] {filenames[i]}', 'cyan'))
        else: print( colored(f'[{i}] {filenames[i]}', 'cyan'))

def print_help():
    print(f'''dir 'C:\XXX'
swap 'x' 'y'
out 'output-name'
run
load
quit''')

def create_pdfs(filenames, dir):  
    for i in range(len(filenames)):
        print(colored(f'criando PDF para [{filenames[i]}]', 'green'))

        f = open(f'{dir}\{filenames[i]}', 'r')

        pdf = FPDF() 
        pdf.add_page()

        pdf.set_font('Helvetica', size = 15) 

        if i != 0:
            pdf.cell(200, 5, txt = filenames[i], ln = 1, align = 'C')
        
        pdf.cell(200, 5, txt = ' ', ln = 1, align = 'L')
 
        pdf.set_font('Helvetica', size = 12)

        for x in f:
            pdf.cell(200, 5, txt = x, ln = 1, align = 'L') 

        pdf.output(f'{filenames[i]}.pdf')

def merge_pdfs(filenames, output):
    merger = PdfFileMerger()

    try:
        for pdf in filenames:
            print(colored(f'juntando ao arquivo final [{pdf}]', 'green'))
            merger.append(f'{pdf}.pdf')
    except: pass

    merger.write(output)
    merger.close()

def delete_files(filenames):
    for f in filenames:
        print(colored(f'deletando arquivo temporario [{f}]', 'green'))
        os.remove(f'{f}.pdf')