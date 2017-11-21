import re

pattern = re.compile(r"(\w+) : (\w+)")
it = pattern.finditer("Hello : world : hola : mundo : ")

while True:
    try:
        match = next(it)
        print(match)
        print(match.span())
    except StopIteration:
        break
#match.groups()
#('Hello', 'world')
#match.span()
#    (0, 11)

gr = re.split(r"\n", "Beautiful ⇢ is better ⇢ than ⇢ ugly.\nExplicit ⇢ is ⇢ better ⇢ than ⇢ implicit.")
print(gr)
print("**"*20)
pattern = re.compile(r"(\W)")
er = pattern.split("hello⇢word")
print(er)
sd = pattern.findall("hello⇢word")
print(sd)
pattern = re.compile(r"(⇢)")
xc = pattern.split("hello⇢word")
print(xc)
print("**"*30)
text = "imagine ⇢ a ⇢ new ⇢ *world*, ⇢ a ⇢ magic ⇢ *world*"
pattern = re.compile(r'\*(.*?)\*')
az= pattern.sub(r"<b>\g<1><\\b>", text)
print(az)
#'imagine ⇢ a ⇢ new ⇢ <b>world<\\b>, ⇢ a ⇢ magic ⇢ <b>world<\\b>'