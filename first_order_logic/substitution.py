class Substitution:
   def __init__(self):
      self.mappings = dict()

   def __repr__(self):
      return str(self.mappings)

   def contains(self, var):
      return var in self.mappings

   def substitute_of(self, var):
      return self.mappings[var]

   def substitute(self, fact):
      for idx, arg in enumerate(fact.args):
         if self.contains(arg):
            fact.args[idx] = self.substitute_of(arg)

   def add(self, var, x):
      self.mappings[var] = x 
