#-*- coding: utf-8-*-
chaineIn = raw_input("Entrez la chaine a crypter en Rot13 : ")
chaineOut = ""
for j in range(1,26):
    for i in range(len(chaineIn)):
        cIn = ord(chaineIn[i])
        if cIn >= 65 and cIn <= 90 :
            if cIn > 65+12 :
                cOut = chr(cIn-j)
            else:
                cOut = chr(cIn+j)
        elif cIn >= 97 and cIn <= 122 :
            if cIn > 97+12 :
                cOut = chr(cIn-j)
            else:
                cOut = chr(cIn+j)
        else:
            cOut = chr(cIn)
        chaineOut += cOut
    print chaineOut
    print ""
    print ""