from bs4 import BeautifulSoup as BS

with open('text.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

soup = BS(text, 'html.parser')
res = soup.find(class_='total-users').get_text()
print(res)
