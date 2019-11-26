import requests,json
serverAddress = 'http://192.168.0.6:9090'
headers = {'Content-Type': 'application/json'}

data= {'code':'b'}
r = requests.post(serverAddress,headers = headers, data=json.dumps(data))
print(r.text)