import re
# coding: utf-8

pattern = re.compile(r"(\w+) \1")
match = pattern.search(r"hello world world world hello")
print(match.groups())

pattern = re.compile(r"(\d+)-(\w+)")
print(pattern.sub(r"\2-\1", "1-a\n20-baer\n34-afcr"))
print("*"*100)
pattern = re.compile(r"(?P<country>\d+)-(?P<id>\w+)")
print(pattern.sub(r"\g<id>-\g<country>", "1-a\n20-baer\n34-afcr"))
print("*"*100)
print(re.search("Españ(?:a|ol)", "Español"))
print(re.search("Españ(?:a|ol)", "Español").groups())

print("+"*100)
pattern = re.compile(r"(\d\d-)?(\w{3,4})(?(1)(-\d\d))")
print(pattern.match("34-erte-22"))


pattern = re.compile(r"(\d\d-)?(\w{3,4})-(?(1)(\d\d)|[a-z]{3,4})$")
print(pattern.match("34-erte-22"))
print(pattern.match("erte-abcd"))

print("*"*100)
print(re.findall(r'(a|b)+', 'abaca'))
print(re.findall(r'((?:a|b)+)', 'abbaca'))
print(re.findall(r'(a|b)', 'abaca'))