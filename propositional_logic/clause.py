from literal import Literal

class Clause:
   def __init__(self):
      self.literals = []

   @staticmethod
   def parse_clause(clause_str):
      list_literal_str = clause_str.strip().split('OR')
      clause = Clause()

      for literal_str in list_literal_str:
         literal = Literal.parse_literal(literal_str)
         clause.add(literal)

      return clause

   def add(self, literal):
      self.literals.append(literal)
