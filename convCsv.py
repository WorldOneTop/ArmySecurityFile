import csv
import json

csvfile = open('relics.csv', 'r', encoding='cp949')
jsonfile = open('relics.json', 'w', encoding='utf-8')


fieldnames = ("rowno","existthing_no","weekqty","acpnyqnty","ttl","englsh_ttl","natlthourperiod_1_ttl_1","natlthourperiod_1_ttl_2","rgmn","author_mftplace","weight","weight_ui_ttl_1","obtm_date","obtm_reson_ttl","obtmplace","rgstdt","appraisal_dvsttl","mgtgrdttl","produ_no","relafr","qltmtr_1_ttl_1","chrtrst","rmrk","atnm_clsfct_1_ttl_1","atnmclsfct_1_ttl_2","atnmclsfct_1_ttl_3","atnmclsfct_1_ttl_4","wrtmyn")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile, ensure_ascii=False)
    jsonfile.write(',')
