from datetime import datetime
import re
pdf = PdfFileReader('path/data.pdf')
info = pdf.getDocumentInfo()
print(info)

create_date = info['/ModDate']#CreationDate if init creation is wanted
Doc_title = info['/Title']
fix = re.search('\d+', create_date)

a = datetime.strptime(fix.group(),'%Y%m%d%H%M%S').date()

print(a)