from fact import Fact
from unify import unify
from substitution import Substitution

class Rule:
   def __init__(self, conclusion=Fact(), premises=[]):
      self.conclusion = conclusion        # Inferred fact
      self.premises = premises            # Conditions: list of facts
      self.ops = self.get_ops()           # List of related relations and functions

      self.premises.sort()
      self.dup_predicate = self.detect_dup_predicate()

   def __repr__(self):
      return '{} => {}'.format(' & '.join([str(cond) for cond in self.premises]), str(self.conclusion))

   def copy(self):
      return Rule(self.conclusion.copy(), self.premises.copy())

   def get_num_premises(self):
      return len(self.premises)

   def get_ops(self):
      ops = set()
      for premise in self.premises:
         ops.add(premise.op)
      return ops

   def may_helpful(self, fact_op):
      return fact_op in self.ops

   def may_triggered(self, new_facts):
      # Check if any fact pi in new_facts is unified with a premise in rule
      for new_fact in new_facts:
         for premise in self.premises:
            if unify(new_fact, premise, Substitution()):
               return True
      return False

   def detect_dup_predicate(self):
      num_premises = self.get_num_premises()
      for i in range(num_premises - 1):
         if self.premises[i].op == self.premises[i + 1].op:
            return True
      return False

   @staticmethod
   def parse_rule(rule_str):       
      # Example: daughter(Person, Parent) :- female(Person), parent(Parent, Person).
      rule_str = rule_str.strip().rstrip('.').replace(' ', '')
      sep_idx = rule_str.find(':-')

      # Get conclusion (lhs) and premises (rhs) seperated by ':-'
      conclusion = Fact.parse_fact(rule_str[: sep_idx])
      premises = []
      list_fact_str = rule_str[sep_idx + 2:].split('),')

      for idx, fact_str in enumerate(list_fact_str):
         if idx != len(list_fact_str) - 1:
            fact_str += ')'
         fact = Fact.parse_fact(fact_str)
         premises.append(fact)

      return Rule(conclusion, premises)
