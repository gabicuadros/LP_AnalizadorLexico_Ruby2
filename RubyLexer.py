import ply.lex as lex
reserved = {
 "while":"WHILE",
 "and":"AND",
 "break":"BREAK",
 "def":"DEF",
 "end":"END",
 "in":"IN",
 "nil":"NIL",
 "or":"OR",
 "begin":"BEGIN",
 "if":"IF",
 "else":"ELSE",
 "elsif":"ELSIF",
 "for":"FOR",
 "puts":"PUTS",
 "gets":"GETS",
 "false":"FALSE",
 "true":"TRUE",
 "print":"PRINT",
 "length":"LENGTH",
 "delete_at":"DELETE_AT",
 "do":"DO"
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
    "DOSPUNTOS",
    "LPAREN",
    "RPAREN",
    "COMA",
    "CADENA",
    "NEGACION",
    "OPAND",
    "OPOR",
    "DIFERENTE",
    "IGUALA",
    "MAYORIGU",
    "MENORIGU",
    "OPXOR",
    "RANGO",
    "ASIGNACION",
    "NEGATIVO"
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
t_DOSPUNTOS = r':'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMA = r'\,'
t_NEGACION=r'!'
t_OPAND=r'\&\&'
t_OPOR=r'\|\|'
t_DIFERENTE=r'!='
t_IGUALA=r'=='
t_OPXOR=r'\^'
t_RANGO=r'\d\.\.\d'
t_ASIGNACION=r'=>'
t_NEGATIVO=r'\-'
def t_WHILE(t):
    r'while'
    return t

def t_IF(t):
        r'if'
        return t


def t_ELSE(t):
    r'else'
    return t

def t_ELSIF(t):
        r'elsif'
        return t

def t_FOR(t):
        r'for'
        return t

def t_AND(t):
        r'and'
        return t

def t_BREAK(t):
        r'break'
        return t

def t_DEF(t):
        r'def'
        return t

def t_END(t):
        r'end'
        return t

def t_LENGTH(t):
        r'\.length'
        return t

def t_DELETE_AT(t):
        r'\.delete_at'
        return t

def t_IN(t):
        r'in'
        return t

def t_NIL(t):
        r'nil'
        return t

def t_OR(t):
        r'or'
        return t

def t_BEGIN(t):
        r'begin'
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

def analizar(data):
        arr = []
        lexer.input(data)   
        # Tokenize	
        while True:	    
                tok = lexer.token()	        
                if not tok:	       
                        break  # No more input	          
                arr.append(tok)
        return arr
    


