import requests
from pprint import pprint
import pygal
def pie():
    url = 'https://opend.data.go.th/govspending/bb_group_by_aspect'
    token = 'A9VPOilnDeOorteHHvLCclobveFpOnOa'
    parameters = {'api-key':token, 
                'year':2562,
                }
    data = requests.get(url,params=parameters)
    doc = data.json()
    allproject = doc['result']
    print(len(allproject))
    list_name = []
    list_amount = []
    for i in allproject:
        list_name.append(i['name'])
        list_amount.append(i['amount'])
    print(list_name)
    print(list_amount)
    pie_chart = pygal.Pie(legend_at_bottom=True, legend_at_bottom_columns=1)
    pie_chart.title = 'ปีงบประมาณ พ.ศ. 2562'
    for i in range (len(list_amount)):
        pie_chart.add(list_name[i], int(list_amount[i]))
    pie_chart.render_to_file('api/SVG/chart_BBGroup_2562.svg')
pie()