# -*- coding: utf-8 -*-



from termcolor import colored
from piston import Steem
from piston.dex import Dex
from piston.account import Account
from pprint import pprint
import urllib, http.client
import hmac, hashlib
import requests
import time
import json
import os
print(colored('________________________________________________________________________', 'green'))
print(colored(' ', 'green'))




arbit = 'true'
transfer = 0.01
dealbuy = 1.0025
dealsell = 0.9975
m = 0.0005


while arbit == 'true':
    steem = Steem('wss://gtg.steem.house:8090', wif ="5KPxeeB9iKYqprrRZRCpFi6uB71xFoBXn3tMAcvVtxhFiTaKqUL")
    new_acc = Dex(steem_instance=steem)
    exchanger = new_acc.returnOrderBook(limit=10)
 
#берем котировки заказов на продажу с steemit.com
    
#1  
    steem_asks_01 = float("%.8f" % exchanger['asks'][0]['price'])
    a_quantity_01 = float("%.8f" % exchanger['asks'][0]['steem'])
#2  
    steem_asks_02 = float("%.8f" % exchanger['asks'][1]['price'])
    a_quantity_02 = float("%.8f" % exchanger['asks'][1]['steem'])
#3  
    steem_asks_03 = float("%.8f" % exchanger['asks'][2]['price'])
    a_quantity_03 = float("%.8f" % exchanger['asks'][2]['steem'])
#4  
    steem_asks_04 = float("%.8f" % exchanger['asks'][3]['price'])
    a_quantity_04 = float("%.8f" % exchanger['asks'][3]['steem'])
#5  
    steem_asks_05 = float("%.8f" % exchanger['asks'][4]['price'])
    a_quantity_05 = float("%.8f" % exchanger['asks'][4]['steem'])
#6  
    steem_asks_06 = float("%.8f" % exchanger['asks'][5]['price'])
    a_quantity_06 = float("%.8f" % exchanger['asks'][5]['steem'])
#7  
    steem_asks_07 = float("%.8f" % exchanger['asks'][6]['price'])
    a_quantity_07 = float("%.8f" % exchanger['asks'][6]['steem'])
#8  
    steem_asks_08 = float("%.8f" % exchanger['asks'][7]['price'])
    a_quantity_08 = float("%.8f" % exchanger['asks'][7]['steem'])
#9  
    steem_asks_09 = float("%.8f" % exchanger['asks'][8]['price'])
    a_quantity_09 = float("%.8f" % exchanger['asks'][8]['steem'])
#10 
    steem_asks_10 = float("%.8f" % exchanger['asks'][9]['price'])
    a_quantity_10 = float("%.8f" % exchanger['asks'][9]['steem'])
    
    
#берем котировки заказов на покупки с steemit.com
   
#1  
    steem_bids_01 = float("%.8f" % exchanger['bids'][0]['price'])
    b_quantity_01 = float("%.8f" % exchanger['bids'][0]['steem'])
#2  
    steem_bids_02 = float("%.8f" % exchanger['bids'][1]['price'])
    b_quantity_02 = float("%.8f" % exchanger['bids'][1]['steem'])
#3  
    steem_bids_03 = float("%.8f" % exchanger['bids'][2]['price'])
    b_quantity_03 = float("%.8f" % exchanger['bids'][2]['steem'])
#4  
    steem_bids_04 = float("%.8f" % exchanger['bids'][3]['price'])
    b_quantity_04 = float("%.8f" % exchanger['bids'][3]['steem'])
#5  
    steem_bids_05 = float("%.8f" % exchanger['bids'][4]['price'])
    b_quantity_05 = float("%.8f" % exchanger['bids'][4]['steem'])
#6  
    steem_bids_06 = float("%.8f" % exchanger['bids'][5]['price'])
    b_quantity_06 = float("%.8f" % exchanger['bids'][5]['steem'])
#7  
    steem_bids_07 = float("%.8f" % exchanger['bids'][6]['price'])
    b_quantity_07 = float("%.8f" % exchanger['bids'][6]['steem'])
#8  
    steem_bids_08 = float("%.8f" % exchanger['bids'][7]['price'])
    b_quantity_08 = float("%.8f" % exchanger['bids'][7]['steem'])
#9  
    steem_bids_09 = float("%.8f" % exchanger['bids'][8]['price'])
    b_quantity_09 = float("%.8f" % exchanger['bids'][8]['steem'])
#10 
    steem_bids_10 = float("%.8f" % exchanger['bids'][9]['price'])
    b_quantity_10 = float("%.8f" % exchanger['bids'][9]['steem'])

    
#Берем котировки с bittrex.com 
    
#STEEM       
    s=requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-STEEM&type=both')
    STEEM = s.json()

#1  buy    
    buy_bittrex_steem_rate_01 = STEEM["result"]['buy'][0]['Rate']
    buy_steem_quantity_01 = STEEM["result"]['buy'][0]['Quantity']
#2  buy
    buy_bittrex_steem_rate_02 = STEEM["result"]['buy'][1]['Rate']
    buy_steem_quantity_02 = STEEM["result"]['buy'][1]['Quantity']
#3  buy
    buy_bittrex_steem_rate_03 = STEEM["result"]['buy'][2]['Rate']
    buy_steem_quantity_03 = STEEM["result"]['buy'][2]['Quantity']
#4  buy    
    buy_bittrex_steem_rate_04 = STEEM["result"]['buy'][3]['Rate']
    buy_steem_quantity_04 = STEEM["result"]['buy'][3]['Quantity']
#5  buy
    buy_bittrex_steem_rate_05 = STEEM["result"]['buy'][4]['Rate']
    buy_steem_quantity_05 = STEEM["result"]['buy'][4]['Quantity']
#6  buy
    buy_bittrex_steem_rate_06 = STEEM["result"]['buy'][5]['Rate']
    buy_steem_quantity_06 = STEEM["result"]['buy'][5]['Quantity']
#7  buy    
    buy_bittrex_steem_rate_07 = STEEM["result"]['buy'][6]['Rate']
    buy_steem_quantity_07 = STEEM["result"]['buy'][6]['Quantity']
#8  buy
    buy_bittrex_steem_rate_08 = STEEM["result"]['buy'][7]['Rate']
    buy_steem_quantity_08 = STEEM["result"]['buy'][7]['Quantity']
#9  buy
    buy_bittrex_steem_rate_09 = STEEM["result"]['buy'][8]['Rate']
    buy_steem_quantity_09 = STEEM["result"]['buy'][8]['Quantity']
#10 buy    
    buy_bittrex_steem_rate_10 = STEEM["result"]['buy'][9]['Rate']
    buy_steem_quantity_10 = STEEM["result"]['buy'][9]['Quantity']


#1  sell    
    sell_bittrex_steem_rate_01 = STEEM["result"]['sell'][0]['Rate']
    sell_steem_quantity_01 = STEEM["result"]['sell'][0]['Quantity']
#2  sell
    sell_bittrex_steem_rate_02 = STEEM["result"]['sell'][1]['Rate']
    sell_steem_quantity_02 = STEEM["result"]['sell'][1]['Quantity']
#3  sell
    sell_bittrex_steem_rate_03 = STEEM["result"]['sell'][2]['Rate']
    sell_steem_quantity_03 = STEEM["result"]['sell'][2]['Quantity']
#4  sell    
    sell_bittrex_steem_rate_04 = STEEM["result"]['sell'][3]['Rate']
    sell_steem_quantity_04 = STEEM["result"]['sell'][3]['Quantity']
#5  sell
    sell_bittrex_steem_rate_05 = STEEM["result"]['sell'][4]['Rate']
    sell_steem_quantity_05 = STEEM["result"]['sell'][4]['Quantity']
#6  sell
    sell_bittrex_steem_rate_06 = STEEM["result"]['sell'][5]['Rate']
    sell_steem_quantity_06 = STEEM["result"]['sell'][5]['Quantity']
#7  sell    
    sell_bittrex_steem_rate_07 = STEEM["result"]['sell'][6]['Rate']
    sell_steem_quantity_07 = STEEM["result"]['sell'][6]['Quantity']
#8  sell
    sell_bittrex_steem_rate_08 = STEEM["result"]['sell'][7]['Rate']
    sell_steem_quantity_08 = STEEM["result"]['sell'][7]['Quantity']
#9  sell
    sell_bittrex_steem_rate_09 = STEEM["result"]['sell'][8]['Rate']
    sell_steem_quantity_09 = STEEM["result"]['sell'][8]['Quantity']
#10 sell    
    sell_bittrex_steem_rate_10 = STEEM["result"]['sell'][9]['Rate']
    sell_steem_quantity_10 = STEEM["result"]['sell'][9]['Quantity']


#SBD
    s=requests.get('https://bittrex.com/api/v1.1/public/getorderbook?market=BTC-SBD&type=both')
    SBD = s.json()

#1  buy  
    buy_bittrex_sbd_rate_01 = SBD["result"]['buy'][0]['Rate']
    buy_sbd_quantity_01 = SBD["result"]['buy'][0]['Quantity']
#2  buy
    buy_bittrex_sbd_rate_02 = SBD["result"]['buy'][1]['Rate']
    buy_sbd_quantity_02 = SBD["result"]['buy'][1]['Quantity']
#3  buy
    buy_bittrex_sbd_rate_03 = SBD["result"]['buy'][2]['Rate']
    buy_sbd_quantity_03 = SBD["result"]['buy'][2]['Quantity']
#4  buy    
    buy_bittrex_sbd_rate_04 = SBD["result"]['buy'][3]['Rate']
    buy_sbd_quantity_04 = SBD["result"]['buy'][3]['Quantity']
#5  buy
    buy_bittrex_sbd_rate_05 = SBD["result"]['buy'][4]['Rate']
    buy_sbd_quantity_05 = SBD["result"]['buy'][4]['Quantity']
#6  buy
    buy_bittrex_sbd_rate_06 = SBD["result"]['buy'][5]['Rate']
    buy_sbd_quantity_06 = SBD["result"]['buy'][5]['Quantity']
#7  buy    
    buy_bittrex_sbd_rate_07 = SBD["result"]['buy'][6]['Rate']
    buy_sbd_quantity_07 = SBD["result"]['buy'][6]['Quantity']
#8  buy
    buy_bittrex_sbd_rate_08 = SBD["result"]['buy'][7]['Rate']
    buy_sbd_quantity_08 = SBD["result"]['buy'][7]['Quantity']
#9  buy
    buy_bittrex_sbd_rate_09 = SBD["result"]['buy'][8]['Rate']
    buy_sbd_quantity_09 = SBD["result"]['buy'][8]['Quantity']
#10 buy    
    buy_bittrex_sbd_rate_10 = SBD["result"]['buy'][9]['Rate']
    buy_sbd_quantity_10 = SBD["result"]['buy'][9]['Quantity']

#1  sell  
    sell_bittrex_sbd_rate_01 = SBD["result"]['sell'][0]['Rate']
    sell_sbd_quantity_01 = SBD["result"]['sell'][0]['Quantity']
#2  sell
    sell_bittrex_sbd_rate_02 = SBD["result"]['sell'][1]['Rate']
    sell_sbd_quantity_02 = SBD["result"]['sell'][1]['Quantity']
#3  sell
    sell_bittrex_sbd_rate_03 = SBD["result"]['sell'][2]['Rate']
    sell_sbd_quantity_03 = SBD["result"]['sell'][2]['Quantity']
#4  sell    
    sell_bittrex_sbd_rate_04 = SBD["result"]['sell'][3]['Rate']
    sell_sbd_quantity_04 = SBD["result"]['sell'][3]['Quantity']
#5  sell
    sell_bittrex_sbd_rate_05 = SBD["result"]['sell'][4]['Rate']
    sell_sbd_quantity_05 = SBD["result"]['sell'][4]['Quantity']
#6  sell
    sell_bittrex_sbd_rate_06 = SBD["result"]['sell'][5]['Rate']
    sell_sbd_quantity_06 = SBD["result"]['sell'][5]['Quantity']
#7  sell    
    sell_bittrex_sbd_rate_07 = SBD["result"]['sell'][6]['Rate']
    sell_sbd_quantity_07 = SBD["result"]['sell'][6]['Quantity']
#8  sell
    sell_bittrex_sbd_rate_08 = SBD["result"]['sell'][7]['Rate']
    sell_sbd_quantity_08 = SBD["result"]['sell'][7]['Quantity']
#9  sell
    sell_bittrex_sbd_rate_09 = SBD["result"]['sell'][8]['Rate']
    sell_sbd_quantity_09 = SBD["result"]['sell'][8]['Quantity']
#10 sell    
    sell_bittrex_sbd_rate_10 = SBD["result"]['sell'][9]['Rate']
    sell_sbd_quantity_10 = SBD["result"]['sell'][9]['Quantity']


#------------------------------------------------------------------------------     
#Работаем с API Bittrex.com


    API_KEY = 'f7b9cd10a5994b959ddbc9d9e3d407f8'
    API_SECRET = b'2d053867edbf4c22aab711715636c5e4'

    API_URL = 'bittrex.com'
    API_VERSION = 'v1.1'

#Свой класс исключений

    class ScriptError(Exception): 
        pass

#Все обращения к API проходят через эту функцию:

    def call_api(**kwargs):
        http_method = kwargs.get('http_method') if kwargs.get('http_method', '') else 'POST'
        method = kwargs.get('method')

        nonce = str(int(round(time.time())))
        payload = {
                'nonce': nonce
        }



        if kwargs:
            payload.update(kwargs)

        uri = "https://" + API_URL + "/api/" + API_VERSION +  method + '?apikey=' + API_KEY  + '&nonce=' + nonce
        uri += urllib.parse.urlencode(payload)

        payload = urllib.parse.urlencode(payload)

        H = hmac.new(key=API_SECRET, digestmod=hashlib.sha512)
        H.update(uri.encode())
        sign = H.hexdigest()
        apisign = hmac.new(API_SECRET,
                           uri.encode(),
                           hashlib.sha512).hexdigest()

        headers = {"Content-type": "application/x-www-form-urlencoded",
                   "Key": API_KEY,
                   "apisign": apisign}


        conn = http.client.HTTPSConnection(API_URL, timeout=60)
        conn.request(http_method, uri, payload, headers)
        response = conn.getresponse().read()
        
        conn.close()


        try:
            obj = json.loads(response.decode('utf-8'))

            if 'error' in obj and obj['error']:
                raise ScriptError(obj['error'])
            return obj
        except json.decoder.JSONDecodeError:
            raise ScriptError('Ошибка анализа возвращаемых данных, получена строка', response)




#------------------------------------------------------------------------------
#Проверяем баланс на Bittrex.com

#SBD    

    bittrex_balance_SBD = call_api(method='/account/getbalance', currency='SBD')
    #print(bittrex_balance_SBD['result']['Balance'])
    
#STEEM   
    
    bittrex_balance_STEEM = call_api(method='/account/getbalance', currency='STEEM')
    #print(bittrex_balance_STEEM['result']['Balance'])
    
#BTC
    
    bittrex_balance_BTC = call_api(method='/account/getbalance', currency='BTC')
    #print(bittrex_balance_BTC['result']['Balance'])

#------------------------------------------------------------------------------   
#Проверяем кошелек на steemit.com
    
    acc_1 = 'cryptocoingram'
    new_acc = Account(acc_1,steem_instance=steem)
    
#SBD    
    
    sbd_wallet = ("%.3f" % new_acc.balances['SBD']) 
    #print(sbd_wallet)
    
#STEEM    
    
    steem_wallet = ("%.3f" % new_acc.balances['STEEM'])
    #print(steem_wallet)
    
#------------------------------------------------------------------------------
#Проверяем актуальность арбитража
    MARG = 0.7
    ACTUAL_RATE = 0.0
    TS = 0.001
    resolution = "false"
    BITTREX_STEEM_SBD = sell_bittrex_steem_rate_01 / buy_bittrex_sbd_rate_01
    BITTREX_STEEM_SBD2 = buy_bittrex_steem_rate_01 / buy_bittrex_sbd_rate_01
    BITTREX_STEEM_SBD3 = buy_bittrex_steem_rate_01 / sell_bittrex_sbd_rate_01
    #print("%.8f" % BITTREX_STEEM_SBD)
#Очищаем экран    
    os.system('clear')
    print(colored('________________________________________________________________________', 'green'))
    print(colored(' ', 'green'))
#Сравниваем котировки на STEEMIT.COM и BITTREX.COM:   
    
    STEEMIT_BITTREX_1 = float("%.2f" % (100*(steem_bids_01 - BITTREX_STEEM_SBD)))
    
    if STEEMIT_BITTREX_1 > MARG:
        ACTUAL_RATE = steem_bids_01
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'green'))
    if STEEMIT_BITTREX_1 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'yellow'))
    if STEEMIT_BITTREX_1 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'red'))
        
    time.sleep(TS)
    
    STEEMIT_BITTREX_2 = float("%.2f" % (100*(steem_bids_02 - BITTREX_STEEM_SBD)))
    
    if STEEMIT_BITTREX_2 > MARG:
        ACTUAL_RATE = steem_bids_02
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'green'))
    if STEEMIT_BITTREX_2 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'yellow'))
    if STEEMIT_BITTREX_2 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'red'))
    
    time.sleep(TS)
    
    STEEMIT_BITTREX_3 = float("%.2f" % (100*(steem_bids_03 - BITTREX_STEEM_SBD)))
    
    if STEEMIT_BITTREX_3 > MARG:
        ACTUAL_RATE = steem_bids_03
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'green'))
    if STEEMIT_BITTREX_3 > 0 and STEEMIT_BITTREX_3 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'yellow'))
    if STEEMIT_BITTREX_3 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'red'))
        
    time.sleep(TS)
    
    STEEMIT_BITTREX_4 = float("%.2f" % (100*(steem_bids_04 - BITTREX_STEEM_SBD)))
    
    if STEEMIT_BITTREX_4 > MARG:
        ACTUAL_RATE = steem_bids_04
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'green'))
    if STEEMIT_BITTREX_4 > 0 and STEEMIT_BITTREX_4 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'yellow'))
    if STEEMIT_BITTREX_4 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'red'))

    time.sleep(TS)
    
    STEEMIT_BITTREX_5 = float("%.2f" % (100*(steem_bids_05 - BITTREX_STEEM_SBD)))
    
    if STEEMIT_BITTREX_5 > MARG:
        ACTUAL_RATE = steem_bids_05
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'green'))
    if STEEMIT_BITTREX_5 > 0 and STEEMIT_BITTREX_5 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'yellow'))
    if STEEMIT_BITTREX_5 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'red'))

    time.sleep(TS)

    STEEMIT_BITTREX_6 = float("%.2f" % (100*(steem_bids_06 - BITTREX_STEEM_SBD)))
    
    if STEEMIT_BITTREX_6 > MARG:
        ACTUAL_RATE = steem_bids_06
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'green'))
    if STEEMIT_BITTREX_6 > 0 and STEEMIT_BITTREX_6 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'yellow'))
    if STEEMIT_BITTREX_6 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'red'))

    time.sleep(TS)

    STEEMIT_BITTREX_7 = float("%.2f" % (100*(steem_bids_07 - BITTREX_STEEM_SBD)))

    if STEEMIT_BITTREX_7 > MARG:
        ACTUAL_RATE = steem_bids_07
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'green'))
    if STEEMIT_BITTREX_7 > 0 and STEEMIT_BITTREX_7 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'yellow'))
    if STEEMIT_BITTREX_7 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'red'))
        
    time.sleep(TS)        
        
    STEEMIT_BITTREX_8 = float("%.2f" % (100*(steem_bids_08 - BITTREX_STEEM_SBD)))

    if STEEMIT_BITTREX_8 > MARG:
        ACTUAL_RATE = steem_bids_08
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'green'))
    if STEEMIT_BITTREX_8 > 0 and STEEMIT_BITTREX_8 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'yellow'))
    if STEEMIT_BITTREX_8 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'red'))
        
    time.sleep(TS)        
    
    STEEMIT_BITTREX_9 = float("%.2f" % (100*(steem_bids_09 - BITTREX_STEEM_SBD)))

    if STEEMIT_BITTREX_9 > MARG:
        ACTUAL_RATE = steem_bids_09
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'green'))
    if STEEMIT_BITTREX_9 > 0 and STEEMIT_BITTREX_9 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'yellow'))
    if STEEMIT_BITTREX_9 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'red'))
    
    time.sleep(TS)
    
    STEEMIT_BITTREX_10 = float("%.2f" % (100*(steem_bids_10 - BITTREX_STEEM_SBD)))

    if STEEMIT_BITTREX_10 > MARG:
        ACTUAL_RATE = steem_bids_10
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'green'))
    if STEEMIT_BITTREX_10 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'yellow'))
    if STEEMIT_BITTREX_10 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'red'))
    
    print(colored('________________________________________________________________________', 'green'))
    print(colored(' ', 'green'))
    
#Определяем сколько можем купить:
    
    steem_available = float(bittrex_balance_BTC['result']['Balance']) / float(sell_bittrex_steem_rate_01 * dealbuy)
    
    
#Сравниваем котировки на STEEMIT.COM и BITTREX.COM:   
    
    STEEMIT_BITTREX_1 = float("%.2f" % (100*(steem_bids_01 - BITTREX_STEEM_SBD2)))
    
    if STEEMIT_BITTREX_1 > MARG:
        ACTUAL_RATE = steem_bids_01
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'green'))
    if STEEMIT_BITTREX_1 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'yellow'))
    if STEEMIT_BITTREX_1 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'red'))
        
    time.sleep(TS)
    
    STEEMIT_BITTREX_2 = float("%.2f" % (100*(steem_bids_02 - BITTREX_STEEM_SBD2)))
    
    if STEEMIT_BITTREX_2 > MARG:
        ACTUAL_RATE = steem_bids_02
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'green'))
    if STEEMIT_BITTREX_2 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'yellow'))
    if STEEMIT_BITTREX_2 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'red'))
    
    time.sleep(TS)
    
    STEEMIT_BITTREX_3 = float("%.2f" % (100*(steem_bids_03 - BITTREX_STEEM_SBD2)))
    
    if STEEMIT_BITTREX_3 > MARG:
        ACTUAL_RATE = steem_bids_03
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'green'))
    if STEEMIT_BITTREX_3 > 0 and STEEMIT_BITTREX_3 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'yellow'))
    if STEEMIT_BITTREX_3 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'red'))
        
    time.sleep(TS)
    
    STEEMIT_BITTREX_4 = float("%.2f" % (100*(steem_bids_04 - BITTREX_STEEM_SBD2)))
    
    if STEEMIT_BITTREX_4 > MARG:
        ACTUAL_RATE = steem_bids_04
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'green'))
    if STEEMIT_BITTREX_4 > 0 and STEEMIT_BITTREX_4 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'yellow'))
    if STEEMIT_BITTREX_4 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'red'))

    time.sleep(TS)
    
    STEEMIT_BITTREX_5 = float("%.2f" % (100*(steem_bids_05 - BITTREX_STEEM_SBD2)))
    
    if STEEMIT_BITTREX_5 > MARG:
        ACTUAL_RATE = steem_bids_05
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'green'))
    if STEEMIT_BITTREX_5 > 0 and STEEMIT_BITTREX_5 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'yellow'))
    if STEEMIT_BITTREX_5 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'red'))

    time.sleep(TS)

    STEEMIT_BITTREX_6 = float("%.2f" % (100*(steem_bids_06 - BITTREX_STEEM_SBD2)))
    
    if STEEMIT_BITTREX_6 > MARG:
        ACTUAL_RATE = steem_bids_06
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'green'))
    if STEEMIT_BITTREX_6 > 0 and STEEMIT_BITTREX_6 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'yellow'))
    if STEEMIT_BITTREX_6 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'red'))

    time.sleep(TS)

    STEEMIT_BITTREX_7 = float("%.2f" % (100*(steem_bids_07 - BITTREX_STEEM_SBD2)))

    if STEEMIT_BITTREX_7 > MARG:
        ACTUAL_RATE = steem_bids_07
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'green'))
    if STEEMIT_BITTREX_7 > 0 and STEEMIT_BITTREX_7 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'yellow'))
    if STEEMIT_BITTREX_7 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'red'))
        
    time.sleep(TS)        
        
    STEEMIT_BITTREX_8 = float("%.2f" % (100*(steem_bids_08 - BITTREX_STEEM_SBD2)))

    if STEEMIT_BITTREX_8 > MARG:
        ACTUAL_RATE = steem_bids_08
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'green'))
    if STEEMIT_BITTREX_8 > 0 and STEEMIT_BITTREX_8 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'yellow'))
    if STEEMIT_BITTREX_8 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'red'))
        
    time.sleep(TS)        
    
    STEEMIT_BITTREX_9 = float("%.2f" % (100*(steem_bids_09 - BITTREX_STEEM_SBD2)))

    if STEEMIT_BITTREX_9 > MARG:
        ACTUAL_RATE = steem_bids_09
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'green'))
    if STEEMIT_BITTREX_9 > 0 and STEEMIT_BITTREX_9 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'yellow'))
    if STEEMIT_BITTREX_9 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'red'))
    
    time.sleep(TS)
    
    STEEMIT_BITTREX_10 = float("%.2f" % (100*(steem_bids_10 - BITTREX_STEEM_SBD2)))

    if STEEMIT_BITTREX_10 > MARG:
        ACTUAL_RATE = steem_bids_10
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'green'))
    if STEEMIT_BITTREX_10 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'yellow'))
    if STEEMIT_BITTREX_10 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'red'))
    
    print(colored('________________________________________________________________________', 'green'))
    print(colored(' ', 'green'))
    

#Сравниваем котировки на STEEMIT.COM и BITTREX.COM:   
    
    STEEMIT_BITTREX_1 = float("%.2f" % (100*(steem_bids_01 - BITTREX_STEEM_SBD3)))
    
    if STEEMIT_BITTREX_1 > MARG:
        ACTUAL_RATE = steem_bids_01
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'green'))
    if STEEMIT_BITTREX_1 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'yellow'))
    if STEEMIT_BITTREX_1 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_1) + '%' + " Доступно: " + str("%.5f" % b_quantity_01), 'red'))
        
    time.sleep(TS)
    
    STEEMIT_BITTREX_2 = float("%.2f" % (100*(steem_bids_02 - BITTREX_STEEM_SBD3)))
    
    if STEEMIT_BITTREX_2 > MARG:
        ACTUAL_RATE = steem_bids_02
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'green'))
    if STEEMIT_BITTREX_2 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'yellow'))
    if STEEMIT_BITTREX_2 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_2) + '%' + " Доступно: " + str("%.5f" % b_quantity_02), 'red'))
    
    time.sleep(TS)
    
    STEEMIT_BITTREX_3 = float("%.2f" % (100*(steem_bids_03 - BITTREX_STEEM_SBD3)))
    
    if STEEMIT_BITTREX_3 > MARG:
        ACTUAL_RATE = steem_bids_03
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'green'))
    if STEEMIT_BITTREX_3 > 0 and STEEMIT_BITTREX_3 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'yellow'))
    if STEEMIT_BITTREX_3 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_3) + '%' + " Доступно: " + str("%.5f" % b_quantity_03), 'red'))
        
    time.sleep(TS)
    
    STEEMIT_BITTREX_4 = float("%.2f" % (100*(steem_bids_04 - BITTREX_STEEM_SBD3)))
    
    if STEEMIT_BITTREX_4 > MARG:
        ACTUAL_RATE = steem_bids_04
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'green'))
    if STEEMIT_BITTREX_4 > 0 and STEEMIT_BITTREX_4 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'yellow'))
    if STEEMIT_BITTREX_4 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_4) + '%' + " Доступно: " + str("%.5f" % b_quantity_04), 'red'))

    time.sleep(TS)
    
    STEEMIT_BITTREX_5 = float("%.2f" % (100*(steem_bids_05 - BITTREX_STEEM_SBD3)))
    
    if STEEMIT_BITTREX_5 > MARG:
        ACTUAL_RATE = steem_bids_05
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'green'))
    if STEEMIT_BITTREX_5 > 0 and STEEMIT_BITTREX_5 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'yellow'))
    if STEEMIT_BITTREX_5 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_5) + '%' + " Доступно: " + str("%.5f" % b_quantity_05), 'red'))

    time.sleep(TS)

    STEEMIT_BITTREX_6 = float("%.2f" % (100*(steem_bids_06 - BITTREX_STEEM_SBD3)))
    
    if STEEMIT_BITTREX_6 > MARG:
        ACTUAL_RATE = steem_bids_06
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'green'))
    if STEEMIT_BITTREX_6 > 0 and STEEMIT_BITTREX_6 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'yellow'))
    if STEEMIT_BITTREX_6 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_6) + '%' + " Доступно: " + str("%.5f" % b_quantity_06), 'red'))

    time.sleep(TS)

    STEEMIT_BITTREX_7 = float("%.2f" % (100*(steem_bids_07 - BITTREX_STEEM_SBD3)))

    if STEEMIT_BITTREX_7 > MARG:
        ACTUAL_RATE = steem_bids_07
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'green'))
    if STEEMIT_BITTREX_7 > 0 and STEEMIT_BITTREX_7 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'yellow'))
    if STEEMIT_BITTREX_7 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_7) + '%' + " Доступно: " + str("%.5f" % b_quantity_07), 'red'))
        
    time.sleep(TS)        
        
    STEEMIT_BITTREX_8 = float("%.2f" % (100*(steem_bids_08 - BITTREX_STEEM_SBD3)))

    if STEEMIT_BITTREX_8 > MARG:
        ACTUAL_RATE = steem_bids_08
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'green'))
    if STEEMIT_BITTREX_8 > 0 and STEEMIT_BITTREX_8 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'yellow'))
    if STEEMIT_BITTREX_8 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_8) + '%' + " Доступно: " + str("%.5f" % b_quantity_08), 'red'))
        
    time.sleep(TS)        
    
    STEEMIT_BITTREX_9 = float("%.2f" % (100*(steem_bids_09 - BITTREX_STEEM_SBD3)))

    if STEEMIT_BITTREX_9 > MARG:
        ACTUAL_RATE = steem_bids_09
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'green'))
    if STEEMIT_BITTREX_9 > 0 and STEEMIT_BITTREX_9 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'yellow'))
    if STEEMIT_BITTREX_9 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_9) + '%' + " Доступно: " + str("%.5f" % b_quantity_09), 'red'))
    
    time.sleep(TS)
    
    STEEMIT_BITTREX_10 = float("%.2f" % (100*(steem_bids_10 - BITTREX_STEEM_SBD3)))

    if STEEMIT_BITTREX_10 > MARG:
        ACTUAL_RATE = steem_bids_10
        resolution = "true"
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'green'))
    if STEEMIT_BITTREX_10 > 0 and STEEMIT_BITTREX_1 < MARG:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'yellow'))
    if STEEMIT_BITTREX_10 < 0:
        print(colored("Разница : "+ str(STEEMIT_BITTREX_10) + '%' + " Доступно: " + str("%.5f" % b_quantity_10), 'red'))
    
    print(colored('________________________________________________________________________', 'green'))
    print(colored(' ', 'green'))

#Определяем сколько покупать:
    
    STEEMIT_BITTREX_quantity = sell_steem_quantity_01 - b_quantity_01
    #print("%.8f" % STEEMIT_BITTREX_quantity)
    STEEM_BUY = 0

    Q1 = b_quantity_01
    Q2 = b_quantity_02
    Q3 = b_quantity_03
    Q4 = b_quantity_04
    Q5 = b_quantity_05
    Q6 = b_quantity_06
    Q7 = b_quantity_07
    Q8 = b_quantity_08
    Q9 = b_quantity_09
    Q10 = b_quantity_10
    
    
    
    if ACTUAL_RATE == steem_bids_01:
        STEEM_BUY = Q1
    if ACTUAL_RATE == steem_bids_02:
        STEEM_BUY = Q1 + Q2
    if ACTUAL_RATE == steem_bids_03:
        STEEM_BUY = Q1 + Q2 + Q3
    if ACTUAL_RATE == steem_bids_04:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4
    if ACTUAL_RATE == steem_bids_05:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4 + Q5   
    if ACTUAL_RATE == steem_bids_06:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4 + Q5 + Q6
    if ACTUAL_RATE == steem_bids_07:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4 + Q5 + Q6 + Q7
    if ACTUAL_RATE == steem_bids_08:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4 + Q5 + Q6 + Q7 +Q8
    if ACTUAL_RATE == steem_bids_09:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4 + Q5 + Q6 + Q7 +Q8 + Q9
    if ACTUAL_RATE == steem_bids_10:
        STEEM_BUY = Q1 + Q2 + Q3 +Q4 + Q5 + Q6 + Q7 +Q8 + Q9 + Q10  
    if STEEM_BUY > steem_available:
        STEEM_BUY = steem_available
    print (STEEM_BUY)

#Баланс на steemit.com 
    print('steemit.com: ', float("%.3f" % new_acc.balances['STEEM']), " STEEM")
    print('steemit.com: ', float("%.3f" % new_acc.balances['SBD']), " SBD")
   
#Обмен на steemit.com
    STEEM_BUY =1.965
    #ACTUAL_RATE = 1.5
    '''
    if resolution == "true":
        
        steem = Steem('wss://gtg.steem.house:8090', wif ="5Jh5fa7sDTB9eLhKpGhes84RbwLwDdGQqwoQDg1UWeUoxRMcQy6")
        DEX = Dex(steem_instance=steem) 
        
        EXChange = DEX.sell(STEEM_BUY-0.01,quote_symbol="STEEM",rate=ACTUAL_RATE - 0.001, expiration=604800,killfill=False,account="cryptocoingram")
        
        
        print (EXChange)        
                
        print (EXChange)
        print ('____________________________________')
        print (EXChange['operations'])
        print ('____________________________________')
        print (EXChange['operations'][0])
        print ('____________________________________')
        print (EXChange['operations'][0][0])
        print ('____________________________________')
        print (EXChange['operations'][0][1])
        print ('____________________________________')
        print (EXChange['operations'][0][1]['fill_or_kill'])
        print ('____________________________________')
        print (EXChange['operations'][0][1]['min_to_receive'])
        print ('____________________________________')
        print (EXChange['operations'][0][1]['orderid'])
        print ('____________________________________')
        print (EXChange['operations'][0][1]['expiration'])
        print ('____________________________________')
        print (EXChange['operations'][0][1]['owner'])
        print ('____________________________________')
        print (EXChange['operations'][0][1]['amount_to_sell'])
        print ('____________________________________')
        
        STOP = float(STEEM_BUY*steem_bids_01)
        while float("%.3f" % new_acc.balances['SBD']) <= STOP:
            time
            float("%.3f" % new_acc.balances['SBD'])
            print("Не купилось")
        
        print("Обмен на steemit.com проведен успешно")
        print("Выставляются ордера на bittrex.com")
        
        
        print(call_api(method='/market/buyllimit', market="BTC-STEEM" , quantity=float(STEEM_BUY) , rate=float(buy_bittrex_steem_rate_01)))
        print("Покупка: ОК")
        
        print(call_api(method='/market/selllimit', market="BTC-SBD" , quantity=float("%.3f" % new_acc.balances['SBD']) , rate=float(sell_bittrex_sbd_rate_01)))
        print("Продажа: ОК")
        
        print("Засыпаю")
        time.sleep(100)
        '''


    
