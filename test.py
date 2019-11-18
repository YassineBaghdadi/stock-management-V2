# from docx import *
# from docx.enum.table import WD_TABLE_ALIGNMENT
# from docx.enum.section import WD_ORIENT, WD_SECTION
# doc = Document()
import sqlite3

import firebase_admin
import datetime
conn = sqlite3.connect('src/db.db')
curs = conn.cursor()
# print(datetime.date.today() + datetime.timedelta(days=7))
# curs.execute('insert into deliy(start_date, end_date)values ("{}", "{}")'.format(datetime.date.today(), str(datetime.date.today() + datetime.timedelta(days=7))))
# conn.commit()
# curs.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='user' ''')
# if curs.fetchone()[0] == 1:
#     print('the table is exists')
#     if
# else:
#     print('the table is not exists')

# # # ####################################################################
# # # import random
# # # days = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30']
# # # months = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
# # # year = '2019'
# # # names = ['yassine', 'simo', 'otman', 'med', 'hamid', 'jilali', 'hafssa', 'farah', 'Liam','Noah','James','Logan','Mason','Oliver','Lucas','Alexander','Daniel','Aiden','Joseph','Samuel','David','Wyatt','John','Dylan','Gabriel','Isaac','Jack','Levi','Joshua','Lincoln','Jaxon']
# # # l_names = ['Noah','James','Logan','Mason','Oliver','Lucas','Alexander','Daniel','yassine', 'simo', 'otman', 'med', 'hamid', 'jilali', 'hafssa', 'farah']
# # # art = ['Lucas','Alexander','Daniel','yassine', 'simo', 'otman', 'med', 'hamid','yassine', 'simo', 'otman', 'med', 'hamid', 'jilali','Mason','Oliver','Lucas']
# # # numsL = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# # # for i in range(100):
# # #     curs.execute('INSERT INTO C_kridi_history (date, name, article, qt, total, pay_date) VALUES ("{}", "{}", "{}", {}, {}, "{}")'
# # #     .format(str(random.choice(days)) + '-' + str(random.choice(months)) + '-'+ str(year),
# # #      random.choice(names) + ' ' + random.choice(names)  , 
# # #      random.choice(art), 
# # #      random.choice(numsL) + random.choice(numsL),
# # #     random.choice(numsL) + random.choice(numsL),
# # #      str(random.choice(days)) + '-' + str(random.choice(months)) + '-' + str(year)))



# # conn.commit()

# section = doc.sections[0]

# heade = section.header
# paragraph = heade.paragraphs[0]

# paragraph.text = "date \n\ttitle\n\tadress\n\ttel "


# curs.execute('SELECT date, name, article, qt, total, pay_date FROM C_kridi_history')
# ii = curs.fetchall()
# # print(curs.fetchall())

# from docx.shared import Inches, Cm
# for i in curs.fetchall():
#     ii.append(i)


# # print(ii)
# # get table data -------------
# current_section = doc.sections[-1]
# new_width, new_height = current_section.page_height, current_section.page_width
# new_section = doc.add_section(WD_SECTION.NEW_PAGE)
# new_section.orientation = WD_ORIENT.LANDSCAPE
# new_section.page_width = new_width
# new_section.page_height = new_height
# # add table ------------------
# table = doc.add_table(1, 6)
# # populate header row --------
# heading_cells = table.rows[0].cells
# # heading_cells[0].text = 'ID'
# heading_cells[0].text = 'date'
# heading_cells[1].text = 'name'
# heading_cells[2].text = 'article'
# heading_cells[3].text = 'qt'
# heading_cells[4].text = 'total'
# heading_cells[5].text = 'pay_date'
# # add a data row for each item
# for item in ii:
#     cells = table.add_row().cells
#     # cells[0].text = str(item[0])
#     # cells[0].width = Inches(0.4)
#     cells[0].text = item[0]
#     cells[1].text = item[1]
#     cells[2].text = item[2]
#     cells[3].text = str(item[3])
#     cells[4].text = str(item[4])
#     cells[5].text = str(item[5])


#     # cells[1].width = 914400
#     # cells[0].width = 0.5 * 914400
#     # cells[2].width = 2 * 914400
#     # cells[3].width = 914400
#     # cells[4].width = 914400
#     # cells[5].width = 914400
#     # cells[6].width = 914400

# sections = doc.sections
# for section in sections:
#     # section.top_margin = 4
#     # section.bottom_margin = Inch(1)
#     section.left_margin = Inches(0.5)
#     section.right_margin = Inches(0.5)
#     print(section)

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


# # # from PyQt5.QtWidgets import (QMainWindow, QTextEdit, 
# # #     QAction, QFileDialog, QApplication)
# # # from PyQt5.QtGui import QIcon


# # # def test_dialog():
# # #     dlg = QFileDialog()
# # #     dlg.setFileMode(QFileDialog.AnyFile)
# # #     if dlg.exec_():
# # #         filenames = dlg.selectedFiles()
# # #         return filenames


# # # if __name__ == '__main__':
# # #     test_dialog()

# # from fpdf import FPDF

# # title = '20000 Leagues Under the Seas'

# # class PDF(FPDF):
# #     def header(self):
# #         # Arial bold 15
# #         self.set_font('Arial', 'B', 15)
# #         # Calculate width of title and position
# #         w = self.get_string_width(title) + 6
# #         self.set_x((210 - w) / 2)
# #         # Colors of frame, background and text
# #         self.set_draw_color(0, 80, 180)
# #         self.set_fill_color(230, 230, 0)
# #         self.set_text_color(220, 50, 50)
# #         # Thickness of frame (1 mm)
# #         self.set_line_width(1)
# #         # Title
# #         self.cell(w, 9, title, 1, 1, 'C', 1)
# #         # Line break
# #         self.ln(10)

# #     def footer(self):
# #         # Position at 1.5 cm from bottom
# #         self.set_y(-15)
# #         # Arial italic 8
# #         self.set_font('Arial', 'I', 8)
# #         # Text color in gray
# #         self.set_text_color(128)
# #         # Page number
# #         self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

# #     def chapter_title(self, num, label):
# #         # Arial 12
# #         self.set_font('Arial', '', 12)
# #         # Background color
# #         self.set_fill_color(200, 220, 255)
# #         # Title
# #         self.cell(0, 6, 'Chapter %d : %s' % (num, label), 0, 1, 'L', 1)
# #         # Line break
# #         self.ln(4)

# #     def chapter_body(self, name):
# #         # # Read text file
# #         # with open(name, 'rb') as fh:
# #         #     txt = fh.read().decode('latin-1')
# #         import sqlite3
# #         conn = sqlite3.connect('src/db.db')
# #         curs = conn.cursor()
# #         curs.execute('SELECT * FROM C_kridi_history')
# #         txt = curs.fetchall()
# #         # Times 12
# #         self.set_font('Times', '', 12)
# #         # Output justified text
# #         self.multi_cell(0, 5, txt)
# #         # Line break
# #         self.ln()
# #         # Mention in italics
# #         self.set_font('', 'I')
# #         self.cell(0, 5, '(end of excerpt)')

# #     def print_chapter(self, num, title, name):
# #         self.add_page()
# #         self.chapter_title(num, title)
# #         self.chapter_body(name)

# # pdf = PDF()
# # pdf.set_title(title)
# # pdf.set_author('Jules Verne')
# # pdf.print_chapter(1, 'A RUNAWAY REEF', '20k_c1.txt')
# # pdf.print_chapter(2, 'THE PROS AND CONS', '20k_c2.txt')
# # pdf.output('tuto3.pdf', 'F')
# # curs.execute('SELECT payed, not_payed_yet FROM selles_history')
# # statu_ = curs.fetchone()
# # print(statu_[0])

# for i, u in range(10), range(10,1):
#     print(i + ' + ' + u)

# d = "hello word"
# print(d)
# print(str(d))

# simple_table.py
 
from fpdf import FPDF
#
# def pdf__(spacing=1):
#     curs.execute('SELECT * FROM selles_history')
#
#     data = curs.fetchall()
#     table_head = ['ID', 'date', 'name', 'art', 'qt', 'total', 'pay_date']
#     data.insert(0, table_head)
#
#     pdf = FPDF()
#     pdf.set_font("Arial", size=10)
#     pdf.add_page()
#     # #  # Add an address
#     pdf.cell(100)
#     pdf.cell(0, 5, 'Mike Driscoll', ln=1)
#     pdf.cell(100)
#     pdf.cell(0, 5, '123 American Way', ln=1)
#     pdf.cell(100)
#     pdf.cell(0, 5, 'Any Town, USA', ln=1)
#
#     # #     # # Line break
#     pdf.ln(20)
#
#
#     col_width = pdf.w / (len(table_head) + 0.5)
#     row_height = pdf.font_size
#     for row in data:
#         for item in row:
#             pdf.cell(col_width, row_height*spacing,txt=str(item), border=1, align='C')
#         pdf.ln(row_height*spacing)
#
#     pdf.output('../Desktop/tttt.pdf')
#
# if __name__ == '__main__':
#     pdf__()

# curs.execute('SELECT * FROM selles_history')
# data = curs.fetchall()
# #table_head = ['ID', 'date', 'name', 'art', 'qt', 'total', 'pay_date']
# table_head = ['رقم الزبون','تاريخ العملية', 'الإسم', 'السلعة', 'الكمية', 'المجموع']
# data.insert(0, table_head)
# pdf = FPDF()
# pdf.set_font("Arial", size=11)
# pdf.add_page()
# # #  # Add an address
# # pdf.cell(100)
# # pdf.cell(0, 5, header_, ln=1)
# # # #     # # Line break
# # pdf.ln(20)
# col_width = pdf.w / (len(table_head) + 0.5)
# row_height = pdf.font_size

# #

# for row in data:
#     for item in row:
#         pdf.cell(col_width, row_height*1,txt=str(item), border=1, align='C')
#     pdf.ln(row_height*1)
# pdf.output('/mnt/AC72F2C272F29076/works/stock/stock-management-V2/src/y.pdf')

#
# from fpdf import FPDF
#
# pdf = FPDF()
# pdf.add_page()
#
# # Add a DejaVu Unicode font (uses UTF-8)
# # Supports more than 200 languages. For a coverage status see:
# # http://dejavu.svn.sourceforge.net/viewvc/dejavu/trunk/dejavu-fonts/langcover.txt
# pdf.add_font('DejaVu', '', 'src/DejaVuSansCondensed.ttf', uni=True)
# pdf.set_font('DejaVu', '', 14)
#
# text = u"""
# English: Hello World
# Greek: Γειά σου κόσμος
# Polish: Witaj świecie
# Portuguese: Olá mundo
# Russian: Здравствуй, Мир
# Vietnamese: Xin chào thế giới
# Arabic: مرحبا العالم
# Hebrew: שלום עולם
# """
#
# for txt in text.split('\n'):
#     pdf.write(8, txt)
#     pdf.ln(8)
#
# pdf.output('src/rrrr.pdf')
#
# import json
# import urllib.request
#
# # download raw json object
# url = "https://api.gdax.com/products/BTC-EUR/ticker"
# data = urllib.request.urlopen(url).read().decode()
#
# # parse json object
# obj = json.loads(data)

# output some object attributes
# print('$ ' + obj['price'])
# # print('$ ' + obj['volume'])
# for i in obj:
#     print(i)
# Import the Firebase service

from firebase_admin import auth

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# default_app = firebase_admin.initialize_app()
# Fetch the service account key JSON file contents
# cred = credentials.Certificate('src/stock-management-4e0de-firebase-adminsdk-j6xb1-87516cfbeb.json')
#
# # Initialize the app with a service account, granting admin privileges
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://stock-management-4e0de.firebaseio.com/'
# })

# As an admin, the app has access to read and write all data, regradless of Security Rules
# ref = db.reference()
#
# ref.update({
#     input('name : '): {
#         'age': input('age : '),
#         'city': input('city : ')
#     }
# # })
# ref.child('users').child('test').update({'age': 21})
# # print('###########')
# if ref.child('users').get() != None:
#     for key, val in ref.child('users').get().items():
#         print(key, val)
#         if key == 'yass083e8e293e87':
#             print(val['user_name'])
# else:
#     print('NULL')
#
# import datetime
# t = datetime.date.today()
# d = t + datetime.timedelta(days=7)
# print('today : ', t)
# print('after 10 days : ', d)
# print(type(t))
# print(type(d))
#
# curs.execute('SELECT user_id, client_id FROM user')
# # print(curs.fetchone())
# userId, clientId = curs.fetchone()
# print(userId)
# print(clientId)

# curs.execute('''CREATE TABLE deliy (key TEXT, start_date TEXT, end_date TEXT);''')
# conn.commit()

"""
#TODO :###################### new way to create pdf ##################
curs.execute('SELECT * FROM C_kridi_history')
data = [('A', 'B', 'C', 'D', 'E', 'F', 'G')]
for i in curs.fetchall() :
    data.append(i)

# for i in data :
#     print(i)

from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import letter
from reportlab.platypus import TableStyle
from reportlab.lib import colors


pdf = SimpleDocTemplate(
    'src/newWay.pdf',
    pagesize=letter,

)

from reportlab.platypus import Table
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
table = Table(data)
pdfmetrics.registerFont(TTFont('Arabic', 'src/Amiri.ttf'))
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.green),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, -1), 'Arabic'),
    ('FONTSIZE', (0, 0), (-1, -1), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('BOX', (0, 0), (-1, -1), 2, colors.black),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ('BOTTOMPADDING', (0, 1), (-1, -1), 10),

]))

elem = []
elem.append(table)
pdf.build(elem)
print('DONE')

"""
####################################################################################