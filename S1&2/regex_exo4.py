import re
# coding: utf-8

url='hTTp://christian.schweickert:toto22!&Azerty@internet-interieur.gouv.fr:8080/ressource/machin'
url2='httpS://internet.gouv.fr:8080/ressource/truc/yo'
url3 ='http://user@www.google.com/a/b'
url4 = 'FTP://username:hispass@www.google.com/'
url5 =   'ssh://missing.ending.slash'
url6 =   'gopher://unsupported.proto.col/'
url7 =   'http:///missing/hostname/'

taburls=[url, url2, url3, url4, url5, url6, url7]

#taburls=['http://www.google.com/a/b', 'HttPS://www.google.com:8080/a/b', 'http://user@www.google.com/a/b', 'FTP://username:hispass@www.google.com/', 'ssh://missing.ending.slash', 'gopher://unsupported.proto.col/',   'http:///missing/hostname/']

#regex = "(?P<proto>((?i)ssh|ftp|http|https))(://)(?P<user>[-\w\.]*?)(:|@)?(?P<password>[A-Za-z0-9!#$%^&+=]*?)(@)?(?P<hostname>[-\w\.]+)[:]?(?P<port>[\d]*)(/)(?P<path>[\w/]*)"
regex = "(?P<proto>((?i)ssh|ftp|http|https))(://)(?P<user>[-\w\.]*?)??(:(?P<password>[A-Za-z0-9!#$%^&+=]*?)@|@)??(?P<hostname>[-\w\.]+){1}[:]?(?P<port>[\d]*)??(/)(?P<path>[\w/]*)?"

pattern = re.compile(regex)
    
for taburl in taburls:
    match = pattern.search(taburl)
    if match:
        print(match.groupdict())
    else:
        print("oups!!")