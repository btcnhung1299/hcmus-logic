from fact import Fact

def is_constant(x):
   return isinstance(x, str) and x[0].isupper()

def is_variable(x):
   return isinstance(x, str) and x[0].islower()

def is_compound(x):
   return isinstance(x, Fact)

def is_list(x):
   return isinstance(x, list)
