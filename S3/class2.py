import pprint

class Fifo:
    def __init__(self):
        self.tab=[]
        
    def incoming(self, value):
        self.tab.append(value)

    def outgoing(self):
        if(len(self.tab) == 0):
            return
        else:
            return self.tab.pop(0)

    def tostr(self):
        return " ".join(self.tab)
f = Fifo()

f.incoming('33')
f.incoming('333')
f.incoming('3333')
print(f.tostr())
s = f.outgoing()
print(s)
print(f.tostr())