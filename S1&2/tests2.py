import re
import locale
# coding: utf-8

locale.setlocale(locale.LC_ALL, '')
chars = ''.join(chr(i) for i in range(512))
print(" ".join(re.findall(r"\w", chars)))

print("*"*100)
print( re.findall(r"\u03a9", u"adeΩa adeΩa adeΩa"))
print(u"Ω".encode("utf-8"))
print(re.findall(r'Ω', "adeΩa"))
print(re.findall(r"\w+", "这是一个例子"))
print(re.search(r"(ab)+c", r"ababc"))
print(re.search("Espan[ao]l[az]", "Espanolaz"))
print("*"*100)
pattern = re.compile(r"(\d+)-\w+")
it = pattern.finditer(r"1-a\n20-baer\n34-afcr")

while True:
    try:
        match = next(it)
        print(match)
        print(match.span())
    except StopIteration:
        break