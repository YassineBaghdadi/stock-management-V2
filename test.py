
import sqlite3

conn = sqlite3.connect('src/db.db')
curs = conn.cursor()
# name = str(input('name : ' ))
# print(name, type(name))
# cne = str(input('cne : ' ))
# print(cne, type(cne))
# debte = int(input('debte : ' ))
# print(debte, type(debte))
# pay_dete = str(input('pay_date : ' ))
# print(pay_dete, type(pay_dete))
# curs.execute('''
#                          INSERT INTO C_kridi(name, cne, debte,  pay_date) VALUES('{}', '{}', {}, '{}')
#                                       '''.format(str(name), cne, int(debte),
#                                                  pay_dete))

# curs.execute('UPDATE C_kridi SET total_rest = debte - total_recived')
curs.execute('SELECT price FROM articles WHERE name LIKE "{}" '.format('banan'))
price = curs.fetchone()[0]
print(price)
conn.commit()