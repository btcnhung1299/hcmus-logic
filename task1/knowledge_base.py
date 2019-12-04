from clause import Clause

class KnowledgeBase:
   def __init__(self):
      self.facts = []
      self.rules = []

   @staticmethod
   def declare(knowledge_base, path):
      with open(path, 'r') as f:
         lines = f.readlines()
         for clause_str in lines:
            clause = Clause.strpclause(clause_str)
            num_literals = clause.get_num_literals()
            if num_literals = 1:
               self.facts.append(clause)
            else:
               self.rules.append(clause)

   def tell():
      pass

   def ask():
      pass
