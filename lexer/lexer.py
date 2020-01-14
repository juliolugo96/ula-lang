from rply import LexerGenerator

# keywords

keywords = [
("FALSE", r"falso"),
("TRUE", r"verdadero"),
("ELSE", r"si_no"),
("BREAK", r"salir"),
("IN", r"en"),
("RETURN", r"retorna"),
("AND", r"y"),
("OR", r"o"),
("NOT", r"no"),
("CONTINUE", r"seguir"),
("FOR", r"repita_para"),
("WHILE", r"repita_mientras"),
("IF", r"si"),
("ASSERT", r"asegura"),
("PRINT", r"mostrar"),
("READ", r"leer"),
("END", r"fin"),
("IMPORT", r"importar"),
("BIGGER", r"es_mayor_que"),
("SMALLER", r"es_menor_que"),
("ATTRIBUTION", r"le_asigno"),
("EQUAL", r"es_igual_a"),
("DIFF", r"es_distinto_a"),
("VAR", r"variable")
]


# Characters

chars = [
  ("DIGIT", r'\d+'),
  ("OPEN_PARENS", r"\("),
  ("CLOSE_PARENS", r"\)"),
  ("OPEN_SQUARE_BRACKETS", r"\["),
  ("CLOSE_SQUARE_BRACKETS", r"\]"),
  ("OPEN_BRACKETS", r"\{"),
  ("CLOSE_BRACKETS", r"\}"),
  ("SMALLER", r"\<"),
  ("BIGGER", r"\>"),
  ("ATTRIBUTION", r":="),
  ("EQUAL", r"="),
  ("DIFF", r"!="),
  ("COMMA", r"\,"),
  ("DOT", r"\."),
  ("COLON", r"\:"),
  ("SEMI_COLON", r"\;"),
  ("HASH", r"\#"),
  ("DOUBLE_QUOTE", r"\""),
  ("ESCAPE", r"\\"),
  ("PLUS", r"\+"),
  ("MINUS", r"\-"),
  ("MUL", r"\*"),
  ("DIV", r"/"),
  ("IDENTIFIER", r'[a-zA-Z_][a-zA-Z_0-9]*'),
  ("QUOTE", r"\'"),
]

class Lexer():
  def __init__(self):
    self.lexer = LexerGenerator()
    
  def add_tokens(self):
    for key, value in keywords:
      self.lexer.add(key, value)

    for key, value in chars:
      self.lexer.add(key, value)

    self.lexer.ignore('\s+')            
  
  def get_lexer(self):
    self.add_tokens()
    return self.lexer.build()
    
