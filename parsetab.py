
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARRAY BEGIN BOOLEANO BREAK CADENA CASE CDER CIZQ CLASS COMA DECIMAL DEF DIFERENTE DIV DOBLECOMILLA DOSPUNTOS ELIF ELSE END ENSURE ENTERO FALSE FILE FOR GETS HASH IF IGUAL IGUALA IMPRIMIR IN INITIALIZE LDER LINE LIZQ LPAREN MAS MAYOR MAYORIGU MENOR MENORIGU MOD MODULE NEGACION NEW NEXT NIL NOT OPAND OPOR OPXOR OR POTENCIA PRINT PROD PUNTO PUNTOYCOMA PUTS RANGO REDO RESCUE RESTA RETRY RETURN RPAREN SELF SUPER THEN TRUE UNDEF UNLESS UNTIL VARIABLE WHEN WHILE YIELDalgoritmo : imprimir\n                 | asignacion\n                 | expresion\n                 | sentenciaIf\n                 | comparacionLog\n                 | sentenciaWhile\n                 | sentenciaFuncion\n                 | expresion_funcion\n                 | ingreso\n                 | sentenciaElse\n    sentenciaIf : IF LPAREN comparacion RPAREN DOSPUNTOS algoritmosentenciaElse : ELSE algoritmo ENDsentenciaWhile : WHILE LPAREN comparacion RPAREN DOSPUNTOS algoritmoasignacion : VARIABLE IGUAL valoresimprimir : print\n                | puts\n    valores : expresion\n                | true\n                | false\n    true : TRUEfalse : FALSEingreso : gets\n    gets : GETS expresionprint : PRINT LPAREN expresion RPARENputs : PUTS expresionexpresion : valor\n    comparacion : expresion operadorCom expresioncomparacionLog : comparacion operadorLog comparacionLogcomparacionLog : comparacion\n    expresion : valor operadorMat expresionoperadorMat : MAS\n                   | RESTA\n                   | DIV\n                   | PROD\n                   | POTENCIA\n                   | MOD\n    operadorCom : MAYOR\n                   | MENOR\n                   | MAYORIGU\n                   | MENORIGU\n                   | DIFERENTE\n                   | IGUALA\n    operadorLog  : OPAND\n                    | OPOR\n                    | OPXOR\n                    | AND\n                    | OR\n    expresion_funcion : VARIABLE LPAREN parametros RPARENparametros : valor\n                  | asignacion                   \n    sentenciaFuncion : DEF expresion_funcion expresion END\n    \n    array : VARIABLE IGUAL CIZQ CDER\n          | VARIABLE IGUAL CIZQ valor CDER  \n          | VARIABLE IGUAL ARRAY NEW\n          | VARIABLE IGUAL ARRAY NEW LPAREN parametros RPAREN\n\n    valor : ENTERO\n             | VARIABLE\n             | CADENA\n             | DECIMAL\n             | array\n    '
    
_lr_action_items = {'VARIABLE':([0,19,21,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,62,85,91,92,93,],[14,54,14,58,58,58,-37,-38,-39,-40,-41,-42,58,69,58,-31,-32,-33,-34,-35,-36,58,58,-43,-44,-45,-46,-47,58,58,58,58,-48,69,14,14,]),'IF':([0,21,92,93,],[16,16,16,16,]),'WHILE':([0,21,92,93,],[18,18,18,18,]),'DEF':([0,21,92,93,],[19,19,19,19,]),'ELSE':([0,21,92,93,],[21,21,21,21,]),'PRINT':([0,21,92,93,],[22,22,22,22,]),'PUTS':([0,21,92,93,],[23,23,23,23,]),'ENTERO':([0,21,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,62,85,91,92,93,],[24,24,24,24,24,-37,-38,-39,-40,-41,-42,24,24,24,-31,-32,-33,-34,-35,-36,24,24,-43,-44,-45,-46,-47,24,24,24,24,-48,24,24,24,]),'CADENA':([0,21,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,62,85,91,92,93,],[25,25,25,25,25,-37,-38,-39,-40,-41,-42,25,25,25,-31,-32,-33,-34,-35,-36,25,25,-43,-44,-45,-46,-47,25,25,25,25,-48,25,25,25,]),'DECIMAL':([0,21,23,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,56,62,85,91,92,93,],[26,26,26,26,26,-37,-38,-39,-40,-41,-42,26,26,26,-31,-32,-33,-34,-35,-36,26,26,-43,-44,-45,-46,-47,26,26,26,26,-48,26,26,26,]),'GETS':([0,21,92,93,],[28,28,28,28,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,20,24,25,26,27,57,58,59,60,61,64,65,66,67,68,73,76,79,82,84,85,88,89,90,95,96,97,],[0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-15,-16,-57,-26,-29,-22,-56,-58,-59,-60,-25,-57,-23,-27,-14,-17,-18,-19,-20,-21,-30,-28,-12,-52,-54,-48,-51,-24,-53,-11,-13,-55,]),'END':([2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,20,24,25,26,27,55,57,58,59,60,61,64,65,66,67,68,73,76,78,79,82,84,85,88,89,90,95,96,97,],[-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-15,-16,-57,-26,-29,-22,-56,-58,-59,-60,79,-25,-57,-23,-27,-14,-17,-18,-19,-20,-21,-30,-28,88,-12,-52,-54,-48,-51,-24,-53,-11,-13,-55,]),'MAYOR':([4,14,15,24,25,26,27,58,73,75,82,84,90,97,],[30,-57,-26,-56,-58,-59,-60,-57,-30,30,-52,-54,-53,-55,]),'MENOR':([4,14,15,24,25,26,27,58,73,75,82,84,90,97,],[31,-57,-26,-56,-58,-59,-60,-57,-30,31,-52,-54,-53,-55,]),'MAYORIGU':([4,14,15,24,25,26,27,58,73,75,82,84,90,97,],[32,-57,-26,-56,-58,-59,-60,-57,-30,32,-52,-54,-53,-55,]),'MENORIGU':([4,14,15,24,25,26,27,58,73,75,82,84,90,97,],[33,-57,-26,-56,-58,-59,-60,-57,-30,33,-52,-54,-53,-55,]),'DIFERENTE':([4,14,15,24,25,26,27,58,73,75,82,84,90,97,],[34,-57,-26,-56,-58,-59,-60,-57,-30,34,-52,-54,-53,-55,]),'IGUALA':([4,14,15,24,25,26,27,58,73,75,82,84,90,97,],[35,-57,-26,-56,-58,-59,-60,-57,-30,35,-52,-54,-53,-55,]),'IGUAL':([14,58,69,],[36,81,36,]),'LPAREN':([14,16,18,22,54,84,],[37,45,52,56,37,91,]),'MAS':([14,15,24,25,26,27,58,82,84,90,97,],[-57,39,-56,-58,-59,-60,-57,-52,-54,-53,-55,]),'RESTA':([14,15,24,25,26,27,58,82,84,90,97,],[-57,40,-56,-58,-59,-60,-57,-52,-54,-53,-55,]),'DIV':([14,15,24,25,26,27,58,82,84,90,97,],[-57,41,-56,-58,-59,-60,-57,-52,-54,-53,-55,]),'PROD':([14,15,24,25,26,27,58,82,84,90,97,],[-57,42,-56,-58,-59,-60,-57,-52,-54,-53,-55,]),'POTENCIA':([14,15,24,25,26,27,58,82,84,90,97,],[-57,43,-56,-58,-59,-60,-57,-52,-54,-53,-55,]),'MOD':([14,15,24,25,26,27,58,82,84,90,97,],[-57,44,-56,-58,-59,-60,-57,-52,-54,-53,-55,]),'OPAND':([15,17,24,25,26,27,58,60,73,82,84,90,97,],[-26,47,-56,-58,-59,-60,-57,-27,-30,-52,-54,-53,-55,]),'OPOR':([15,17,24,25,26,27,58,60,73,82,84,90,97,],[-26,48,-56,-58,-59,-60,-57,-27,-30,-52,-54,-53,-55,]),'OPXOR':([15,17,24,25,26,27,58,60,73,82,84,90,97,],[-26,49,-56,-58,-59,-60,-57,-27,-30,-52,-54,-53,-55,]),'AND':([15,17,24,25,26,27,58,60,73,82,84,90,97,],[-26,50,-56,-58,-59,-60,-57,-27,-30,-52,-54,-53,-55,]),'OR':([15,17,24,25,26,27,58,60,73,82,84,90,97,],[-26,51,-56,-58,-59,-60,-57,-27,-30,-52,-54,-53,-55,]),'RPAREN':([15,24,25,26,27,58,60,61,64,65,66,67,68,69,70,71,72,73,74,77,80,82,84,90,94,97,],[-26,-56,-58,-59,-60,-57,-27,-14,-17,-18,-19,-20,-21,-57,85,-49,-50,-30,86,87,89,-52,-54,-53,97,-55,]),'CDER':([24,25,26,27,58,62,82,83,84,90,97,],[-56,-58,-59,-60,-57,82,-52,90,-54,-53,-55,]),'CIZQ':([36,81,],[62,62,]),'ARRAY':([36,81,],[63,63,]),'TRUE':([36,],[67,]),'FALSE':([36,],[68,]),'NEW':([63,],[84,]),'DOSPUNTOS':([86,87,],[92,93,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'algoritmo':([0,21,92,93,],[1,55,95,96,]),'imprimir':([0,21,92,93,],[2,2,2,2,]),'asignacion':([0,21,37,91,92,93,],[3,3,72,72,3,3,]),'expresion':([0,21,23,28,29,36,38,45,46,52,53,56,92,93,],[4,4,57,59,60,64,73,75,75,75,78,80,4,4,]),'sentenciaIf':([0,21,92,93,],[5,5,5,5,]),'comparacionLog':([0,21,46,92,93,],[6,6,76,6,6,]),'sentenciaWhile':([0,21,92,93,],[7,7,7,7,]),'sentenciaFuncion':([0,21,92,93,],[8,8,8,8,]),'expresion_funcion':([0,19,21,92,93,],[9,53,9,9,9,]),'ingreso':([0,21,92,93,],[10,10,10,10,]),'sentenciaElse':([0,21,92,93,],[11,11,11,11,]),'print':([0,21,92,93,],[12,12,12,12,]),'puts':([0,21,92,93,],[13,13,13,13,]),'valor':([0,21,23,28,29,36,37,38,45,46,52,53,56,62,91,92,93,],[15,15,15,15,15,15,71,15,15,15,15,15,15,83,71,15,15,]),'comparacion':([0,21,45,46,52,92,93,],[17,17,74,17,77,17,17,]),'gets':([0,21,92,93,],[20,20,20,20,]),'array':([0,21,23,28,29,36,37,38,45,46,52,53,56,62,91,92,93,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'operadorCom':([4,75,],[29,29,]),'operadorMat':([15,],[38,]),'operadorLog':([17,],[46,]),'valores':([36,],[61,]),'true':([36,],[65,]),'false':([36,],[66,]),'parametros':([37,91,],[70,94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> algoritmo","S'",1,None,None,None),
  ('algoritmo -> imprimir','algoritmo',1,'p_algoritmo','SintacticoLex.py',7),
  ('algoritmo -> asignacion','algoritmo',1,'p_algoritmo','SintacticoLex.py',8),
  ('algoritmo -> expresion','algoritmo',1,'p_algoritmo','SintacticoLex.py',9),
  ('algoritmo -> sentenciaIf','algoritmo',1,'p_algoritmo','SintacticoLex.py',10),
  ('algoritmo -> comparacionLog','algoritmo',1,'p_algoritmo','SintacticoLex.py',11),
  ('algoritmo -> sentenciaWhile','algoritmo',1,'p_algoritmo','SintacticoLex.py',12),
  ('algoritmo -> sentenciaFuncion','algoritmo',1,'p_algoritmo','SintacticoLex.py',13),
  ('algoritmo -> expresion_funcion','algoritmo',1,'p_algoritmo','SintacticoLex.py',14),
  ('algoritmo -> ingreso','algoritmo',1,'p_algoritmo','SintacticoLex.py',15),
  ('algoritmo -> sentenciaElse','algoritmo',1,'p_algoritmo','SintacticoLex.py',16),
  ('sentenciaIf -> IF LPAREN comparacion RPAREN DOSPUNTOS algoritmo','sentenciaIf',6,'p_sentenciaIf','SintacticoLex.py',20),
  ('sentenciaElse -> ELSE algoritmo END','sentenciaElse',3,'p_sentenciaElse','SintacticoLex.py',23),
  ('sentenciaWhile -> WHILE LPAREN comparacion RPAREN DOSPUNTOS algoritmo','sentenciaWhile',6,'p_sentenciaWhile','SintacticoLex.py',26),
  ('asignacion -> VARIABLE IGUAL valores','asignacion',3,'p_asignacion','SintacticoLex.py',29),
  ('imprimir -> print','imprimir',1,'p_imprimir','SintacticoLex.py',34),
  ('imprimir -> puts','imprimir',1,'p_imprimir','SintacticoLex.py',35),
  ('valores -> expresion','valores',1,'p_asignacion_bool','SintacticoLex.py',39),
  ('valores -> true','valores',1,'p_asignacion_bool','SintacticoLex.py',40),
  ('valores -> false','valores',1,'p_asignacion_bool','SintacticoLex.py',41),
  ('true -> TRUE','true',1,'p_true','SintacticoLex.py',44),
  ('false -> FALSE','false',1,'p_false','SintacticoLex.py',47),
  ('ingreso -> gets','ingreso',1,'p_ingreso','SintacticoLex.py',50),
  ('gets -> GETS expresion','gets',2,'p_gets','SintacticoLex.py',54),
  ('print -> PRINT LPAREN expresion RPAREN','print',4,'p_print','SintacticoLex.py',57),
  ('puts -> PUTS expresion','puts',2,'p_puts','SintacticoLex.py',60),
  ('expresion -> valor','expresion',1,'p_expresion','SintacticoLex.py',63),
  ('comparacion -> expresion operadorCom expresion','comparacion',3,'p_comparacion','SintacticoLex.py',66),
  ('comparacionLog -> comparacion operadorLog comparacionLog','comparacionLog',3,'p_comparacionLogica','SintacticoLex.py',69),
  ('comparacionLog -> comparacion','comparacionLog',1,'p_comparacionLog','SintacticoLex.py',72),
  ('expresion -> valor operadorMat expresion','expresion',3,'p_expresion_aritmetica','SintacticoLex.py',76),
  ('operadorMat -> MAS','operadorMat',1,'p_operadorMat','SintacticoLex.py',79),
  ('operadorMat -> RESTA','operadorMat',1,'p_operadorMat','SintacticoLex.py',80),
  ('operadorMat -> DIV','operadorMat',1,'p_operadorMat','SintacticoLex.py',81),
  ('operadorMat -> PROD','operadorMat',1,'p_operadorMat','SintacticoLex.py',82),
  ('operadorMat -> POTENCIA','operadorMat',1,'p_operadorMat','SintacticoLex.py',83),
  ('operadorMat -> MOD','operadorMat',1,'p_operadorMat','SintacticoLex.py',84),
  ('operadorCom -> MAYOR','operadorCom',1,'p_operadorComp','SintacticoLex.py',88),
  ('operadorCom -> MENOR','operadorCom',1,'p_operadorComp','SintacticoLex.py',89),
  ('operadorCom -> MAYORIGU','operadorCom',1,'p_operadorComp','SintacticoLex.py',90),
  ('operadorCom -> MENORIGU','operadorCom',1,'p_operadorComp','SintacticoLex.py',91),
  ('operadorCom -> DIFERENTE','operadorCom',1,'p_operadorComp','SintacticoLex.py',92),
  ('operadorCom -> IGUALA','operadorCom',1,'p_operadorComp','SintacticoLex.py',93),
  ('operadorLog -> OPAND','operadorLog',1,'p_operadorLog','SintacticoLex.py',96),
  ('operadorLog -> OPOR','operadorLog',1,'p_operadorLog','SintacticoLex.py',97),
  ('operadorLog -> OPXOR','operadorLog',1,'p_operadorLog','SintacticoLex.py',98),
  ('operadorLog -> AND','operadorLog',1,'p_operadorLog','SintacticoLex.py',99),
  ('operadorLog -> OR','operadorLog',1,'p_operadorLog','SintacticoLex.py',100),
  ('expresion_funcion -> VARIABLE LPAREN parametros RPAREN','expresion_funcion',4,'p_expresion_funcion','SintacticoLex.py',103),
  ('parametros -> valor','parametros',1,'p_parametros','SintacticoLex.py',106),
  ('parametros -> asignacion','parametros',1,'p_parametros','SintacticoLex.py',107),
  ('sentenciaFuncion -> DEF expresion_funcion expresion END','sentenciaFuncion',4,'p_sentenciafuncion','SintacticoLex.py',111),
  ('array -> VARIABLE IGUAL CIZQ CDER','array',4,'p_array','SintacticoLex.py',116),
  ('array -> VARIABLE IGUAL CIZQ valor CDER','array',5,'p_array','SintacticoLex.py',117),
  ('array -> VARIABLE IGUAL ARRAY NEW','array',4,'p_array','SintacticoLex.py',118),
  ('array -> VARIABLE IGUAL ARRAY NEW LPAREN parametros RPAREN','array',7,'p_array','SintacticoLex.py',119),
  ('valor -> ENTERO','valor',1,'p_valor','SintacticoLex.py',124),
  ('valor -> VARIABLE','valor',1,'p_valor','SintacticoLex.py',125),
  ('valor -> CADENA','valor',1,'p_valor','SintacticoLex.py',126),
  ('valor -> DECIMAL','valor',1,'p_valor','SintacticoLex.py',127),
  ('valor -> array','valor',1,'p_valor','SintacticoLex.py',128),
]
