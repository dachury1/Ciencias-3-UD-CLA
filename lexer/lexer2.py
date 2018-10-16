# -*- coding: utf-8 -*-
import ply.lex as lex

tokens = [ 'NAME','NUMBER','JUMPLINE'  ]
reserved = {'SUMA' : 'PLUS', 'RESTA':'MINUS', 'MULTIPLICACION':'TIMES', 'DIVISION':'DIVIDE', 'IGUAL':'EQUALS' }
tokens += reserved.values()

t_ignore = ' \t'

t_JUMPLINE = r'\n'
# t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMENTARIO(t):
    r'\#.*'
    pass

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in reserved:
        t.type = reserved[t.value.upper()]
    return t

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

#lex.input("x = 3 - 4 + 5 * 6")

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
    print (str(tok.value) + " - " + str(tok.type))
