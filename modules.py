import os
from shutil import SpecialFileError
from fpdf import FPDF
from PyPDF2 import PdfFileMerger
from termcolor import colored

def list_of_files(dir):
    for (dirpath, dirnames, filenames) in os.walk(dir):
        break

    return filenames

def print_list_of_files(filenames, specials):
    for i in range(len(filenames)):
        if filenames.index(filenames[i]) in specials:
            color = 'green'
        else: color = 'cyan'
        if i < 10:
            print(colored(f'[0{i}] {filenames[i]}', color))
        else: print( colored(f'[{i}] {filenames[i]}', color))

def print_help():
    with open('help.txt', 'r') as helpt:
        print(helpt.read())

def create_pdfs(filenames, dir, specials):
    global first_page_font
    global code_font

    normal_font = './fonts/Arial'
    code_font = './fonts/Hack-Regular'

    for i in range(len(filenames)):
        print(f'creating PDF to [{filenames[i]}]')

        f = open(f'{dir}\{filenames[i]}', encoding="utf-8").read()

        pdf = FPDF() 
        pdf.add_font(normal_font, '', normal_font + '.ttf', uni = True)
        pdf.add_font(code_font, '', code_font + '.ttf', uni = True)

        pdf.add_page()

        if filenames.index(filenames[i]) in specials:
            pdf.set_font(normal_font, size = 22)
            pdf.cell(190, 5, txt = filenames[i], ln = 1, align = 'C')
            pdf.ln(16)

            pdf.set_font(normal_font, size = 12)
            pdf.write(5, f)

        else:
            pdf.set_font(normal_font, size = 16)
            pdf.write(5, filenames[i] + '\n\n\n')
            
            pdf.set_font(code_font, size = 12)
            pdf.write(5, f)

        pdf.output(f'{dir}\{filenames[i]}.pdf')

def merge_pdfs(filenames, output, dir):
    merger = PdfFileMerger()

    try:
        for pdf in filenames:
            print(f'merging to final file [{pdf}]')
            merger.append(f'{dir}\{pdf}.pdf')
    except: pass

    merger.write(f'{output}')
    merger.close()

def delete_files(filenames, dir):
    for f in filenames:
        print(f'deleting temp files [{f}]')
        os.remove(f'{dir}\{f}.pdf')