import requests
import json
import asyncio
async def main():
	count = 0
	for i in range(12):
			currentUrl = f'https://reqres.in/api/users?page={i}'
			print(currentUrl)
			res = json.loads(requests.get(currentUrl).text)
			b = list(res.values())[4]
			for i in range(len(b)):
				print(b[i]['first_name']+' '+b[i]['last_name'])
				count+=1
			print(count)
asyncio.run(main())




