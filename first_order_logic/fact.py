class Fact:
   def __init__(self, op='', args=[], negated=False):
      self.op = op               # Relation or function
      self.args = args           # Varibles and constants
      self.negated = negated     # Not

   def __repr__(self):
      return '{}({})'.format(self.op, ', '.join(self.args))

   def __lt__(self, rhs):
      if self.op != rhs.op:
         return self.op < rhs.op
      if self.negated != rhs.negated:
         return self.negated < rhs.negated
      return self.args < rhs.args

   def __eq__(self, rhs):
      if self.op != rhs.op:
         return False
      if self.negated != rhs.negated:
         return False
      return self.args == rhs.args

   def __hash__(self):
      return hash(str(self))
   
   def copy(self):
      return Fact(self.op, self.args.copy(), self.negated)

   def negate(self):
      self.negated = 1 - self.negated

   def get_args(self):
      return self.args

   def get_op(self):
      return self.op

   @staticmethod
   def parse_fact(fact_str):
      # Example: female(princess_diana).
      fact_str = fact_str.strip().rstrip('.').replace(' ', '')
      sep_idx = fact_str.index('(')

      # Op and args are separated by '('
      op = fact_str[:sep_idx]
      args = fact_str[sep_idx + 1 : -1].split(',')
      return Fact(op, args)
