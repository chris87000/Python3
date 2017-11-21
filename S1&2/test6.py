import re
# coding: utf-8

regex = "^(?:(\w+)(?::(\w+))?@)?((?:\d{1,3})(?:\.\d{1,3}){3})(?::(\d{1,5}))?$"
text ='user:pass@112.213.123.12:3847'

pattern = re.compile(regex)

match = pattern.search(text)
if match:
    print(match.groupdict())
else:
    print("oups!!")