import ply.yacc as yacc
 

from RubyLexer import tokens

def p_algoritmo(p):
    '''algoritmo : imprimir
                 | asignacion
                 | expresion
                 | sentenciaIf
                 | comparacionLog
                 | sentenciaWhile
                 | sentenciaFuncion
                 | expresion_funcion
                 | ingreso
                 | varianteIf
    '''

def p_sentenciaIf(p):

    'sentenciaIf : IF comparacion algoritmo varianteIf'



def p_varienteIf(p):

    '''varianteIf : ELSIF comparacion algoritmo varianteIf

                  | ELSE algoritmo END

                  | END

    '''

def p_sentenciaWhile(p):
    'sentenciaWhile : WHILE LPAREN comparacion RPAREN DOSPUNTOS algoritmo'

def p_asignacion(p):
    'asignacion : VARIABLE IGUAL valores'



def p_imprimir(p):
    '''imprimir : print
                | puts
    '''

def p_asignacion_bool(p):
    '''valores : expresion
                | true
                | false
    '''
def p_true(p):
    'true : TRUE'
 
def p_false(p):
    'false : FALSE'
 
def p_ingreso(p):
    '''ingreso : gets
    '''
 
def p_gets(p):
    'gets : GETS expresion'

def p_print(p):
    'print : PRINT LPAREN expresion RPAREN'

def p_puts(p):
    'puts : PUTS expresion'
    
def p_expresion(p):
    '''expresion : valor
    '''
def p_comparacion(p):
    'comparacion : expresion operadorCom expresion'

def p_comparacionLogica(p):
    'comparacionLog : comparacion operadorLog comparacionLog'

def p_comparacionLog(p):
    '''comparacionLog : comparacion
    '''
    
def p_expresion_aritmetica(p):
    'expresion : valor operadorMat expresion'

def p_operadorMat(p):
    '''operadorMat : MAS
                   | RESTA
                   | DIV
                   | PROD
                   | POTENCIA
                   | MOD
    '''

def p_operadorComp(p):
    '''operadorCom : MAYOR
                   | MENOR
                   | MAYORIGU
                   | MENORIGU
                   | DIFERENTE
                   | IGUALA
    '''
def p_operadorLog(p):
    '''operadorLog  : OPAND
                    | OPOR
                    | OPXOR
                    | AND
                    | OR
    '''
def p_expresion_funcion(p):
    'expresion_funcion : VARIABLE LPAREN parametros RPAREN'

def p_parametros(p):
    '''parametros : valor
                  | asignacion  
                  | valor COMA parametros
                  
    '''

def p_sentenciafuncion(p): 
    """sentenciaFuncion : DEF expresion_funcion expresion END
    """
  
def p_array(p): 
    """
    array : VARIABLE IGUAL CIZQ CDER
          | VARIABLE IGUAL CIZQ parametros CDER
          | VARIABLE IGUAL ARRAY NEW
          | VARIABLE IGUAL ARRAY NEW CIZQ parametros CDER
    

    """

def p_hash(p):
    ''' hash : VARIABLE IGUAL LIZQ params_hash LDER
    '''

def p_params_hash(p):
    '''params_hash : CADENA ASIGNACION valor
                   | ENTERO ASIGNACION valor
                   | DECIMAL ASIGNACION valor
                   | CADENA ASIGNACION valor COMA params_hash
    '''

def p_valor(p):
    '''valor : ENTERO
             | VARIABLE
             | CADENA
             | DECIMAL
             | array
             | hash
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

     

