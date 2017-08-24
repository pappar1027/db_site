from django.db import connection
import requests
from bs4 import BeautifulSoup
import datetime
from .models import Option

def remove_comma(num):
    if ',' in num:
        num=num.replace(',','')
    return(int(num))

def get_web_data(url='https://finance.yahoo.com/quote/bp/options?p=bp'):
	r=requests.get(url)
	soup=BeautifulSoup(r.content,"lxml")
	calls_data=soup.body.find_all('table')[1]

	calls_entry_data=calls_data.tbody.find_all('tr')
	last_edit=str(datetime.datetime.now())

	for tr in calls_entry_data:
		tb_entry_list=tr.contents
		contract_name=tb_entry_list[0].a.get('title')
		last_trade_date_raw=tb_entry_list[1].string[:-4]
		last_trade_date=datetime.datetime.strptime(last_trade_date_raw,'%Y-%m-%d %I:%M%p')
		strike=float(tb_entry_list[2].string)
		last_price=float(tb_entry_list[3].string)
		bid=float(tb_entry_list[4].string)
		ask=float(tb_entry_list[5].string)
		change=float(tb_entry_list[6].span.contents[1])
		percentage_change=tb_entry_list[7].span.contents[1]
		volume=remove_comma(tb_entry_list[8].string)
		open_interest=remove_comma(tb_entry_list[9].string)
		implied_volatility=tb_entry_list[10].string
		with connection.cursor() as cursor:
			if Option.objects.filter(contract_name=contract_name).count()==0:
				cursor.execute("INSERT INTO datasheet_option(contract_name,last_trade_date,strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,calls_or_puts,last_edit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[contract_name,last_trade_date,strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,'calls',last_edit])
			elif Option.objects.filter(contract_name=contract_name).count()==1:
				cursor.execute("UPDATE datasheet_option SET last_trade_date=%s, strike=%s, last_price=%s, bid=%s, ask=%s, change=%s, percentage_change=%s, volume=%s, open_interest=%s, implied_volatility=%s, last_edit=%s WHERE contract_name=%s",[last_trade_date,strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,last_edit,contract_name])
			row = cursor.fetchone()
	

   