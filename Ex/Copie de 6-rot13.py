#-*- coding: utf-8-*-
chaineIn = raw_input("Entrez la chaine a crypter en Rot13 : ")
chaineOut = ""
for i in range(len(chaineIn)):
    cIn = ord(chaineIn[i])
    if cIn >= 65 and cIn <= 90 :
        if cIn > 65+12 :
            cOut = chr(cIn-13)
        else:
            cOut = chr(cIn+13)
    elif cIn >= 97 and cIn <= 122 :
        if cIn > 97+12 :
            cOut = chr(cIn-13)
        else:
            cOut = chr(cIn+13)
    else:
        cOut = chr(cIn)
    chaineOut += cOut
print chaineOut