import this

# dico
#print(this.d)
#{'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R', 'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F', 'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M', 'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

#print(dir(this))
#print(len(this.s))
# texte crypté
#print(this.s)

def decode_zen(this):
     #print(this.s[0])
     r = []
     for i, c in enumerate(this.s):
         #print (i, ", ", c)
         #if c != " "  and  c != "," and c != "\n" and c != "." and c != "'" and c != "-" and c != "*" and c != "!":
         if c not in [" ", ",", "\n", ".", "'", "-", "*", "!"]:
             #print (this.d[c])
             r.append(this.d[c])
         else:
             #print(c)
             r.append(c)
     return  "".join(r)

print(decode_zen(this)) 