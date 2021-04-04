from bs4 import BeautifulSoup,NavigableString
import pandas as pd
import requests
import csv

url = "https://vision.cs.uiuc.edu/pascal-sentences/"
req = requests.get(url)

csv_file = open('data.csv','w')
csv_writer = csv.writer(csv_file)
rowlist = ['img_url','s1','s2','s3','s4','s5']

soup = BeautifulSoup(req.content, 'html.parser')

t_upper = soup.find('table')

for r_upper in t_upper.find_all('tr'):
    x = r_upper.find('td')

    col1 = x.find('img')
    if col1:
        csv_writer.writerow(rowlist)
        rowlist = []
        y = col1['src']
        rowlist.append(url +y)
    else:
        rowlist.append(x.text)
      
csv_writer.writerow(rowlist)