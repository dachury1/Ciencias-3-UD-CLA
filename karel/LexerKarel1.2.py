#-------------------------------------------------------------------------------
# Name:        lexerkarel1.2.py
# linkografia: http://www.cmirg.com/karelotitlan/curso/introduccion.html
#http://www.olimpiadadeinformatica.org.mx/omi/OMI_Primaria/material/EntrenamientoOMIKarel/Varios/Tutorial-de-Karel-Final.pdf
#
#-------------------------------------------------------------------------------

import ply.lex as lex
a=0
tokens = ['FIN','ESTRUCTURAS','RESERVADA','INSTRUCCION','E_MOVE','E_TURNOFF','NUMERO','EST_CONTROL','EST_ITERACION','E_BOOL','E_FIN',
'NEW_INSTRUCTION','PROGRAMA','ABRIRPARENTESIS','CERRARPARENTESIS','FIN_INSTRUCCION','OPERADOR_Y','OPERADOR_NO','OPERADOR_O','OPENBLOCK','CLOSEDBLOCK',
'TYPE_DEFINE']


estructurasControl=['SI','SINO','ENTONCES','ningun','algun']

estructurasIteracion=['PARA','HASTA','SALTAR','MIENTRAS','VECES','HACER','REPETIR']

expresionesLIST1=['iniciar-programa','deja-zumbador','coge-zumbador','gira-izquierda','inicia-ejecucion','termina-ejecucion']

reservadasLIST=['fin','inicio','mochila','como']

funcionBooleana1LIST=['frente-libre','frente-bloqueado','izquierda-libre','izquierda-bloqueada','derecha-libre','derecha-bloqueada','algun-zumbador-en-la-mochila',
                     'ningun-zumbador-en-la-mochila','orientado-al-norte','orientado-al-sur','orientado-al-este',
                     'orientado-al-oeste','no-orientado-al-este','no-orientado-al-oeste','no-junto-a-zumbador',
                      'no-orientado-al-norte','no-orientado-al-sur','junto-a-zumbador','no-junto-a-zumbador']

t_ignore = ' \n'
t_ABRIRPARENTESIS = r'\('
t_CERRARPARENTESIS = r'\)'
t_FIN_INSTRUCCION	= ';'
t_TYPE_DEFINE = r'void'
t_OPERADOR_Y = r'&&'
t_OPERADOR_NO = r'!'
#t_OPERADOR_O= r'\||'
t_OPENBLOCK =r'\{'
t_CLOSEDBLOCK =r'\}'
t_NEW_INSTRUCTION= r'define-nueva-instruccion'


def t_FIN(t):
    r'[finalizar]*'r'\-+'r'[programa]*'
    t.type = 'E_FIN'
    return t

def t_APAGATE(t):
    r'apagate'
    t.type = 'E_TURNOFF'
    return t

def t_PROGRAMA(t):
    r'programa'
    return t


def t_MOVE(t):
    r'avanza'
    t.type = 'E_MOVE'
    return t

def t_BOOl(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*' r'\-' r'[_a-zA-Z_][_a-zA-Z0-9_]*'
    #print(t.value)
    if t.value in funcionBooleana1LIST:
        t.type = 'E_BOOL'
        return t
    elif t.value in expresionesLIST1:
        t.type = 'INSTRUCCION'
        return t



def t_ESTRUCTURAS(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    for r in estructurasControl:
        if r.upper() == t.value.upper():
            t.type = 'EST_CONTROL'
    return t

    for r  in funcionesIteracion:
      if r.upper() == t.value.upper():
        t.type = 'EST_ITERACION'
        return t

    for r in reservadasLIST:
         if r.upper() == t.value.upper():
            t.type = 'RESERVADA'
            return t


def t_COMENTARIO(t):
    r'\#.*'
    pass


def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def abrir_archivo(nombre):
    archivo = open(nombre, 'r')
    return  archivo.readlines()

# Error handling rule
def t_error(t):
    print("Caracter invalido '%s'" % t.value[0])
    t.lexer.skip(1)


listaExpresiones = [x.strip('\n') for x in abrir_archivo("expresiones.txt")]
#print (listaExpresiones)

lex.lex() # Build the lexer
for x in listaExpresiones:
    lex.input(x)
    #print (x)
    while True:
        tok = lex.token()
        if not tok: break
        guion=-1
        guion = x.find("-")
        if guion != -1:
            #print ('compuestas')
            print (str(tok.value) + " ---> " + str(tok.type))
            a=1
        else :

            print (str(tok.value) + " ---> " + str(tok.type))
            a=2
