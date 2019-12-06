class Fact:
   def __init__(self, relation='', args=[], negated=False):
      self.relation = relation
      self.args = args.copy()
      self.negated = negated

   def __repr__(self):
      return '{}({})'.format(self.relation, ','.join(self.args))

   def negate(self):
      self.negated = 1 - self.negated

   @staticmethod
   def parse_fact(fact_str):
      fact_str = fact_str.strip().rstrip('.').replace(' ', '')
      sep_idx = fact_str.index('(')
      relation = fact_str[: sep_idx]
      args = fact_str[sep_idx + 1 : -1].split(',')
      return Fact(relation=relation, args=args)
