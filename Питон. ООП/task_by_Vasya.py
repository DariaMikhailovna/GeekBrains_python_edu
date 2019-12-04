import re


def go_format(string):
    t = re.sub(r'\b[\w\']+', lambda x: x.group(0).capitalize(), string)
    return t


def main():
    strings = [
        'SaMpLe tExT',
        'this is a test (yes it is)',
        'quote: "hello", end',
        'SELF-DECEIT',
        'привет',
        "ásmegin",
        "hAtE/lOvE",
        "Thrash 'till deAth",
        "Hi, i'm JohN",
    ]
    results = [
        'Sample Text',
        'This Is A Test (Yes It Is)',
        'Quote: "Hello", End',
        'Self-Deceit',
        "Thrash 'Till Death",
        "Ásmegin",
        "Hate/Love",
        "Hi, I'm John",
        'Привет',
    ]
    for string in strings:
        result = go_format(string)
        if result not in results:
            print("Эта строка отформатирована неправильно: ", result)
        else:
            print(string, ' --> ', result)


if __name__ == '__main__':
    main()
