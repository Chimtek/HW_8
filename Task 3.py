import requests
import datetime as dt
import time

hour = int(input('Введите - за сколько последних часов вывести вопросы: '))

sec_finish = int(time.time())
sec_start = int(time.time() - (3600 * hour))
print(sec_start)
print(sec_finish)

# url = f'https://api.stackexchange.com/2.3/questions?page=10&pagesize=100&fromdate={sec_start}&todate={sec_finish}&' \
#       f'order=desc&sort=creation&tagged=python&site=stackoverflow'

url = f'https://api.stackexchange.com/2.3/search?page=10&pagesize=100&fromdate={sec_start}&todate={sec_finish}&' \
      f'order=desc&sort=activity&tagged=python&site=stackoverflow'

req = requests.get(url)
print(req)

for i in req.json()['items']:
    date = dt.datetime.fromtimestamp(int(i['creation_date']))
    print(f"Дата создания вопроса: {date}")
    print(f"Тема вопроса: {i['title']}")
    print(i['link'])
    print('-' * 100)
