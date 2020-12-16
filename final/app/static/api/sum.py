import requests
from pprint import pprint
import pygal
def sumbudget():
    url = 'https://opend.data.go.th/govspending/summary_cgdcontract'
    token = 'A9VPOilnDeOorteHHvLCclobveFpOnOa'
    year = ['2559', '2560', '2561', '2562', '2563']
    dict_sum = {}
    for i in range(5):
        parameters = {'api-key':token, 
                    'year': year[i],
                    }
        data = requests.get(url,params=parameters)
        doc = data.json()
        allproject = doc['summary']
        total = allproject['total_price'].replace(',', '')
        dict_sum[year[i]] = total
    print(dict_sum.items())
    pie_chart = pygal.HorizontalBar()
    pie_chart.title = 'ข้อมูลผลสรุปโครงการจัดซื้อจัดจ้าง (ล้านบาท)'
    for i in dict_sum.items():
        pie_chart.add(i[0], float(i[1]))
    pie_chart.render_to_file('chart_sum.svg')
sumbudget()