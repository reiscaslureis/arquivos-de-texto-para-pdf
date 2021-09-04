import os
from fpdf import FPDF
from PyPDF2 import PdfFileMerger

def list_of_files(dir):
    for (dirpath, dirnames, filenames) in os.walk(dir):
        break

    new = []

    for i in filenames:
        aux = []
        aux.append(i)
        aux.append(False)
        new.append(aux)

    filenames = new

    return filenames

def create_pdfs(filenames, dir):
    global first_page_font
    global code_font

    normal_font = './fonts/Arial'
    code_font = './fonts/Hack-Regular'

    for i in range(len(filenames)):
        print(f'creating PDF to [{filenames[i][0]}]')

        f = open(f'{dir}\{filenames[i][0]}', encoding="utf-8").read()

        pdf = FPDF() 
        pdf.add_font(normal_font, '', normal_font + '.ttf', uni = True)
        pdf.add_font(code_font, '', code_font + '.ttf', uni = True)

        pdf.add_page()

        if filenames[i][1] == True:
            aux = ''

            for j in range(len(filenames[i][0])):
                if filenames[i][0][j] == '.':
                    break
                else: aux += filenames[i][0][j]

            pdf.set_font(normal_font, size = 22)
            pdf.cell(190, 5, txt = aux, ln = 1, align = 'C')
            pdf.ln(16)

            pdf.set_font(normal_font, size = 12)
            pdf.write(5, f)

        else:
            pdf.set_font(normal_font, size = 16)
            pdf.write(5, filenames[i][0] + '\n\n\n')
            
            pdf.set_font(code_font, size = 12)
            pdf.write(5, f)

        pdf.output(f'{dir}\{filenames[i][0]}.pdf')

def merge_pdfs(filenames, output, dir):
    merger = PdfFileMerger()

    try:
        for i in range(len(filenames)):
            print(f'merging to final file [{filenames[i][0]}]')
            merger.append(f'{dir}\{filenames[i][0]}.pdf')
    except: pass

    merger.write(f'{output}.pdf')
    merger.close()

def delete_files(filenames, dir):
    for i in range(len(filenames)):
        print(f'deleting temp files [{filenames[i][0]}.pdf]')
        os.remove(f'{dir}\{filenames[i][0]}.pdf')