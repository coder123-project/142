from bs4 import BeautifulSoup as bs
import requests
import pandas as pd


# NOTE: The page at the given URL is maintained by "wikipedia", which might be updated in future.

url = ' '
# use requests to get data from url
page = 

soup = bs(page.text,'html.parser')

star_table = soup.find_all('table')

# create a empty list temp_list


table_rows = star_table[7].find_all('tr')

for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append(row)

Star_names = []
Distance =[]
Mass = []
Radius =[]


for i in range(1,len(temp_list)):
    
    Star_names.append(temp_list[i][0])

    # append data to Distance from 5 th coloumn of i row

    # append data to Distance from 7 th coloumn of i row


    # append data to Distance from 8 th coloumn of i row

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,)),columns=['Star_name','Distance','Mass','Radius'])
print(df2)


# convert to csv and save it as dwarf_stars.csv

