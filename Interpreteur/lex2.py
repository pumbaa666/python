import ply.lex as lex

tokens = ('NUMBER', 'FONCTION')
t_FONCTION = "setBackGroundColor|setTitle|setImageTitle|setFontType|setFontColor|setFontSize|setFont|print|endl|Menu|drawImage"

def t_NUMBER(t):
    r'\d+\.\d+|\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print "Line %d : Problem while parsing %s!" %(t.lineno, t.value)
        t.value = 0
    return t
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore = ' \t|'

def t_error(t):
    print "Illegal character '%s'"%t.value[0]
    t.lexer.skip(1)

lex.lex()

if __name__ == "__main__":
    import sys
    try:
        prog = file(sys.argv[1]).read()
    except ValueError:
        print "Erreur lors de la lecture du fichier"
        sys.exit(1)
        
    lex.input(prog)
    while 1:
        tok = lex.token()
        if not tok : break
        print "line %d: %s(%s)"%(tok.lineno, tok.type, tok.value)