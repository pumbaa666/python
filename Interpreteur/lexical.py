import ply.lex as lex
import string

tokens =('NUMBER', 'FONCTION', 'STRING')

t_FONCTION = "setTabColor|setBackGroundColor|setTitle|setImageTitle|setFontType|setFontColor|setFontSize|setFont|print|endl|Menu|endMenu|drawImage"
#~ t_STRING = '''("[^"]*")|('[^']*')''' #~ Commence par un ", contient tout sauf un guillemet, fini par un " OU idem avec '
#~ '".*?"'  #~   Aussi court que possible. N'est pas très portable

t_CONSTANTE = "GRAS|ITALIQUE|SOULIGNE|B|I|U"
t_MASQUE = CONSTANTE + "(\|" + CONSTANTE + ")*"

literals ="()-,;{}:|"

t_ignore = ' \t'

def t_STRING(t):
    '''("[^"]*")|('[^']*')''' #~ Commence par un ", contient tout sauf un guillemet, fini par un " OU idem avec '
    if string.find(t.value, "</table>") != -1 or string.find(t.value, "</td>") != -1 or string.find(t.value, "</tr>") != -1:
        print "WARNING : Vous manipulez des tableaux, cela peut provoquer un rendu incorrect de la page. Ligne n°%f"%t.lineno

def t_NUMBER(t):
	r'\d+\.\d+|\d+'
	try:
		t.value = float(t.value)
	except ValueError:
		print "Line %f: Problem while parsing %s!" % (t.lineno,t.value)
		t.value = 0
	return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_error(t):
	print "Illegal character '%s'" % t.value[0]
	t.lexer.skip(1)
	
lex.lex()

if __name__ == "__main__":
	import sys
	prog = file(sys.argv[1]).read()
	
	lex.input(prog)
	
	while 1:
		tok = lex.token()
		if not tok: break
		print "line %d: %s(%s)" % (tok.lineno, tok.type, tok.value)