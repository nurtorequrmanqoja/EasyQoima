import sqlite3

import numpy
import tabula
import pandas as pd
import math
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

list_lower_right = ["a1", "a3", "a5", "a7"]
list_lower_right2 = ["a1", "a3", "a5", "a7", "no place"]
no_place = "no place"
list_place = []
def read_pdf():
    file_path = 'order2.pdf'
    dfs = []
    pages = tabula.read_pdf(file_path, pages='all', encoding='utf-8', errors='ignore')
    for page in pages:
        dfs.append(page)
    combined_df = pd.concat(dfs)
    # df1 = tabula.read_pdf_with_template(file_path, multiple_tables=True)
    # for i in df1[0].index[3:]:
    #     id_book = df1[0].values[i][1]
    return combined_df


def connect_db(table):
    con = sqlite3.connect('db/lower_right.db')
    cur = con.cursor()
    sql = "SELECT * FROM {place}".format(place=table)
    cur.execute(sql) 
    rows = cur.fetchall()
    return rows

def save_book_place(table, id_book, name_book, amount, pack_divided_amout):
    list_place.append([table, id_book, name_book, amount, pack_divided_amout])

def sort_list(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if list_lower_right2.index(arr[j][0]) > list_lower_right2.index(arr[j+1][0]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if (swapped == False):
            break
def write_pdf():

    pdf = canvas.Canvas('example.pdf')
    font_path = 'fonts/Kz_Ante_kz.ttf'
    pdfmetrics.registerFont(TTFont('myfont', font_path))


    x = 50
    y = 800
    z = y
    line_height = 20
    count = 0
    for i in list_place:
        pdf.setFont('myfont', 10)
        pdf.drawString(x, y, str(i))
        y -= line_height
        count += line_height

        if count >= z:
            pdf.showPage()
            count = 0
            y = 800
    pdf.save()


def find_book_place():
    index = 0
    file_path = 'order2.pdf'
    pages = tabula.read_pdf(file_path, pages='all', encoding='cp1251 ')
    for page in pages:
        if index == 0:
            start = page.index[3:]
        else:
            start = page.index
        for line in start:
            status = 0
            id_book = page.values[line][1]
            name_book = page.values[line][2]
            amount = int(page.values[line][6])
            if math.isnan(float(page.values[line][0])):
                pack_divided_amout = "Пачкадағы штук саны белгісіз"
            else:
                number_pieces_pack = int(page.values[line][0])
                pack_divided_amout = "(" + str(amount // number_pieces_pack) + " пачка " + str(amount % number_pieces_pack) + " шт)"

            for table in list_lower_right:
                rows = connect_db(table)
                for row in rows:
                    if id_book == row[0]:
                        # print(table + " - " + name_book)
                        save_book_place(table, id_book, name_book, amount, pack_divided_amout)
                        status = 1

            if status == 0:
                # print(no_place + " - " + name_book)
                save_book_place(no_place, id_book, name_book, amount, pack_divided_amout)
        index += 1
    # print(len(list_place))
    # print(sorted(list_place))
    # list_placed = sorted(list_place)

    # write_pdf()
    sort_list(list_place)
    for i in list_place:
        print(i)