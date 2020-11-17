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
 "for":"FOR",
 "Array":"ARRAY"    
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
    "TRUE",
    "FALSE"   

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
t_TRUE=r"([Tt]rue|TRUE)"
t_FALSE=r"([Ff]alse|FALSE)"

def t_while(t):
    r'while'
    return t

def t_IF(t):
        r'if'
        return t

def t_FOR(t):
        r'for'
        return t

def t_alias(t):
        r'alias'
        return t

def t_and(t):
        r'and'
        return t

def t_break(t):
        r'break'
        return t

def t_class(t):
        r'class .*'
        return t

def t_def(t):
        r'def'
        return t

def t_end(t):
        r'end'
        return t

def t_ensure(t):
        r'ensure'
        return t

def t_in(t):
        r'in'
        return t

def t_module(t):
        r'module'
        return t

def t_nil(t):
        r'nil'
        return t

def t_not(t):
        r'not'
        return t

def t_or(t):
        r'or'
        return t

def t_redo(t):
        r'redo'
        return t

def t_rescue(t):
        r'rescue'
        return t

def t_retry(t):
        r'retry'
        return t

def t_return(t):
        r'return'
        return t

def t_self(t):
        r'self'
        return t

def t_super(t):
        r'super'
        return t

def t_then(t):
        r'then'
        return t

def t_undef(t):
        r'undef'
        return t

def t_until(t):
        r'until'
        return t

def t_when(t):
        r'when'
        return t

def t_yield(t):
        r'yield'
        return t

def t_FILE(t):
        r'_FILE_'
        return t

def t_LINE(t):
        r'_LINE_'
        return t

def t_case(t):
        r'case'
        return t

def t_begin(t):
        r'begin'
        return t

def t_array(t):
        r'array'
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
