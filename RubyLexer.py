import ply.lex as lex
reserved = {
 "while":"WHILE",
 "alias":"ALIAS",
 "and":"AND",
 "break":"BREAK",
 "class":"CLASS",
 "def":"DEF",
 "end":"END",
 "ensure":"ENSURE",
 "in":"IN",
 "module":"MODULE",
 "next":"NEXT",
 "nil":"NIL",
 "not":"NOT",
 "or":"OR",
 "redo":"REDO",
 "rescue":"RESCUE",
 "retry":"RETRY",
 "return":"RETURN",
 "self":"SELF",
 "super":"SUPER",
 "then":"THEN",
 "undef":"UNDEF",
 "unless":"UNLESS",
 "until":"UNTIL",
 "when":"WHEN",
 "yield":"YIELD",
 "_FILE_":"FILE",
 "_LINE_":"LINE",
 "case":"CASE",
 "begin":"BEGIN",
 "if":"IF",
"else":"ELSE",
 "elif":"ELIF",
 "for":"FOR",
 "Array":"ARRAY",
 "puts":"PUTS",
 "gets":"GETS",
 "false":"FALSE",
 "true":"TRUE",
 "print":"PRINT",
 "initialize":"INITIALIZE",
 ".new":"NEW",
 "Hash":"HASH"
}
tokens = [
    "VARIABLE",
    "IGUAL",
    "PROD",
    "MOD",
    "MAYOR",
    "ENTERO",
    "MAS",
    "DECIMAL",
    "DIV",
    "RESTA",
    "POTENCIA",
    "LIZQ",
    "LDER",
    "CIZQ",
    "CDER",
    "MENOR",
    "BOOLEANO",
    "PUNTO",
    "PUNTOYCOMA",
    "DOSPUNTOS",
    "LPAREN",
    "RPAREN",
    "COMA",
    "DOBLECOMILLA",
    "CADENA",
    "NEGACION",
    "OPAND",
    "OPOR",
    "DIFERENTE",
    "IGUALA",
    "MAYORIGU",
    "MENORIGU",
    "IMPRIMIR",
    "OPXOR",
    "RANGO"
] + list(reserved.values())
t_IGUAL= r"="
t_PROD = r"\*"
t_MAS = r"\+"
t_DECIMAL = r"\d+\.\d+"
t_MOD = r"%"
t_MAYOR = r">"
t_MENOR = r"<"
t_MAYORIGU = r">="
t_MENORIGU = r"<="
t_ENTERO = r"\d+"
t_DIV=r"/"
t_POTENCIA=r"\*\*"
t_RESTA=r"-"
t_CIZQ=r"\["
t_CDER=r"\]"
t_LIZQ=r"\{"
t_LDER=r"\}"
t_PUNTO = r'\.'
t_PUNTOYCOMA = r'\;'
t_DOSPUNTOS = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMA = r'\,'
t_DOBLECOMILLA= r'\"'
t_NEGACION=r'!'
t_OPAND=r'\&\&'
t_OPOR=r'\|\|'
t_DIFERENTE=r'!='
t_IGUALA=r'=='
t_OPXOR=r'\^'
t_RANGO=r'\.\.'

def t_WHILE(t):
    r'while'
    return t

def t_IF(t):
        r'if'
        return t


def t_ELSE(t):
    r'else'
    return t

def t_ELIF(t):
        r'elif'
        return t

def t_FOR(t):
        r'for'
        return t

def t_ALIAS(t):
        r'alias'
        return t

def t_AND(t):
        r'and'
        return t

def t_BREAK(t):
        r'break'
        return t

def t_CLASS(t):
        r'class .*'
        return t

def t_DEF(t):
        r'def'
        return t

def t_END(t):
        r'end'
        return t

def t_ENSURE(t):
        r'ensure'
        return t

def t_IN(t):
        r'in'
        return t

def t_MODULE(t):
        r'module'
        return t

def t_NIL(t):
        r'nil'
        return t

def t_NOT(t):
        r'not'
        return t

def t_OR(t):
        r'or'
        return t

def t_REDO(t):
        r'redo'
        return t

def t_RESCUE(t):
        r'rescue'
        return t

def t_RETRY(t):
        r'retry'
        return t

def t_RETURN(t):
        r'return'
        return t

def t_SELF(t):
        r'self'
        return t

def t_SUPER(t):
        r'super'
        return t

def t_THEN(t):
        r'then'
        return t

def t_UNDEF(t):
        r'undef'
        return t

def t_UNTIL(t):
        r'until'
        return t

def t_WHEN(t):
        r'when'
        return t

def t_YIELD(t):
        r'yield'
        return t

def t_FILE(t):
        r'_FILE_'
        return t

def t_LINE(t):
        r'_LINE_'
        return t

def t_CASE(t):
        r'case'
        return t

def t_BEGIN(t):
        r'begin'
        return t

def t_ARRAY(t):
        r'array'
        return t

def t_CADENA(t):
        r'(\'[a-zA-Z0-9\!\s\.,:]*\'|\"[a-zA-Z0-9\!\s\.,:]*\")'
        return t

def t_PUTS(t):
        r'puts'
        return t

def t_GETS(t):
        r'gets'
        return t

def t_TRUE(t):
        r'[Tt]rue'
        return t

def t_FALSE(t):
        r'[Ff]alse'
        return t

def t_PRINT(t):
        r'printf?'
        return t

def t_INITIALIZE(t):
        r'initialize'
        return t

def t_NEW(t):
        r'\.new'
        return t

def t_HASH(t):
        r'Hash'
        return t

def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

def t_VARIABLE(t):
    r"(_|@|@@|\$)?[a-zA-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'
t_ignore_COMMENT=r'(\#.*)'
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
'''def analizar(data):
    lexer.input(data)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break  # No more input
        print(tok)



print("Mi primer analizador léxico:")
# Testing

archivo = open("codigo.txt")
for linea in archivo:
    print(">>"+linea)
    analizar(linea)
    if len(linea)==0:
        break'''
