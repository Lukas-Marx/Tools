import os
import csv
from datetime import datetime
import re
import pandas as pd
from PyPDF2 import PdfFileReader

file_names = os.listdir('/path')

f= open('/path/PDF_liste.csv', 'w', encoding='UTF8')
laenge = len(file_names)

writer = csv.writer(f)
writer.writerow(['PDF_name'])

i=0
while i < laenge:
    writer.writerow([file_names[i]])
    i += 1

f.close()

PDF_list = pd.read_csv ('/path/PDF_liste.csv', sep = ';')

PDF_name = PDF_list['PDF_name'].tolist()

repeat = len(PDF_name)-1
i=0

p = open('/path/PDF_data.csv', 'w', encoding='UTF8')
writer_p = csv.writer(p)
writer_p.writerow(['PDF_name','Creation_date'])

while i < repeat:
    pdf = PdfFileReader('/path/'+PDF_name[i])
    info = pdf.getDocumentInfo()
    create_date = info['/ModDate']#CreationDate if init creation is wanted
    fix = re.search('\d+', create_date)
    a = datetime.strptime(fix.group(),'%Y%m%d%H%M%S').date()
    write_xx = (PDF_name[i], a)
    writer_p.writerow(write_xx)
    i += 1

p.close()
