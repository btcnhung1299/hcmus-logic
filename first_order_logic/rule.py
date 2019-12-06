from fact import Fact

class Rule:
   def __init__(self, conclusion=Fact(), conditions=[]):
      self.conditions = conditions.copy()
      self.conclusion = conclusion

   @staticmethod
   def parse_rule(rule_str):
      rule_str = rule_str.strip().rstrip('.').replace(' ', '')
      sep_idx = rule_str.find(':-')
      conclusion = Fact.parse_fact(rule_str[: sep_idx])
      conditions = []
      list_fact_str = rule_str[sep_idx + 2 :].split('),')

      for idx, fact_str in enumerate(list_fact_str):
         if idx != len(list_fact_str) - 1:
            fact_str += ')'
         fact = Fact.parse_fact(fact_str)
         conditions.append(fact)

      return Rule(conclusion=conclusion, conditions=conditions)

