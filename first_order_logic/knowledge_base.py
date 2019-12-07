from sentence import Sentence
from fact import Fact
from rule import Rule
from forward_chaining import forward_chaining

class KnowledgeBase:
   def __init__(self):
      self.facts = []
      self.rules = []

   def add_fact(self, fact):
      self.facts.append(fact)

   def add_rule(self, rule):
      self.rules.append(rule)

   def query(self, query_str):
      alpha = Fact.parse_fact(query_str)
      return forward_chaining(self, alpha)

   @staticmethod
   def declare(kb, list_sent_str):
      while list_sent_str:
         sent_str, list_sent_str = Sentence.next(list_sent_str)
         sent_type = Sentence.categorize(sent_str)
         if sent_type == 'fact':
            fact = Fact.parse_fact(sent_str)
            kb.add_fact(fact)
         elif sent_type == 'rule':
            rule = Rule.parse_rule(sent_str)
            kb.add_rule(rule)
