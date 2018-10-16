#-------------------------------------------------------------------------------
# Name:        lexerkarel1.1.py
# linkografia: http://www.cmirg.com/karelotitlan/curso/introduccion.html
#http://www.olimpiadadeinformatica.org.mx/omi/OMI_Primaria/material/EntrenamientoOMIKarel/Varios/Tutorial-de-Karel-Final.pdf
#
#-------------------------------------------------------------------------------
import ply.lex as lex


listaReservadas = {

    	'apagate' : 'E_TURNOFF',
    	'avanza':'INSTRUCCION_MOVE',
    	'coge-zumbador':'INSTRUCCION_PICKBEEPER',
    	'deja-zumbador':'INSTRUCCION_PUTBEEPER',
        'iniciar-programa':'INSTRUCCION_START_PROGRAM',
        'finalizar-programa':'INSTRUCCION_END_PROGRAM',
        'gira-izquierda':'INSTRUCCION_TURNLEFT',
        'inicia-ejecucion':'INSTRUCCION_START_EXECUTION',
        'termina-ejecucion':'INSTRUCCION_END_EXECUTION',
    	'inicio':'E_RESERVADA',
        'fin' : 'E_RESERVADA',
        'como' : 'E_RESERVADA',
    	'entonces' : 'EST_CONTROL',
        'sino' : 'EST_CONTROL',
        'si' : 'EST_CONTROL',
    	'mientras' : 'EST_ITERACION',
       'para' : 'EST_ITERACION',
    	'hasta' : 'EST_ITERACION',
    	'hacer' : 'EST_ITERACION',
    	'repetir' : 'EST_ITERACION',
    	'veces' : 'EST_ITERACION',
        'frente-libre':'Bool_frontIsClear',
        'frente-bloqueado':'Bool_frontIsBlocked',
        'izquierda-libre':'Bool_leftIsClear',
        'izquierda-bloqueada':'Bool_leftIsBlocked',
        'derecha-libre':'Bool_rightIsClear',
        'derecha-bloqueada':'Bool_rightIsBlocked',
        'junto-a-zumbador':'Bool_nextToABeeper',
        'no-junto-a-zumbador':'Bool_notNextToABeeper',
        'algun-zumbador-en-la mochila':'Bool_anyBeepersInBeeperBag',
        'ningun-zumbador-en-la mochila':'Bool_noBeepersInBeeperBag',
        'orientado-al-norte':'Bool_facingNorth',
        'orientado-al-sur':'Bool_facingSouth',
        'orientado-al-este':'Bool_facingEast',
        'orientado-al-oeste':'Bool_facingWest',
        'no-orientado-al-norte':'Bool_notFacingNorth',
        'no-orientado-al-sur':'Bool_notFacingSouth',
        'no-orientado-al-este':'Bool_notFacingEast',
        'no-orientado-al-oeste':'Bool_notFacingWest'
}


tokens = ['IDENTIFICADOR','NUMERO','PROGRAMA','FIN_INSTRUCCION','NEW_INSTRUCTION','ABRIRPARENTESIS','CERRARPARENTESIS','PUNTOCOMA','OPERADOR_Y','OPERADOR_NO','OPERADOR_O','OPENBLOCK','CLOSEDBLOCK',
'GUION','TYPE_DEFINE']

tokens = tokens + list(listaReservadas.values())

t_ignore = ' \t'
t_FIN_INSTRUCCION = '\;'
t_GUION = '\-'
t_ignore_COMMENT = r'\{.*'
t_ABRIRPARENTESIS = r'\('
t_CERRARPARENTESIS = r'\)'
t_TYPE_DEFINE = r'void'
t_OPERADOR_Y = r'&&'
t_OPERADOR_NO = r'!'
#t_OPERADOR_O= r'\||'
t_OPENBLOCK =r'\{'
t_CLOSEDBLOCK =r'\}'
t_NEW_INSTRUCTION= r'define-nueva-instruccion'

def t_NUMERO(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t
def t_PROGRAMA(t):
    r'programa'
    return t

def t_SALTOLINEA(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
def t_IDENTIFICADOR(t):
    r'[-a-zA-Z][-a-zA-Z]*'
    t.type = listaReservadas.get(t.value,'IDENTIFICADOR')
    return t


def abrir_archivo(nombre):
    archivo = open(nombre, 'r')
    return  archivo.readlines()

def t_error(t):
    print("ERROR -> %s" % t.value)
    t.lexer.skip(1)

def abrir_archivo(nombre):
    archivo = open(nombre, 'r')
    return  archivo.read()


lex.lex()

lex.input(abrir_archivo("expresiones.txt"))

while True:
    tok = lex.token()
    if not tok: break
    print (str(tok.value) + " ---> " + str(tok.type))