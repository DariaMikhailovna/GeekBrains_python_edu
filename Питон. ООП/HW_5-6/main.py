words = []


class Word:
    def __init__(self, text):
        self.text = text

# Правильнее делать так, чтобы показать, что метод part и свойство _grammar должны быть реализованы в наследниках:
# class Word:
#     _grammar = None
#
#     def __init__(self, text):
#         self.text = text
#
#     def part(self):
#         raise NotImplementedError


class Sentence:
    def __init__(self, content):
        self.content = content

    def show(self):
        sentence = ' '.join(words[number].text for number in self.content)
        print('Show: ' + sentence)

    def show_parts(self):
        parts = ' '.join(set(words[number].part() for number in self.content))
        print('Show_parts: ' + parts)


class Noun(Word):
    _grammar = 'сущ'

    def part(self):
        return 'существительное'


class Verb (Word):
    _grammar = 'гл'

    def part(self):
        return 'глагол'


def main():
    words.append(Noun("собака"))
    words.append(Verb("ела"))
    words.append(Noun("колбасу"))
    words.append(Noun("кот"))
    my_content = [0, 1, 2]
    sentence = Sentence(my_content)
    sentence.show()
    sentence.show_parts()


if __name__ == '__main__':
    main()
