#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8
import requests
import pprint
import codecs
from urllib import parse

question = "Ночные клубы"
city_number = input("Number city: ")
req_data_1 = {'region_id': city_number }
req_data_2 = {'type':'street,adm_div.city,crossroad,adm_div.settlement,station,building,adm_div.district,road,adm_div.division,adm_div.region,adm_div.living_area,attraction,adm_div.place,adm_div.district_area,branch,parking,gate,route,foreign_city'}             
req_data_3 = {'page': '1'}
req_data_4 = {'page_size': '12'}
req_data_5 = {'q': question }
req_data_6 = {'locale': 'ru_RU'}
req_data_7 = {'fields':'request_type,items.adm_div,items.attribute_groups,items.contact_groups,items.flags,items.address,items.rubrics,items.name_ex,items.point,items.geometry.centroid,items.region_id,items.segment_id,items.external_content,items.org,items.group,items.schedule,items.timezone_offset,items.ads.options,items.stat,items.reviews,items.purpose,search_type,context_rubrics,search_attributes,widgets,filters'}
req_data_8 = {'stat[sid]': '61cd1fc8-8532-49fd-a3d4-a024b62b96fd'}
req_data_9 = {'stat[user]': '9b678d2b-4dba-42c3-88e1-e0b23863f90f'}
req_data_10 = {'key': 'ruoedw9225'}

url = 'https://catalog.api.2gis.ru/3.0/items?' + parse.urlencode(req_data_1) + '&' + parse.urlencode(req_data_2) + '&' + parse.urlencode(req_data_3) + '&' + parse.urlencode(req_data_4) + '&' + parse.urlencode(req_data_5) + '&' + parse.urlencode(req_data_6) + '&' + parse.urlencode(req_data_7) + '&' + parse.urlencode(req_data_8) + '&' + parse.urlencode(req_data_9) + '&' + parse.urlencode(req_data_10)

resp = requests.get(url)
pprint.pprint(resp.json()['result']['items'])
