from bs4 import BeautifulSoup
from googlesearch import search
import pandas as pd
import csv
import time

data = pd.read_csv ('Searchrequests.csv', sep=';') #insert the path to the relevant document
data.head() #check for the relevant columns

#change columnnames to relevant columns
Requests = datenbasis['Requests'].tolist()
Names = datenbasis['Names'].tolist()

i = 0
Requestlength = len(Requests)-1
print(Requestlength)

Sequences = Requestlength/50
s = 1

f = open('results.csv', 'w')
writer = csv.writer(f)

while s <= Sequences :
    while i <= s*50 :
        for j in search(Requests[i], tld="com", num=2, stop=2, pause=25, user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15'):
            writer.writerow([j, Names[i]])
            print(Names[i])
            print(i)
        i += 1
    s += 1
    time.sleep(600) #necessary to avoid http 429 error
f.close()
