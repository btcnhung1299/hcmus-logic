from clause import Clause

class KnowledgeBase:
   def __init__(self):
      self.clauses = []
   
   @staticmethod
   def declare(kb, list_clause_str):
      for clause_str in list_clause_str:
         clause = Clause.parse_clause(clause_str)
         clause.flatten()
         kb.add(clause)

   def add(self, clause):
      self.clauses.append(clause)
