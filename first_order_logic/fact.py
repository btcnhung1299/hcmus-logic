class Fact:
   def __init__(self, op='', args=[], negated=False):
      self.op = op
      self.args = args.copy()
      self.negated = negated

   def __repr__(self):
      return '{}({})'.format(self.op, ','.join(self.args))

   def negate(self):
      self.negated = 1 - self.negated

   def args(self):
      return self.agrs.copy()

   def op(self):
      return self.op

   @staticmethod
   def parse_fact(fact_str):
      fact_str = fact_str.strip().rstrip('.').replace(' ', '')
      sep_idx = fact_str.index('(')
      op = fact_str[: sep_idx]
      args = fact_str[sep_idx + 1 : -1].split(',')
      return Fact(op=op, args=args)
