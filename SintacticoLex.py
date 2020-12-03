import ply.yacc as yacc
 

from RubyLexer import tokens

def p_algoritmo(p):
    '''algoritmo : imprimir
                 | asignacion
                 | sentenciaIf
                 | comparacionLog
                 | sentenciaWhile
                 | sentenciaFuncion
                 | expresion_funcion
                 | ingreso
                 | varianteIf
                 | estructurabegin
                 | array_func
                 | estructura_for
                 | slice_array
    '''
def p_break(p):
    '''break : BREAK
             | empty 
    '''

def p_sentenciaIf(p):

    'sentenciaIf : IF comparacionLog algoritmo varianteIf'


def p_varienteIf(p):
    '''varianteIf : ELSIF comparacionLog algoritmo varianteIf

                  | ELSE algoritmo break END

                  | break END

    '''

def p_sentenciaWhile(p):
    'sentenciaWhile : WHILE LPAREN comparacionLog RPAREN DOSPUNTOS algoritmo'

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
    'true : negacion TRUE'
 
def p_false(p):
    'false : negacion FALSE'
 
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

def p_estructura_for(p):
    '''estructura_for : FOR VARIABLE IN array DO algoritmo END
                      | FOR VARIABLE IN RANGO DO algoritmo END
                      | FOR VARIABLE IN array algoritmo END
    '''

def p_array(p): 
    """
    array : CIZQ CDER
          | CIZQ parametros CDER
    """
def p_array_func(p):
    'array_func : VARIABLE funciones_Array'
    
def p_funciones_Array(p):
    '''funciones_Array : length_array 
                       | deleteAT_array               
    '''
def p_deleteAT_array(p):
    ''' deleteAT_array : DELETE_AT LPAREN ENTERO RPAREN
    '''

def p_length_array(p):
    ''' length_array : LENGTH
                     | LENGTH LPAREN RPAREN
    '''
#slicing
def p_slice_array(p):
    ''' slice_array : VARIABLE CIZQ ENTERO CDER
                    | VARIABLE CIZQ RANGO CDER
    '''
    
def p_hash(p):
    ''' hash :  LIZQ params_hash LDER
             |  LIZQ  LDER
    '''

def p_params_hash(p):
    '''params_hash : CADENA ASIGNACION valor
                   | negativo ENTERO ASIGNACION valor
                   | negativo DECIMAL ASIGNACION valor
                   | CADENA ASIGNACION valor COMA params_hash
                   | negativo ENTERO ASIGNACION valor COMA params_hash
                   | negativo DECIMAL ASIGNACION valor COMA params_hash
    '''

def p_valor(p):
    '''valor : negativo ENTERO
             | VARIABLE
             | CADENA
             | negativo DECIMAL
             | array
             | hash
             | NIL
             | RANGO
    '''
              
def p_negativo(p):
    '''negativo : NEGATIVO
                | empty
    '''

def p_estructurabegin(p):
    'estructurabegin : BEGIN algoritmo END'

def p_negacion(p):
    '''negacion : NEGACION
                | empty
    '''
def p_empty(p):
    'empty :'
    pass

# Error rule for syntax errors
error=[]
error.append("")
def p_error(p):
    error[0] = "Syntax error in input!"
    print("Syntax error in input!")
 
# Build the parser
parser = yacc.yacc()