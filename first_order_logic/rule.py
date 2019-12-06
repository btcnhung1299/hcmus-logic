from fact import Fact

class Rule:
   def __init__(self, rhs=Fact(), lhs=[]):
      self.rhs = rhs.copy()   # Conclusion
      self.lhs = lhs.copy()   # Conditions
      self.vars = set()

   def __repr__(self):
      return '{} => {}'.format(' & '.join([str(cond) for cond in self.lhs]), str(self.rhs))

   def copy(self):
      return Rule(rhs=self.rhs, lhs=self.lhs)

   def num_conditions(self):
      return len(self.lhs)

   @staticmethod
   def parse_rule(rule_str):
      rule_str = rule_str.strip().rstrip('.').replace(' ', '')
      sep_idx = rule_str.find(':-')

      rhs = Fact.parse_fact(rule_str[: sep_idx])
      lhs = []
      list_fact_str = rule_str[sep_idx + 2:].split('),')

      for idx, fact_str in enumerate(list_fact_str):
         if idx != len(list_fact_str) - 1:
            fact_str += ')'
         fact = Fact.parse_fact(fact_str)
         lhs.append(fact)

      return Rule(rhs=rhs, lhs=lhs)

