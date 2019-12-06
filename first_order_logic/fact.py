class Fact:
   def __init__(self, relation='', args=[]):
      self.relation = relation
      self.args = args.copy()

   @staticmethod
   def parse_fact(fact_str):
      fact_str = fact_str.strip().rstrip('.')
      sep_idx = fact_str.index('(')
      relation = fact_str[: sep_idx]
      args = fact_str[sep_idx + 1 : -1].replace(' ', '').split(',')
      print(relation, *args)
      return Fact(relation=relation, args=args)
