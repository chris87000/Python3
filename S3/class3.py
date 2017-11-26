class Parser:
    def __init__(self, sep):
        self.sep = sep
        self.parsed_line = []

    def parse(self, line):
        self.parsed_line = [i.strip() for i in line.split(self.sep)
                            if i.strip().isdigit()]

    def __str__(self):
        return ' '.join(self.parsed_line)

test = '123  : fj356:34:fjjd:    707'

p = Parser(':')
p.parse(test)
print(p)
print(type(Parser))
print(type(p))