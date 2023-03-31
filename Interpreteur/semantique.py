import ply.yacc as yacc
from lexical import tokens, literals
import string

def p_programme(p):
    'programme : programme expression '
    p[0]=p[2]
    
def p_programme_exp(p):
    'programme : expression '
    p[0]=p[1]

def p_expression_1str(p):
    '''expression : FONCTION '(' STRING ')' ';' '''
    global isMenu
    global body
    global menu
    
    if p[1] == 'setTitle':
        global title
        title = str(p[3]).strip('\"\'')
    elif p[1] == 'setImageTitle':
        global imageTitle
        imageTitle = "\n<tr>\n<td height='125' colspan='2' width='100%'>\n<p align='center'>\n<img src='"
        imageTitle = imageTitle+str(p[3]).strip('\"\'')
        imageTitle = imageTitle+"' width='100%' height='100%'>\n</td>\n</tr>"
    elif p[1] == 'setFontType':
        if isMenu == 0 :
            body = body + "<font face = '"+p[3].strip('\"\'')+"'>"
        else:
            menu = menu + "<font face = '"+p[3].strip('\"\'')+"'>"
    elif p[1] == 'drawImage':
        if isMenu == 0 :
            body = body + "<img src = '"+p[3].strip('\"\'')+"'>"
        else:
            menu = menu + "<img src = '"+p[3].strip('\"\'')+"'>"
    elif p[1] == 'print':
        if isMenu == 0 :
            body = body + p[3].strip('\"\'')
        else:
            menu = menu + p[3].strip('\"\'')+"<br><br>"

def p_expression_printMEF(p): #Mise en forme
    '''expression : FONCTION '(' STRING ',' MASQUE ')' ';' '''
    global isMenu
    global body
    global menu
    
    header = ""
    end = ""
    
    line = p[5]
    string.split(line, "|")
    
    for i in string.split(line, "|"):
        if i == "GRAS" or i == "B" :
            header = header + "<b>"
            end = "</b>" + end
        elif i == "SOULIGNE" or i == "U" :
            header = header + "<u>"
            end = "</u>" + end
        elif i == "ITALIQUE" or i == "I" :
            header = header + "<i>"
            end = "</i>" + end
    
    
    if isMenu == 0 :
        body = body + header + p[3].strip('\"\'') + end
    else:
        menu = menu + header + p[3].strip('\"\'') + end + "<br><br>"

def p_expression_void(p):
    '''expression : FONCTION '('  ')' ';' '''
    global body
    global isMenu
    global menu
    
    if p[1] == "endl":
        if isMenu == 0 :
            body = body + "<br>"
        else:
            menu = menu + "<br>"
    elif p[1] == "endMenu":
        isMenu = 0
        menu = menu + "</td>"
        
def p_expression_setFontSize(p):
    '''expression : FONCTION '(' NUMBER ')' ';' '''
    global body
    global isMenu
    global menu
    
    if isMenu == 0 :
        body = body + "<font size = '"+str(int(p[3]))+"'>"
    else:
        menu = menu + "<font size = '"+str(int(p[3]))+"'>"
    
def p_expression_setFont(p):
    '''expression : FONCTION '(' STRING ',' NUMBER ',' NUMBER ',' NUMBER ',' NUMBER ')' ';' '''
    global body
    global isMenu
    global menu
    
    rouge = convertIntToHexStr(p[7])
    vert = convertIntToHexStr(p[9])
    bleu = convertIntToHexStr(p[11])
    if isMenu == 0 :
        body = body + "<font face = '"+p[3]+"' size = '"+str(int(p[5]))+"' color = '"+rouge+vert+bleu+"'>"
    else:
        menu = menu + "<font face = '"+p[3]+"' size = '"+str(int(p[5]))+"' color = '"+rouge+vert+bleu+"'>"
    
def p_expression_2str(p):
    '''expression : FONCTION '(' STRING ',' STRING ')' ';' '''
    
    global isMenu
    global body
    global menu
    
    if p[1] == "drawImage":
        if isMenu == 0 :
            body = body + "<a href = '"+p[5].strip('\"\'')+"'>" + "<img src = '"+p[3].strip('\"\'')+"'></a>"
        else:
            menu = menu + "<a href = '"+p[5].strip('\"\'')+"'>" + "<img src = '"+p[3].strip('\"\'')+"'></a>"
    elif p[1] == "link":
        if isMenu == 0 :
            body = body + "<a href = '"+p[5].strip('\"\'')+"'>" + p[3].strip('\"\'')+"</a>"
        else:
            menu = menu + "<a href = '"+p[5].strip('\"\'')+"'>" + p[3].strip('\"\'')+"</a><br><br>"

def p_expression_menu(p):
    '''expression : FONCTION ':' STRING '''
    global isMenu
    global menu
    
    isMenu = 1
    menu = "\n<td width = '22%' valign = 'top' align = 'center'><u><font size = '6'></u>"+p[3].strip("\"")+"<br><br>"

def p_expression_3int(p):
    '''expression : FONCTION '(' NUMBER ',' NUMBER ',' NUMBER ')' ';' '''
    
    if p[1] == 'setBackGroundColor' :
        global bgColor
        rouge = convertIntToHexStr(p[3])
        vert = convertIntToHexStr(p[5])
        bleu = convertIntToHexStr(p[7])
    
        bgColor = "#"+rouge+vert+bleu
        
    elif p[1] == 'setTabColor' :
        global tabBgColor
        rouge = convertIntToHexStr(p[3])
        vert = convertIntToHexStr(p[5])
        bleu = convertIntToHexStr(p[7])
        
        tabBgColor = "bgcolor = '#"+rouge+vert+bleu+"'"
        
    elif p[1] == 'setFontColor' :
        global body
        global isMenu
        global menu
        rouge = convertIntToHexStr(p[3])
        vert = convertIntToHexStr(p[5])
        bleu = convertIntToHexStr(p[7])
        
        if isMenu == 0 :
            body = body + "<font color = '#"+rouge+vert+bleu+"'>"
        else:
            menu = menu + "<font color = '#"+rouge+vert+bleu+"'>"

def convertIntToHexStr(nombre):
    chaine = str(hex(int(nombre))).lstrip("0x")
    if len(chaine) == 0:
        chaine = "00"
    elif len(chaine) == 1:
        chaine = "0"+chaine
    return chaine

def p_error(p):
    print "Syntaxe error in line %d" % p.lineno

title = ""
imageTitle = ""
menu = ""
body = ""
bgColor = "#FFFFFF'"
tabBgColor = "#FFFFFF"
isMenu = 0

yacc.yacc()

def gen():
    global title
    global bgColor
    global tabBgColor
    global imageTitle
    global body
    global menu
    
    #~ Titre
    titre = "<HEAD><TITLE>" + title + "</TITLE></HEAD>\n"
    
    #~ Couleur de fond
    couleurFond = "<BODY BGCOLOR = '" + bgColor + "'>\n"
    
    #~ Tableau
    tableau = "<TABLE border = '1' width = '100%' height = '100%' "+tabBgColor+">"
    tableau = tableau+imageTitle
    
    #~ Body
    body = "<td valign = 'top' align = 'center'>" + body + "</td>"
    
    #~ Total
    renduHTML = "<HTML>\n" + titre + couleurFond + tableau + "\n<tr>" + menu + body + "\n</tr>"
    renduHTML = renduHTML + "</TABLE></BODY></HTML>"
    return renduHTML

if __name__=="__main__":
    import sys

    prog = file(sys.argv[1]).read()
    result = yacc.parse(prog)
    genererTout = gen()
    
    filePath = ""
    if len(sys.argv) > 2 :
        filePath = sys.argv[2]
    else
        filePath = "rendu.html"
        
    fichier = open(filePath,"w")
    fichier.writelines(genererTout)
    fichier.close()
