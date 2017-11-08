from django.db import connection
import requests
from bs4 import BeautifulSoup
import datetime
from .models import Option

def remove_comma(num):
    if ',' in num:
        num=num.replace(',','')
    return(int(num))

def remove_react_text(contents):
    updated=[]
    for content in contents:
        if 'r' not in content:
            updated.append(content)
    num=''.join(updated)
    return num

def process_table(table_data,data_type,last_edit):
	entry_data=table_data.tbody.find_all('tr')

	for tr in entry_data:
		tb_entry_list=tr.contents
		contract_name=tb_entry_list[0].a.get('title')
		last_trade_date_raw=tb_entry_list[1].string[:-4]
		last_trade_date=datetime.datetime.strptime(last_trade_date_raw,'%Y-%m-%d %I:%M%p')
		strike=float(tb_entry_list[2].string)
		last_price=float(tb_entry_list[3].string)
		bid=float(tb_entry_list[4].string)
		ask=float(tb_entry_list[5].string)
		change=float(remove_react_text(tb_entry_list[6].span.contents))
		percentage_change=remove_react_text(tb_entry_list[7].span.contents)
		volume=remove_comma(tb_entry_list[8].string)
		open_interest=remove_comma(tb_entry_list[9].string)
		implied_volatility=tb_entry_list[10].string
		with connection.cursor() as cursor:
			if Option.objects.filter(contract_name=contract_name).count()==0:
				cursor.execute("INSERT INTO datasheet_option(contract_name,last_trade_date,strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,calls_or_puts,last_edit) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[contract_name,last_trade_date,strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,data_type,last_edit])
			elif Option.objects.filter(contract_name=contract_name).count()==1:
				cursor.execute("UPDATE datasheet_option SET last_trade_date=%s, strike=%s, last_price=%s, bid=%s, ask=%s, change=%s, percentage_change=%s, volume=%s, open_interest=%s, implied_volatility=%s, last_edit=%s WHERE contract_name=%s",[last_trade_date,strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,last_edit,contract_name])
			row = cursor.fetchone()



def process_data_change(data_dict):
	contract_name=data_dict['contract_name']
	calls_or_puts=data_dict['calls_or_puts']
	strike=float(data_dict['strike'])
	last_price=float(data_dict['last_price'])
	bid=float(data_dict['bid'])
	ask=float(data_dict['ask'])
	change=float(data_dict['change'])
	percentage_change=data_dict['percentage_change']
	volume=int(data_dict['volume'])
	open_interest=int(data_dict['open_interest'])
	implied_volatility=data_dict['implied_volatility']
	last_edit=str(datetime.datetime.now())
	with connection.cursor() as cursor:
		cursor.execute("UPDATE datasheet_option SET strike=%s, last_price=%s, bid=%s, ask=%s, change=%s, percentage_change=%s, volume=%s, open_interest=%s, implied_volatility=%s, last_edit=%s WHERE contract_name=%s",[strike,last_price,bid,ask,change,percentage_change,volume,open_interest,implied_volatility,last_edit,contract_name])
		row = cursor.fetchone()

def get_web_data(url='https://finance.yahoo.com/quote/bp/options?p=bp'):
	r=requests.get(url)
	soup=BeautifulSoup(r.content,"lxml")
	calls_data=soup.body.find_all('table')[0]
	puts_data=soup.body.find_all('table')[1]
	last_edit=str(datetime.datetime.now())
	process_table(calls_data,'calls',last_edit)
	process_table(puts_data,'puts',last_edit)


	

   