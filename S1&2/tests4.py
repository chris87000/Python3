import re

pattern = re.compile(r'fox')
result = pattern.search("The quick brown and red fox jumps over the lazy dog")
print (result.start(), result.end())

print("*"*100)
pattern = re.compile(r'(?=fox)')
result = pattern.search("The quick brown and red fox jumps over the lazy dog")
print (result.start(), result.end())

print("*"*100)
pattern = re.compile(r'\w+(?=,|;|\.)')
st=pattern.findall("They were three: Felix, Victor; and Carlos.")
print(st)

print("*"*100)
pattern = re.compile(r'John(?!\sBon|\sSmith)')  
result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")
for i in result:
    print(i)

print("*"*100)
pattern = re.compile(r'\d{1,3}')
print(pattern.findall("The number is: 1234556789000"))

print("*"*100)
pattern = re.compile(r'\d{1,3}(?=(\d{3})+(?!\d))')
results = pattern.finditer('1234567890')
for i in results:
    print(i)
print(pattern.sub(r'\g<0>,', "1234567890"))

print("*"*100)
pattern = re.compile(r'(?<=John\s)McLane')
result = pattern.finditer("I would rather go out with John McLane than with John Smith or John Bon Jovi")
for i in result:
    print(i)
 
print("*"*100)   
pattern = re.compile(r'\B@[\w_]+') 
se = pattern.findall("Know your Big Data = 5 for $50 on eBooks and 40% off all @toto_rere eBooks until Friday #bigdata #hadoop @HadoopNews packtpub.com/bigdataoffers")
print(se)
print("*"*100)   
pattern = re.compile(r'(?<=\B@)[\w_]+')
de = pattern.findall("Know your Big Data = 5 for $50 on eBooks and 40% off all @toto_rere eBooks until Friday #bigdata #hadoop @HadoopNews packtpub.com/bigdataoffers")
print(de)

print("*"*100)   
pattern = re.compile(r'(?<!John\s)Doe')
results = pattern.finditer("John Doe, Calvin Doe, Hobbes Doe")
for result in results:
    print(result)