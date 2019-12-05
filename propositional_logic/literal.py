class Literal:
   def __init__(self, symbol='', negated=False):
      self.negated = negated
      self.symbol = symbol

   def copy(self):
      clone = Literal(self.symbol, self.negated)
      return clone

   def __repr__(self):
      return '-{}'.format(self.symbol) if self.negated else self.symbol

   def __eq__(self, rhs):
      return self.symbol == rhs.symbol and self.negated == rhs.negated

   def __lt__(self, rhs):
      if self.symbol != rhs.symbol:
         return self.symbol < rhs.symbol
      return self.negated < rhs.negated      # which means A < -A

   def __hash__(self):
      s = '-' + self.symbol if self.negated else self.symbol
      return hash(s)

   def complement(self, rhs):
      return self.symbol == rhs.symbol and self.negated != rhs.negated

   def negate(self):
      self.negated = 1 - self.negated

   def negative(self):
      return self.negated
   
   def set_symbol(self, symbol):
      self.symbol = symbol

   @staticmethod
   def parse_literal(literal_str):
      literal_str = literal_str.strip()
      if literal_str[0] == '-':
         literal = Literal(symbol=literal_str[1], negated=True)
      else:
         literal = Literal(symbol=literal_str[0])
      return literal
