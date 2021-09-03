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
    print(f''' > dir 'directory'
 > swap 'x' 'y'
 > out 'output-name'
 > load
 > run
 > quit''')

def create_pdfs(filenames, dir):
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

        if i == 0:
            page_one_title = ''

            for j in range(len(filenames[i])):
                if filenames[i][j] == '.':
                    break
                page_one_title += filenames[i][j]

            pdf.set_font(normal_font, size = 22)
            pdf.cell(200, 5, txt = page_one_title, ln = 1, align = 'C')
            pdf.ln(16)

            pdf.set_font(normal_font, size = 12)
            pdf.write(5, f)

        else:
            pdf.set_font(normal_font, size = 16)
            pdf.write(5, filenames[i] + '\n\n\n')
            
            pdf.set_font(code_font, size = 12)
            pdf.write(5, f)

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