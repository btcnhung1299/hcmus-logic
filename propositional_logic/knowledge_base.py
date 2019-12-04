from clause import Clause

class KnowledgeBase:
   def __init__(self):
      self.clauses = []

   @staticmethod
   def ask(kb, path):
      with open(path, 'r') as f:
         alpha = f.readline()
         num_clauses = int(f.readline())
         list_clauses = f.readlines()
      f.close()
      kb.declare(list_clauses)
      kb.resolution(alpha)

   def declare(self, list_clause_str):
      for clause_str in list_clause_str:
         clause = Clause.parse_clause(clause_str)
         self.add(clause)

   def add(self, clause):
      self.clauses.append(clause)

   def resolution(self, alpha):
      pass
