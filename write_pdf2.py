import functions
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors

def write_pdf():
    pdfmetrics.registerFont(TTFont('MyFont', 'fonts/Alice-Regular_kz.ttf'))
    # Пример данных в формате Pandas DataFrame
    data = functions.list_place

    df = pd.DataFrame(data)

    # Преобразуем данные в формат списка списков
    data_list = [df.columns.tolist()] + df.values.tolist()

    # Создаем PDF-документ
    pdf_file = "table_example.pdf"
    pdf = SimpleDocTemplate(pdf_file, pagesize=letter)

    # Определяем стили для таблицы
    table_style = [('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                   ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                   ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                   ('FONTNAME', (0, 0), (-1, -1), 'MyFont'),
                   ('FONTSIZE', (0, 0), (-1, 0), 12),
                   ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                   ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                   ('GRID', (0, 0), (-1, -1), 1, colors.black)]

    # Создаем таблицу и устанавливаем стиль
    table = Table(data_list)
    table.setStyle(table_style)

    # Добавляем таблицу в документ
    pdf.build([table])

    print(f"PDF-файл '{pdf_file}' успешно создан.")


