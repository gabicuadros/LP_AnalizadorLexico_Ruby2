
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ALIAS AND ARRAY BEGIN BOOLEANO BREAK CADENA CASE CDER CIZQ CLASS COMA DECIMAL DEF DIFERENTE DIV DOBLECOMILLA DOSPUNTOS END ENSURE ENTERO FALSE FILE FOR GETS HASH IF IGUAL IGUALA IMPRIMIR IN INITIALIZE LDER LINE LIZQ LPAREN MAS MAYOR MAYORIGU MENOR MENORIGU MOD MODULE NEGACION NEW NEXT NIL NOT OPAND OPOR OPXOR OR POTENCIA PRINT PROD PUNTO PUNTOYCOMA PUTS RANGO REDO RESCUE RESTA RETRY RETURN RPAREN SELF SUPER THEN TRUE UNDEF UNLESS UNTIL VARIABLE WHEN WHILE YIELDalgoritmo : imprimir\n                 | asignacion\n                 | expresion\n                 | comparacion\n                 | sentenciaIf\n                 | comparacionLog\n                 | sentenciaWhile\n    sentenciaIf : IF LPAREN comparacion RPAREN DOSPUNTOS algoritmosentenciaWhile : WHILE LPAREN comparacion RPAREN DOSPUNTOS algoritmosentenciaIgualA :  valor  IGUALA valorasignacion : VARIABLE IGUAL expresionimprimir : print\n                | puts\n    print : PRINT LPAREN expresion RPARENputs : PUTS expresionexpresion : valor\n    comparacion : expresion operadorCom expresioncomparacionLog : comparacion operadorLog comparacionexpresion : valor operadorMat expresionoperadorMat : MAS\n                   | RESTA\n                   | DIV\n                   | PROD\n                   | POTENCIA\n                   | MOD\n    operadorCom : MAYOR\n                   | MENOR\n                   | MAYORIGU\n                   | MENORIGU\n                   | DIFERENTE\n                   | sentenciaIgualA\n    operadorLog  : OPAND\n                    | OPOR\n                    | OPXOR\n                    | AND\n                    | OR\n    valor : ENTERO\n             | VARIABLE\n             | CADENA\n             | DECIMAL\n    '
    
_lr_action_items = {'VARIABLE':([0,4,11,12,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,50,52,56,60,61,],[11,28,-38,-16,28,-37,-39,-40,28,-26,-27,-28,-29,-30,-31,-38,28,-32,-33,-34,-35,-36,28,28,-20,-21,-22,-23,-24,-25,28,28,28,28,28,-19,-10,11,11,]),'IF':([0,60,61,],[13,13,13,]),'WHILE':([0,60,61,],[14,14,14,]),'PRINT':([0,60,61,],[15,15,15,]),'PUTS':([0,60,61,],[16,16,16,]),'ENTERO':([0,4,11,12,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,50,52,56,60,61,],[17,17,-38,-16,17,-37,-39,-40,17,-26,-27,-28,-29,-30,-31,-38,17,-32,-33,-34,-35,-36,17,17,-20,-21,-22,-23,-24,-25,17,17,17,17,17,-19,-10,17,17,]),'CADENA':([0,4,11,12,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,50,52,56,60,61,],[18,18,-38,-16,18,-37,-39,-40,18,-26,-27,-28,-29,-30,-31,-38,18,-32,-33,-34,-35,-36,18,18,-20,-21,-22,-23,-24,-25,18,18,18,18,18,-19,-10,18,18,]),'DECIMAL':([0,4,11,12,16,17,18,19,20,21,22,23,24,25,26,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,48,50,52,56,60,61,],[19,19,-38,-16,19,-37,-39,-40,19,-26,-27,-28,-29,-30,-31,-38,19,-32,-33,-34,-35,-36,19,19,-20,-21,-22,-23,-24,-25,19,19,19,19,19,-19,-10,19,19,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,17,18,19,28,46,47,49,51,52,59,62,63,],[0,-1,-2,-3,-4,-5,-6,-7,-12,-13,-38,-16,-37,-39,-40,-38,-15,-17,-18,-11,-19,-14,-8,-9,]),'MAYOR':([4,11,12,17,18,19,28,50,52,],[21,-38,-16,-37,-39,-40,-38,21,-19,]),'MENOR':([4,11,12,17,18,19,28,50,52,],[22,-38,-16,-37,-39,-40,-38,22,-19,]),'MAYORIGU':([4,11,12,17,18,19,28,50,52,],[23,-38,-16,-37,-39,-40,-38,23,-19,]),'MENORIGU':([4,11,12,17,18,19,28,50,52,],[24,-38,-16,-37,-39,-40,-38,24,-19,]),'DIFERENTE':([4,11,12,17,18,19,28,50,52,],[25,-38,-16,-37,-39,-40,-38,25,-19,]),'OPAND':([5,12,17,18,19,28,47,52,],[30,-16,-37,-39,-40,-38,-17,-19,]),'OPOR':([5,12,17,18,19,28,47,52,],[31,-16,-37,-39,-40,-38,-17,-19,]),'OPXOR':([5,12,17,18,19,28,47,52,],[32,-16,-37,-39,-40,-38,-17,-19,]),'AND':([5,12,17,18,19,28,47,52,],[33,-16,-37,-39,-40,-38,-17,-19,]),'OR':([5,12,17,18,19,28,47,52,],[34,-16,-37,-39,-40,-38,-17,-19,]),'IGUAL':([11,],[35,]),'MAS':([11,12,17,18,19,28,],[-38,37,-37,-39,-40,-38,]),'RESTA':([11,12,17,18,19,28,],[-38,38,-37,-39,-40,-38,]),'DIV':([11,12,17,18,19,28,],[-38,39,-37,-39,-40,-38,]),'PROD':([11,12,17,18,19,28,],[-38,40,-37,-39,-40,-38,]),'POTENCIA':([11,12,17,18,19,28,],[-38,41,-37,-39,-40,-38,]),'MOD':([11,12,17,18,19,28,],[-38,42,-37,-39,-40,-38,]),'RPAREN':([12,17,18,19,28,47,52,53,54,55,],[-16,-37,-39,-40,-38,-17,-19,57,58,59,]),'LPAREN':([13,14,15,],[43,44,45,]),'IGUALA':([17,18,19,27,28,],[-37,-39,-40,48,-38,]),'DOSPUNTOS':([57,58,],[60,61,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'algoritmo':([0,60,61,],[1,62,63,]),'imprimir':([0,60,61,],[2,2,2,]),'asignacion':([0,60,61,],[3,3,3,]),'expresion':([0,16,20,29,35,36,43,44,45,60,61,],[4,46,47,50,51,52,50,50,55,4,4,]),'comparacion':([0,29,43,44,60,61,],[5,49,53,54,5,5,]),'sentenciaIf':([0,60,61,],[6,6,6,]),'comparacionLog':([0,60,61,],[7,7,7,]),'sentenciaWhile':([0,60,61,],[8,8,8,]),'print':([0,60,61,],[9,9,9,]),'puts':([0,60,61,],[10,10,10,]),'valor':([0,4,16,20,29,35,36,43,44,45,48,50,60,61,],[12,27,12,12,12,12,12,12,12,12,56,27,12,12,]),'operadorCom':([4,50,],[20,20,]),'sentenciaIgualA':([4,50,],[26,26,]),'operadorLog':([5,],[29,]),'operadorMat':([12,],[36,]),}

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
  ('algoritmo -> comparacion','algoritmo',1,'p_algoritmo','SintacticoLex.py',10),
  ('algoritmo -> sentenciaIf','algoritmo',1,'p_algoritmo','SintacticoLex.py',11),
  ('algoritmo -> comparacionLog','algoritmo',1,'p_algoritmo','SintacticoLex.py',12),
  ('algoritmo -> sentenciaWhile','algoritmo',1,'p_algoritmo','SintacticoLex.py',13),
  ('sentenciaIf -> IF LPAREN comparacion RPAREN DOSPUNTOS algoritmo','sentenciaIf',6,'p_sentenciaIf','SintacticoLex.py',16),
  ('sentenciaWhile -> WHILE LPAREN comparacion RPAREN DOSPUNTOS algoritmo','sentenciaWhile',6,'p_sentenciaWhile','SintacticoLex.py',19),
  ('sentenciaIgualA -> valor IGUALA valor','sentenciaIgualA',3,'p_sentenciaIgualA','SintacticoLex.py',22),
  ('asignacion -> VARIABLE IGUAL expresion','asignacion',3,'p_asignacion','SintacticoLex.py',25),
  ('imprimir -> print','imprimir',1,'p_imprimir','SintacticoLex.py',28),
  ('imprimir -> puts','imprimir',1,'p_imprimir','SintacticoLex.py',29),
  ('print -> PRINT LPAREN expresion RPAREN','print',4,'p_print','SintacticoLex.py',33),
  ('puts -> PUTS expresion','puts',2,'p_puts','SintacticoLex.py',36),
  ('expresion -> valor','expresion',1,'p_expresion','SintacticoLex.py',41),
  ('comparacion -> expresion operadorCom expresion','comparacion',3,'p_comparacion','SintacticoLex.py',44),
  ('comparacionLog -> comparacion operadorLog comparacion','comparacionLog',3,'p_comparacionLogica','SintacticoLex.py',47),
  ('expresion -> valor operadorMat expresion','expresion',3,'p_expresion_aritmetica','SintacticoLex.py',50),
  ('operadorMat -> MAS','operadorMat',1,'p_operadorMat','SintacticoLex.py',53),
  ('operadorMat -> RESTA','operadorMat',1,'p_operadorMat','SintacticoLex.py',54),
  ('operadorMat -> DIV','operadorMat',1,'p_operadorMat','SintacticoLex.py',55),
  ('operadorMat -> PROD','operadorMat',1,'p_operadorMat','SintacticoLex.py',56),
  ('operadorMat -> POTENCIA','operadorMat',1,'p_operadorMat','SintacticoLex.py',57),
  ('operadorMat -> MOD','operadorMat',1,'p_operadorMat','SintacticoLex.py',58),
  ('operadorCom -> MAYOR','operadorCom',1,'p_operadorComp','SintacticoLex.py',62),
  ('operadorCom -> MENOR','operadorCom',1,'p_operadorComp','SintacticoLex.py',63),
  ('operadorCom -> MAYORIGU','operadorCom',1,'p_operadorComp','SintacticoLex.py',64),
  ('operadorCom -> MENORIGU','operadorCom',1,'p_operadorComp','SintacticoLex.py',65),
  ('operadorCom -> DIFERENTE','operadorCom',1,'p_operadorComp','SintacticoLex.py',66),
  ('operadorCom -> sentenciaIgualA','operadorCom',1,'p_operadorComp','SintacticoLex.py',67),
  ('operadorLog -> OPAND','operadorLog',1,'p_operadorLog','SintacticoLex.py',70),
  ('operadorLog -> OPOR','operadorLog',1,'p_operadorLog','SintacticoLex.py',71),
  ('operadorLog -> OPXOR','operadorLog',1,'p_operadorLog','SintacticoLex.py',72),
  ('operadorLog -> AND','operadorLog',1,'p_operadorLog','SintacticoLex.py',73),
  ('operadorLog -> OR','operadorLog',1,'p_operadorLog','SintacticoLex.py',74),
  ('valor -> ENTERO','valor',1,'p_valor','SintacticoLex.py',78),
  ('valor -> VARIABLE','valor',1,'p_valor','SintacticoLex.py',79),
  ('valor -> CADENA','valor',1,'p_valor','SintacticoLex.py',80),
  ('valor -> DECIMAL','valor',1,'p_valor','SintacticoLex.py',81),
]
