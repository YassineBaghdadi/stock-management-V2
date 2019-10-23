from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType

import os
from os import path
import sys
from datetime import *
import time
import sqlite3
import random
import multiprocessing as mp



today = date.today()

print("Today's date:", today)


first_open_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "first_open_win.ui"))
home_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "home.ui"))
splash_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "splash.ui"))
virification_alert_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "virification_alert.ui"))
#TODO : # setting_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "setting.ui"))
history_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "history.ui"))
add_new_pea_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "add_new_pea.ui"))
add_new_art_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "add_new_art.ui"))
delete_pea_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "delet_pea.ui"))
fix_kridi_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "fix_kridi.ui"))
fix_kridi_history_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "fix_history.ui"))
kridi_history_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "kridi_history.ui"))
edite_pea_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "edit_pea.ui"))
edite_art_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "edit_art.ui"))
#TODO : # help_win_dir,_ = loadUiType(path.join(path.dirname(__file__), "help.ui"))


conn = sqlite3.connect('src/db.db')
curs = conn.cursor()
curs.execute('CREATE TABLE IF NOT EXISTS user (NAME TEXT, PASSWORD TEXT)')

# curs.execute('INSERT INTO clients ( F_name, L_name, cne, total_debted, total_recived, total_rest, pay_date, note) VALUES ("{}", "{}", "{}", {}, {}, {}, "{}", "{}" ); '.format('qq', 'qq', 'qq', 77, 77, 77, str(today), 'note'))
# conn.commit()

class Splash(QWidget, splash_win_dir):#TODO :DONE
    def __init__(self, parent = None):
        super(Splash, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        # self.setWindowTitle("yassine")
        # self.progress()
        # self.prog()
        # self.show()
        self.timer = QBasicTimer()
        self.step = 0
        self.prog()
    def prog(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(100, self)
    def timerEvent(self, event):
        if self.step >= 100 :
            self.timer.stop()
            curs.execute('SELECT first FROM tools')
            first_stat = curs.fetchone()
            # print(kk[0])
            if first_stat[0] == 1:
                print('its the first open ')
                self.first_open_w = FirstOpen()
                self.first_open_w.show()
                self.close()

            else:
                curs.execute('SELECT safe FROM tools ;')
                curent_safe_stat = curs.fetchone()
                if curent_safe_stat[0] == 0:
                    print('its not the the first open ')
                    self.virification_alert_wn = VirificationAlert()
                    self.virification_alert_wn.show()
                    self.close()
                else:
                    self.home_wn = Home()
                    self.home_wn.show()
                    self.close()
            # f = open("ya.txt", "r")
            # jj = f.read()
            # if jj == "a":
            #     print('its : ', jj)
            #     w = open("ya.txt", "w")
            #     w.write("b")
            #     self.first_open_w = FirstOpen()
            #     self.first_open_w.show()
            #     self.close()
            # else:
            #     self.virification_alert_wn = VirificationAlert()
            #     self.virification_alert_wn.show()
            #     self.close()

            return
        self.step += 4
        self.progressBar.setValue(self.step)




#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
class FirstOpen(QMainWindow, first_open_win_dir):# almost done
    def __init__(self, parent = None):
        super(FirstOpen, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.save_btn.clicked.connect(self.save_info_first_open)
        # .setEchoMode(QtGui.QLineEdit.Password)
        self.pass_entry.setEchoMode(QLineEdit.Password)
        self.pass_confirmation.setEchoMode(QLineEdit.Password)


    def save_info_first_open(self):
        print(self.user_name_entry.text(),  self.pass_entry.text())
        if self.user_name_entry.text() == '' or self.user_name_entry.text() == ' ' or self.user_name_entry.text() == 0 :
            print('the user name cant be null ')
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('لايمكن ترك إسم المستخدم فارغ ')
            self.err.setWindowTitle('خطأ')
            self.user_name_entry.setFocus()

        elif self.safe_mod_checkBox.isChecked():
            print('safe mod is activated')
            curs.execute('INSERT INTO user (NAME, PASSWORD) VALUES ( "{}", "{}" ); '.format(self.user_name_entry.text(), ''))
            curs.execute('UPDATE tools SET user = "{}" , safe = 1  ;'.format(self.user_name_entry.text()))
            curs.execute('UPDATE tools SET first = {}'.format(2))
            conn.commit()
            print('user : {}'.format(self.user_name_entry.text()))
            wilcome_msg = QMessageBox.information(self, 'the title ', 'the message', QMessageBox.Ok)
            if wilcome_msg == QMessageBox.Ok:
                print('OK was clicked')
                self.home_wn = Home()
                self.home_wn.show()
                self.close()
        else:

            print('safe mode is not activated ')
            if self.pass_entry.text() == '' or self.pass_entry.text() == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('كلمة مرور غير صالحة ')
                self.err.setWindowTitle('خطأ')
                self.pass_entry.setFocus()

            elif self.pass_confirmation.text() == '' or self.pass_confirmation.text() == ' ' or self.pass_confirmation.text() != self.pass_entry.text():
                print('the fucking password is in wrong format ')
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('الكلمات غير متطابقة ')
                self.err.setWindowTitle('خطأ')
                self.pass_confirmation.setFocus()
            else:
                print('all DONE')
                curs.execute(
                    'INSERT INTO user (NAME, PASSWORD) VALUES ( "{}", "{}" ); '.format(self.user_name_entry.text(),self.pass_entry.text()))
                curs.execute('UPDATE tools SET user = "{}", first = {} , safe = 0 ;'.format(self.user_name_entry.text(), 2))
                # curs.execute('UPDATE tools SET first = {}'.format(2))
                conn.commit()
                self.user_name_entry.setText('')
                self.pass_entry.setText('')
                self.pass_confirmation.setText('')
                #TODO : add nice wilcome message
                wilcome_msg = QMessageBox.information(self, 'the title ', "the nice it'll be here soon ", QMessageBox.Ok)
                if wilcome_msg == QMessageBox.Ok:
                    print('OK was clicked')
                    self.home_wn = Home()
                    self.home_wn.show()
                    self.close()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Selles_history(QWidget, history_win_dir):
    def __init__(self, parent = None):
        super(Selles_history, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.refresh_()
        self.back_from_history.clicked.connect(self.back_home)
        self.print_history.clicked.connect(self.print_selles_history)


    def print_selles_history(self):#TODO : Print selles history table
        print('Print selles history ')

    def back_home(self):
        self.close()
        self.home_wn = Home()
        self.home_wn.show()

    def refresh_(self):
        while self.selles_history_table.rowCount() > 0 :
            self.selles_history_table.removeRow(0)
        curs.execute('SELECT  date, client, article, qt, payed, not_payed_yet, pay_date FROM selles_history ORDER BY ID DESC')
        rus_ = curs.fetchall()
        self.selles_history_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.selles_history_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.selles_history_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

        print(curs.fetchall())


class Buyes_history(QWidget, history_win_dir):
    def __init__(self, parent = None):
        super(Buyes_history, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.refresh_()
        self.back_from_history.clicked.connect(self.back_home)
        self.print_history.clicked.connect(self.print_buyes_history)


    def print_buyes_history(self):#TODO : Print buying history table
        print('Print buying history ')

    def back_home(self):
        self.close()
        self.home_wn = Home()
        self.home_wn.show()

    def refresh_(self):
        while self.selles_history_table.rowCount() > 0 :
            self.selles_history_table.removeRow(0)
        curs.execute('SELECT  date, seller, article, qt, payed, not_payed_yet, pay_date FROM buys_history ORDER BY ID DESC')
        rus_ = curs.fetchall()
        self.selles_history_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.selles_history_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.selles_history_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

        print(curs.fetchall())

class ADD_new_client(QWidget, add_new_pea_win_dir):# DONE
    def __init__(self, parent = None):
        super(ADD_new_client, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.cancel_btn.clicked.connect(self.cancel)
        self.save_new_client.clicked.connect(self.save_new_client_)

        self.clients_full_names = []
    def save_new_client_(self):
        if self.F_name.text() == '' or self.F_name.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الإسم الأول ')
            self.err.setWindowTitle('خطأ')
            self.F_name.setFocus()

        elif self.L_name.text() == '' or self.L_name.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الإسم الأخير ')
            self.err.setWindowTitle('خطأ')
            self.L_name.setFocus()

        else:
            self.clients_cne_list = []
            curs.execute('SELECT cne FROM clients')
            for cne in curs.fetchall():
                # print('#####################\n', cne[0], '##', '\n#######################')
                self.clients_cne_list.append(cne[0])

            curs.execute('SELECT F_name, L_name FROM clients')
            for fname, lname in curs.fetchall():
                self.clients_full_names.append(fname + ' ' + lname)

            print('Clients full names list \n******************************************\n{}\n***************************'.format(self.clients_full_names))
            if self.F_name.text() + ' ' + self.L_name.text() in self.clients_full_names:
                current_info = curs.execute('SELECT F_name, L_name, cne FROM clients'
                                            ' WHERE F_name LIKE "{}" AND L_name LIKE "{}";'.format(self.F_name.text(),
                                                                                                   self.L_name.text()))
                self.current = []
                for oo in current_info.fetchall():
                    print('00 = {}'.format(oo))
                    self.current.append(oo[0])
                    self.current.append(oo[1])
                    self.current.append(oo[2])
                print('##########', self.current)
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage(
                    ' هذا الزبون موجود بالفعل في قاعدة البيانات \n #الإسم : " ‏؜{} "  #اللقب : " {} "  #البطاقة الوطنية : " {} " '
                    .format(str(self.current[0]), str(self.current[1]), str(self.current[2])))
                self.err.setWindowTitle('هذا الزبون موجود في قاعدة البيانات')
                self.F_name.setFocus()

            elif self.cne.text() in self.clients_cne_list:
                bb = curs.execute('SELECT F_name, L_name FROM clients WHERE cne LIKE "{}"'.format(self.cne.text()))
                liss = bb.fetchone()
                msg = 'هذه البطاقة الوطنية هي للسيد : {} {}'
                self.err = QtWidgets.QErrorMessage()
                self.err.setWindowTitle('هناك تداخل في البيانات')
                self.err.showMessage(msg.format(liss[0], liss[1]))

            else:
                if self.cne.text() == '' or self.cne.text() == ' ':
                    self.cne.setText('-')

                if self.note.text() == '' or self.note.text() == ' ':
                    self.note.setText('-')
                #
                curs.execute('INSERT INTO clients (F_name, L_name, cne, note) VALUES("{}", "{}", "{}", "{}");'
                             .format(self.F_name.text(), self.L_name.text(), self.cne.text(), self.note.text()))

                conn.commit()
                self.F_name.setText('')
                self.F_name.setFocus()
                self.L_name.setText('')
                self.cne.setText('')
                self.note.setText('')
                # self.cancel()
                print('its broken')

    def cancel(self):
        self.close()
        self.home_wn = Home()
        self.home_wn.show()



class ADD_new_seller(QWidget, add_new_pea_win_dir):# DONE
    def __init__(self, parent = None):
        super(ADD_new_seller, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.cancel_btn.clicked.connect(self.cancel)
        self.save_new_client.clicked.connect(self.save_new_client_)

        self.sellers_full_names = []
    def save_new_client_(self):
        if self.F_name.text() == '' or self.F_name.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الإسم الأول ')
            self.err.setWindowTitle('خطأ')
            self.F_name.setFocus()

        elif self.L_name.text() == '' or self.L_name.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الإسم الأخير ')
            self.err.setWindowTitle('خطأ')
            self.L_name.setFocus()

        else:
            self.sellers_cne_list = []
            curs.execute('SELECT cne FROM sellers')
            for cne in curs.fetchall():
                # print('#####################\n', cne[0], '##', '\n#######################')
                self.sellers_cne_list.append(cne[0])

            curs.execute('SELECT F_name, L_name FROM sellers')
            for fname, lname in curs.fetchall():
                self.sellers_full_names.append(fname + ' ' + lname)

            print('sellers full names list \n******************************************\n{}\n***************************'.format(self.sellers_full_names))
            if self.F_name.text() + ' ' + self.L_name.text() in self.sellers_full_names:
                current_info = curs.execute('SELECT F_name, L_name, cne FROM sellers'
                                            ' WHERE F_name LIKE "{}" AND L_name LIKE "{}";'.format(self.F_name.text(),
                                                                                                   self.L_name.text()))
                self.current = []
                for oo in current_info.fetchall():
                    print('00 = {}'.format(oo))
                    self.current.append(oo[0])
                    self.current.append(oo[1])
                    self.current.append(oo[2])
                print('##########', self.current)
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage(
                    ' هذا الزبون موجود بالفعل في قاعدة البيانات \n #الإسم : " ‏؜{} "  #اللقب : " {} "  #البطاقة الوطنية : " {} " '
                    .format(str(self.current[0]), str(self.current[1]), str(self.current[2])))
                self.err.setWindowTitle('هذا الزبون موجود في قاعدة البيانات')
                self.F_name.setFocus()

            elif self.cne.text() in self.sellers_cne_list:
                bb = curs.execute('SELECT F_name, L_name FROM sellers WHERE cne LIKE "{}"'.format(self.cne.text()))
                liss = bb.fetchone()
                msg = 'هذه البطاقة الوطنية هي للسيد : {} {}'
                self.err = QtWidgets.QErrorMessage()
                self.err.setWindowTitle('هناك تداخل في البيانات')
                self.err.showMessage(msg.format(liss[0], liss[1]))

            else:
                if self.cne.text() == '' or self.cne.text() == ' ':
                    self.cne.setText('-')

                if self.note.text() == '' or self.note.text() == ' ':
                    self.note.setText('-')
                #
                curs.execute('INSERT INTO sellers (F_name, L_name, cne, note) VALUES("{}", "{}", "{}", "{}");'
                             .format(self.F_name.text(), self.L_name.text(), self.cne.text(), self.note.text()))

                conn.commit()
                self.F_name.setText('')
                self.F_name.setFocus()
                self.L_name.setText('')
                self.cne.setText('')
                self.note.setText('')
                # self.cancel()

    def cancel(self):
        self.close()
        self.home_wn = Home()
        self.home_wn.show()



class ADD_new_art(QWidget, add_new_art_win_dir):# DONE
    def __init__(self, parent = None):
        super(ADD_new_art, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.cancel_btn.clicked.connect(self.cancel)
        self.save_new_art.clicked.connect(self.save_new_art_)

        
        self.art_list = []
    def save_new_art_(self):
        if self.name.text() == '' or self.name.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الإسم  ')
            self.err.setWindowTitle('خطأ')
            self.name.setFocus()

        elif self.qt.text() == '' or self.qt.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الكمية ')
            self.err.setWindowTitle('خطأ')
            self.qt.setFocus()

        elif self.price.text() == '' or self.price.text() == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال الثمن ')
            self.err.setWindowTitle('خطأ')
            self.price.setFocus()


        else:
            self.current = []
            curs.execute('SELECT name FROM articles')
            for nn in curs.fetchall():
                self.art_list.append(nn[0])

            if self.name.text() in self.art_list:
                curs.execute('SELECT name, qt, price FROM articles WHERE name LIKE "{}" '.format(self.name.text()))
                
                for oo in curs.fetchone():
                    self.current.append(oo)#name
                    
                print(self.current)
                
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('" {} " هي موجودة بالفعل في قاعدة البيانات و كميتها الحالية : "{}" و ثمنها : {} درهم'
                    .format(self.current[0], self.current[1], self.current[2]))
                self.err.setWindowTitle('هذه السلعة موجود في قاعدة البيانات')
                self.name.setFocus()
                
            else:
                if self.note.text() == '' or self.note.text() == ' ':
                    self.note.setText('-')
                if self.type.text() == '' or self.type.text() == ' ':
                    self.type.setText('-')

                curs.execute('INSERT INTO articles (name, type, qt, price, note) VALUES("{}", "{}", {}, {}, "{}");'
                             .format(self.name.text(), self.type.text(), self.qt.text(), self.price.text(), self.note.text()))

                conn.commit()
                self.name.setText('')
                self.name.setFocus()
                self.type.setText('')
                self.qt.setText('')
                self.price.setText('')
                self.note.setText('')
                # self.cancel()

    def cancel(self):
        self.close()
        self.home_wn = Home()
        self.home_wn.show()





class Remove_client(QWidget, delete_pea_win_dir): # DONE
    def __init__(self, parent = None):
        super(Remove_client, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.fill_combo()
        self.shose_pea_to_rmv.currentTextChanged.connect(self.set_cne)
        self.rmv_btn.clicked.connect(self.delete)
        self.cancel_rmv.clicked.connect(self.cncl)



    def set_cne(self):
        if self.shose_pea_to_rmv.currentText() != '':
            curs.execute('SELECT cne FROM clients WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
                         .format(self.shose_pea_to_rmv.currentText().split('|')[0], self.shose_pea_to_rmv.currentText().split('|')[1]))
            print(self.shose_pea_to_rmv.currentText())
            print('selected F_name : {}'.format(self.shose_pea_to_rmv.currentText().split('|')[0]))
            print('selected L_name : {}'.format(self.shose_pea_to_rmv.currentText().split('|')[1]))
            # print('selected client cne : {}'.format(curs.fetchone()[0]))
            self.show_cne_rmv_page.setText(curs.fetchone()[0])
    def fill_combo(self):
        clients_names_list_ = ['']
        curs.execute('SELECT F_name, L_name  FROM clients')
        for fn, ln in curs.fetchall():
            clients_names_list_.append(fn + '|' + ln)
        print('CLIENTS : ', clients_names_list_)
        self.shose_pea_to_rmv.addItems(clients_names_list_)

    def delete(self):
        print('selected F_name : {}'.format(self.shose_pea_to_rmv.currentText().split('|')[0]))
        print('selected L_name : {}'.format(self.shose_pea_to_rmv.currentText().split('|')[1]))
        curs.execute('DELETE FROM clients WHERE F_name LIKE "{}" AND L_name LIKE "{}" AND cne LIKE "{}" '
                     .format(self.shose_pea_to_rmv.currentText().split('|')[0],
                             self.shose_pea_to_rmv.currentText().split('|')[1],
                     self.show_cne_rmv_page.text()))
        self.shose_pea_to_rmv.clear()
        self.fill_combo()
        self.shose_pea_to_rmv.setCurrentIndex(0)
        self.show_cne_rmv_page.setText('')
        conn.commit()




    def cncl(self):
        self.close()
        self.home = Home()
        self.home.show()



class Remove_seller(QWidget, delete_pea_win_dir): # DONE
    def __init__(self, parent = None):
        super(Remove_seller, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.fill_combo()
        self.shose_pea_to_rmv.currentTextChanged.connect(self.set_cne)
        self.rmv_btn.clicked.connect(self.delete_)
        self.cancel_rmv.clicked.connect(self.cncl)



    def set_cne(self):
        if self.shose_pea_to_rmv.currentText() != '':
            curs.execute('SELECT cne FROM sellers WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
                         .format(self.shose_pea_to_rmv.currentText().split('|')[0], self.shose_pea_to_rmv.currentText().split('|')[1]))

            self.show_cne_rmv_page.setText(curs.fetchone()[0])
    def fill_combo(self):
        clients_names_list_ = ['']
        curs.execute('SELECT F_name, L_name  FROM sellers')
        for fn, ln in curs.fetchall():
            clients_names_list_.append(fn + '|' + ln)
        print('CLIENTS : ', clients_names_list_)
        self.shose_pea_to_rmv.addItems(clients_names_list_)

    def delete_(self):
        print('selected F_name : {}'.format(self.shose_pea_to_rmv.currentText().split('|')[0]))
        print('selected L_name : {}'.format(self.shose_pea_to_rmv.currentText().split('|')[1]))
        curs.execute('DELETE FROM sellers WHERE F_name LIKE "{}" AND L_name LIKE "{}" AND cne LIKE "{}" '
                     .format(self.shose_pea_to_rmv.currentText().split('|')[0],
                             self.shose_pea_to_rmv.currentText().split('|')[1],
                     self.show_cne_rmv_page.text()))
        self.shose_pea_to_rmv.clear()
        self.fill_combo()
        self.shose_pea_to_rmv.setCurrentIndex(0)
        self.show_cne_rmv_page.setText('')
        conn.commit()




    def cncl(self):
        self.close()
        self.home = Home()
        self.home.show()




class C_kridi_fix_history(QWidget, fix_kridi_history_win_dir):
    def __init__(self, parent = None):
        super(C_kridi_fix_history, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.refresh_()
        self.back_btn.clicked.connect(self.back__)
        self.print_btn.clicked.connect(self.print_)


    def print_(self):##~ TODO ~~PRINT fucking DATA 
        pass

    def back__(self):
        self.close()
        self.fix = C_kridi_fix()
        self.fix.show()

    def refresh_(self):
        while self.fix_table.rowCount() > 0 :
            self.articles_fix_tablewill_end.removeRow(0)

        curs.execute('SELECT  date, name , payed_money, rest FROM fix_C_kridi_history ORDER BY ID DESC')
        rus_ = curs.fetchall()
        self.fix_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.fix_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.fix_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


class C_kridi_fix(QWidget, fix_kridi_win_dir):
    def __init__(self, parent = None):
        super(C_kridi_fix, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.fill_comboB()
        self.fix_kridi_done.clicked.connect(self.done)
        self.fix_kridi_save.clicked.connect(self.save_)
        self.fix_kridi_editeLine.textChanged.connect(self.check_state)
        self.fix_kridi_save.setEnabled(False)
        self.fix_kridi_editeLine.setEnabled(False)
        self.fix_kridi_editeLine.setValidator(QtGui.QIntValidator(1, 2147483647, self))
        self.fix_kridi_combo.currentTextChanged.connect(self.on_combo_changed)
        self.fix_kridi_history_btn.clicked.connect(self.fix_C_kridi_history)



    def fix_C_kridi_history(self):
        self.close()
        self.fixC_H = C_kridi_fix_history()
        self.fixC_H.show()

    def on_combo_changed(self):
        if self.fix_kridi_combo.currentText() != '':
            self.fix_kridi_editeLine.setEnabled(True)
        else:
            self.fix_kridi_editeLine.setEnabled(False)

        self.fix_kridi_editeLine.setText('')
        self.fix_kridi_editeLine.setFocus()
        

    def check_state(self):
        color = '#b6b6b6'#normal
        tt = 0
        for i in self.fix_kridi_editeLine.text():
            tt += int(i)
        curs.execute('SELECT total_rest FROM C_kridi WHERE name LIKE "{}"'.format(self.fix_kridi_combo.currentText()))
        rest = curs.fetchone()[0]
        if  self.fix_kridi_editeLine.text() == '':
            color = '#b6b6b6'#normal
            self.fix_kridi_save.setEnabled(False)
            self.rest_label.setText('')

            
        elif float(self.fix_kridi_editeLine.text()) > rest or tt == 0:
            color = '#f6989d'#red
            self.fix_kridi_save.setEnabled(False)
            self.rest_label.setText('خطأ')

        else:
            self.fix_kridi_save.setEnabled(True)
            self.rest_label.setText(str(rest - float(self.fix_kridi_editeLine.text())) + ' DH')
        self.fix_kridi_editeLine.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def fill_comboB(self):
        self.fix_kridi_combo.clear()
        curs.execute('SELECT name FROM C_kridi')
        names = ['']
        for i in curs.fetchall():
            names.append(i[0])
        self.fix_kridi_combo.addItems(names)

    def done(self):
        self.close()
        self.home = Home()
        self.home.show()

    def save_(self):
        try:
            cll = self.fix_kridi_combo.currentText()
            curs.execute('UPDATE C_kridi SET total_recived = total_recived + {} WHERE name LIKE "{}"'
                    .format(self.fix_kridi_editeLine.text(), self.fix_kridi_combo.currentText()))
            curs.execute('UPDATE clients SET total_recived = total_recived + {} WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
                    .format(self.fix_kridi_editeLine.text(), cll.split(' ')[0], cll.split(' ')[1]))
            curs.execute('UPDATE C_kridi SET total_rest = debte - total_recived ')
            curs.execute('UPDATE clients SET total_rest = total_debted - total_recived ')
            curs.execute('SELECT total_rest FROM C_kridi WHERE name LIKE "{}"'.format(self.fix_kridi_combo.currentText()))
            curs.execute('INSERT INTO fix_C_kridi_history (date, name, payed_money, rest) VALUES ("{}", "{}", {}, {})'
                    .format(str(today), self.fix_kridi_combo.currentText(), self.fix_kridi_editeLine.text(), curs.fetchone()[0]))
            conn.commit()
        except ERROR as er:
            print(er)
            

class S_kridi_fix_history(QWidget, fix_kridi_history_win_dir):
    def __init__(self, parent = None):
        super(S_kridi_fix_history, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.refresh_()
        self.back_btn.clicked.connect(self.back__)
        self.print_btn.clicked.connect(self.print_)


    def print_(self):##~ TODO ~~PRINT fucking DATA 
        pass

    def back__(self):
        self.close()
        self.fix = S_kridi_fix()
        self.fix.show()

    def refresh_(self):
        while self.fix_table.rowCount() > 0 :
            self.articles_fix_tablewill_end.removeRow(0)

        curs.execute('SELECT  date, name , payed_money, rest FROM fix_S_kridi_history ORDER BY ID DESC')
        rus_ = curs.fetchall()
        self.fix_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.fix_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.fix_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

class S_kridi_fix(QWidget, fix_kridi_win_dir):
    def __init__(self, parent = None):
        super(S_kridi_fix, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.fill_comboB()
        self.fix_kridi_done.clicked.connect(self.done)
        self.fix_kridi_save.clicked.connect(self.save_)
        self.fix_kridi_editeLine.textChanged.connect(self.check_state)
        self.fix_kridi_save.setEnabled(False)
        self.fix_kridi_editeLine.setEnabled(False)
        self.fix_kridi_editeLine.setValidator(QtGui.QIntValidator(1, 2147483647, self))
        self.fix_kridi_combo.currentTextChanged.connect(self.on_combo_changed)
        self.fix_kridi_history_btn.clicked.connect(self.fix_S_kridi_history)

    def fix_S_kridi_history(self):
        self.close()
        self.fixS_H = S_kridi_fix_history()
        self.fixS_H.show()

    def on_combo_changed(self):
        if self.fix_kridi_combo.currentText() != '':
            self.fix_kridi_editeLine.setEnabled(True)
        else:
            self.fix_kridi_editeLine.setEnabled(False)

        self.fix_kridi_editeLine.setText('')
        self.fix_kridi_editeLine.setFocus()
        

    def check_state(self):
        color = '#b6b6b6'#normal
        tt = 0
        for i in self.fix_kridi_editeLine.text():
            tt += int(i)
        curs.execute('SELECT total_rest FROM S_kridi WHERE name LIKE "{}"'.format(self.fix_kridi_combo.currentText()))
        rest = curs.fetchone()[0]
        if  self.fix_kridi_editeLine.text() == '':
            color = '#b6b6b6'#normal
            self.fix_kridi_save.setEnabled(False)
            self.rest_label.setText('')

            
        elif float(self.fix_kridi_editeLine.text()) > rest or tt == 0:
            color = '#f6989d'#red
            self.fix_kridi_save.setEnabled(False)
            self.rest_label.setText('خطأ')

        else:
            self.fix_kridi_save.setEnabled(True)
            self.rest_label.setText(str(rest - float(self.fix_kridi_editeLine.text())) + ' DH')
        self.fix_kridi_editeLine.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def fill_comboB(self):
        self.fix_kridi_combo.clear()
        curs.execute('SELECT name FROM S_kridi')
        names = ['']
        for i in curs.fetchall():
            names.append(i[0])
        self.fix_kridi_combo.addItems(names)

    def done(self):
        self.close()
        self.home = Home()
        self.home.show()

    def save_(self):
        try:
            cll = self.fix_kridi_combo.currentText()
            curs.execute('UPDATE S_kridi SET total_recived = total_recived + {} WHERE name LIKE "{}"'
                    .format(self.fix_kridi_editeLine.text(), self.fix_kridi_combo.currentText()))
            curs.execute('UPDATE sellers SET total_recived = total_recived + {} WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
                    .format(self.fix_kridi_editeLine.text(), cll.split(' ')[0], cll.split(' ')[1]))
            curs.execute('UPDATE S_kridi SET total_rest = debte - total_recived ')
            curs.execute('UPDATE sellers SET total_rest = total_debted - total_recived ')
            curs.execute('SELECT total_rest FROM S_kridi WHERE name LIKE "{}"'.format(self.fix_kridi_combo.currentText()))
            curs.execute('INSERT INTO fix_S_kridi_history (date, name, payed_money, rest) VALUES ("{}", "{}", {}, {})'
                    .format(str(today), self.fix_kridi_combo.currentText(), self.fix_kridi_editeLine.text(), curs.fetchone()[0]))
            conn.commit()
        except ERROR as er:
            print(er)
           
 
class C_kridi_history(QWidget, kridi_history_win_dir):
    def __init__(self, parent = None):
        super(C_kridi_history, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.back_from_history.clicked.connect(self.bback)
        self.print_history.clicked.connect(self.pprint)
        self.refresh()

    def refresh(self):
        while self.kridi_history_table.rowCount() > 0 :
            self.kridi_history_table.removeRow(0)

        curs.execute('SELECT date, name, article , qt, total, pay_date FROM C_kridi_history ORDER BY ID DESC')
        rus_ = curs.fetchall()
        self.kridi_history_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.kridi_history_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.kridi_history_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


    def pprint(self):#TODO PRINT data 
        pass

    def bback(self):
        self.close()
        self.home = Home()
        self.home.show()




class S_kridi_history(QWidget, kridi_history_win_dir):
    def __init__(self, parent = None):
        super(S_kridi_history, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.back_from_history.clicked.connect(self.bback)
        self.print_history.clicked.connect(self.pprint)
        self.refresh()

    def refresh(self):
        while self.kridi_history_table.rowCount() > 0 :
            self.kridi_history_table.removeRow(0)

        curs.execute('SELECT date, name, article , qt, total, pay_date FROM S_kridi_history ORDER BY ID DESC')
        rus_ = curs.fetchall()
        self.kridi_history_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.kridi_history_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.kridi_history_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


    def pprint(self):#TODO PRINT data 
        pass

    def bback(self):
        self.close()
        self.home = Home()
        self.home.show()

class Edite_client(QWidget, edite_pea_win_dir):
    def __init__(self, parent = None):
        super(Edite_client, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.done.clicked.connect(self.DONE)
        self.cliients_names_combo.currentTextChanged.connect(self.selected)
        self.refresh()
        self.save_.clicked.connect(self.save)


    def save(self):
        curs.execute('UPDATE clients SET F_name = "{}", L_name = "{}", cne = "{}", note = "{}" WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
        .format(self.F_name.text(), self.L_name.text(), self.cne.text(), self.note.toPlainText(), self.cliients_names_combo.currentText().split('|')[0], 
        self.cliients_names_combo.currentText().split('|')[1]))
        conn.commit()
        self.cliients_names_combo.setCurrentIndex(0)
        self.refresh()

    def selected(self):
        if self.cliients_names_combo.currentText() == '':
            self.F_name.setEnabled(False)
            self.L_name.setEnabled(False)
            self.cne.setEnabled(False)
            self.note.setEnabled(False)
            self.save_.setEnabled(False)

            self.F_name.setText('')
            self.L_name.setText('')
            self.cne.setText('')
            self.note.setText('')
        else:
            curs.execute('SELECT F_name, L_name, cne, note FROM clients WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
                .format(self.cliients_names_combo.currentText().split('|')[0], self.cliients_names_combo.currentText().split('|')[1]))
            info = curs.fetchone()
            print(info)

            self.F_name.setEnabled(True)
            self.L_name.setEnabled(True)
            self.cne.setEnabled(True)
            self.note.setEnabled(True)
            self.save_.setEnabled(True)

            self.F_name.setText(info[0])
            self.L_name.setText(info[1])
            self.cne.setText(info[2])
            self.note.setText(info[3])


    def refresh(self):
        self.cliients_names_combo.clear()
        curs.execute('SELECT F_name, L_name FROM clients')
        names =['']
        for i in curs.fetchall():
            names.append(i[0] + '|' + i[1])
        
        self.cliients_names_combo.addItems(names)



    def DONE(self):
        self.close()
        self.home = Home()
        self.home.show()


class Edite_seller(QWidget, edite_pea_win_dir):
    def __init__(self, parent = None):
        super(Edite_seller, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.done.clicked.connect(self.DONE)
        self.cliients_names_combo.currentTextChanged.connect(self.selected)
        self.refresh()
        self.save_.clicked.connect(self.save)


    def save(self):
        curs.execute('UPDATE sellers SET F_name = "{}", L_name = "{}", cne = "{}", note = "{}" WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
        .format(self.F_name.text(), self.L_name.text(), self.cne.text(), self.note.toPlainText(), self.cliients_names_combo.currentText().split('|')[0], 
        self.cliients_names_combo.currentText().split('|')[1]))
        conn.commit()
        self.cliients_names_combo.setCurrentIndex(0)
        self.refresh()

    def selected(self):
        if self.cliients_names_combo.currentText() == '':
            self.F_name.setEnabled(False)
            self.L_name.setEnabled(False)
            self.cne.setEnabled(False)
            self.note.setEnabled(False)
            self.save_.setEnabled(False)

            self.F_name.setText('')
            self.L_name.setText('')
            self.cne.setText('')
            self.note.setText('')
        else:
            curs.execute('SELECT F_name, L_name, cne, note FROM sellers WHERE F_name LIKE "{}" AND L_name LIKE "{}"'
                .format(self.cliients_names_combo.currentText().split('|')[0], self.cliients_names_combo.currentText().split('|')[1]))
            info = curs.fetchone()
            print(info)

            self.F_name.setEnabled(True)
            self.L_name.setEnabled(True)
            self.cne.setEnabled(True)
            self.note.setEnabled(True)
            self.save_.setEnabled(True)

            self.F_name.setText(info[0])
            self.L_name.setText(info[1])
            self.cne.setText(info[2])
            self.note.setText(info[3])


    def refresh(self):
        self.cliients_names_combo.clear()
        curs.execute('SELECT F_name, L_name FROM sellers')
        names =['']
        for i in curs.fetchall():
            names.append(i[0] + '|' + i[1])
        
        self.cliients_names_combo.addItems(names)



    def DONE(self):
        self.close()
        self.home = Home()
        self.home.show()




class Edite_art(QWidget, edite_art_win_dir):
    def __init__(self, parent = None):
        super(Edite_art, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.done.clicked.connect(self.DONE)
        self.articles_combo.currentTextChanged.connect(self.selected)
        self.refresh()
        self.save_.clicked.connect(self.save)


    def save(self):
        curs.execute('UPDATE articles SET name = "{}", type = "{}", qt = {}, price = {}, note = "{}" WHERE name LIKE "{}" '
        .format(self.name.text(), self.type.text(), self.qt.text(), self.price.text(), self.note.toPlainText(), self.articles_combo.currentText() ))
        conn.commit()
        self.articles_combo.setCurrentIndex(0)
        self.refresh()

    def selected(self):
        if self.articles_combo.currentText() == '':
            self.name.setEnabled(False)
            self.type.setEnabled(False)
            self.qt.setEnabled(False)
            self.price.setEnabled(False)
            self.note.setEnabled(False)
            self.save_.setEnabled(False)

            self.name.setText('')
            self.type.setText('')
            self.qt.setText('')
            self.price.setText('')
            self.note.setText('')
        else:
            curs.execute('SELECT name, type, qt, price, note FROM articles WHERE name LIKE "{}" '
                .format(self.articles_combo.currentText()))
            info = curs.fetchone()
            print(info)

            self.name.setEnabled(True)
            self.type.setEnabled(True)
            self.qt.setEnabled(True)
            self.price.setEnabled(True)
            self.note.setEnabled(True)
            self.save_.setEnabled(True)

            self.name.setText(info[0])
            self.type.setText(info[1])
            self.qt.setText(str(info[2]))
            self.price.setText(str(info[3]))
            self.note.setText(info[4])


    def refresh(self):
        self.articles_combo.clear()
        curs.execute('SELECT name FROM articles')
        names =['']
        for i in curs.fetchall():
            names.append(i[0])
        
        self.articles_combo.addItems(names)



    def DONE(self):
        self.close()
        self.home = Home()
        self.home.show()




class Home(QWidget, home_win_dir):# almost...
    def __init__(self, parent = None):
        super(Home, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.logOut_Button.clicked.connect(self.log_out)
        self.refresh_data()
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setWindowFlag(QtCore.Qt.WindowCloseButtonHint, False)

        # self.home_tabWidget.setCurrentIndex(current_tab)
        self.home_tabWidget.currentChanged.connect(self.onTabChange)
        self.setWindowTitle('الرئيسية')
        self.sell_choose_article_comboBox.currentTextChanged.connect(self.set_sell_article_type)
        self.save_selling_operation_pushButton.clicked.connect(self.save_sell_operation)
        self.save_buying_operation_pushButton.clicked.connect(self.save_buy_operation)
        self.sell_qt.lineEdit().setEnabled(False)
        self.sell_qt.valueChanged.connect(self.on_sell_qt_spin_box_changed)
        self.buy_article_qt.valueChanged.connect(self.on_buy_qt_spin_box_changed)
        self.sell_date_to_pay.setDateTime(QtCore.QDateTime.currentDateTime())
        self.add_client_Button.clicked.connect(self.add_new_client)
        self.add_seller_Button.clicked.connect(self.add_new_seller)
        self.add_art_Button.clicked.connect(self.add_new_article)
        self.buy_articl_name_lineEdit.hide()
        self.buy_choose_article_comboBox.hide()
        self.buy_new_article.clicked.connect(self.new_art_)
        self.buy_exists_article.clicked.connect(self.exists_art_)
        self.reset_buying_info_pushButton.clicked.connect(self.rest_btns)
        self.buy_art_stat = ''
        self.buy_choose_article_comboBox.currentTextChanged.connect(self.set_bb_article_type)
        self.sell_history_Button.clicked.connect(self.open_sell_history)
        self.buy_and_buy_history_Button.clicked.connect(self.open_buy_history)
        self.exit_Button.clicked.connect(self.exit)
        self.remove_client_Button.clicked.connect(self.delete_client)
        self.remove_seller_Button.clicked.connect(self.remove_seller)
        self.take_kridi_btn.clicked.connect(self.fix_C_kridi)
        self.pay_kridi_btn.clicked.connect(self.fix_S_kridi)
        self.C_kridi_history_btn.clicked.connect(self.c_k_history)
        self.S_kridi_history_btn.clicked.connect(self.s_k_history)
        self.edit_client_Button.clicked.connect(self.edit_client)
        self.edit_seller_Button.clicked.connect(self.edit_seller)
        self.edit_art_Button.clicked.connect(self.edit_article)
        # self.print_clients_table.clicked.connect(self.print_clients_info)
        self.searsh_client_EditText.textChanged.connect(self.searsh_clients)
        self.searsh_seller_EditText.textChanged.connect(self.searsh_sellers)
        self.searsh_art.textChanged.connect(self.searsh_articles)


    def searsh_articles(self):
        # self.searsh_art.setText('*' + self.searsh_art.text() + '*')
        if self.searsh_art.text() != '' or self.searsh_art.text() != ' ':
            #sellers table
            while self.articles_table.rowCount() > 0 :
                self.articles_table.removeRow(0)
            curs.execute('''
            SELECT name,  type, qt, price, note FROM articles 
                WHERE name LIKE "{}" OR type LIKE "{}" OR qt = "{}" OR price = "{}" OR note LIKE "{}"'''
            .format( '%' + str(self.searsh_art.text()) + '%', '%' + str(self.searsh_art.text()) + '%', '%' + self.searsh_art.text() + '%', '%' + self.searsh_art.text() + '%',
            '%' + self.searsh_art.text() + '%'))
            # print(curs.fetchall())
            rus__ = curs.fetchall()
            self.articles_table.setRowCount(0)
            for r_n, r_d in enumerate(rus__):
                self.articles_table.insertRow(r_n)
                for c_n, d in enumerate(r_d):
                    self.articles_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


        else:

            #sellers table
            while self.articles_table.rowCount() > 0 :
                self.articles_table.removeRow(0)
            curs.execute(
                'SELECT  name,  type, qt, price, note  FROM articles ORDER BY ID DESC;')
            rus__ = curs.fetchall()
            self.articles_table.setRowCount(0)
            for r_n, r_d in enumerate(rus__):
                self.articles_table.insertRow(r_n)
                for c_n, d in enumerate(r_d):
                    self.articles_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))






    def searsh_sellers(self):
        # self.searsh_seller_EditText.setText('*' + self.searsh_seller_EditText.text() + '*')
        if self.searsh_seller_EditText.text() != '' or self.searsh_seller_EditText.text() != ' ':
            #sellers table
            while self.sellers_table.rowCount() > 0 :
                self.sellers_table.removeRow(0)
            curs.execute('''
            SELECT F_name,  L_name, cne, total_debted, total_recived, total_rest, pay_date, note FROM sellers 
                WHERE F_name LIKE "{}" OR L_name LIKE "{}" OR cne LIKE "{}" OR total_debted = "{}" OR total_recived = "{}" OR pay_date LIKE "{}" OR note LIKE "{}"'''
            .format('%' + self.searsh_seller_EditText.text() + '%', '%' + self.searsh_seller_EditText.text() + '%', '%' + self.searsh_seller_EditText.text() + '%',
            '%' + self.searsh_seller_EditText.text() + '%', '%' + str(self.searsh_seller_EditText.text()) + '%', '%' + str(self.searsh_seller_EditText.text()) + '%', 
            '%' + self.searsh_seller_EditText.text() + '%'))
            # print(curs.fetchall())
            rus__ = curs.fetchall()
            self.sellers_table.setRowCount(0)
            for r_n, r_d in enumerate(rus__):
                self.sellers_table.insertRow(r_n)
                for c_n, d in enumerate(r_d):
                    self.sellers_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


        else:

            #sellers table
            while self.sellers_table.rowCount() > 0 :
                self.sellers_table.removeRow(0)
            curs.execute(
                'SELECT  F_name,  L_name, cne, total_debted, total_recived, total_rest, pay_date, note FROM sellers ORDER BY ID DESC;')
            rus__ = curs.fetchall()
            self.sellers_table.setRowCount(0)
            for r_n, r_d in enumerate(rus__):
                self.sellers_table.insertRow(r_n)
                for c_n, d in enumerate(r_d):
                    self.sellers_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

    def searsh_clients(self):
        # self.searsh_client_EditText.setText('*' + self.searsh_client_EditText.text() + '*')
        if self.searsh_client_EditText.text() != '' or self.searsh_client_EditText.text() != ' ':
            #clients table
            while self.clients_table.rowCount() > 0 :
                self.clients_table.removeRow(0)
            curs.execute('''
            SELECT F_name,  L_name, cne, total_debted, total_recived, total_rest, pay_date, note FROM clients 
                WHERE F_name LIKE "{}" OR L_name LIKE "{}" OR cne LIKE "{}" OR total_debted = "{}" OR total_recived = "{}" OR pay_date LIKE "{}" OR note LIKE "{}"'''
            .format('%' + self.searsh_client_EditText.text() + '%', '%' + self.searsh_client_EditText.text() + '%', '%' + self.searsh_client_EditText.text() + '%',
            '%' + self.searsh_client_EditText.text() + '%', '%' + str(self.searsh_client_EditText.text()) + '%', '%' + str(self.searsh_client_EditText.text()) + '%', 
            '%' + self.searsh_client_EditText.text() + '%'))
            # print(curs.fetchall())
            rus__ = curs.fetchall()
            self.clients_table.setRowCount(0)
            for r_n, r_d in enumerate(rus__):
                self.clients_table.insertRow(r_n)
                for c_n, d in enumerate(r_d):
                    self.clients_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


        else:

            #clients table
            while self.clients_table.rowCount() > 0 :
                self.clients_table.removeRow(0)
            curs.execute(
                'SELECT  F_name,  L_name, cne, total_debted, total_recived, total_rest, pay_date, note FROM clients ORDER BY ID DESC;')
            rus__ = curs.fetchall()
            self.clients_table.setRowCount(0)
            for r_n, r_d in enumerate(rus__):
                self.clients_table.insertRow(r_n)
                for c_n, d in enumerate(r_d):
                    self.clients_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


    #TODO PRINT 
    # self print_clients_info(self):
    #     pass

    def c_k_history(self):
        self.c_k_h = C_kridi_history()
        self.c_k_h.show()
        self.close()

    def s_k_history(self):
        self.c_k_h = S_kridi_history()
        self.c_k_h.show()
        self.close()

    def fix_C_kridi(self):
        self.close()
        self.fix_C_K = C_kridi_fix()
        self.fix_C_K.show()


    def fix_S_kridi(self):
        self.close()
        self.fix_S_K = S_kridi_fix()
        self.fix_S_K.show()

    def delete_client(self):
        self.close()
        self.delete_client_win = Remove_client()
        self.delete_client_win.show()

    def exit(self):
        conn.close()
        self.close()



    def set_bb_article_type(self):

        try:
            curs.execute(
                'SELECT type FROM articles WHERE name LIKE "{}";'.format(
                    self.buy_choose_article_comboBox.currentText()))
            self.buy_article_type_lineEdit.setText(curs.fetchone()[0])
        except Exception:
            print(Exception)

        curs.execute('SELECT price FROM articles WHERE name LIKE "{}"'.format(self.buy_choose_article_comboBox.currentText()))
        self.buy_article_price.setValue(curs.fetchone()[0])

    def new_art_(self):
        self.buy_art_stat = 'new'
        self.buy_articl_name_lineEdit.show()
        self.buy_new_article.hide()
        self.buy_exists_article.hide()
        self.buy_article_price.setEnabled(True)
        self.buy_article_type_lineEdit.setEnabled(True)

    def exists_art_(self):
        self.buy_art_stat = 'exists'
        self.buy_choose_article_comboBox.show()
        self.buy_exists_article.hide()
        self.buy_new_article.hide()
        self.buy_article_price.setEnabled(False)
        self.buy_article_type_lineEdit.setEnabled(False)
        self.buy_choose_article_comboBox.clear()
        self.articles_list_ = ['']
        curs.execute('SELECT name FROM articles WHERE qt > 0')
        for i in curs.fetchall():
            self.articles_list_.append(i[0])
        print(self.articles_list_)
        self.buy_choose_article_comboBox.addItems(self.articles_list_)

    def rest_btns(self):
        self.buy_art_stat = ''
        self.buy_articl_name_lineEdit.hide()
        self.buy_choose_article_comboBox.hide()
        self.buy_exists_article.show()
        self.buy_new_article.show()
        self.buy_article_price.setEnabled(True)
        self.buy_article_type_lineEdit.setEnabled(True)

    def log_out(self):
        curs.execute('SELECT first FROM tools')
        if curs.fetchone()[0] == 1:
            self.close()
            self.log_out = VirificationAlert()
            self.log_out.show()
        else:
            self.exit()

    def refresh_data(self):  # refresh all app data
        self.refresh_labels()
        self.refresh_tables()
        self.fill_combos()


    def onTabChange(self): #todo Fix this shit
        print('the current tab is : ', self.home_tabWidget.currentIndex())
        self.refresh_data()
        if self.home_tabWidget.currentIndex() == 0:
            # current_tab = 0
            self.setWindowTitle('الرئيسية')

        elif self.home_tabWidget.currentIndex() == 1:
            # current_tab = 1
            self.setWindowTitle('معاملات')

        elif self.home_tabWidget.currentIndex() == 2:
            # current_tab = 2
            self.setWindowTitle('الزبائن')

        elif self.home_tabWidget.currentIndex() == 3:
            # current_tab = 3
            self.setWindowTitle('الموزعين')

        elif self.home_tabWidget.currentIndex() == 4:
            # current_tab = 4
            self.setWindowTitle('السلع')


    def refresh_labels(self):
        curs.execute('SELECT NAME FROM user')
        self.wilcom_label.setText('مرحبا بالسيد ' + curs.fetchone()[0])
        self.date_time_label.setText(str(today))
        curs.execute('SELECT hadit FROM hadit ;')
        self.hadit_list = []
        for i in curs.fetchall():
            self.hadit_list.append(i[0])
        self.hadit_label.setText(random.choice(self.hadit_list))
        # print(self.hadit_list)
        curs.execute('SELECT sum(total_rest) FROM C_kridi')
        total_rest_C = curs.fetchone()[0]
        
        self.total_money_debt.setText(str(total_rest_C))
        self.total_money_debt.setText(self.total_money_debt.text() + ' DH ')
        curs.execute('SELECT sum(total_rest) FROM S_kridi ')
        total_debt_S = curs.fetchone()[0]
        
        self.money_u_have_to_pay.setText(str(total_debt_S))
        self.money_u_have_to_pay.setText(self.money_u_have_to_pay.text() + ' DH ')
        print( 'set_total_sellers_dept_money', total_debt_S)

        curs.execute('SELECT COUNT(ID) FROM clients WHERE total_rest > 0;')
        self.clients_debteds_counter.setText(str(curs.fetchone()[0]))
        curs.execute('SELECT COUNT(ID) FROM clients WHERE pay_date LIKE "{}"'.format(str(today)))
        # print(curs.fetchone()[0] == str(today))
        clients_pay_today_list = curs.fetchone()[0]
        
        self.clients_must_pay_counter_today.setText(str(clients_pay_today_list))



    def refresh_tables(self):
        curs.execute('UPDATE clients SET total_rest = total_debted - total_recived')
        curs.execute('UPDATE sellers SET total_rest = total_debted - total_recived')
        curs.execute('DELETE FROM C_kridi WHERE total_rest = 0')
        curs.execute('DELETE FROM S_kridi WHERE total_rest = 0')
        curs.execute('DELETE FROM articles WHERE qt = 0')
        conn.commit()
        #clients have to pay today table
        while self.clients_pay_today_table.rowCount() > 0 :
            self.clients_pay_today_table.removeRow(0)

        curs.execute('SELECT  name , total_rest FROM C_kridi  WHERE pay_date LIKE "{}"'.format(str(today)))
        rus_ = curs.fetchall()
        self.clients_pay_today_table.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.clients_pay_today_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.clients_pay_today_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

        print('rus_- = ', rus_)


        #articles will end table
        while self.articles_will_end.rowCount() > 0 :
            self.articles_will_end.removeRow(0)

        curs.execute('SELECT  name , qt FROM articles  WHERE qt < 10 ')
        rus_ = curs.fetchall()
        self.articles_will_end.setRowCount(0)
        for r_n, r_d in enumerate(rus_):
            self.articles_will_end.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.articles_will_end.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))



        #clients table
        while self.clients_table.rowCount() > 0 :
            self.clients_table.removeRow(0)
        curs.execute(
            'SELECT  F_name,  L_name, cne, total_debted, total_recived, total_rest, pay_date, note FROM clients ORDER BY ID DESC;')
        rus__ = curs.fetchall()
        self.clients_table.setRowCount(0)
        for r_n, r_d in enumerate(rus__):
            self.clients_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.clients_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

        print(curs.fetchall())
        #
        #TODO : contuni with all tables
        #sellers table
        while self.sellers_table.rowCount() > 0 :
            self.sellers_table.removeRow(0)

        curs.execute(
            'SELECT  F_name,  L_name, cne, total_debted, total_recived, total_rest, pay_date, note FROM sellers ORDER BY ID DESC;')
        rus__ = curs.fetchall()
        self.sellers_table.setRowCount(0)
        for r_n, r_d in enumerate(rus__):
            self.sellers_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.sellers_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


        #articles table

        while self.articles_table.rowCount() > 0 :
            self.articles_table.removeRow(0)
        curs.execute(
            'SELECT name, type, qt, price, note FROM articles ORDER BY ID DESC;')
        rus__ = curs.fetchall()
        self.articles_table.setRowCount(0)
        for r_n, r_d in enumerate(rus__):
            self.articles_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.articles_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))

        while self.C_kridi_table.rowCount() > 0 :
            self.C_kridi_table.removeRow(0)
        curs.execute(
            'SELECT name, cne, total_rest FROM C_kridi ORDER BY ID DESC;')
        rus__ = curs.fetchall()
        self.C_kridi_table.setRowCount(0)
        for r_n, r_d in enumerate(rus__):
            self.C_kridi_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.C_kridi_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


        while self.S_kridi_table.rowCount() > 0 :
            self.S_kridi_table.removeRow(0)
        curs.execute(
            'SELECT name, cne, total_rest FROM S_kridi ORDER BY ID DESC;')
        rus__ = curs.fetchall()
        self.S_kridi_table.setRowCount(0)
        for r_n, r_d in enumerate(rus__):
            self.S_kridi_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.S_kridi_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))



        #clients kridi
        while self.S_kridi_table.rowCount() > 0 :
            self.S_kridi_table.removeRow(0)
        curs.execute(
            'SELECT name, cne, total_rest FROM S_kridi ORDER BY ID DESC;')
        rus__ = curs.fetchall()
        self.S_kridi_table.setRowCount(0)
        for r_n, r_d in enumerate(rus__):
            self.S_kridi_table.insertRow(r_n)
            for c_n, d in enumerate(r_d):
                self.S_kridi_table.setItem(r_n, c_n, QtWidgets.QTableWidgetItem(str(d)))


    def fill_combos(self):

        self.sell_choose_article_comboBox.clear()
        self.sell_choose_buyer_comboBox.clear()
        self.buy_choose_seller_comboBox.clear()
        self.articles_list_  = ['']
        curs.execute('SELECT name FROM articles WHERE qt > 0')
        for i in curs.fetchall():
            self.articles_list_.append(i[0])
        print(self.articles_list_)
        self.sell_choose_article_comboBox.addItems(self.articles_list_)

        clients_names_list_ = []

        curs.execute('SELECT F_name, L_name  FROM clients')
        for fn, ln in curs.fetchall():

            clients_names_list_.append(fn + ' ' + ln)
        print('CLIENTS : ', clients_names_list_)
        self.sell_choose_buyer_comboBox.addItems(clients_names_list_)

        selers_names_list_ = ['']
        curs.execute('SELECT F_name, L_name FROM sellers ')
        for sfn, sln in curs.fetchall():
            selers_names_list_.append(sfn + ' ' + sln)
        print('SELLRES : ', selers_names_list_)
        self.buy_choose_seller_comboBox.addItems(selers_names_list_)

    def set_sell_article_type(self):
        print(str(self.sell_choose_article_comboBox.currentText()))
        # r_count = curs.execute('SELECT COUNT(*) FROM articles')
        # print('articles table has {} rows '.format(str(r_count.fetchone())))
        if self.sell_choose_article_comboBox.currentText() == '' or self.sell_choose_article_comboBox.currentText() == ' ':
            self.sell_article_type.setText('')
        else:
            self.sell_qt.lineEdit().setEnabled(True)
            curs.execute('SELECT type FROM articles WHERE name like "{}"'.format(
                str(self.sell_choose_article_comboBox.currentText())))
            self.sell_article_type.setText(curs.fetchone()[0])
            curs.execute('SELECT qt FROM articles WHERE name like "{}"'.format(
                str(self.sell_choose_article_comboBox.currentText())))
            self.sell_qt.setMaximum(curs.fetchone()[0])

    def on_sell_qt_spin_box_changed(self):
        if str(self.sell_choose_article_comboBox.currentText()) != '' or str(self.sell_choose_article_comboBox.currentText()) != '':
            curs.execute('SELECT price FROM articles WHERE name like "{}"'.format(
                    str(self.sell_choose_article_comboBox.currentText())))
            total_price = self.sell_qt.value() * curs.fetchone()[0]
            self.total_selling_price.setText(str(total_price) + ' DH')
        else:
            self.total_selling_price.setText('إختر سلعة لإظهار المجموع')

    def on_buy_qt_spin_box_changed(self):
        if self.buy_art_stat == 'exists':
            if str(self.buy_choose_article_comboBox.currentText()) != '' or str(self.buy_choose_article_comboBox.currentText()) != '':
                curs.execute('SELECT price FROM articles WHERE name like "{}"'.format(
                        str(self.buy_choose_article_comboBox.currentText())))
                total_price = self.buy_article_qt.value() * curs.fetchone()[0]
                self.total_buying_price.setText(str(total_price) + ' DH')
            else:
                self.total_buying_price.setText('إختر سلعة لإظهار المجموع')
        elif self.buy_art_stat == 'new':
            total_price = self.buy_article_qt.value() * self.buy_article_price.value()
            self.total_buying_price.setText(str(total_price) + ' DH')


    def save_sell_operation(self):
        if str(self.sell_choose_article_comboBox.currentText()) == '' or  str(self.sell_choose_article_comboBox.currentText()) == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إختيار سلعة ')
            self.err.setWindowTitle('خطأ')
            self.sell_choose_article_comboBox.setFocus()
        elif str(self.sell_choose_buyer_comboBox.currentText()) == '' or  str(self.sell_choose_buyer_comboBox.currentText()) == ' ':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إختيار زبون')
            self.err.setWindowTitle('خطأ')
            self.sell_choose_buyer_comboBox.setFocus()
        elif self.sell_qt.value() == 0:
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('لايمكن بيع هذه الكمية')
            self.err.setWindowTitle('خطأ')
            self.sell_qt.setFocus()
        elif self.sell_pay_by_debt_radioButton.isChecked():
            curs.execute('SELECT price FROM articles WHERE name LIKE "{}" '.format(
                self.sell_choose_article_comboBox.currentText()))
            price = curs.fetchone()[0]

            curs.execute('SELECT name FROM C_kridi ')
            cll = []
            for n in curs.fetchall():
                cll.append(n[0])
            tt = self.sell_qt.value() * price
            if self.sell_choose_buyer_comboBox.currentText() in cll:
                curs.execute(
                    'UPDATE C_kridi SET debte = debte + {} , pay_date = "{}" WHERE name LIKE "{}"'
                        .format(tt, str(self.sell_date_to_pay.date().toPyDate()),
                                self.sell_choose_buyer_comboBox.currentText()))
                curs.execute('UPDATE C_kridi SET total_rest = debte - total_recived')
                conn.commit()
            else:
                cne = curs.execute('SELECT cne FROM clients WHERE F_name LIKE "{}" AND L_name LIKE "{}" '
                                   .format(self.sell_choose_buyer_comboBox.currentText().split(' ')[0],
                                           self.sell_choose_buyer_comboBox.currentText().split(' ')[1]))

                curs.execute('''
                                                 INSERT INTO C_kridi(name, cne, debte, total_recived, pay_date) VALUES("{}", "{}", {}, 0, "{}")
                                                              '''.format(self.sell_choose_buyer_comboBox.currentText(),
                                                                         cne.fetchone()[0], int(tt),
                                                                         self.sell_date_to_pay.date().toPyDate()))
                curs.execute('UPDATE C_kridi SET total_rest = debte - total_recived')

                conn.commit()
            curs.execute('''
            UPDATE articles 
            SET qt = qt - {}
             WHERE name LIKE "{}";
             '''.format( self.sell_qt.value()
                         , self.sell_choose_article_comboBox.currentText()))

            curs.execute('''
            SELECT price 
            FROM articles 
            WHERE name LIKE "{}";
             '''.format(self.sell_choose_article_comboBox.currentText()))

            curs.execute('''
            UPDATE clients SET
            total_debted = total_debted + {}
            WHERE F_name like "{}"
            AND L_name like "{}" ;
            '''.format(self.sell_qt.value() * curs.fetchone()[0]
                       , self.sell_choose_buyer_comboBox.currentText().split(' ')[0]
                       , self.sell_choose_buyer_comboBox.currentText().split(' ')[1] ))


            curs.execute('''
            UPDATE clients SET
            pay_date = "{}"
            WHERE F_name like "{}"
            AND L_name like "{}" ;
            '''.format(str(self.sell_date_to_pay.date().toPyDate())
                       , self.sell_choose_buyer_comboBox.currentText().split(' ')[0]
                       , self.sell_choose_buyer_comboBox.currentText().split(' ')[1] ))


            curs.execute('''
                                    SELECT price 
                                    FROM articles 
                                    WHERE name LIKE "{}";
                                     '''.format(self.sell_choose_article_comboBox.currentText()))
            curs.execute('''
                                    INSERT INTO selles_history (date, client, article, qt, not_payed_yet, pay_date) VALUES("{}", "{}", "{}", {}, {}, "{}") ;
                                    '''.format(today, self.sell_choose_buyer_comboBox.currentText(),
                                               self.sell_choose_article_comboBox.currentText(),
                                               self.sell_qt.value(), self.sell_qt.value() * curs.fetchone()[0],
                                               str(self.sell_date_to_pay.date().toPyDate())))


            conn.commit()
            print(self.sell_date_to_pay.date().toPyDate())
            self.sell_choose_article_comboBox.setCurrentIndex(0)
            self.sell_choose_buyer_comboBox.setCurrentIndex(0)
            self.sell_qt.setValue(0)
            self.refresh_data()
        else:
            curs.execute('''
                        UPDATE articles 
                        SET qt = qt - {}
                         WHERE name LIKE "{}";
                         '''.format(self.sell_qt.value()
                                    , self.sell_choose_article_comboBox.currentText()))

            curs.execute('''
                        SELECT price 
                        FROM articles 
                        WHERE name LIKE "{}";
                         '''.format(self.sell_choose_article_comboBox.currentText()))

            curs.execute('''
                        INSERT INTO selles_history (date, client, article, qt, payed, pay_date) VALUES("{}", "{}", "{}", {}, {}, "{}") 
                        '''.format(today, self.sell_choose_buyer_comboBox.currentText(), self.sell_choose_article_comboBox.currentText(),
                                   self.sell_qt.value(),self.sell_qt.value() * curs.fetchone()[0], str(self.sell_date_to_pay.date().toPyDate()) ))

            conn.commit()
            print('DONE')
            self.sell_choose_article_comboBox.setCurrentIndex(0)
            self.sell_choose_buyer_comboBox.setCurrentIndex(0)
            self.sell_qt.setValue(0)
            self.refresh_data()


    def save_buy_operation(self):

        print(self.buy_art_stat)
        if self.buy_art_stat == '':
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('المرجو إدخال إسم السلعة ')
            self.err.setWindowTitle('خطأ')

        if self.buy_art_stat == 'new':
            if self.buy_articl_name_lineEdit.text() == '' or self.buy_articl_name_lineEdit.text() == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('المرجو إدخال إسم السلعة ')
                self.err.setWindowTitle('خطأ')
                self.buy_articl_name_lineEdit.setFocus()

            elif self.buy_article_type_lineEdit.text() == '' or self.buy_article_type_lineEdit.text() == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('المرجو إدخال نوع السلعة ')
                self.err.setWindowTitle('خطأ')
                self.buy_article_type_lineEdit.setFocus()

            elif str(self.buy_choose_seller_comboBox.currentText()) == '' or str(
                    self.buy_choose_seller_comboBox.currentText()) == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('المرجو اختيار الموزع')
                self.err.setWindowTitle('خطأ')
                self.buy_choose_seller_comboBox.setFocus()

            elif self.buy_article_price.value() == 0:
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('لا يمكنك ترك الثمن 0 درهم')
                self.err.setWindowTitle('خطأ')
                self.buy_article_price.setFocus()

            elif self.buy_article_qt.value() == 0:
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('لا يمكنك ترك الكمية 0')
                self.err.setWindowTitle('خطأ')
                self.buy_article_price.setFocus()

            elif self.buy_pay_by_debt_radioButton.isChecked():

                ##########################
                # curs.execute('SELECT price FROM articles WHERE name LIKE "{}" '.format(self.sell_choose_article_comboBox.currentText()))
                price = self.buy_article_price.value()

                curs.execute('SELECT name FROM S_kridi ')
                Sll = []
                for n in curs.fetchall():
                    Sll.append(n[0])
                tt = self.buy_article_qt.value() * price
                if self.buy_choose_seller_comboBox.currentText() in Sll:
                    curs.execute(
                        'UPDATE S_kridi SET debte = debte + {} , pay_date = "{}" WHERE name LIKE "{}"'
                            .format(tt, str(self.buy_date_to_pay.date().toPyDate()),
                                    self.buy_choose_seller_comboBox.currentText()))
                    curs.execute('UPDATE S_kridi SET total_rest = debte - total_recived')
                    conn.commit()
                else:
                    cne = curs.execute('SELECT cne FROM sellers WHERE F_name LIKE "{}" AND L_name LIKE "{}" '
                                       .format(self.buy_choose_seller_comboBox.currentText().split(' ')[0],
                                               self.buy_choose_seller_comboBox.currentText().split(' ')[1]))

                    curs.execute('''
                                 INSERT INTO S_kridi(name, cne, debte, total_recived, pay_date) VALUES("{}", "{}", {}, 0, "{}")
                                 '''.format(
                        self.buy_choose_seller_comboBox.currentText(),
                        cne.fetchone()[0], int(tt),
                        self.buy_date_to_pay.date().toPyDate()))
                    curs.execute('UPDATE S_kridi SET total_rest = debte - total_recived')

                    conn.commit()
                ###############################

                curs.execute('''
                              INSERT INTO articles
                                          (name, type, qt, price) VALUES ("{}", "{}", {}, {});
                                          '''.format(self.buy_articl_name_lineEdit.text(),
                                                     self.buy_article_type_lineEdit.text(), self.buy_article_qt.value(),
                                                     self.buy_article_price.value()))

                curs.execute('UPDATE sellers SET total_debted = total_debted + {}, pay_date = "{}"  WHERE F_name LIKE "{}" AND L_name LIKE "{}";'.format(
                    self.buy_article_price.value() * self.buy_article_qt.value(), str(self.buy_date_to_pay.date().toPyDate())
                        , self.buy_choose_seller_comboBox.currentText().split(' ')[0], self.buy_choose_seller_comboBox.currentText().split(' ')[1]))

                curs.execute('INSERT INTO buys_history (date, seller, article, qt, not_payed_yet, pay_date) VALUES("{}", "{}", "{}", {}, {}, "{}") ;'
                             .format(today, self.buy_choose_seller_comboBox.currentText(), self.buy_articl_name_lineEdit.text(), self.buy_article_qt.value()
                                     , self.buy_article_price.value() * self.buy_article_qt.value(), str(self.buy_date_to_pay.date().toPyDate())))




            else:

                curs.execute('''INSERT INTO articles
                                 (name, type, qt, price) VALUES ("{}", "{}", {}, {});
                                                          '''.format(self.buy_articl_name_lineEdit.text(),
                                                                     self.buy_article_type_lineEdit.text(),
                                                                     self.buy_article_qt.value(),
                                                                     self.buy_article_price.value()))

                curs.execute(
                    'UPDATE sellers SET total_recived = total_recived + {}, pay_date = "{}"  WHERE F_name LIKE "{}" AND L_name LIKE "{}";'.format(
                        self.buy_article_price.value() * self.buy_article_qt.value(),
                        today
                        , self.buy_choose_seller_comboBox.currentText().split(' ')[0],
                        self.buy_choose_seller_comboBox.currentText().split(' ')[1]))

                curs.execute(
                    '''INSERT INTO buys_history
                     (date, seller, article, qt, payed, pay_date) 
                     VALUES("{}", "{}", "{}", {}, {}, "{}") ;
                     '''.format(today, self.buy_choose_seller_comboBox.currentText(), self.buy_articl_name_lineEdit.text(),
                            self.buy_article_qt.value()
                            , self.buy_article_price.value() * self.buy_article_qt.value(),
                            today))


            conn.commit()
        elif self.buy_art_stat == 'exists':
            if self.buy_choose_article_comboBox.currentText() == '' or self.buy_choose_article_comboBox.currentText() == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('المرجو إختيار إسم السلعة ')
                self.err.setWindowTitle('خطأ')
                self.buy_choose_article_comboBox.setFocus()


            elif self.buy_article_type_lineEdit.text() == '' or self.buy_article_type_lineEdit.text() == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('المرجو إدخال نوع السلعة ')
                self.err.setWindowTitle('خطأ')
                self.buy_article_type_lineEdit.setFocus()

            elif str(self.buy_choose_seller_comboBox.currentText()) == '' or str(self.buy_choose_seller_comboBox.currentText()) == ' ':
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('المرجو اختيار الموزع')
                self.err.setWindowTitle('خطأ')
                self.buy_choose_seller_comboBox.setFocus()

            # elif self.buy_article_price.value() == 0:
            #     self.err = QtWidgets.QErrorMessage()
            #     self.err.showMessage('لا يمكنك ترك الثمن 0 درهم')
            #     self.err.setWindowTitle('خطأ')
            #     self.buy_article_price.setFocus()

            elif self.buy_article_qt.value() == 0:
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('لا يمكنك ترك الكمية 0')
                self.err.setWindowTitle('خطأ')
                self.buy_article_price.setFocus()

            elif self.buy_pay_by_debt_radioButton.isChecked():

                ##########################
                curs.execute('SELECT price FROM articles WHERE name LIKE "{}" '.format(self.buy_choose_article_comboBox.currentText()))
                price = curs.fetchone()

                curs.execute('SELECT name FROM S_kridi ')
                Sll = []
                for n in curs.fetchall():
                    Sll.append(n[0])
                tt = self.buy_article_qt.value() * price
                if self.buy_choose_seller_comboBox.currentText() in Sll:
                    curs.execute(
                        'UPDATE S_kridi SET debte = debte + {} , pay_date = "{}" WHERE name LIKE "{}"'
                            .format(tt, str(self.buy_date_to_pay.date().toPyDate()),
                                    self.buy_choose_seller_comboBox.currentText()))
                    curs.execute('UPDATE S_kridi SET total_rest = debte - total_recived')
                    conn.commit()
                else:
                    cne = curs.execute('SELECT cne FROM sellers WHERE F_name LIKE "{}" AND L_name LIKE "{}" '
                                       .format(self.buy_choose_seller_comboBox.currentText().split(' ')[0],
                                               self.buy_choose_seller_comboBox.currentText().split(' ')[1]))

                    curs.execute('''
                                 INSERT INTO S_kridi(name, cne, debte, total_recived, pay_date) VALUES("{}", "{}", {}, 0, "{}")
                                 '''.format(
                        self.buy_choose_seller_comboBox.currentText(),
                        cne.fetchone()[0], int(tt),
                        self.buy_date_to_pay.date().toPyDate()))
                    curs.execute('UPDATE S_kridi SET total_rest = debte - total_recived')

                    conn.commit()
                ###############################


                curs.execute('''
                UPDATE articles SET qt = qt - {} WHERE name LIKE "{}"
                '''.format(self.buy_article_qt.value(), self.buy_choose_article_comboBox.currentText()))



                curs.execute(
                    'UPDATE sellers SET total_debted = total_debted + {}, pay_date = "{}"  WHERE F_name LIKE "{}" AND L_name LIKE "{}";'.format(
                        self.buy_article_price.value() * self.buy_article_qt.value(),
                        str(self.buy_date_to_pay.date().toPyDate())
                        , self.buy_choose_seller_comboBox.currentText().split(' ')[0],
                        self.buy_choose_seller_comboBox.currentText().split(' ')[1]))

                curs.execute(
                    'INSERT INTO buys_history (date, seller, article, qt, not_payed_yet, pay_date) VALUES("{}", "{}", "{}", {}, {}, "{}") ;'
                    .format(today, self.buy_choose_seller_comboBox.currentText(), self.buy_choose_article_comboBox.currentText(),
                            self.buy_article_qt.value()
                            , self.buy_article_price.value() * self.buy_article_qt.value(),
                            str(self.buy_date_to_pay.date().toPyDate())))
            else:

                curs.execute('''
                UPDATE articles SET qt = qt - {} WHERE name LIKE "{}"
                '''.format(self.buy_article_qt.value(), self.buy_choose_article_comboBox.currentText()))

                curs.execute(
                    'UPDATE sellers SET total_recived = total_recived + {}, pay_date = "{}"  WHERE F_name LIKE "{}" AND L_name LIKE "{}";'.format(
                        self.buy_article_price.value() * self.buy_article_qt.value(),
                        today
                        , self.buy_choose_seller_comboBox.currentText().split(' ')[0],
                        self.buy_choose_seller_comboBox.currentText().split(' ')[1]))

                curs.execute(
                    '''INSERT INTO buys_history
                     (date, seller, article, qt, payed, pay_date) 
                     VALUES("{}", "{}", "{}", {}, {}, "{}") ;
                     '''.format(today, self.buy_choose_seller_comboBox.currentText(),
                                self.buy_choose_article_comboBox.currentText(),
                                self.buy_article_qt.value()
                                , self.buy_article_price.value() * self.buy_article_qt.value(),
                                today))

            conn.commit()

    def open_sell_history(self):
        self.selles_history_wn = Selles_history()
        self.selles_history_wn.show()
        self.close()
        print('sell win opened')

    def open_buy_history(self):
        self.close()
        self.buy_history_wn = Buyes_history()
        self.buy_history_wn.show()

    def add_new_client(self):
        self.close()
        self.add_client_wn = ADD_new_client()
        self.add_client_wn.show()

    

    def edit_client(self):
        self.close()
        self.edite = Edite_client()
        self.edite.show()

    def search_client(self):
        pass

    def add_new_seller(self):
        self.close()
        self.add_seller_wn = ADD_new_seller()
        self.add_seller_wn.show()

    def remove_seller(self):
        self.close()
        self.delete_seller_win = Remove_seller()
        self.delete_seller_win.show()

    def edit_seller(self):
        self.close()
        self.edite = Edite_seller()
        self.edite.show()

    def search_seller(self):
        pass

    def add_new_article(self):
        self.close()
        self.add_art_wn = ADD_new_art()
        self.add_art_wn.show()

    def remove_article(self):
        pass

    def edit_article(self):
        self.close()
        self.edit_art = Edite_art()
        self.edit_art.show()

    def search_article(self):
        pass
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

class Reset_pass(QMainWindow, first_open_win_dir):
    def __init__(self, parent=None):
        super(Reset_pass, self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('إستعادة كلمة المرور ')
        self.save_btn.clicked.connect(self.reset__)
        self.safe_mod_checkBox.hide()
        # .setEchoMode(QtGui.QLineEdit.Password)
        self.pass_entry.setEchoMode(QLineEdit.Password)
        self.pass_confirmation.setEchoMode(QLineEdit.Password)

    def reset__(self):
        curs.execute('SELECT NAME FROM user;')
        curent_user_name = curs.fetchone()[0]
        print('the user name is : ', curent_user_name)

        if self.user_name_entry.text() == '':
            self.err = QErrorMessage()
            self.err.showMessage('يجب ملأ إسم المستخدم')
            self.err.setWindowTitle('خطأ في إسم المستخدم ')
            self.user_name_entry.setFocus()

        elif self.pass_entry.text() == '':
            self.err = QErrorMessage()
            self.err.showMessage('يجب ملأ كلمة مرور')
            self.err.setWindowTitle('خطأ في كلمة مرور')
            self.pass_entry.setFocus()

        elif self.pass_confirmation.text() == '':
            self.err = QErrorMessage()
            self.err.showMessage('يجب إعادة كلمة مرور')
            self.err.setWindowTitle('خطأ في إعادة كلمة مرور')
            self.pass_confirmation.setFocus()

        elif self.pass_entry.text() != self.pass_confirmation.text():
            self.err = QErrorMessage()
            self.err.showMessage('كلمات المرور غير متطابقة')
            self.err.setWindowTitle('خطأ في كلمة مرور')
            self.pass_confirmation.setFocus()

        elif self.user_name_entry.text() != curent_user_name:
            self.err = QErrorMessage()
            self.err.showMessage('لقد أدخلت إسم المستخدم خاطئ')
            self.err.setWindowTitle('إسم المستخدم خاطئ')
            self.user_name_entry.setFocus()

        else:
            curs.execute('SELECT PASSWORD FROM user ;')
            if self.pass_confirmation.text() == curs.fetchone()[0]:
                self.err = QErrorMessage()
                self.err.showMessage('يجب إختيار كلمة مرور لا تشبه القديمة')
                self.err.setWindowTitle('كلمة مرور موجودة بالفعل ')
                self.pass_entry.setFocus()
            else:
                curs.execute('UPDATE user SET PASSWORD = "{}";'.format(self.pass_confirmation.text()))
                conn.commit()
                self.back_to_app = VirificationAlert()
                self.back_to_app.show()
                self.close()

class VirificationAlert(QWidget, virification_alert_win_dir):
    def __init__(self, parent = None):
        super(VirificationAlert, self).__init__(parent)
        QWidget.__init__(self)
        self.setupUi(self)
        self.setFixedSize(289,161)
        self.virif_btn.clicked.connect(self.virife_password)
        self.virif_pass_line.setEchoMode(QLineEdit.Password)
        self.help.mousePressEvent = self.get_help
        self.reset_password.mousePressEvent = self.get_reset_password

    def virife_password(self):
        curs.execute('SELECT PASSWORD FROM user')
        curent_pass = curs.fetchone()
        print(curent_pass[0])

        if self.virif_pass_line.text() !='':
            if curent_pass[0] == self.virif_pass_line.text():
                print('yes {} is same '.format(curent_pass[0]))
                self.home_wn = Home()
                self.home_wn.show()
                self.close()

            else:
                self.err = QtWidgets.QErrorMessage()
                self.err.showMessage('كلمة مرور غير صحيحة ')
                self.err.setWindowTitle('خطأ')
                self.virif_pass_line.setFocus()
                self.virif_pass_line.setText('')
        else:
            self.err = QtWidgets.QErrorMessage()
            self.err.showMessage('كلمة مرور غير صالحة ')
            self.err.setWindowTitle('خطأ')
            self.virif_pass_line.setFocus()

    def get_reset_password(self, event):
        print('the reset password was clicked')
        self.reset_pass_wn = Reset_pass()
        self.reset_pass_wn.show()
        self.close()



    def get_help(self, event):
        print('the help was clicked')

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
#TODO
# class Setting(QWidget, setting_win_dir):
#     def __init__(self, parent = None):
#         super(Setting, self).__init__(parent)
#         QWidget.__init__(self)
#         self.setupUi(self)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class History(QWidget, history_win_dir):
#     def __init__(self, parent = None):
#         super(History, self).__init__(parent)
#         QWidget.__init__(self)
#         self.setupUi(self)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# class Help(QWidget, history_win_dir):
#     def __init__(self, parent = None):
#         super(History, self).__init__(parent)
#         QWidget.__init__(self)
#         self.setupUi(self)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def delay_counter():
    curs.execute('SELECT delay FROM tools;')
    delay = curs.fetchone()[0]
    while True:
        delay += 1
        time.sleep(1)
        print(delay)
        if delay == 180000:
            break




def main():
    app = QtWidgets.QApplication(sys.argv)
    splash_wn = Splash()
    splash_wn.show()
    sys.exit(app.exec_())
#
# pr1 = mp.Process(target=main)
# pr2 =mp.Process(target=delay_counter)
# pr1.start()
# pr2.start()
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

if __name__ == '__main__' :
    main()
