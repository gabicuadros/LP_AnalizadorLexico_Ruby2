import ply.lex as lex
reserved = {

 "while":"WHILE",

 "alias":"ALIAS",

 "and":"AND",

 "break":"BREAK",

 "class": "CLASS",

 "def":"DEF",

 "end":"END",

 "ensure":"ENSURE",

 "false":"FALSE",

 "true":"TRUE",

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

 "_FILE_":"_FILE_",

 "_LINE_":"_LINE_",

 "case":"CASE",

 "begin":"BEGIN"
    
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
    "less",
    "BOOLEANO",
    "IF",
    "FOR"

] + list(reserved.values())
t_IGUAL= r"="
t_PROD = r"\*"
t_MAS = r"\+"
t_DECIMAL = r"\d+\.\d+"
t_MOD = r"%"
t_MAYOR = r">"
t_ENTERO = r"\d+"
t_DIV=r"/"
t_POTENCIA=r"\*\*"
t_RESTA=r"-"
t_CIZQ=r"\["
t_CDER=r"\]"
t_LIZQ=r"\{"
t_LDER=r"\}"
t_BOOLEANO=r"(true|false)"


def t_while(t):
    r'while'
    return t

def t_IF(t):
        r'if'
        return t

def t_FOR(t):
        r'for'
        return t

def build(self, **kwargs):
        self.lexer = lex.lex(module=self, **kwargs)

def t_VARIABLE(t):
    r"(_|@|@@|$)?[a-zA-Z][a-zA-Z0-9_]*"
    t.type = reserved.get(t.value, 'VARIABLE')  # Check for reserved words
    return t

def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)
t_ignore = ' \t'
def t_error(t):
    print("No es reconocido '%s'" % t.value[0])
    t.lexer.skip(1)
lexer = lex.lex()
def analizar(data):
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
        break
