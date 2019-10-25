# from docx import *
# from docx.enum.table import WD_TABLE_ALIGNMENT
# doc = Document()
# import sqlite3

# conn = sqlite3.connect('src/db.db')
# curs = conn.cursor()

# # ####################################################################
# # import random
# # days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
# # months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# # year = '2019'
# # names = ['yassine', 'simo', 'otman', 'med', 'hamid', 'jilali', 'hafssa', 'farah', 'Liam','Noah','James','Logan','Mason','Oliver','Lucas','Alexander','Daniel','Aiden','Joseph','Samuel','David','Wyatt','John','Dylan','Gabriel','Isaac','Jack','Levi','Joshua','Lincoln','Jaxon']
# # l_names = ['Noah','James','Logan','Mason','Oliver','Lucas','Alexander','Daniel','yassine', 'simo', 'otman', 'med', 'hamid', 'jilali', 'hafssa', 'farah']
# # art = ['Lucas','Alexander','Daniel','yassine', 'simo', 'otman', 'med', 'hamid','yassine', 'simo', 'otman', 'med', 'hamid', 'jilali','Mason','Oliver','Lucas']
# # numsL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # for i in range(100):
# #     curs.execute('INSERT INTO C_kridi_history (date, name, article, qt, total, pay_date) VALUES ("{}", "{}", "{}", {}, {}, "{}")'
# #     .format(str(random.choice(days)) + '-' + str(random.choice(months)) + '-'+ str(year),
# #      random.choice(names) + ' ' + random.choice(names)  , 
# #      random.choice(art), 
# #      random.choice(numsL) + random.choice(numsL),
# #     random.choice(numsL) + random.choice(numsL),
# #      str(random.choice(days)) + '-' + str(random.choice(months)) + '-' + str(year)))



# conn.commit()

# section = doc.sections[0]

# heade = section.header
# paragraph = heade.paragraphs[0]

# paragraph.text = "date \n\ttitle\n\tadress\n\ttel "


# curs.execute('SELECT * FROM C_kridi_history')
# ii = curs.fetchall()
# # print(curs.fetchall())

# from docx.shared import Inches, Cm
# for i in curs.fetchall():
#     ii.append(i)


# # print(ii)
# # get table data -------------

# # add table ------------------
# table = doc.add_table(1, 7)
# # populate header row --------
# heading_cells = table.rows[0].cells
# heading_cells[0].text = 'ID'
# heading_cells[1].text = 'date'
# heading_cells[2].text = 'name'
# heading_cells[3].text = 'article'
# heading_cells[4].text = 'qt'
# heading_cells[5].text = 'total'
# heading_cells[6].text = 'pay_date'
# # add a data row for each item
# for item in ii:
#     cells = table.add_row().cells
#     cells[0].text = str(item[0])
#     cells[1].text = item[1]
#     cells[2].text = item[2]
#     cells[3].text = item[3]
#     cells[4].text = str(item[4])
#     cells[5].text = str(item[5])
#     cells[6].text = str(item[6])


#     # cells[1].width = 914400
#     # cells[0].width = 0.5 * 914400
#     # cells[2].width = 2 * 914400
#     # cells[3].width = 914400
#     # cells[4].width = 914400
#     # cells[5].width = 914400
#     # cells[6].width = 914400

# # sections = doc.sections
# # for section in sections:
# #     # section.top_margin = 4
# #     # section.bottom_margin = Inch(1)
# #     section.left_margin = Inches(0.5)
# #     section.right_margin = Inches(0.5)
# #     print(section)

# # # table.autofit = True
# # # widths = (Inches(0.7), Inches(1), Inches(1.5), Inches(0.8), Inches(0.9), Inches(0.9), Inches(1))
# # for row in table.rows:
# #     for idx in row.cells:
# #         idx.width = 0.5 * 914400



# table.allow_autofit = True
# table.style = 'TableGrid'
# table.alignment=WD_TABLE_ALIGNMENT.CENTER

# # table.style = 'LightShading-Accent1'
# doc.save('src/testDOC.docx')


# # from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
# #     QAction, QFileDialog, QApplication)
# # from PyQt5.QtGui import QIcon


# # def test_dialog():
# #     dlg = QFileDialog()
# #     dlg.setFileMode(QFileDialog.AnyFile)
# #     if dlg.exec_():
# #         filenames = dlg.selectedFiles()
# #         return filenames


# # if __name__ == '__main__':
# #     test_dialog()

import os
 os.system('ls')