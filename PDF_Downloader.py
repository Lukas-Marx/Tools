import pandas as pd
import os
import urllib
from urllib import request
import requests
import csv
import numpy as np

df = pd.read_csv('Linklist.csv', sep = ';') # can also index sheet by name or fetch all sheets

df.head() #get relevant columns
url_list = df['URL'].tolist() #column with links
name_list = df['Name'].tolist() #column with name
name_list_2 =df['Year'].to_list() #column with second identifier here a year for example

Year_date = []

for element in name_list_2:
    Year_date.append(str(element))


max_length = len(url_list)
i = 0

f = open('results.csv', 'w')
writer = csv.writer(f)

DEFAULT_TIMEOUT = 180

old_send = requests.Session.send

def new_send(*args, **kwargs):
    if kwargs.get("timeout", None) is None:
        kwargs["timeout"] = DEFAULT_TIMEOUT
    return old_send(*args, **kwargs)

requests.Session.send = new_send


while i <= max_length-1:
    try:
        response = requests.get(url_list[i], headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15' + name_list[i]})
        opener = urllib.request.build_opener()
        opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15')]
        if response.status_code != 200:
            a = str(response.status_code)
            write_a = (name_list[i], Year_date[i], a)
            writer.writerow(write_a)
            print(name_list[i]+' '+ Year_date[i]+ ' ' +a)
            print(i)
            i += 1

        else:
            urllib.request.install_opener(opener)
            request.urlretrieve( url_list[i],'/path/'+ name_list[i] + Year_date[i] + '.pdf') #.pdf if it is a pdf doc you want to download
            b = str(response.status_code)
            write_b = (name_list[i], Year_date[i], b)
            writer.writerow(write_b)
            print(name_list[i]+' '+ Year_date[i] + ' '+ b)
            print(i)
            i += 1
    except requests.exceptions.RequestException as e:
        c = 'Timeout'
        write_a = (name_list[i], Year_date[i], c)
        writer.writerow(write_a)
        print(name_list[i]+' '+ Year_date[i]+ ' ' +c)
        print(i)
        i += 1

f.close()