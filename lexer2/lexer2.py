#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      LEIDY K
#
# Created:     01/10/2018
# Copyright:   (c) LEIDY K 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------
    
import ply.lex as lex

tokens = ['NAME','NUMBER','JUMPLINE']
reserved={'SUMA':'PLUS','RESTA':'MINUS','MULTIPLICACION':'TIMES','DIVISION':'DIVIDE','IGUAL':'EQUALS'}
#variable={'[a-zA-Z_][a-zA-Z0-9_]*'}
tokens += reserved.values()

t_ignore = ' \t'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_EQUALS = r'='
t_JUMPLINE = r'\n'
#t_NAME = r'[a-zA-Z_][a-zA-Z0-9_]*'


def t_NAME(t):
   r'[a-zA-Z_][a-zA-Z0-9_]*'
   if t.value.upper()in reserved:
       t.type=reserved [t.value.upper()]
   return t

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
archivo = open("expresiones.txt","r")
listaExpresiones  = (archivo.read())
palabra = ''.join(listaExpresiones)
lex.input (palabra)
lista=[0,0]

while True:
    tok = lex.token()
    
    if not tok: break
    print (str(tok.value) + " ----> " + str(tok.type))
    
    if tok.type=='NUMBER':
        lista.append(tok.value)
        ##print (lista)
    
    
    if tok.type=='PLUS':
            if lista != []:
                a1=(lista.pop())
                b1=(lista.pop()) 

            d1=(b1 + a1)
            lista.append(d1)
            #print ('es la suma ')
            #print (d1)
    if tok.type=='TIMES':
            if lista != []:
                a1=(lista.pop())
                b1=(lista.pop()) 

            d1=(b1 * a1)
            lista.append(d1)
            #print ('es la multi ')
            #print (d1)
    if tok.type=='MINUS':
            if lista != []:
                a1=(lista.pop())
                b1=(lista.pop()) 

            d1=(b1- a1)
            lista.append(d1)
            #print ('es la resta ')
            #print (d1)
    if tok.type=='DIVIDE':
            if lista != []:
                a1=(lista.pop())
                b1=(lista.pop()) 

            d1=(b1/a1)
            lista.append(d1)
            #print ('es la division')
            #print (d1)
    if tok.type=='JUMPLINE':
        lista.clear
        a=0
        b=0
        print('result',d1)
        #print (d1)
        
