import requests
from pprint import pprint #จัดรูปแบบการแสดงผลลัพธ์


def SearchProject(keyword_search='เรือดำน้ำ',year=2562,limit=20):

    url = 'https://opend.data.go.th/govspending/cgdcontract'
    token = 'A9VPOilnDeOorteHHvLCclobveFpOnOa' #Key ที่ได้จากการลงทะเบียน
    parameters = {'api-key':token, 'year': year, 'limit':limit, 'keyword':keyword_search}
    record = requests.get(url, params=parameters) #ยิง request ไปขอที่ url ขอดูค่าตามที่เขียนไว้ใน parameter
    result = record.json()

    all = result['result']

    count = len(all)
    print('ผลลัพธ์ที่ค้นพบ', count, 'ข้อมูล')

    for item in all:
        print(item['dept_name'])
        print(item['sum_price_agree'])
        print(item['project_name'])
        print('---------------')

SearchProject(keyword_search=input(), year=int(input()), limit=int(input()))
