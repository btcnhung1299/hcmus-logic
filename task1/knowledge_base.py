from clause import Clause

class KnowledgeBase:
   def __init__(self):
      self.facts = []
      self.rules = []

   @staticmethod
   def declare(knowledge_base, path):
      with open(path, 'r') as f:
         list_clause_str = f.readlines()

         for clause_str in list_clause_str:
            clause = Clause.strpclause(clause_str)
            num_literals = clause.get_num_literals()
            if num_literals == 1:
               knowledge_base.add_fact(clause)
            else:
               knowledge_base.add_rule(clause)

   def add_fact(self, fact):
      self.facts.append(fact)

   def add_rule(self, rule):
      self.rules.append(rule)

   @staticmethod
   def tell():
      pass

   @staticmethod
   def ask():
      pass
