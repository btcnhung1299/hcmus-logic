class Substitution:
   def __init__(self):
      self.mappings = dict()

   def contains(self, var):
      return var in self.mappings

   def substitute_of(self, var):
      return self.mappings[var]

   def substitute(self, fact):
      for idx, arg in fact.args:
         fact[idx] = self.substitute_of(arg)

   def add(self, var, x):
      self.mappings[var] = x 
