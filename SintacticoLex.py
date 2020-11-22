import ply.yacc as yacc
 

from RubyLexer2 import tokens



def p_algoritmo(p):
    '''algoritmo : imprimir
                 | asignacion
                 | expresion
                 | comparacion
                 | sentenciaIf
    '''
def p_sentenciaIf(p):
    'sentenciaIf : IF LPAREN comparacion RPAREN DOSPUNTOS algoritmo'
def p_asignacion(p):
    'asignacion : VARIABLE IGUAL expresion'

def p_imprimir(p):
    'imprimir : PRINT LPAREN expresion RPAREN'
    
def p_expresion(p):
    '''expresion : valor
    '''
def p_comparacion(p):
    'comparacion : expresion operadorCom expresion'

def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_operadorMat(p):
    '''operadorMat : MAS
                   | RESTA
                   | DIV
                   | PROD
    '''

def p_operadorComp(p):
    '''operadorCom : MAYOR
                   | MENOR
                   | MAYORIGU
                   | MENORIGU
                   | DIFERENTE
    '''



def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
    '''
# Error rule for syntax errors
def p_error(p):
     print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()
 
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    print(result)

     

