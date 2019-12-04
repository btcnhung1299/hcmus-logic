import itertools

from literal import Literal

class Clause:
   def __init__(self):
      self.literals = []

   def __repr__(self):
      return '{}' if len(self.literals) == 0 else ' OR '.join(str(literal) for literal in self.literals)

   def empty(self):
      return len(self.literals) == 0

   def add(self, literal):
      self.literals.append(literal)

   def negate(self):
      for literal in self.literals:
         literal.negate()

   def copy_except(self, exp_literal):
      clone = Clause()
      for literal in self.literals:
         if literal != exp_literal:
            clone.add(literal)
      return clone

   def is_pointless(self):
      for (li, lj) in itertools.combinations(self.literals, 2):
         if li.complement(lj):
            return True
      return False

   @staticmethod
   def parse_clause(clause_str):
      list_literal_str = clause_str.strip().split('OR')
      clause = Clause()
      for literal_str in list_literal_str:
         literal = Literal.parse_literal(literal_str)
         clause.add(literal)
      return clause

   @staticmethod
   def merge(c1, c2):
      merge_clause = Clause()
      merge_clause.literals = sorted(c1.literals + c2.literals)
      return merge_clause

   @staticmethod
   def resolve(ci, cj):
      resolvents = set()
      contain_empty = False

      for li in ci.literals:
         for lj in cj.literals:
            if li.complement(lj):
               new_clause = Clause.merge(ci.copy_except(li), cj.copy_except(lj))
               if new_clause.is_pointless():
                  continue
               if new_clause.empty():
                  contain_empty = True
               resolvents.add(new_clause)

      return resolvents, contain_empty
