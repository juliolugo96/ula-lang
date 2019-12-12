from rply import LexerGenerator

# keywords

keywords = [
("FALSE", r"falso"),
("TRUE", r"verdadero"),
("ELSE", r"contrario"),
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
("IMPORT", r"importar")
]


# Characters

chars = [
  ("lower", r'[a-z]'),
  ("upper", r'[A-Z]'),
  ("digit", r'\d+'),
  ("open_par", r"\("),
  ("close_par", r"\)"),
  ("open_bracket", r"\["),
  ("close_bracket", r"\]"),
  ("open_brace", r"\{"),
  ("close_brace", r"\}"),
  ("open_ang", r"\<"),
  ("close_ang", r"\>"),
  ("assign", r"\="),
  ("comma", r"\,"),
  ("dot", r"\."),
  ("colon", r"\:"),
  ("semicolon", r"\;"),
  ("hash_sym", r"\#"),
  ("mark", r"\'"),
  ("double_mark", r"\""),
  ("scape", r"\\"),
  ("add", r"\+"),
  ("subs", r"\-"),
  ("mult", r"\*"),
  ("div", r"\/"),
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
    
