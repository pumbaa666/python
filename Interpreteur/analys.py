import ply.yacc as yacc
import sys
from lex2 import tokens

operations = {
    '+' : lambda x,y: x+y,
    '-' : lambda x,y: x-y,
    '*' : lambda x,y: x*y,
    '/' : lambda x,y: x/y,
        }

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = p[1] # construire l'arbre ici si necessaire

def p_expression_op(p):
    '''expression : expression ADD_OP expression 
    | expression MUL_OP expression'''
    p[0] = operations[p[2]](p[1],p[3])

def p_error(p):
    print "Syntax error in line %d"%p.lineno

precedence =    (
                    ('left', 'FONCTION'),
                    ('left', 'LETTRE_OU_CHIFFRE'),
                    ('left', 'PARENTHESE'),
                    ('left', 'ADD_OP'),
                    ('left', 'MUL_OP'),
                )

yacc.yacc()

if __name__ == "__main__":
    try:
        prog = file(sys.argv[1]).read()
    except ValueError:
        print "Erreur lors de la lecture du fichier"
        sys.exit(1)
    
    result = yacc.parse(prog)