import requests


def get_link(topic):
    return 'https://ru.wikipedia.org/wiki/' + topic.capitalize()


def get_page(link):
    return requests.get(link).text

