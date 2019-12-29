
from rply import ParserGenerator
from syntax_tree.ast import Number, Sum, Sub, Print
from lexer.lexer import keywords, chars


class Parser():
    def __init__(self,module, builder, printf):
        
        q = [x[0] for x in keywords]
        q.extend([x[0] for x in chars])

        self.pg = ParserGenerator(
            # A list of all token names accepted by the parser.
            q
        )

        self.module = module
        self.builder = builder
        self.printf = printf

    def parse(self):
        @self.pg.production('program : PRINT open_par expression close_par')
        def program(p):
            return Print(self.builder, self.module, self.printf, p[2])

        @self.pg.production('expression : expression sum expression')
        @self.pg.production('expression : expression sub expression')
        def expression(p):
            left = p[0]
            right = p[2]
            operator = p[1]
            if operator.gettokentype() == 'sum':
                return Sum(self.builder, self.module, left, right)
            elif operator.gettokentype() == 'sub':
                return Sub(self.builder, self.module, left, right)

        @self.pg.production('expression : digit')
        def number(p):
            return Number(self.builder, self.module, p[0].value)

        @self.pg.error
        def error_handle(token):
            raise ValueError(token)

    def get_parser(self):
        return self.pg.build()