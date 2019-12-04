from wiki_requests import get_link, get_page
import re
from bs4 import BeautifulSoup as BS


max_links = 20
words_count = 100
pattern = re.compile(r'\b[ёЁа-яА-Я\'\-]{3,}\b')


def get_page_body(html):
    soup = BS(html, 'html.parser')
    return soup.find(id='bodyContent').get_text()


def get_neighboring_links(link):
    html_content = get_page(link)
    soup = BS(html_content, 'html.parser')
    links = set(link['href'] for link in soup.find(id='bodyContent').find_all('a', href=True))
    return ['https://ru.wikipedia.org' + link for link in links if link.startswith('/wiki/')]


def get_page_words(link):
    print(link)
    html_content = get_page(link)
    text = get_page_body(html_content)
    words = pattern.findall(text)
    return [word.lower() for word in words]


def get_neighboring_words(link):
    links = get_neighboring_links(link)
    return [word for link in links[:max_links] for word in get_page_words(link)]


def get_common_words(link):
    words = get_page_words(link)
    words += get_neighboring_words(link)
    rate = {}
    for word in words:
        rate[word] = rate.get(word, 0) + 1
    rate_list = list(rate.items())
    rate_list.sort(key=lambda x: -x[1])
    return rate_list


def visualize_common_words(link):
    words = get_common_words(link)
    for word, cnt in words[:words_count]:
        print(cnt, word)


def main():
    topic = input('Topic: ')
    visualize_common_words(get_link(topic))


if __name__ == '__main__':
    main()
