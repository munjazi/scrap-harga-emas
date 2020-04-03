import requests, bs4
import pandas as pd
from datetime import datetime as dt

url = 'http://semar.co.id/'
res = requests.get(url)
soup = bs4.BeautifulSoup(res.content, 'html.parser') 

df=soup.find("td", text="Buy Back Price").find_next_sibling("td").text
buy=df.replace(": Rp ", "").replace("/gram", "").replace(".", "").strip()    
print (buy)

df1=soup.find("td", text="1").find_next_sibling("td").text
sell=df1.replace("/gram", "").replace(".", "").strip()
print(sell)

d = {'Date':[], 'Sell': [], 'Buy Back': []}
# iterate each quote
d['Date'].append(dt.now().strftime('%Y-%m-%d'))
d['Buy Back'].append(buy)
d['Sell'].append(sell)

emas_df = pd.DataFrame(d)

df = pd.read_csv('hargaemassemar.csv'.format(dt.now().strftime('%Y')))
df1 = pd.read_csv('hargaemassemar{}.csv'.format(dt.now().strftime('%Y')))
df=df[['Date','Sell','Buy Back']]

emas= df.append(df1).append(emas_df)
print(emas)

emas.to_csv('hargaemassemar{}.csv'.format(dt.now().strftime('%Y')),index=False)