import string
# coding: utf-8

def inconnue(composite, connue):
    lcon = len(connue)
    lcom = len(composite)
    return composite[lcon:lcom-lcon]

ret = inconnue('0bf1a9730e150bf1','0bf1')
print(ret)