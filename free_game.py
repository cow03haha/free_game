import requests
import json

webhook_url = 'https://discord.com/api/webhooks/908350313357017110/9DMd7YF3V4YQMChKo1kCZ2DF2D6ItD3fOPyhXutYOuPz745gf1G8NJmtcq-8JuBYc3Wk'
url = 'https://www.4gamers.com.tw/site/api/news/by-tag?tag=限時免費&nextStart=0&pageSize=5'
response = requests.get(url)

data = json.loads(response.text)
new = data['data']['pager']['totalCount']
with open('free_game', 'r') as f:
    old = f.readline()

if int(old) != new:
    for i in range(new - int(old)):
        request_data = {
            "content": f'{data["data"]["results"][i]["title"]}\n{data["data"]["results"][i]["canonicalUrl"]}',
            "username": '限時免費',
            "avatar_url": 'https://i.imgur.com/4N8ZXLB.jpg',
        }
        requests.post(url = webhook_url, data = request_data)

    with open('free_game', 'w') as f:
        f.write(str(new))