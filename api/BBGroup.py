import requests
from pprint import pprint
def SearchProject(keyword_search='เรือดำน้ำ',year=2562,limit=20):

  url = 'https://opend.data.go.th/govspending/cgdcontract'

  token = 'A9VPOilnDeOorteHHvLCclobveFpOnOa'

  parameters = {'api-key':token, 
                'year':year,
                'keyword':keyword_search,
                'limit':limit
                }

  r = requests.get(url,params=parameters)
  result = r.json()
  print(result)

  allproject = result['result']
  pprint(allproject)
SearchProject()