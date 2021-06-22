import requests

r = requests.get("https://my-json-server.typicode.com/typicode/demo/posts")
postData = r.json()
print(postData)
r = requests.get("https://my-json-server.typicode.com/typicode/demo/comments")
commentsData = r.json()
print(commentsData)

for i in range(len(postData)):
    for j in range(len(commentsData)):
        if (commentsData[j]['postId'] == postData[i]['id'] and ('body' in postData[i])):
            postData[i]['body'].append(commentsData[j]['body'])
        elif (commentsData[j]['postId'] == postData[i]['id']):
            postData[i]['body'] = [commentsData[j]['body']]
print(postData)







