import requests
from bs4 import BeautifulSoup


url = 'https://elbrusboot.camp/'

page = requests.get(url).text
soup = BeautifulSoup(page, 'lxml')

events = soup.find(class_="thisweek-wrap")  # <class 'bs4.element.Tag'>
for event in events.find_all('a'):
    print(event.find(class_="name").text, event.find(class_='date').text.strip(), event.get('href').strip())
