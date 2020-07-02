import requests, bs4, os
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
d['Date'].append(dt.now().strftime('%Y-%m-%d'))
d['Buy Back'].append(buy)
d['Sell'].append(sell)

emas_df = pd.DataFrame(d)

filename = 'hargaemassemar{}.csv'
abs_filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)

if dt.now().strftime('%d') == '01':
	pass
else:
	df = pd.read_csv(abs_filename.format(dt.now().strftime('%Y%m')))
	df=df[['Date','Sell','Buy Back']]
	emas_df= df.append(emas_df)
print(emas_df)

emas_df.to_csv(abs_filename.format(dt.now().strftime('%Y%m')),index=False)
