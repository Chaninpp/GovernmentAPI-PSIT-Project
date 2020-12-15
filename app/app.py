from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/',)
def home():
    return render_template('search.html',title='home')

@app.route('/', methods=['POST'])
def foo():
    text = request.form['input_keyword']
    num = request.form['input_year']
    url = 'https://opend.data.go.th/govspending/cgdcontract'
    token = 'A9VPOilnDeOorteHHvLCclobveFpOnOa' #Key ที่ได้จากการลงทะเบียน
    if text == " " or num == " ":
        parameters = {'api-key':token, 'limit':100} 
    else:
        parameters = {'api-key':token, 'limit':100, 'keyword':text, 'year': num} 
    record = requests.get(url, params=parameters) #ยิง request ไปขอที่ url ขอดูค่าตามที่เขียนไว้ใน parameter
    result = record.json()

    all = result['result']
    # num = len(all)
    # return str(all)
    dict_ans = {}
    for item in all:
        if item['dept_name'] in dict_ans:
            dict_ans[item['dept_name']].append(item['project_name'])
            dict_ans[item['dept_name']].append(item['contract'][0]['price_agree'])
        else:
            dict_ans[item['dept_name']] = [(item['project_name']), item['contract'][0]['price_agree']]
    return render_template('result.html', members=dict_ans)

if __name__ == '__main__':
    app.run(debug=True)