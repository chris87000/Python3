import re
# coding: utf-8

tabs = ['0123456789', '01234567890'	, '012345678', '1234567890'	, '+33123456789', '3312345678', '+330123456789']

regex = "^(0|\+33)(?P<number>[\d]{9}\Z)"

pattern = re.compile(regex)

for tab in tabs:
    rez = pattern.search(tab)
    if rez:
        print(rez.groupdict())
    else:
        print("None")