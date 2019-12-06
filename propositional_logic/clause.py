import itertools

from literal import Literal

class Clause:
   def __init__(self):
      # List of literals is implemented using list but it should work as ordered set under the hood
      self.literals = []

   def __repr__(self):
      # Literals are seperated by 'OR'; use '{}' to represent empty clause
      return '{}' if len(self.literals) == 0 else ' OR '.join(str(literal) for literal in self.literals)

   def flatten(self):
      # Remove duplicate literals
      self.literals = sorted(set(self.literals))

   def __lt__(self, rhs):
      if len(self.literals) != len(rhs.literals):
         return len(self.literals) < len(rhs.literals)
      for idx, lit in enumerate(self.literals):
         if lit != rhs.literals[idx]:
            return lit < rhs.literals[idx]
      return False

   def __eq__(self, rhs):
      if len(self.literals) != len(rhs.literals):
         return False
      for idx, lit in enumerate(self.literals):
         if lit != rhs.literals[idx]:
            return False
      return True

   def __hash__(self):
      return hash(tuple(self.literals))

   def empty(self):
      return len(self.literals) == 0

   def add(self, literal):
      self.literals.append(literal)

   def negate(self):
      # Negate a clause by negating all of its literals; may cause unexpected behaviors
      for literal in self.literals:
         literal.negate()

   def is_pointless(self):
      # The clause in which two complementary literals appear (e.g A OR B OR -B) is not helpful
      for i in range(len(self.literals) - 1):   # List of literals are sorted ascendingly
         if self.literals[i].complement(self.literals[i + 1]):
            return True
      return False

   def copy_except(self, exp_literal):
      clone = Clause()
      for literal in self.literals:
         if literal != exp_literal:
            clone.add(literal.copy())
      return clone

   @staticmethod
   def parse_clause(clause_str):
      list_literal_str = clause_str.strip().split('OR')
      clause = Clause()
      for literal_str in list_literal_str:
         literal = Literal.parse_literal(literal_str)
         clause.add(literal)
      clause.flatten()
      return clause

   @staticmethod
   def merge(c1, c2):
      merge_clause = Clause()
      merge_clause.literals = c1.literals.copy() + c2.literals.copy()
      merge_clause.flatten()
      return merge_clause

   @staticmethod
   def resolve(ci, cj):
      resolvents = set()
      empty_clause = False

      for li in ci.literals:
         for lj in cj.literals:
            if li == lj:
               continue
            if li.complement(lj):
               new_clause = Clause.merge(ci.copy_except(li), cj.copy_except(lj))
               if new_clause.is_pointless():
                  continue
               if new_clause.empty():
                  empty_clause = True
               resolvents.add(new_clause)

      return resolvents, empty_clause
