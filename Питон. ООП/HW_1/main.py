import re
from collections import defaultdict

# задание 1
with open('text.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

# задание 2
sentences = re.split(r'[.?!]+\s+', text)
print(sentences)

# задание 3
words = re.findall(r'[ёЁа-яА-Я]{4,}', text)
words = [word.lower() for word in words]
print(words)

d = defaultdict(int)
for word in words:
    d[word] += 1
key, val = max(d.items(), key=lambda p: p[1])
print(key)

# задание 4
# сделала так на случай, если будут ссылки, заканчивающиеся не только на .ru
pattern = re.compile(r'(((\w+\.)*\w+\.\w+)(/\w*)*)')
links = pattern.findall(text)
links = [link[0] for link in links]
print(links)

# задание 5
domains = re.findall(pattern, text)
domains = [domain[1] for domain in domains]
print(domains)

d = defaultdict(int)
for domain in domains:
    d[domain] += 1
key, val = max(d.items(), key=lambda p: p[1])
print(key)

# задание 6
text = re.sub(pattern, 'Ссылка отобразится после регистрации', text)
print(text)
