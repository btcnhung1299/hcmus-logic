class Literal:
   def __init__(self):
      self.negated = False
      self.symbol = ''

   @staticmethod
   def parse_literal(literal_str):
      literal_str = literal_str.strip()
      literal = Literal()

      if literal_str[0] == '-':
         literal.negate()
         literal.set_symbol(literal_str[1])
      else:
         literal.set_symbol(literal_str[0])

      return literal

   def negate(self):
      self.negated = True
   
   def set_symbol(self, symbol):
      self.symbol = symbol
