import requests
from pprint import pprint
import pygal
def main():
    url = 'https://opend.data.go.th/govspending/gf_per_month'
    token = 'A9VPOilnDeOorteHHvLCclobveFpOnOa'
    deptid = [ '02004', "02005", "02006"]
    amount = {}
    for i in deptid:
        parameters = {'api-key':token, 
                    'year':2562,
                    'dept_id' : i,
                    }
        data = requests.get(url,params=parameters)
        doc = data.json()
        allproject = doc['result']
        name1 = doc['summary']
        name2 = name1['dept_name']
        allproject.sort(key=lambda x: x['month'])
        amount[name2] = [float(i['amount']) for i in allproject]

    line_chart = pygal.Bar()
    line_chart.title = 'ข้อมูลการเบิกจ่ายรายเดือน พ.ศ. 2562'
    line_chart.x_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    # line_chart.x_labels = [str(i['month']) for i in allproject]
    for key, values in amount.items():
        line_chart.add(key, values)
    line_chart.render_to_file('chart.svg')

main()