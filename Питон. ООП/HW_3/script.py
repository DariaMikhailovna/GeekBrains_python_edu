import requests
import json


def get_iata(origin, destination):
    my_link = f'https://www.travelpayouts.com/widgets_suggest_params?q=Из {origin} в {destination}'
    return json.loads(requests.get(my_link).text)


def main():
    origin = input('(введите в правильном падеже) Вы летите из: ')
    destination = input('(введите в правильном падеже) Вы летите в: ')
    iata = get_iata(origin, destination)
    try:
        link = f"http://min-prices.aviasales.ru/calendar_preload?origin={iata['origin']['iata']}&destination={iata['destination']['iata']}"
    except KeyError:
        print('Что-то пошло не так. Скорее всего, Вы ввели названия городов в неправильном формате')
        exit(1)
    data = json.loads(requests.get(link).text)
    try:
        # print(data)
        print(f"Лучшая цена: {data['best_prices'][0]['value']} рублей")
    except IndexError:
        print('Билетов не нашлось')


if __name__ == '__main__':
    main()
