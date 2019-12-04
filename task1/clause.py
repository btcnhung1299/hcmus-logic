from literal import Literal

class Clause:
   def __init__(self):
      self.literals = []

   @staticmethod
   def strpclause(clause_str):
      list_literal_str = clause_str.split('OR')
      clause = Clause()

      for literal_str in list_literal_str:
         literal = Literal.strpliteral(literal_str)
         clause.add(literal)

      return clause

   def get_num_literals(self):
      return len(self.literals)

   def add(self, literal):
      self.literals.append(literal)
