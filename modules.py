import os
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
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
    print(f''' > dir 'C:\XXX'
 > swap 'x' 'y'
 > out 'output-name'
 > load
 > run
 > quit''')

def create_pdfs(filenames, dir):  
    for i in range(len(filenames)):
        print(f'creating PDF to [{filenames[i]}]')

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
            print(f'merging to final file [{pdf}]')
            merger.append(f'{pdf}.pdf')
    except: pass

    merger.write(output)
    merger.close()

def delete_files(filenames):
    for f in filenames:
        print(f'deleting temp files [{f}]')
        os.remove(f'{f}.pdf')