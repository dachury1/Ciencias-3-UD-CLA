
import ply.lex as lex

tokens = [ 'NAME','NUMBER','PLUS','MINUS','TIMES','DIVIDE', 'EQUALS','JUMPLINE'  ]


t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_JUMPLINE = r'\n'
t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer


#lectura del archivo
archivo = open("expresiones.in","r")
#sin mostrar salto linea
#listaExpresiones  = (archivo.read().splitlines())
#mostrar salto linea
listaExpresiones  = (archivo.read())
palabra = ''.join(listaExpresiones)
lex.input (palabra)

while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
