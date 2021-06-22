import requests
import json
link = "https://reqres.in/api/users"
res = json.loads(requests.get(link).text)
b = list(res.values())[4]
for i in range(len(b)):
	print(b[i]['first_name']+' '+b[i]['last_name'])




